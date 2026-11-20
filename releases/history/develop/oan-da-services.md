# oan-da-services: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.10-develop.64

<!-- source-commit: d1b2d002fc2095dec7f27293476db2b449566b45 version: 0.0.10-develop.64 -->
Published 2026-11-20. Archive SHA-256 `04d56ed41480a90ae44108e6f2eb5ee43abb99687f423380b49e4a41fb698fa2`.

- Change: Merge pull request #93 from Nikky-05/chore/remove-leave-flow
- Source: [Centre-for-Open-Societal-Systems/oan_da_app_services@d1b2d002fc20](https://github.com/Centre-for-Open-Societal-Systems/oan_da_app_services/commit/d1b2d002fc2095dec7f27293476db2b449566b45)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-da-services/da-services:0.0.10-develop.64` |

Return to this version:

```sh
helm upgrade da-services https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-da-services-0.0.10-develop.64.tgz -n da-app --reset-values -f helm/environments/dev/oan-da-services.yaml --wait --timeout 15m
```

