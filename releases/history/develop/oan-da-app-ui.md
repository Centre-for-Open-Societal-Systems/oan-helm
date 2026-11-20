# oan-da-app-ui: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.59

<!-- source-commit: 77b769158ad1871d2209e36b472904b530ae3132 version: 0.0.1-develop.59 -->
Published 2026-11-20. Archive SHA-256 `7ee7143977f971bbc3a3dbc5ddd3393ca04db5a2a2e9fa066014f0939927b54d`.

- Change: Merge pull request #79 from rajujha-ptn/da_agent_responsive-19Nov2026
- Source: [Centre-for-Open-Societal-Systems/oan_da_app_ui@77b769158ad1](https://github.com/Centre-for-Open-Societal-Systems/oan_da_app_ui/commit/77b769158ad1871d2209e36b472904b530ae3132)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-da-app-ui/da-app-ui:0.0.1-develop.59` |

Return to this version:

```sh
helm upgrade da-app-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-da-app-ui-0.0.1-develop.59.tgz -n da-app --reset-values -f helm/environments/dev/oan-da-app-ui.yaml --wait --timeout 15m
```

