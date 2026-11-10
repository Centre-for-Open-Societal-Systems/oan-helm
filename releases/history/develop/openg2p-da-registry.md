# openg2p-da-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.87

<!-- source-commit: b2eea8171fadc4c9dcb1c953e2511cc70ff87530 version: 0.0.0-develop.87 -->
Published 2026-11-10. Archive SHA-256 `8612c8631803bbbfe5c67acae993b2642dbad1b0e13613430365bfdf11ad8627`.

- Change: Add a load sample data option to the staging build (#51)
- Source: [Centre-for-Open-Societal-Systems/da-registry@b2eea8171fad](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/b2eea8171fadc4c9dcb1c953e2511cc70ff87530)
- Changes since 0.0.0-develop.86: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/ea2fa29f43af527d4a7d8345f8b62db413d93408...b2eea8171fadc4c9dcb1c953e2511cc70ff87530

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:b2eea8171fad@sha256:1e4f683b907e9c0293c1d28b6b4ff0dabecc12b7e53e83f30aa94e68c9625b51` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:b2eea8171fad@sha256:a1b549c78151990dd29e5b620e52489efd1f0052478bcf422e430305f8d47722` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:b2eea8171fad@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:b2eea8171fad@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:b2eea8171fad@sha256:cb8cfdc0dc07a826c089c9b33f6cc4f991d08c210a6f4022dff6413a5f20b6ef` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:b2eea8171fad@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.87.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.86

<!-- source-commit: ea2fa29f43af527d4a7d8345f8b62db413d93408 version: 0.0.0-develop.86 -->
Published 2026-11-09. Archive SHA-256 `cfc18c4eb7e4b5db18f96e4a03ec97254a2aa66463f8902d7f2da0eeb71d2f74`.

- Change: Right-align and group every number widget in the DA register (#49)
- Source: [Centre-for-Open-Societal-Systems/da-registry@ea2fa29f43af](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/ea2fa29f43af527d4a7d8345f8b62db413d93408)
- Changes since 0.0.0-develop.85: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/acf5e374a852bf6fe634de6f100dc4e7f845f058...ea2fa29f43af527d4a7d8345f8b62db413d93408

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:ea2fa29f43af@sha256:1e4f683b907e9c0293c1d28b6b4ff0dabecc12b7e53e83f30aa94e68c9625b51` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:ea2fa29f43af@sha256:a1b549c78151990dd29e5b620e52489efd1f0052478bcf422e430305f8d47722` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:ea2fa29f43af@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:ea2fa29f43af@sha256:39edbb87e7caa7cb3e8954c6e637e73169e5e42da64d126dc7abe8b03c093ce5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:ea2fa29f43af@sha256:cb8cfdc0dc07a826c089c9b33f6cc4f991d08c210a6f4022dff6413a5f20b6ef` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:ea2fa29f43af@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.86.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.85

<!-- source-commit: acf5e374a852bf6fe634de6f100dc4e7f845f058 version: 0.0.0-develop.85 -->
Published 2026-11-08. Archive SHA-256 `6f6115ba1c79faa0bb47152f320ebe4fb2e8da133bfd57ca405e9172870d7543`.

- Change: DA staging deploys on merge with no Build with Parameters (#47)
- Source: [Centre-for-Open-Societal-Systems/da-registry@acf5e374a852](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/acf5e374a852bf6fe634de6f100dc4e7f845f058)
- Changes since 0.0.0-develop.83: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/9dc1ebfea8706c5d2d5332c1220210e15c407be8...acf5e374a852bf6fe634de6f100dc4e7f845f058

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:acf5e374a852@sha256:0d67b3258027f84a36137a9c9303ff9b31148e8f6091d2f67d0fc17a5d8e53ab` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:acf5e374a852@sha256:82527bb1fe813d1055b1cec04a1228cebeed8523b330a9dfff754e575b682a60` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:acf5e374a852@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:acf5e374a852@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:acf5e374a852@sha256:0bf44c81d90d5012ecdfcb6c7837c1b79c9af0fc8191183a52a19d0a2c56853c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:acf5e374a852@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.85.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.83

<!-- source-commit: 9dc1ebfea8706c5d2d5332c1220210e15c407be8 version: 0.0.0-develop.83 -->
Published 2026-11-05. Archive SHA-256 `a69fe54de600bd9883511de2bcf54dcc6edc4732508ae98bda3974e7fcf6da5e`.

- Change: Merge pull request #43 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/da-registry@9dc1ebfea870](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/9dc1ebfea8706c5d2d5332c1220210e15c407be8)
- Changes since 0.0.0-develop.81: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/4ad52ab0f37556383a0b51b32677e7237e710e1c...9dc1ebfea8706c5d2d5332c1220210e15c407be8

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:9dc1ebfea870@sha256:0d67b3258027f84a36137a9c9303ff9b31148e8f6091d2f67d0fc17a5d8e53ab` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:9dc1ebfea870@sha256:82527bb1fe813d1055b1cec04a1228cebeed8523b330a9dfff754e575b682a60` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:9dc1ebfea870@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:9dc1ebfea870@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:9dc1ebfea870@sha256:0bf44c81d90d5012ecdfcb6c7837c1b79c9af0fc8191183a52a19d0a2c56853c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:9dc1ebfea870@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.83.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.81

<!-- source-commit: 4ad52ab0f37556383a0b51b32677e7237e710e1c version: 0.0.0-develop.81 -->
Published 2026-11-05. Archive SHA-256 `9b5e3c57d1256b571e15209c11232d32df0f27390f27750ed1a6e1c47aabdaa3`.

- Change: Move the DA chart into this repository and deploy the chart each build packages
- Source: [Centre-for-Open-Societal-Systems/da-registry@4ad52ab0f375](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/4ad52ab0f37556383a0b51b32677e7237e710e1c)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:4ad52ab0f375@sha256:0d67b3258027f84a36137a9c9303ff9b31148e8f6091d2f67d0fc17a5d8e53ab` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:4ad52ab0f375@sha256:82527bb1fe813d1055b1cec04a1228cebeed8523b330a9dfff754e575b682a60` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:4ad52ab0f375@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:4ad52ab0f375@sha256:a1fb9d4ccbc8d86bf7265ea7fbdc58d05b234f4e236154bf0d1bea8eab09241a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:4ad52ab0f375@sha256:0bf44c81d90d5012ecdfcb6c7837c1b79c9af0fc8191183a52a19d0a2c56853c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:4ad52ab0f375@sha256:2e7beae5f18882d342203f5b49bd2248ae13a5239bfd8ed0fa0a5780e1c40281` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.81.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

