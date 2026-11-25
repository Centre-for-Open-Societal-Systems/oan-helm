# oan-farmer-app-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.5

<!-- source-commit: 794b5f1333704d245d38573e83fa0ad2535022e0 version: 0.0.1-develop.5 -->
Published 2026-11-25. Archive SHA-256 `41cf266b53f385d4fa7caeff0d926aaf9b6172c2f1df232b25747be6f6905f72`.

- Change: Merge pull request #8 from arnavam/ci/staging-qa-pipeline
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@794b5f133370](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/794b5f1333704d245d38573e83fa0ad2535022e0)
- Changes since 0.0.1-develop.2: https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/compare/0bdcff4a353354d017b89ab22601d36e8ec2d52b...794b5f1333704d245d38573e83fa0ad2535022e0

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-farmer-app-service/farmer-app-service:0.0.1-develop.5@sha256:42c175dc823da405166a50154b4b8b31cd8b28a45d6a87c558adfbdd9ae54cf1` |

Return to this version:

```sh
helm upgrade farmer-app https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-farmer-app-service-0.0.1-develop.5.tgz -n farmer-app --reset-values -f helm/environments/dev/oan-farmer-app-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.2

<!-- source-commit: 0bdcff4a353354d017b89ab22601d36e8ec2d52b version: 0.0.1-develop.2 -->
Published 2026-11-19. Archive SHA-256 `efaa6437036b2ab512f367fd38625433a497c91f783221f494fca3b58affe353`.

- Change: Merge pull request #4 from arnavam/chore/develop-chart-version
- Source: [Centre-for-Open-Societal-Systems/oan_farmer_app_service@0bdcff4a3533](https://github.com/Centre-for-Open-Societal-Systems/oan_farmer_app_service/commit/0bdcff4a353354d017b89ab22601d36e8ec2d52b)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-farmer-app-service/farmer-app-service:0.0.1-develop.2` |

Return to this version:

```sh
helm upgrade farmer-app https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-farmer-app-service-0.0.1-develop.2.tgz -n farmer-app --reset-values -f helm/environments/dev/oan-farmer-app-service.yaml --wait --timeout 15m
```

