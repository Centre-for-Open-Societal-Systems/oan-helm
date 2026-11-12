# oan-a2c-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.3

<!-- source-commit: 5dee47de0581cde91c7239f93ab7e2f2ed06144a version: 0.0.0-develop.3 -->
Published 2026-11-12. Archive SHA-256 `bca3e88d8261449c1088c73d216f79ead6db2e92e5cde57345cb5ae8317fdf43`.

- Change: Merge pull request #118 from arnavam/feat/a2c-helm-chart-ci
- Source: [Centre-for-Open-Societal-Systems/oan_a2c@5dee47de0581](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/commit/5dee47de0581cde91c7239f93ab7e2f2ed06144a)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan-a2c-service/a2c-service:0.0.0-develop.3` |

Return to this version:

```sh
helm upgrade a2c https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-a2c-service-0.0.0-develop.3.tgz -n a2c-develop --reset-values -f helm/environments/dev/oan-a2c-service.yaml --wait --timeout 15m
```

