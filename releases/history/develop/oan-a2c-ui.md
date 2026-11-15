# oan-a2c-ui: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.6

<!-- source-commit: 3fce7d7431f631bf28befa87ab1a02301bfb97bd version: 0.0.0-develop.6 -->
Published 2026-11-13. Archive SHA-256 `99bc4608abf35018400d43ee4d4bda1d625a6c535dd40265577a700c48150351`.

- Change: Merge pull request #114 from arnavam/feat/a2c-ui-helm-deploy-dev
- Source: [Centre-for-Open-Societal-Systems/oan_a2c_ui@3fce7d7431f6](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c_ui/commit/3fce7d7431f631bf28befa87ab1a02301bfb97bd)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan-a2c-ui/a2c-ui:0.0.0-develop.6` |

Return to this version:

```sh
helm upgrade a2c-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-a2c-ui-0.0.0-develop.6.tgz -n a2c-develop --reset-values -f helm/environments/dev/oan-a2c-ui.yaml --wait --timeout 15m
```

