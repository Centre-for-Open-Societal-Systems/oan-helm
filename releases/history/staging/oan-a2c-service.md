# oan-a2c-service: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.4

<!-- source-commit: f53c54d4a911c1c437eaaef15184599b23afa517 version: 0.0.1-staging.4 -->
Published 2026-11-25. Archive SHA-256 `ad21a66cacb7d76aeafe1f3d825428c3ee1c25c1478699b469f2130b828349c2`.

- Change: Merge pull request #155 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_a2c@f53c54d4a911](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/commit/f53c54d4a911c1c437eaaef15184599b23afa517)
- Changes since 0.0.1-staging.3: https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/compare/4ea6aa41582366a4b2c5cdcce87d8d71c6581975...f53c54d4a911c1c437eaaef15184599b23afa517

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-a2c-service/a2c-service:0.0.1-staging.4` |

Return to this version:

```sh
helm upgrade a2c https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-a2c-service-0.0.1-staging.4.tgz -n a2c --reset-values -f helm/environments/staging/oan-a2c-service.yaml --wait --timeout 15m
```

## 0.0.1-staging.3

<!-- source-commit: 4ea6aa41582366a4b2c5cdcce87d8d71c6581975 version: 0.0.1-staging.3 -->
Published 2026-11-24. Archive SHA-256 `33b377993ab2c437b53fe3954d1ca29f7a4327faecade70d84ad5ae0676edcf1`.

- Change: Merge pull request #153 from Centre-for-Open-Societal-Systems/develop
- Source: [Centre-for-Open-Societal-Systems/oan_a2c@4ea6aa415823](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/commit/4ea6aa41582366a4b2c5cdcce87d8d71c6581975)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-a2c-service/a2c-service:0.0.1-staging.3` |

Return to this version:

```sh
helm upgrade a2c https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-a2c-service-0.0.1-staging.3.tgz -n a2c --reset-values -f helm/environments/staging/oan-a2c-service.yaml --wait --timeout 15m
```

