# oan-identitygovernance-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.3

<!-- source-commit: ebaf08d2e0a77be1c1d36fb164d3e99b600a8574 version: 0.0.0-develop.3 -->
Published 2026-11-25. Archive SHA-256 `c08816ac69a8b46221f3688d89c4f52be2aa25e0ba23b33984904396348f64be`.

- Change: Merge pull request #4 from arnavam/fix/ci-chart-convention
- Source: [Centre-for-Open-Societal-Systems/oan_identitygovernance_service@ebaf08d2e0a7](https://github.com/Centre-for-Open-Societal-Systems/oan_identitygovernance_service/commit/ebaf08d2e0a77be1c1d36fb164d3e99b600a8574)

| Values path | Image |
| --- | --- |
| `image` | `eoan/oan-identitygovernance-service/identitygovernance-service:0.0.0-develop.3` |

Return to this version:

```sh
helm upgrade identitygovernance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-identitygovernance-service-0.0.0-develop.3.tgz -n identitygovernance --reset-values -f helm/environments/dev/oan-identitygovernance-service.yaml --wait --timeout 15m
```

