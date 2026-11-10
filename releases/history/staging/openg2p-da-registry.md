# openg2p-da-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.89

<!-- source-commit: ea2fa29f43af527d4a7d8345f8b62db413d93408 version: 1.0.0-rc.89 -->
Published 2026-11-10. Archive SHA-256 `423c90bf1cb2a645bcd00b510d75414313602fa3b6453e7f4a5bcb45e8dfd338`.

- Change: Right-align and group every number widget in the DA register (#49)
- Source: [Centre-for-Open-Societal-Systems/da-registry@ea2fa29f43af](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/ea2fa29f43af527d4a7d8345f8b62db413d93408)
- Changes since 1.0.0-rc.87: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/acf5e374a852bf6fe634de6f100dc4e7f845f058...ea2fa29f43af527d4a7d8345f8b62db413d93408

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:1.0.0-rc.89@sha256:1e4f683b907e9c0293c1d28b6b4ff0dabecc12b7e53e83f30aa94e68c9625b51` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:1.0.0-rc.89@sha256:a1b549c78151990dd29e5b620e52489efd1f0052478bcf422e430305f8d47722` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.89@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.89@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:1.0.0-rc.89@sha256:cb8cfdc0dc07a826c089c9b33f6cc4f991d08c210a6f4022dff6413a5f20b6ef` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:1.0.0-rc.89@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-da-registry-1.0.0-rc.89.tgz -n da-registry --reset-values -f environments/staging/values/da.yaml --wait --timeout 15m
```

## 1.0.0-rc.87

<!-- source-commit: acf5e374a852bf6fe634de6f100dc4e7f845f058 version: 1.0.0-rc.87 -->
Published 2026-11-08. Archive SHA-256 `bd75f833d358747446b2cbc2fcbb8987657fde2a57454bf75c815c1385e85de8`.

- Change: DA staging deploys on merge with no Build with Parameters (#47)
- Source: [Centre-for-Open-Societal-Systems/da-registry@acf5e374a852](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/acf5e374a852bf6fe634de6f100dc4e7f845f058)
- Changes since 1.0.0-rc.84: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/9dc1ebfea8706c5d2d5332c1220210e15c407be8...acf5e374a852bf6fe634de6f100dc4e7f845f058

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:1.0.0-rc.87@sha256:0d67b3258027f84a36137a9c9303ff9b31148e8f6091d2f67d0fc17a5d8e53ab` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:1.0.0-rc.87@sha256:82527bb1fe813d1055b1cec04a1228cebeed8523b330a9dfff754e575b682a60` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.87@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.87@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:1.0.0-rc.87@sha256:0bf44c81d90d5012ecdfcb6c7837c1b79c9af0fc8191183a52a19d0a2c56853c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:1.0.0-rc.87@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-da-registry-1.0.0-rc.87.tgz -n da-registry --reset-values -f environments/staging/values/da.yaml --wait --timeout 15m
```

## 1.0.0-rc.84

<!-- source-commit: 9dc1ebfea8706c5d2d5332c1220210e15c407be8 version: 1.0.0-rc.84 -->
Published 2026-11-05. Archive SHA-256 `ae48b9fa2e20f097c7ba1d8943247737c79c2d9e4b8cfc5c5a938d92cae65a47`.

- Change: Merge pull request #43 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/da-registry@9dc1ebfea870](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/9dc1ebfea8706c5d2d5332c1220210e15c407be8)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:1.0.0-rc.84@sha256:0d67b3258027f84a36137a9c9303ff9b31148e8f6091d2f67d0fc17a5d8e53ab` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:1.0.0-rc.84@sha256:82527bb1fe813d1055b1cec04a1228cebeed8523b330a9dfff754e575b682a60` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.84@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1.0.0-rc.84@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:1.0.0-rc.84@sha256:0bf44c81d90d5012ecdfcb6c7837c1b79c9af0fc8191183a52a19d0a2c56853c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:1.0.0-rc.84@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-da-registry-1.0.0-rc.84.tgz -n da-registry --reset-values -f environments/staging/values/da.yaml --wait --timeout 15m
```

