# oan-a2c-gateway: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.3

<!-- source-commit: 4ea6aa41582366a4b2c5cdcce87d8d71c6581975 version: 0.0.1-staging.3 -->
Published 2026-11-24. Archive SHA-256 `c649849fec87f499f28b4a527c789acc98377fab0a77ebdfd8c00eae8f19a02b`.

- Change: Merge pull request #153 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_a2c@4ea6aa415823](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/commit/4ea6aa41582366a4b2c5cdcce87d8d71c6581975)

Return to this version:

```sh
helm upgrade a2c-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-a2c-gateway-0.0.1-staging.3.tgz -n a2c --reset-values -f helm/environments/staging/oan-a2c-gateway.yaml --wait --timeout 15m
```

