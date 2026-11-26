# oan-farmer-app-service: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.3

<!-- source-commit: 992170dc48ffc7a31611c3e281f0d340298e543f version: 0.0.1-staging.3 -->
Published 2026-11-26. Archive SHA-256 `829b7b1c708aa33245a30a4f9542540f4baeadc1b2c84da97eb4f479ec4514ee`.

- Change: Merge pull request #10 from arnavam/ci/staging-qa-pipeline
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@992170dc48ff](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/992170dc48ffc7a31611c3e281f0d340298e543f)
- Changes since 0.0.1-staging.2: https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/compare/794b5f1333704d245d38573e83fa0ad2535022e0...992170dc48ffc7a31611c3e281f0d340298e543f

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-farmer-app-service/farmer-app-service:0.0.1-staging.3@sha256:5f684915c70b297954fe3176a86fa4db786054c50bfe0d81ad46a550ccbe8f5f` |

Return to this version:

```sh
helm upgrade farmer-app https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-farmer-app-service-0.0.1-staging.3.tgz -n farmer-app --reset-values -f helm/environments/staging/oan-farmer-app-service.yaml --wait --timeout 15m
```

## 0.0.1-staging.2

<!-- source-commit: 794b5f1333704d245d38573e83fa0ad2535022e0 version: 0.0.1-staging.2 -->
Published 2026-11-26. Archive SHA-256 `cf3dad9906a64ed9faa7ab9f63a205fc5222c265e7629f2cc42acaf67b90309d`.

- Change: Merge pull request #8 from arnavam/ci/staging-qa-pipeline
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@794b5f133370](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/794b5f1333704d245d38573e83fa0ad2535022e0)
- Changes since 0.0.1-staging.1: https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/compare/794b5f1333704d245d38573e83fa0ad2535022e0...794b5f1333704d245d38573e83fa0ad2535022e0

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-farmer-app-service/farmer-app-service:0.0.1-staging.2@sha256:42c175dc823da405166a50154b4b8b31cd8b28a45d6a87c558adfbdd9ae54cf1` |

Return to this version:

```sh
helm upgrade farmer-app https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-farmer-app-service-0.0.1-staging.2.tgz -n farmer-app --reset-values -f helm/environments/staging/oan-farmer-app-service.yaml --wait --timeout 15m
```

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

