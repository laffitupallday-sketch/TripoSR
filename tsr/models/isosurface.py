from typing import Callable, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn

try:
    from torchmcubes import marching_cubes as _torchmcubes_marching_cubes
except ImportError:
    _torchmcubes_marching_cubes = None

try:
    import mcubes as _mcubes
except ImportError:
    _mcubes = None


def marching_cubes(
    level: torch.FloatTensor, thresh: float = 0.0
) -> Tuple[torch.FloatTensor, torch.LongTensor]:
    if _torchmcubes_marching_cubes is not None:
        return _torchmcubes_marching_cubes(level, thresh)

    if _mcubes is None:
        raise ImportError(
            "Install torchmcubes or PyMCubes to run marching cubes isosurface extraction."
        )

    volume = level.detach().cpu().numpy()
    vertices, faces = _mcubes.marching_cubes(np.ascontiguousarray(volume), thresh)
    return (
        torch.from_numpy(np.ascontiguousarray(vertices)).float(),
        torch.from_numpy(np.ascontiguousarray(faces).astype(np.int64)),
    )


class IsosurfaceHelper(nn.Module):
    points_range: Tuple[float, float] = (0, 1)

    @property
    def grid_vertices(self) -> torch.FloatTensor:
        raise NotImplementedError


class MarchingCubeHelper(IsosurfaceHelper):
    def __init__(self, resolution: int) -> None:
        super().__init__()
        self.resolution = resolution
        self.mc_func: Callable = marching_cubes
        self._grid_vertices: Optional[torch.FloatTensor] = None

    @property
    def grid_vertices(self) -> torch.FloatTensor:
        if self._grid_vertices is None:
            # keep the vertices on CPU so that we can support very large resolution
            x, y, z = (
                torch.linspace(*self.points_range, self.resolution),
                torch.linspace(*self.points_range, self.resolution),
                torch.linspace(*self.points_range, self.resolution),
            )
            x, y, z = torch.meshgrid(x, y, z, indexing="ij")
            verts = torch.cat(
                [x.reshape(-1, 1), y.reshape(-1, 1), z.reshape(-1, 1)], dim=-1
            ).reshape(-1, 3)
            self._grid_vertices = verts
        return self._grid_vertices

    def forward(
        self,
        level: torch.FloatTensor,
    ) -> Tuple[torch.FloatTensor, torch.LongTensor]:
        level = -level.view(self.resolution, self.resolution, self.resolution)
        try:
            v_pos, t_pos_idx = self.mc_func(level.detach(), 0.0)
        except AttributeError:
            print("torchmcubes was not compiled with CUDA support, use CPU version instead.")
            v_pos, t_pos_idx = self.mc_func(level.detach().cpu(), 0.0)
        v_pos = v_pos[..., [2, 1, 0]]
        v_pos = v_pos / (self.resolution - 1.0)
        return v_pos.to(level.device), t_pos_idx.to(level.device)
