# Launch security 20 — TripoSR

Upstream Stability/Tripo research snapshot for 3D reconstruction. Not a JMorex
product launch surface. Status tokens: `in_code` | `n_a` | `blocked_a4`.

Item 2 does not rewrite git history.

| # | Item | Status | Evidence | Notes |
|---|------|--------|----------|-------|
| 1 | Hide API keys | in_code | `README.md` `.github/workflows/secret-scan.yml` | No product secrets. Workflow scans high-signal shapes. |
| 2 | Purge Git secrets | blocked_a4 | `.github/workflows/secret-scan.yml` | Scanner only. No history rewrite. |
| 3 | Use public DB key | n_a | `README.md` | Research code, no DB. |
| 4 | Enable row-level security | n_a | `README.md` | No DB. |
| 5 | Encrypt sensitive data | n_a | `README.md` | No user data. |
| 6 | Enforce server-side auth | n_a | `README.md` | No app accounts. |
| 7 | Lock record access | n_a | `README.md` | No records. |
| 8 | Block field tampering | n_a | `README.md` | No writes API. |
| 9 | Secure session cookies | n_a | `README.md` | No sessions. |
| 10 | Hash passwords | n_a | `README.md` | No passwords. |
| 11 | Rate limit login | n_a | `README.md` | No login. |
| 12 | Add bot protection | n_a | `README.md` | No public signup. |
| 13 | Parameterize queries | n_a | `README.md` | No SQL. |
| 14 | Validate all input | n_a | `README.md` | Research CLI, not a public API. |
| 15 | Escape user content | n_a | `README.md` | No web UGC. |
| 16 | Restrict file uploads | n_a | `README.md` | Local image inference, not a hosted upload API. |
| 17 | Trim API responses | n_a | `README.md` | No hosted API. |
| 18 | Add security headers | n_a | `README.md` | No hosted web origin. |
| 19 | Force HTTPS | n_a | `README.md` | No hosted web origin. |
| 20 | Scan dependencies | partial | `README.md` | Upstream Python deps; no Dependabot in this snapshot. |
