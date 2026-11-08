# openg2p-da-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

