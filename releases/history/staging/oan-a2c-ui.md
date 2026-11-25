# oan-a2c-ui: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.4

<!-- source-commit: 7f935642ed64896df6a95634c1758babd60f0275 version: 0.0.1-staging.4 -->
Published 2026-11-25. Archive SHA-256 `81896110363f1a894c3738c5a1502db900487a3962c6c4de857c56e74341e072`.

- Change: Merge pull request #125 from arnavam/ci/use-app-chart
- Source: [Centre-for-Open-Societal-Systems/oan_a2c_ui@7f935642ed64](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c_ui/commit/7f935642ed64896df6a95634c1758babd60f0275)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-a2c-ui/a2c-ui:0.0.1-staging.4@sha256:88d80ad0cc5209600ec203c17cdeef3863cc97d28b697c7a60121447291b2a41` |

Return to this version:

```sh
helm upgrade a2c-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-a2c-ui-0.0.1-staging.4.tgz -n a2c --reset-values -f helm/environments/staging/oan-a2c-ui.yaml --wait --timeout 15m
```

