# openg2p-cropsown-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.512

<!-- source-commit: 8db1a47c847519997f1c5f21c6fc97f2a96f9d9d version: 1.0.0-rc.512 -->
Published 2026-11-10. Archive SHA-256 `8bf27f0a16895c95ef705f88e7e697ebe624770a12f542644bc17f657d7e29a0`.

- Change: Staging connector: expect the staging Keycloak issuer (#263)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@8db1a47c8475](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/8db1a47c847519997f1c5f21c6fc97f2a96f9d9d)
- Changes since 1.0.0-rc.508: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/7880d51210c46b996070f8d8413c02bd284bf6b2...8db1a47c847519997f1c5f21c6fc97f2a96f9d9d

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.512@sha256:988099c5d872a8f2733beafe1385c1de15dd494da768a71cb406d97183669cd0` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.512@sha256:148b58776eed7d072ddc6f621fd7282b43b62ae5c753edb65a65e59b0ce3237f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.512@sha256:1067fa46b08e2a702064d60c914f32dec5067f58cbecfaa376810c2c5feaa742` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.512@sha256:1067fa46b08e2a702064d60c914f32dec5067f58cbecfaa376810c2c5feaa742` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.512@sha256:cbc1c6e637031028d04b195e0c1a5321f972a0a7839d7d80e3f8bb8d98ccd5df` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.512@sha256:22b1898810c2785dd1981295a4c68c4e7c2b75946919a76c1f5418df5552e035` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.512@sha256:dc15203a17ee303ce6f1ac27b4550ffe5dfc27fad010a600514f73aa3fd2c29a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.512@sha256:6701e33f2b28fbe8f85526f4601de710b4c78c9e10a79b046b010ab486f8c211` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.512@sha256:9ac89fbf35bb645f761d7d1e5334ced71f5af2f59b6081ea71692e2703aa787f` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.512.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

## 1.0.0-rc.508

<!-- source-commit: 7880d51210c46b996070f8d8413c02bd284bf6b2 version: 1.0.0-rc.508 -->
Published 2026-11-10. Archive SHA-256 `a1865db8af0b1313b746d19aa4ee5c3b8bba68f98f8fb898bcee256f5fb516df`.

- Change: Staging connector upgrade: parse on the build agents' bash 4.2 (#258)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@7880d51210c4](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/7880d51210c46b996070f8d8413c02bd284bf6b2)
- Changes since 1.0.0-rc.503: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/97e9a92e1fb86f20019efb1241102554074d2826...7880d51210c46b996070f8d8413c02bd284bf6b2

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.508@sha256:feae223e997182d8507a902c680f812256ca34a49e3f4f500dca6f3710932148` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.508@sha256:eca573befd47fc76888682d8719bfc84349ec1d45dcdaff6939757a71ff2bc86` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.508@sha256:bd3e8ec6f63f0534599698ddeef7d80fa76603bf6a568b2b19a2cf3a2b5be8ff` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.508@sha256:bd3e8ec6f63f0534599698ddeef7d80fa76603bf6a568b2b19a2cf3a2b5be8ff` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.508@sha256:f40d9599491d030de00b3875f90efb28902e72a5b6fed74a575aa3d4788e8913` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.508@sha256:85156a5fd5c605538cf8d4dd8232797b9d87ba1bd316a532b3381994468ad967` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.508@sha256:5b3bf8199becb1320d78527d1b6682afc6c0cee2ec0d83ddb6f4fb3f8805f5f8` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.508@sha256:0fd057d3c61bf32e25f86f6366fce9b007a9293988c2b03100b298e5e8a70e17` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.508@sha256:a4d2d6bc6983c9d43e0b065d1495a7188aa0114067bd3c30ced06ace9a0ec76f` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.508.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

## 1.0.0-rc.503

<!-- source-commit: 97e9a92e1fb86f20019efb1241102554074d2826 version: 1.0.0-rc.503 -->
Published 2026-11-08. Archive SHA-256 `aa5b6dbba51d4e41a90e83470576300eca39947398ea975338e048fa74c40988`.

- Change: Operator job: a parameter to accept a deliberate connector chart change (#253)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@97e9a92e1fb8](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/97e9a92e1fb86f20019efb1241102554074d2826)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.503@sha256:b5443b0e56c10e288200c21789dbcfe0ef2bd0ac7f24d59f1c740dc5197bd0b7` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.503@sha256:3a0b820e2ab6d44e9e3a69e8602a9f0d3f47d6949640bdfa8c77b3419f9794b8` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.503@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.503@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.503@sha256:c79eb58105666e937558f43724c12bcf617890b99524aabe2e1c309aecd50864` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.503@sha256:8e656d962a466803f02dc43442aac79cf73832b207149cd159080c25eeba3b57` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.503@sha256:f2eeada6551ff6be1b1b3d4edf07914b1e50f33b7679c53aa05392d4c86d593c` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.503@sha256:2dfde9e664de3d1a8f61a8149daede9889e57e3914703d163027046693218739` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.503@sha256:77e5859ab4b343b897b0d6cfe3c84220e27a6261fba8acf9204e4b0d7565af8c` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.503.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

