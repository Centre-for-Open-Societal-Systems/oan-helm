# oan-identitygovernance-gateway: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.5

<!-- source-commit: 9a75c8460136bc3a9453b48f27a1acd84115513e version: 0.0.0-develop.5 -->
Published 2026-11-25. Archive SHA-256 `7749cdec8339eadc44e91afb9af88ffa00132ec60ea04e5839d4009ed8091e31`.

- Change: Merge pull request #5 from arnavam/feat/apisix-gateway
- Source: [Centre-for-Open-Societal-Systems/oan_identitygovernance_service@9a75c8460136](https://github.com/Centre-for-Open-Societal-Systems/oan_identitygovernance_service/commit/9a75c8460136bc3a9453b48f27a1acd84115513e)

Return to this version:

```sh
helm upgrade identitygovernance-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-identitygovernance-gateway-0.0.0-develop.5.tgz -n identitygovernance --reset-values -f helm/environments/dev/oan-identitygovernance-gateway.yaml --wait --timeout 15m
```

