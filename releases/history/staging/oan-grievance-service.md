# oan-grievance-service: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

