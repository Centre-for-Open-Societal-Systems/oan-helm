# oan-grievance-service: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.16

<!-- source-commit: 1b285c9d5f729f392d22baadc8c2bc3c04c8d8d6 version: 0.0.1-staging.16 -->
Published 2026-11-28. Archive SHA-256 `8a2fb316c592cbaba4366dc68569487d155e6e8d4eae0f53ed206dfd77674f0c`.

- Change: Merge pull request #167 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@1b285c9d5f72](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/1b285c9d5f729f392d22baadc8c2bc3c04c8d8d6)
- Changes since 0.0.1-staging.15: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/711b081ebd710a9b868b9f07a1e96f16c89c5178...1b285c9d5f729f392d22baadc8c2bc3c04c8d8d6

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-staging.16` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-grievance-service-0.0.1-staging.16.tgz -n grievance --reset-values -f helm/environments/staging/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-staging.15

<!-- source-commit: 711b081ebd710a9b868b9f07a1e96f16c89c5178 version: 0.0.1-staging.15 -->
Published 2026-11-25. Archive SHA-256 `f0610d4e0fc2ce7a765bc4cd65dbb75cfb224f198084d1c91a32f1c1b5c56b72`.

- Change: Merge pull request #155 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@711b081ebd71](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/711b081ebd710a9b868b9f07a1e96f16c89c5178)
- Changes since 0.0.1-staging.14: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93...711b081ebd710a9b868b9f07a1e96f16c89c5178

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-staging.15` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-grievance-service-0.0.1-staging.15.tgz -n grievance --reset-values -f helm/environments/staging/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-staging.14

<!-- source-commit: f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93 version: 0.0.1-staging.14 -->
Published 2026-11-24. Archive SHA-256 `a086455ac0422ec288135f78ad3e519b9ee552f2579b147ca271123bd84a3365`.

- Change: Merge pull request #151 from arnavam/resync/staging-into-develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@f4b2bda4b44a](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-staging.14` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-grievance-service-0.0.1-staging.14.tgz -n grievance --reset-values -f helm/environments/staging/oan-grievance-service.yaml --wait --timeout 15m
```

