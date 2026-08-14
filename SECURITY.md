# Security Policy — TripoSR (research snapshot)

This repository is an upstream **TripoSR** research snapshot (MIT License,
Tripo AI & Stability AI) used for 3D reconstruction experiments. It is not a
JMorex hosted product and has no public login, database, or upload API.

## Reporting a vulnerability

**Please do not open a public GitHub issue for security vulnerabilities in
JMorex-operated copies.**

Report privately through:

- **GitHub private vulnerability reporting** on this fork — Security → Report a
  vulnerability (preferred) for issues introduced in JMorex-tracked files
  (workflows, ignore rules, docs).
- Upstream TripoSR / Stability AI channels for issues in the original research
  code.

Include a description and affected paths. Redact secrets.

## Scope

In scope here:

- Accidental commit of `.env`, keys, or operator credentials.
- CI workflows added in this fork (secret-scan, Dependabot).

Out of scope:

- Volumetric testing.
- Treating this snapshot as a hosted public inference API.

## Handling

If a credential lands in a tracked file, remove it **and rotate it**. Git
history keeps the original. History rewrite is an operator decision; this
repo does not rewrite history from a PR.

The upstream MIT `LICENSE` stays. Do not replace it with a JMorex proprietary
license.
