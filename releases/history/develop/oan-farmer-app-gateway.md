# oan-farmer-app-gateway: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.2

<!-- source-commit: 0bdcff4a353354d017b89ab22601d36e8ec2d52b version: 0.0.1-develop.2 -->
Published 2026-11-19. Archive SHA-256 `c842eeb49fc86adb693bc752aa963e58932a144aab1a3a207c466db0ac44d97a`.

- Change: Merge pull request #4 from arnavam/chore/develop-chart-version
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@0bdcff4a3533](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/0bdcff4a353354d017b89ab22601d36e8ec2d52b)

Return to this version:

```sh
helm upgrade farmer-app-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-farmer-app-gateway-0.0.1-develop.2.tgz -n farmer-app --reset-values -f helm/environments/dev/oan-farmer-app-gateway.yaml --wait --timeout 15m
```

