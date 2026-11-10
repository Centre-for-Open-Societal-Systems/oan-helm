# openg2p-cropsown-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.504

<!-- source-commit: 7880d51210c46b996070f8d8413c02bd284bf6b2 version: 0.0.0-develop.504 -->
Published 2026-11-10. Archive SHA-256 `9c9d8efce6b6380d8ba692d6bc7e57281da66b4c5944521b58d5e148c3be6ed8`.

- Change: Staging connector upgrade: parse on the build agents' bash 4.2 (#258)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@7880d51210c4](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/7880d51210c46b996070f8d8413c02bd284bf6b2)
- Changes since 0.0.0-develop.503: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/98014b3200cd75c9fdc018143a39a622290b8590...7880d51210c46b996070f8d8413c02bd284bf6b2

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-266@sha256:feae223e997182d8507a902c680f812256ca34a49e3f4f500dca6f3710932148` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-266@sha256:eca573befd47fc76888682d8719bfc84349ec1d45dcdaff6939757a71ff2bc86` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-266@sha256:bd3e8ec6f63f0534599698ddeef7d80fa76603bf6a568b2b19a2cf3a2b5be8ff` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-266@sha256:bd3e8ec6f63f0534599698ddeef7d80fa76603bf6a568b2b19a2cf3a2b5be8ff` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-266@sha256:f40d9599491d030de00b3875f90efb28902e72a5b6fed74a575aa3d4788e8913` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-266@sha256:85156a5fd5c605538cf8d4dd8232797b9d87ba1bd316a532b3381994468ad967` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-266@sha256:5b3bf8199becb1320d78527d1b6682afc6c0cee2ec0d83ddb6f4fb3f8805f5f8` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-266@sha256:0fd057d3c61bf32e25f86f6366fce9b007a9293988c2b03100b298e5e8a70e17` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:a4d2d6bc6983c9d43e0b065d1495a7188aa0114067bd3c30ced06ace9a0ec76f` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.504.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.503

<!-- source-commit: 98014b3200cd75c9fdc018143a39a622290b8590 version: 0.0.0-develop.503 -->
Published 2026-11-09. Archive SHA-256 `943d2e5baa113785cf3d238dc9da4f1f4ed406775294e6e47825dac0b7ba9b7e`.

- Change: Accept the farmer.profile.updates.v1 event name next to the three older names (#259)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@98014b3200cd](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/98014b3200cd75c9fdc018143a39a622290b8590)
- Changes since 0.0.0-develop.502: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/4875c5686ee221a34bbbbda888521b4ff9673751...98014b3200cd75c9fdc018143a39a622290b8590

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-265@sha256:100fb98115826ea262b4441ec9fa7786a0c5f1da8ac76929e7451576849dce34` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-265@sha256:c399188596e1f3cec25332efd1abd7a74818f81839e261b670d8373cebe5c604` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-265@sha256:820dbd70ec0255162fd5ca94eb5ab2eff68b5514762c4edc458a5fdd89daf575` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-265@sha256:820dbd70ec0255162fd5ca94eb5ab2eff68b5514762c4edc458a5fdd89daf575` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-265@sha256:8532eedcb74258b0eb828b831496a4cc89517183c0ccc540e88e3c49765a4779` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-265@sha256:851f3a90d0373943fe52459da522978d576a6a8be333be8d566b9ff91e8207ee` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-265@sha256:bdc73a808207132ce5c09987b37cd1a398d8486115d76e76bd7bb863886fa42e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-265@sha256:0a9babd10f978770385248c7960bbd152be066cae26356df8465a92af8ca94df` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:8d7163fa174a19eb7986d5f9401d11a9f33e326ebdf3d46b8128322b79518b9a` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.503.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.502

<!-- source-commit: 4875c5686ee221a34bbbbda888521b4ff9673751 version: 0.0.0-develop.502 -->
Published 2026-11-09. Archive SHA-256 `15673d6748379496610396db99e837fd83e39504abfc766ece057f63ac620904`.

- Change: Right-align and group every number widget in the crop register (#256)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@4875c5686ee2](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/4875c5686ee221a34bbbbda888521b4ff9673751)
- Changes since 0.0.0-develop.500: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/97e9a92e1fb86f20019efb1241102554074d2826...4875c5686ee221a34bbbbda888521b4ff9673751

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-264@sha256:6e01e8c48df3d2c7157921f91fe57134082aba542ff3e19c19b5f08f702b2c41` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-264@sha256:865f3f0258fadd1980ec7c31658f9bc4756f54c82169889db34fb6aa38bf2669` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-264@sha256:219447fa5d01fbd63fb16a7df04b12b78432d118d5f6800f5bd5172fbab1432e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-264@sha256:219447fa5d01fbd63fb16a7df04b12b78432d118d5f6800f5bd5172fbab1432e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-264@sha256:c373ee24ba99893894180710f2aec3e8767addee68b14d50e3be239c69d342ad` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-264@sha256:f947a8e4115740e6caa307a0f153036efb007fcddedc14702511272cf3203ad3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-264@sha256:ce54c1733a1ed028f2a7ebc0d0d64a26ba257490e5eb16daae5e0beed9cc056b` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-264@sha256:dab21bade2c7e15d6f4208d88b91f1e3e4758bbf635138f4608a0f6bf6e7d161` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:8eec376e37a164fe267f90f5cf6710ea88bfb0cd51e25922601c8448e8b97765` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.502.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.500

<!-- source-commit: 97e9a92e1fb86f20019efb1241102554074d2826 version: 0.0.0-develop.500 -->
Published 2026-11-08. Archive SHA-256 `529c882fc314ea5f8faf8d6a60725e726f7909fc707dc27b95507e4bacfff1e6`.

- Change: Operator job: a parameter to accept a deliberate connector chart change (#253)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@97e9a92e1fb8](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/97e9a92e1fb86f20019efb1241102554074d2826)
- Changes since 0.0.0-develop.499: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/5287a40657f0b711cfd511ad809af7bc822c3dfd...97e9a92e1fb86f20019efb1241102554074d2826

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-262@sha256:b5443b0e56c10e288200c21789dbcfe0ef2bd0ac7f24d59f1c740dc5197bd0b7` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-262@sha256:3a0b820e2ab6d44e9e3a69e8602a9f0d3f47d6949640bdfa8c77b3419f9794b8` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-262@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-262@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-262@sha256:c79eb58105666e937558f43724c12bcf617890b99524aabe2e1c309aecd50864` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-262@sha256:8e656d962a466803f02dc43442aac79cf73832b207149cd159080c25eeba3b57` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-262@sha256:f2eeada6551ff6be1b1b3d4edf07914b1e50f33b7679c53aa05392d4c86d593c` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-262@sha256:2dfde9e664de3d1a8f61a8149daede9889e57e3914703d163027046693218739` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:77e5859ab4b343b897b0d6cfe3c84220e27a6261fba8acf9204e4b0d7565af8c` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.500.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.499

<!-- source-commit: 5287a40657f0b711cfd511ad809af7bc822c3dfd version: 0.0.0-develop.499 -->
Published 2026-11-08. Archive SHA-256 `9f4db2a252aa60eef4f6ae714b9a88356b2b54b1d43054a20a9d117983ed2122`.

- Change: Wait for every table the crop reporting views read before applying them (#252)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@5287a40657f0](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/5287a40657f0b711cfd511ad809af7bc822c3dfd)
- Changes since 0.0.0-develop.498: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/e1fa219edac4535eaf399e132fdba11b3bf27c7e...5287a40657f0b711cfd511ad809af7bc822c3dfd

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-261@sha256:3923ea486955142fb3523f5c59474f99cd1dba899622de6f05e1fee9e9bb4c92` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-261@sha256:da43e16378e99d31296aadf3b67dab0b656b06c99e92b51284278ab84b70a09d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-261@sha256:04931900e042919e63f7419adf176d20fb5f7db00321cf37dd6b503a380f72ff` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-261@sha256:04931900e042919e63f7419adf176d20fb5f7db00321cf37dd6b503a380f72ff` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-261@sha256:0c8fe909264abf6bf653deef9848cd5aafe538f494f2014c5525811bb722d675` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-261@sha256:4e532ac2b307aa9313e086a41631ab076242c3df7b8535a821ade5eba77c6225` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-261@sha256:e3c90a234ea1c28e6a174912a14f1b1d6cf01cb643681d00e7523626ac4992ac` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-261@sha256:947d50fcdaf0987c670f6cac7986fab620052f7885e02e06ee7ca1deff657f6a` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:2bc6e2ebd03ebeaad0cefcb0b6932ac742764215977b028f3b2d32c176e2b3e2` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.499.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.498

<!-- source-commit: e1fa219edac4535eaf399e132fdba11b3bf27c7e version: 0.0.0-develop.498 -->
Published 2026-11-08. Archive SHA-256 `f9c0410e2a7b8f7f79e30cafc1f7df9ddc5662b36e334e99f3fb9571c3c3b990`.

- Change: Seed renames the Farmer-reference tables before it writes the archive (#251)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@e1fa219edac4](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/e1fa219edac4535eaf399e132fdba11b3bf27c7e)
- Changes since 0.0.0-develop.496: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/bad56edad2ed14027813f8a553db2cace1c57fe3...e1fa219edac4535eaf399e132fdba11b3bf27c7e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-260@sha256:cba23ac0247fc39303214d8f0e10a94ff3ea0a3f8a5abb951cd9769cd195d9cf` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-260@sha256:095a0a7147e794599c6f1934bc2a2e8037aa7bcd87f91edea8859a0516c3a246` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-260@sha256:8e7197616ae2c7bbecd4f0790fe8e6e261d55e15266c5be230b544b4ad0f79de` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-260@sha256:8e7197616ae2c7bbecd4f0790fe8e6e261d55e15266c5be230b544b4ad0f79de` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-260@sha256:765ddf5f05e8a6f1a27ebedfe1023e97c4a07c907384300f76048454f3f95809` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-260@sha256:f474f32adedd629860465a6aca9effd7a32c3266133d3f656c9106ecc04581a9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-260@sha256:c6f859de3e83bf6f2b7b3d049091507fb13b559ef53241cfbf9d0523e3986150` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-260@sha256:cb9355c783e264a8245e9704ec41bd0fef0821dcaa6a3424607dcd65b9c42955` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:8955d245a35ce467a54520175199ba9c9946c49f31722b82d0d52b45dfaa2425` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.498.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.496

<!-- source-commit: bad56edad2ed14027813f8a553db2cace1c57fe3 version: 0.0.0-develop.496 -->
Published 2026-11-08. Archive SHA-256 `c28275cbcfa00b2c3f1b0e2d670b398c88f758c36bccd7038ba1813e98c64364`.

- Change: Upgrade the staging crop connector to the registry-connector image from the pipeline (#246)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@bad56edad2ed](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/bad56edad2ed14027813f8a553db2cace1c57fe3)
- Changes since 0.0.0-develop.494: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/3ee052a6b0de1c3f3483538211f9983c71ed55d9...bad56edad2ed14027813f8a553db2cace1c57fe3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-259@sha256:3af039dd6d5c800b9a1874e607c76e2997454ed33a3060578ff2f1e7d0c78e32` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-259@sha256:6244496edce112cf9d2d54d1236cd6b7e106f9b6168d25d24385c6d835997fd3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-259@sha256:973cce34830c7cd3f9542ee334087b399529acfc150191dfa724a7c6590746b7` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-259@sha256:973cce34830c7cd3f9542ee334087b399529acfc150191dfa724a7c6590746b7` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-259@sha256:4d355d67d612c2b481ebec3fc0dce52ec2070d8668fb0e8b3ece95821148000a` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-259@sha256:d6a6ba154edfc975282d32c6e2aa2f9108615205cd8b0b0c3748c3fd8f3fa3b5` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-259@sha256:b195269d39429c7c207cb95b8642292ad7a9d9404fe21cd1d792c0c8f4f302e2` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-259@sha256:3ebcd40a7ad167fd109617e45f8e786e9bb016909deaf56dfe6238c23ecfc257` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:6e17fbd42f233daef48ad671bcde54dfac2dbfa736bebf1b1238dbac1552ff97` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.496.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.494

<!-- source-commit: 3ee052a6b0de1c3f3483538211f9983c71ed55d9 version: 0.0.0-develop.494 -->
Published 2026-11-06. Archive SHA-256 `1f5b971e44603d9958d236edf9b384247929b12d760fe32b9c689da97cf9dabb`.

- Change: Crop chart refreshes its own ECR pull secret and stops loading seed images (#247)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@3ee052a6b0de](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/3ee052a6b0de1c3f3483538211f9983c71ed55d9)
- Changes since 0.0.0-develop.493: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/4a4c2fa3a91e9205cee3e8950af638ec2b1004d7...3ee052a6b0de1c3f3483538211f9983c71ed55d9

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-258@sha256:d3fabe065f95a1d02d10733d557fcfdff87487a5c851812e67b73437ff291875` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-258@sha256:3217a3a89730711962021f0410a6c3a8697f3f8f615f7f9179151cb11891f87e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-258@sha256:cd91fd28780d48ba827dbd860e913d3ecb734839e830afcf2f5a3171b2846df5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-258@sha256:cd91fd28780d48ba827dbd860e913d3ecb734839e830afcf2f5a3171b2846df5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-258@sha256:10efd0a030e388344a71ada7d2e10d890f7e1b96fede3522023cb65f53ae5069` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-258@sha256:77e38563e1bceabe7528aae3b5d4b482f925557198fb4288e2d644fde0f829da` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-258@sha256:b640a620029f8c44a1d1ad216c6b8811ba6d6f4dbba4adb0a343b0bf4efdc7e0` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-258@sha256:228dc21694adde6ac4d122551aa9129191e0a6abb505dc980ba004fa190f61d1` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:f52df392e9f71f32d0a4810e7a1eb244f772732f86dc7593f96de2ac07269843` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.494.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.493

<!-- source-commit: 4a4c2fa3a91e9205cee3e8950af638ec2b1004d7 version: 0.0.0-develop.493 -->
Published 2026-11-06. Archive SHA-256 `d9aebefd1cced331a053b47fd4508cd07dddd9b158955e3eb66a328de4607c02`.

- Change: Declare crop connector definitions in git and apply them with a Helm hook (#245)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@4a4c2fa3a91e](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/4a4c2fa3a91e9205cee3e8950af638ec2b1004d7)
- Changes since 0.0.0-develop.489: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/deabbfe47dca3509099d9e2b2af94a017c50fa44...4a4c2fa3a91e9205cee3e8950af638ec2b1004d7

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-257@sha256:b27dbe6a8bab4dc7348dcbc036dbeb393cedfe339c5de167815b5657a1caf09a` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-257@sha256:97c65e03be801aed35e201d91951f99dd1738e552c0ea2808c44b6cdec6bd285` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-257@sha256:d3e499f3e3acec9dc7b7c8259f5a30faf89bc5e067c0dcb5b4acb7a5bdb3121a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-257@sha256:d3e499f3e3acec9dc7b7c8259f5a30faf89bc5e067c0dcb5b4acb7a5bdb3121a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-257@sha256:7c592d594abc4edf721114e8c9df1a1b679a68d3d1371b03dcff533475babacc` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-257@sha256:00ca2509339f3f477f4953cab123645ebc30685352014d5d19c232fef92f5e5b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-257@sha256:d2f8116ec0691fab359d028c4565648f3c64db39b522c0a881f64714eca52f1d` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-257@sha256:e1e1b3168e666605ae1e284ceff130606c253cd98578050be19e53cfbdf6dd1a` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:af689fdb8e5d073b7c1f03d17404e5ee2d8b4d67c3c89963d22f1cd80f0eb3fa` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.493.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.489

<!-- source-commit: deabbfe47dca3509099d9e2b2af94a017c50fa44 version: 0.0.0-develop.489 -->
Published 2026-11-06. Archive SHA-256 `9831c87dae764bc62de0db2b63f155ecdcb20b6c22d215ef9e1c2bb892fba7aa`.

- Change: Run the browser tests on Ubuntu 24.04 (#244)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@deabbfe47dca](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/deabbfe47dca3509099d9e2b2af94a017c50fa44)
- Changes since 0.0.0-develop.488: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/fbe5a37e41f2e7a98ed9283b4825a0a5b4be6f4c...deabbfe47dca3509099d9e2b2af94a017c50fa44

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-256@sha256:0f5f1e74fad726d4709945c5719b10078b02b6c5e41b2081f23c3467fa94a992` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-256@sha256:8bb5e557cb651ff41e282b5d3e370becb26b2c76377a419b55aff0c21bcafb9d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-256@sha256:42a29700419ea5ca751cfffcfa572785941f4b95bbc87ed458663f04fb5871d7` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-256@sha256:42a29700419ea5ca751cfffcfa572785941f4b95bbc87ed458663f04fb5871d7` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-256@sha256:c1a0d4387c6b054f5989084acef5fc193cd328cd51b4ca49dd3fbde4e5d21f53` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-256@sha256:fbedb507075c91ef201dc623e297fd7586d7c44875c8187d15cbbcd965823de6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-256@sha256:380f6e9421dca37e7ace9fc3b60590199eb3ddc7b092abaffd6c3dbe4a877114` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-256@sha256:53681f7fa1f6267ec63daf4e4f367590a034bb14dc544cf8d59c1f27508e192f` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:480562cd9d1fd5ffdd87142554d4e33cfd249e581a4119ff2be416e4e8fb31de` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.489.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.488

<!-- source-commit: fbe5a37e41f2e7a98ed9283b4825a0a5b4be6f4c version: 0.0.0-develop.488 -->
Published 2026-11-05. Archive SHA-256 `2dfcfcb93ca0c71ea8cfbb7ceb8d2537fb4ad5e2beb38e5122e31852f5afde9f`.

- Change: Merge pull request #239 from asmitonweb/use-pack-codes-for-growth-stage-and-severity
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@fbe5a37e41f2](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/fbe5a37e41f2e7a98ed9283b4825a0a5b4be6f4c)
- Changes since 0.0.0-develop.485: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/51d9894158b1b857e9573d927964a0c2f5a86bab...fbe5a37e41f2e7a98ed9283b4825a0a5b4be6f4c

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-255@sha256:383c77d877c8bdbe38d85d6a099ee5b4763fca5e95b15954d2c26a78d1290e11` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-255@sha256:eb03adfffa98c300b269d27ec4cbdb2c0f1dc5baa0720eb4034a7ea9a1a7e583` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-255@sha256:9214470ac064d48575997cd1a392dffa8cd328108bb3a3c29ee5e5b527377c61` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-255@sha256:9214470ac064d48575997cd1a392dffa8cd328108bb3a3c29ee5e5b527377c61` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-255@sha256:24018e6c0d16fa4bb097ce3cec6ed6bf7f4672ef04039c720c4a1c812090048e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-255@sha256:ca0e2a791cde08f2e9796d6504640e783251c8bcbeef41cd7375c2431fb9cfa5` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-255@sha256:9db3c37c0731cb16bc0aecc26237cdf25a8b7ecb9f3a16c850502683069f128e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-255@sha256:539614853774fe6ed2a947055f3cb2f512f0c9c594cd83227ce869442f17108d@sha256:397cef051fa9e4dc67262986363edbc91844ef23b85dceefd1024b3f4d15a782` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:bb332012424bf0bf5d54fdafaa6354b4479608fa8d4172896d7691f13ce7c622` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.488.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.485

<!-- source-commit: 51d9894158b1b857e9573d927964a0c2f5a86bab version: 0.0.0-develop.485 -->
Published 2026-11-05. Archive SHA-256 `b64af267a5c603d7bb187b6eff628d72410005471908e8eb844c6636a47ccc8f`.

- Change: Merge pull request #235 from asmitonweb/record-staging-history
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@51d9894158b1](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/51d9894158b1b857e9573d927964a0c2f5a86bab)
- Changes since 0.0.0-develop.469: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/e591be837fade714691def40905eacb39e6f42d4...51d9894158b1b857e9573d927964a0c2f5a86bab

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-253@sha256:1464abb0a75efc508bd41020d348723315442db697f7777875ab2fcef9bea8ca` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-253@sha256:45174ab70ddda5775ec8cadbc68d68cfc6576efb83d514e99f48c64078101d7b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-253@sha256:9c2b4e5e17d93d1a5a76fa971250d333963582e6330401570373eca73073e384` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-253@sha256:9c2b4e5e17d93d1a5a76fa971250d333963582e6330401570373eca73073e384` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-253@sha256:9606ad96110f79eb13675741e067384ce5de320ae89a075043686736f7871aae` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-253@sha256:0a3887b60ca84db33824be9458b67bf510f9df77af37d80a241672d304f1ff08` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-253@sha256:5b18400399c3a09e8bf13acb40a1d84af32edd0900597f37c1f6ec02bd40e3e0` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-253@sha256:1cdc73b004c02e7d7902be03d901788e46d5781ad55792c53c1473ab5515c93a@sha256:397cef051fa9e4dc67262986363edbc91844ef23b85dceefd1024b3f4d15a782` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:b1a283783430fcd105da6997357dd93c1449d40656d254bfa3610e44c8c21387` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.485.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.469

<!-- source-commit: e591be837fade714691def40905eacb39e6f42d4 version: 0.0.0-develop.469 -->
Published 2026-11-05. Archive SHA-256 `542faac61a6720114a13a884d7be469643a4106d69953928009d423e5c3a5e35`.

- Change: Merge pull request #234 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@e591be837fad](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/e591be837fade714691def40905eacb39e6f42d4)
- Changes since 0.0.0-develop.467: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/791c66f9d0081c29641f6396581d7b9d62c2078f...e591be837fade714691def40905eacb39e6f42d4

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-251@sha256:b3024a94ea05a2a5dab41a4cd6f91e951ee4f53a10372df9981c1fb15ad1a6aa` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-251@sha256:b3429e93a61de61bd72977603fde2658ea21db3fc932ebfe6afe3c9f0a7d6b99` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-251@sha256:ffc6eac9dc039e7965881d03b77eb01dc32ea35d4812ba9145c3cd60a384d025` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-251@sha256:ffc6eac9dc039e7965881d03b77eb01dc32ea35d4812ba9145c3cd60a384d025` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-251@sha256:ea73dfa94d197b9907a848f4ff8d3cbf44fd8a7910fe1dd9268640f68f7e9aa6` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-251@sha256:6caa12094505ddcf04d284c8737e47a7d3b95074c64dc83c229bb84177a89476` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-251@sha256:9f880764019a211eb2b50cd401a85c95c7e9accc481c9c575120183cd28afaac` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-251@sha256:599b6117db90c6d68842cd08e7d6a551cbd76eef9af6cd539eac28f8ca732a8f@sha256:397cef051fa9e4dc67262986363edbc91844ef23b85dceefd1024b3f4d15a782` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:dd2a9f31250ea0499dd4c9a5d35dda66a35c3eb08d1a4fce98b3576ca4531934` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.469.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.467

<!-- source-commit: 791c66f9d0081c29641f6396581d7b9d62c2078f version: 0.0.0-develop.467 -->
Published 2026-11-05. Archive SHA-256 `e957a78f5ff9c68235f0ac121f8197edbf3ffe79eec115d1bd112435e8d2021a`.

- Change: Move the Crop chart into this repository and deploy the chart each build packages
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@791c66f9d008](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/791c66f9d0081c29641f6396581d7b9d62c2078f)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-246@sha256:9e7e5ea1b13bb2be3cbbe033b01b99de24c1bbbbbb0db821b4d1807327e3ab0c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-246@sha256:cbad0bfd8647b24f15a24f05480386466760ed0888b249f85247a63bdfe7ceef` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-246@sha256:c4b23d51503c8531377afae17cc92739fbffe069abb89d1f58cf728b787310b2` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-246@sha256:c4b23d51503c8531377afae17cc92739fbffe069abb89d1f58cf728b787310b2` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-246@sha256:2091e56f1c54ba59994611b8024a204d383be7596edfa4723d637d6a85e256c9` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-246@sha256:ce7e414e89fc981bc508cea702c15f187e54dfc63c4f288ab52f89f6d0217944` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-246@sha256:0321540de125146a88bb2c4d937888a74e5eddc9b205330a0e246969368dfcd6` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-246@sha256:297a7f704d80e56b9eedd784b728c272af138ce0ef781597e9f347751a63b047@sha256:397cef051fa9e4dc67262986363edbc91844ef23b85dceefd1024b3f4d15a782` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:dbf8bd31ed64a7a77459662958d4583443572baf3265c7d812fce9fe09646304` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.467.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

