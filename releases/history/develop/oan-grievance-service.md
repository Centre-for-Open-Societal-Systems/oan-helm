# oan-grievance-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.79

<!-- source-commit: c84d8e9af2eee60773b0346581af810a49125859 version: 0.0.0-develop.79 -->
Published 2026-11-12. Archive SHA-256 `251af7392ec29c4225dfd6c0ffd0b5c6111e2e1f5b588dd3cedfe892ccbabb95`.

- Change: Merge pull request #108 from arnavam/fix/grievance-develop-chart-version
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@c84d8e9af2ee](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/c84d8e9af2eee60773b0346581af810a49125859)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan-grievance-service/grievance-service:0.0.0-develop.79` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.0-develop.79.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

