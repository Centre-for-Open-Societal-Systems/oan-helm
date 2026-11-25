# oan-farmer-app-service: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.1

<!-- source-commit: 794b5f1333704d245d38573e83fa0ad2535022e0 version: 0.0.1-staging.1 -->
Published 2026-11-25. Archive SHA-256 `82681b40ecd84f67c65e069924e47e754636d6943b9e8ea8d27ada5f57b443cf`.

- Change: Merge pull request #8 from arnavam/ci/staging-qa-pipeline
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@794b5f133370](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/794b5f1333704d245d38573e83fa0ad2535022e0)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-farmer-app-service/farmer-app-service:0.0.1-staging.1@sha256:42c175dc823da405166a50154b4b8b31cd8b28a45d6a87c558adfbdd9ae54cf1` |

Return to this version:

```sh
helm upgrade farmer-app https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-farmer-app-service-0.0.1-staging.1.tgz -n farmer-app --reset-values -f helm/environments/staging/oan-farmer-app-service.yaml --wait --timeout 15m
```

