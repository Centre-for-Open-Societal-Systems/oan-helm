# openg2p-cropsown-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.523

<!-- source-commit: 2af99b4c005ca99de92ed6b35f964a5c7545e646 version: 1.0.0-rc.523 -->
Published 2026-11-11. Archive SHA-256 `0314fb84cb8f61bd72dfeeed93c7cb490de815fdb8ca5089efb2aa976f142b98`.

- Change: AWE callback registration follows the registry's HMAC Secret (#274)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@2af99b4c005c](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/2af99b4c005ca99de92ed6b35f964a5c7545e646)
- Changes since 1.0.0-rc.521: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/6a554d1708b328d97db3307ecbbd44a33dd1b422...2af99b4c005ca99de92ed6b35f964a5c7545e646

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.523@sha256:774ab78dec7d1061511b6da5400cacfac44e88c20a272c49e60d0a05eebf032d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.523@sha256:24fd80e884c2ad1b6966c5fb2fcfdcb4953603d5611675fc68cab63393c1c574` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.523@sha256:05c7043065c3f3ea56db02797103bd7350106d4b347b23ec3ab95e95887c5849` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.523@sha256:05c7043065c3f3ea56db02797103bd7350106d4b347b23ec3ab95e95887c5849` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.523@sha256:3d7bc0d94d425c1d90afea524761908ac6e5079858c25b118a192c92b0de33ce` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.523@sha256:7096fca354f54f560e27251d9c69c7c76eeb64ad3e5feebce58d2fceffd5c77d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.523@sha256:83d1e05cc5b6c8fce61b33e9a43c606bbd606afe8ec5160ec4a39ca32beeda47` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.523@sha256:bb01176a357aa3cf79559dc410f0b64b0f7e4eb878595908aea6933ac8442890` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.523@sha256:64d16738ba49e1db08da6ee0188e10681917cfde3e80fd48257cf21c161cd7ee` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.523.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

## 1.0.0-rc.521

<!-- source-commit: 6a554d1708b328d97db3307ecbbd44a33dd1b422 version: 1.0.0-rc.521 -->
Published 2026-11-11. Archive SHA-256 `a73484f29a2894d82c1effe37213148db9c7a151b6125a98c5bb9284427cb800`.

- Change: Staging connector: sign Farmer-reference deliveries with the crop lookup key (#272)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@6a554d1708b3](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/6a554d1708b328d97db3307ecbbd44a33dd1b422)
- Changes since 1.0.0-rc.519: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/36d4f2277c7a7ac82a8f4d77492fc50b0783fc28...6a554d1708b328d97db3307ecbbd44a33dd1b422

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.521@sha256:0673c76d312112cc2cfdf3e1bbb29f26feed32b3d4a324abeb1c286e51e6dba6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.521@sha256:e5f5849aca2fabfb148b3b759925f39cb5f065252479877a99194473f255dc6a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.521@sha256:1ea2439617bdb2d835fd3b22764c713ac51a202314c7a5f727ba9b977aecdbe5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.521@sha256:1ea2439617bdb2d835fd3b22764c713ac51a202314c7a5f727ba9b977aecdbe5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.521@sha256:d7c53851e888f3159647733cfa7d183d5ee1e8b19960350276994573f2b4f61f` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.521@sha256:b4d48ae8ba15519657a0e43ec27805613fa132cbb916507ccbab8d93e627aef9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.521@sha256:448a628b9780f0dcb2824d2d514177fae9507a1bcb3c49b05b0651afd68c6388` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.521@sha256:ecefc598e0dc2527f72031ceaf16646ec649e1a59581dfad4af470da2942e372` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.521@sha256:627c6be725ae6c60554d601420daba483d4c8442fe5e4cf1a517dd90ca6e1cde` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.521.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

## 1.0.0-rc.519

<!-- source-commit: 36d4f2277c7a7ac82a8f4d77492fc50b0783fc28 version: 1.0.0-rc.519 -->
Published 2026-11-11. Archive SHA-256 `cfc60a6dc6da0bbc25d69d1491b2852dbef3556845953a2b3cc9dba1f120d8d6`.

- Change: CI: on-demand agents: ECR layer cache, retry on agent loss, real Postgres readiness (#268)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@36d4f2277c7a](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/36d4f2277c7a7ac82a8f4d77492fc50b0783fc28)
- Changes since 1.0.0-rc.512: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/8db1a47c847519997f1c5f21c6fc97f2a96f9d9d...36d4f2277c7a7ac82a8f4d77492fc50b0783fc28

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.519@sha256:4992ed62d3c40daea3bcdcb1199aa4ead72eae69eb2a225282ae9564ae373bae` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.519@sha256:cc907e2e9abf307aa0a4d684eb6273bc9252976fb13af7b678614c6a000c309b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.519@sha256:3e8646709f326091db11cb87736a39d00e7ed041633c7164ab2fb4e0b8abe27f` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.519@sha256:3e8646709f326091db11cb87736a39d00e7ed041633c7164ab2fb4e0b8abe27f` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.519@sha256:2d0ae5f19fad8ef0e9c3901c9e157af8ff07ea9fe9e0ab148c2c5b2c94f9b9e0` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.519@sha256:f160efa5edbeddfd1eb5d0c026ab650d4ff7e1cea393e4cb12cc365f83b23c34` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.519@sha256:8ceaccaa96c9dc7b6089bfcee4d1f28fc140ff0921e975ea228cdc2ff2fccb2b` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.519@sha256:f10d60601ea34fd5152fd5fbf77e0ed9a4b1ed561859daf8fc76cc65688154d5` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.519@sha256:c23273d0c79280dba3325ebb039f637f5fdf9417839ec5e656e5642eaef04a6a` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.519.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

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

