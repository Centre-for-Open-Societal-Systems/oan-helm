# oan-grievance-gateway: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.82

<!-- source-commit: 031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25 version: 0.0.1-develop.82 -->
Published 2026-11-13. Archive SHA-256 `62d4d0d77f1054cbc660e51af181581d2e7c34a497826f7e6a437fc2f80238d6`.

- Change: Merge pull request #111 from arnavam/feat/publish-gateway-chart
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@031d425de8bf](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25)

Return to this version:

```sh
helm upgrade grievance-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-gateway-0.0.1-develop.82.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-gateway.yaml --wait --timeout 15m
```

