# oan-da-services-gateway: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.10-develop.64

<!-- source-commit: d1b2d002fc2095dec7f27293476db2b449566b45 version: 0.0.10-develop.64 -->
Published 2026-11-20. Archive SHA-256 `be3bdb4d43227811329e378f639738c0a605e16108c94eb1e419d9c3d6a4b69f`.

- Change: Merge pull request #93 from Nikky-05/chore/remove-leave-flow
- Source: [Centre-for-Open-Societal-Systems/oan_da_app_services@d1b2d002fc20](https://github.com/Centre-for-Open-Societal-Systems/oan_da_app_services/commit/d1b2d002fc2095dec7f27293476db2b449566b45)

Return to this version:

```sh
helm upgrade da-services-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-da-services-gateway-0.0.10-develop.64.tgz -n da-app --reset-values -f helm/environments/dev/oan-da-services-gateway.yaml --wait --timeout 15m
```

