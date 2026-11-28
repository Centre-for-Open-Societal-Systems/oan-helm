# oan-da-app-ui: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.4

<!-- source-commit: 0db0f518ebca7bafaf5d8f4f7188f3b8f672f5fc version: 0.0.1-staging.4 -->
Published 2026-11-28. Archive SHA-256 `7d5c52072038a46228e8766ce5cb2a1a20553d02a75b4933e2b3316a257e638f`.

- Change: Merge pull request #104 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_da_app_ui@0db0f518ebca](https://github.com/Centre-for-Open-Societal-Systems/oan_da_app_ui/commit/0db0f518ebca7bafaf5d8f4f7188f3b8f672f5fc)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-da-app-ui/da-app-ui:0.0.1-staging.4` |

Return to this version:

```sh
helm upgrade da-app-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-da-app-ui-0.0.1-staging.4.tgz -n da-app --reset-values -f helm/environments/staging/oan-da-app-ui.yaml --wait --timeout 15m
```

