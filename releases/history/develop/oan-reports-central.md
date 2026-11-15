# oan-reports-central: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.7

<!-- source-commit: 1f9322c0334c402f4c080f77f8b1386ba3b881f7 version: 0.0.0-develop.7 -->
Published 2026-11-15. Archive SHA-256 `be69a757a16cacee7b22a41d0eef890478982a04eabf65a8be4d3b178d3092ab`.

- Change: Merge pull request #2 from simretyibeltal-commits/developer
- Source: [Centre-for-Open-Societal-Systems/OAN_Reports_Central@1f9322c0334c](https://github.com/Centre-for-Open-Societal-Systems/OAN_Reports_Central/commit/1f9322c0334c402f4c080f77f8b1386ba3b881f7)

| Values path | Image |
| --- | --- |
| `ecr.image` | `alpine/k8s:1.31.4` |
| `api.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan_reports_central/oan-report-central-api:0.0.0.develop.1@sha256:914f78156ef357efa0e708764d5105ba52077d1096d32a5eb51319a9b0e5f58f` |
| `web.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan_reports_central/oan-report-central-ui:0.0.0.develop.1@sha256:41d60b7eface8a4a0c4bd6cae500af52600519a962310bd5688a770b39c86124` |
| `postgresql.image` | `postgres:16-alpine` |

Return to this version:

```sh
helm upgrade oan-reports-central https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-reports-central-0.0.0-develop.7.tgz -n reports --reset-values -f helm/oan-reports-central/values-dev-registries.yaml --wait --timeout 15m
```

