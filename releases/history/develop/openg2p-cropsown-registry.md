# openg2p-cropsown-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.519

<!-- source-commit: 63f88801416355011ae3f4f786c5debacabfd4b8 version: 0.0.0-develop.519 -->
Published 2026-11-12. Archive SHA-256 `503bcb8fa87c562649d617d9c68f310b8adfb2ff937264a4db281f3b630917af`.

- Change: Staging connector moves to the qa.oanstaging.com scope (#276)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@63f888014163](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/63f88801416355011ae3f4f786c5debacabfd4b8)
- Changes since 0.0.0-develop.518: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/9384c7f77f8eb5d4f3a83317e12802a82206e3e7...63f88801416355011ae3f4f786c5debacabfd4b8

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-286@sha256:07b1646dd74aed5eaf7c7ea0f38450d6edd59be6a98fbc8fbe799737dce42890` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-286@sha256:0c22114ea7bbf10c65b0d58fd0ad0e5901e3fe8134a80cc80b2599c89431eec6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-286@sha256:5c6a3dfb66c77bcba33f5a289059f97f4d50dae0d222a8eeb3977fbcda0ddd3d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-286@sha256:5c6a3dfb66c77bcba33f5a289059f97f4d50dae0d222a8eeb3977fbcda0ddd3d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-286@sha256:1331cebadca09f25ee5641796f9680e47aa6e8346e0bec7826b0f6693ab3f738` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-286@sha256:984e29a220898b8a2faf8dc22c94466a993035b0f8bdeb1b80da773966c6b489` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-286@sha256:8e00d378bc8cb5283b9bfcec98fcd7d5b98aef4d7e175189932ab01a8059d442` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-286@sha256:b02af2d78ba216e7f01711f751564567b2bf1cfc4a5d77616786b30339acbc18` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:53e9941f6b9a36b02fb68df65397e1a22fa9d0948b7add796652ae21a3e78d6e` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.519.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.518

<!-- source-commit: 9384c7f77f8eb5d4f3a83317e12802a82206e3e7 version: 0.0.0-develop.518 -->
Published 2026-11-12. Archive SHA-256 `b0a5369c0230b7ab4823f8a7b5438ed0c66449dff259a53dd376ff494df41bdf`.

- Change: Sample loader: no Address section; the land position goes on the Planning rows (#281)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@9384c7f77f8e](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/9384c7f77f8eb5d4f3a83317e12802a82206e3e7)
- Changes since 0.0.0-develop.517: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/afb7129dee430ce96fc115bfa4b4057ab4d96653...9384c7f77f8eb5d4f3a83317e12802a82206e3e7

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-284@sha256:f5b1a6587468ad163d1749dc827becff30f7191482672b05ac4dffe72e082c50` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-284@sha256:38d1bdf39008523a0560b1eec5cda335e709f60c5588b558baaf47578ef5b466` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-284@sha256:cddeba4f0e0507ebb3a3f0b20342268ad2dc12cb54c68b8b5ebc7d453990e7ca` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-284@sha256:cddeba4f0e0507ebb3a3f0b20342268ad2dc12cb54c68b8b5ebc7d453990e7ca` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-284@sha256:e8ae1143d40b4e8365d5edb65e18e08e11ad90393db5bcbbd436d89ac6f7dc2f` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-284@sha256:d186ca892f87308a2b926cf4f2368bd5c37730756bf89fdb01a91c5e5d46c422` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-284@sha256:bf58c92b5b9b3895f50c8e784a2784937eaecc36be01c7baad58413f7f711b70` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-284@sha256:9bf8605576e41c9c0203d6329500a9f0fdc068ae65849db803464be53b616ee1` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:c1b8bb9f522efda2f593143e3856248cc09b9a1f962e011f549c08bd6f0cd933` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.518.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.517

<!-- source-commit: afb7129dee430ce96fc115bfa4b4057ab4d96653 version: 0.0.0-develop.517 -->
Published 2026-11-12. Archive SHA-256 `dbe235fbd3cafd426136181d8dcf0aea7c2610712c4d9ca0d370677c90843a0b`.

- Change: db-seed: pin openg2p-data at the sample crop records with list codes (#279)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@afb7129dee43](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/afb7129dee430ce96fc115bfa4b4057ab4d96653)
- Changes since 0.0.0-develop.516: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/1329040a210c6729c95818c55db2803743c18127...afb7129dee430ce96fc115bfa4b4057ab4d96653

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-283@sha256:49de9cf471190ff0855f7bf205a1bfc428311da86d156df7bfa3f34086ac7e93` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-283@sha256:b883a5343d7ae1c2e9a5ab05d4895bce1f3f0a8877cf66e235569b354366ac15` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-283@sha256:d71f7ae14362b882f1d2caa46a69050dc4950810564e642cf6acb51332600f26` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-283@sha256:d71f7ae14362b882f1d2caa46a69050dc4950810564e642cf6acb51332600f26` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-283@sha256:9c447a8874f9b3f973ed1442858bbc2ff132d579838d4aabd041add66d749fc8` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-283@sha256:6919798848f4f98b424a3d97718a0963d9a0411c3e799bb2adc2abe7ed436d8a` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-283@sha256:84cb048360b167d3c8658da625e120674e71410c07e360c8f9a3120856900fea` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-283@sha256:8530c5fa1b3e8fde9d0e0750cba534ef637bc600f1ba691939cbd8a101898325` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:9cc8f6e0f6a826db13a455150e6d19ffa6f818f75f350683fb2366b270dc8240` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.517.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.516

<!-- source-commit: 1329040a210c6729c95818c55db2803743c18127 version: 0.0.0-develop.516 -->
Published 2026-11-12. Archive SHA-256 `d66a89c6b13352368d4c4867e26b4d9547a8bf004b842f300cc25f0a38955974`.

- Change: Crop Sown: land rows for Cultivation, Sowing and Harvest, maps, ODK forms, FIN farmers (#278)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@1329040a210c](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/1329040a210c6729c95818c55db2803743c18127)
- Changes since 0.0.0-develop.515: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/2af99b4c005ca99de92ed6b35f964a5c7545e646...1329040a210c6729c95818c55db2803743c18127

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-282@sha256:f10695398e84ea5ff971bf91306371212175ca6d13f6695d3fa074c394340441` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-282@sha256:69bee3609edc36754c7f45eb2040f33f23f97b12109a1fbdd0bee37f3f1ab9e9` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-282@sha256:7d177e58e97de441ace30ad4d654e03e7453433f61242994ef962ae16ca00d69` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-282@sha256:7d177e58e97de441ace30ad4d654e03e7453433f61242994ef962ae16ca00d69` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-282@sha256:e402323d6b9f2722b2d4079469786e40632e59af17fa90089c727def73c3d4e7` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-282@sha256:0ad8fecf32fc62600ddefdf25079782d51cb4504fdf1e9a589d529dccf817f1f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-282@sha256:c7fd89e72b9f8a83c58f0c8f099a9517b1cb2e668acdec70ed8580c58b854f0c` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-282@sha256:5a9d223e3b63a7082ca3b7421a5f4de3f4953bf2d1093819643388114a7714b3` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:a4583570a1b843bce8df7f04e0ddf8dca54e172497c82de17a9ab2009884d04f` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.516.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.515

<!-- source-commit: 2af99b4c005ca99de92ed6b35f964a5c7545e646 version: 0.0.0-develop.515 -->
Published 2026-11-11. Archive SHA-256 `89caa85ab5dbaf0486b4006feef1d342f4fb7e55fedc4617b797e7b7cb9068e7`.

- Change: AWE callback registration follows the registry's HMAC Secret (#274)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@2af99b4c005c](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/2af99b4c005ca99de92ed6b35f964a5c7545e646)
- Changes since 0.0.0-develop.514: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/6a554d1708b328d97db3307ecbbd44a33dd1b422...2af99b4c005ca99de92ed6b35f964a5c7545e646

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-281@sha256:774ab78dec7d1061511b6da5400cacfac44e88c20a272c49e60d0a05eebf032d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-281@sha256:24fd80e884c2ad1b6966c5fb2fcfdcb4953603d5611675fc68cab63393c1c574` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-281@sha256:05c7043065c3f3ea56db02797103bd7350106d4b347b23ec3ab95e95887c5849` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-281@sha256:05c7043065c3f3ea56db02797103bd7350106d4b347b23ec3ab95e95887c5849` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-281@sha256:3d7bc0d94d425c1d90afea524761908ac6e5079858c25b118a192c92b0de33ce` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-281@sha256:7096fca354f54f560e27251d9c69c7c76eeb64ad3e5feebce58d2fceffd5c77d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-281@sha256:83d1e05cc5b6c8fce61b33e9a43c606bbd606afe8ec5160ec4a39ca32beeda47` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-281@sha256:bb01176a357aa3cf79559dc410f0b64b0f7e4eb878595908aea6933ac8442890` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:64d16738ba49e1db08da6ee0188e10681917cfde3e80fd48257cf21c161cd7ee` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.515.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.514

<!-- source-commit: 6a554d1708b328d97db3307ecbbd44a33dd1b422 version: 0.0.0-develop.514 -->
Published 2026-11-11. Archive SHA-256 `b7ced36d76b29781776c56f9cbbe62620c5a76a89f623b6de5b3b151763fbbaf`.

- Change: Staging connector: sign Farmer-reference deliveries with the crop lookup key (#272)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@6a554d1708b3](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/6a554d1708b328d97db3307ecbbd44a33dd1b422)
- Changes since 0.0.0-develop.513: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/36d4f2277c7a7ac82a8f4d77492fc50b0783fc28...6a554d1708b328d97db3307ecbbd44a33dd1b422

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-280@sha256:0673c76d312112cc2cfdf3e1bbb29f26feed32b3d4a324abeb1c286e51e6dba6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-280@sha256:e5f5849aca2fabfb148b3b759925f39cb5f065252479877a99194473f255dc6a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-280@sha256:1ea2439617bdb2d835fd3b22764c713ac51a202314c7a5f727ba9b977aecdbe5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-280@sha256:1ea2439617bdb2d835fd3b22764c713ac51a202314c7a5f727ba9b977aecdbe5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-280@sha256:d7c53851e888f3159647733cfa7d183d5ee1e8b19960350276994573f2b4f61f` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-280@sha256:b4d48ae8ba15519657a0e43ec27805613fa132cbb916507ccbab8d93e627aef9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-280@sha256:448a628b9780f0dcb2824d2d514177fae9507a1bcb3c49b05b0651afd68c6388` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-280@sha256:ecefc598e0dc2527f72031ceaf16646ec649e1a59581dfad4af470da2942e372` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:627c6be725ae6c60554d601420daba483d4c8442fe5e4cf1a517dd90ca6e1cde` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.514.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.513

<!-- source-commit: 36d4f2277c7a7ac82a8f4d77492fc50b0783fc28 version: 0.0.0-develop.513 -->
Published 2026-11-10. Archive SHA-256 `0a57c991c7605deb69637e2b1d6b532ad331ee92dd28c3939b16d278135b352a`.

- Change: CI: on-demand agents: ECR layer cache, retry on agent loss, real Postgres readiness (#268)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@36d4f2277c7a](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/36d4f2277c7a7ac82a8f4d77492fc50b0783fc28)
- Changes since 0.0.0-develop.512: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/a0e7ca371f0b3b1d8769cd899dd43841eafcd903...36d4f2277c7a7ac82a8f4d77492fc50b0783fc28

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-279@sha256:4992ed62d3c40daea3bcdcb1199aa4ead72eae69eb2a225282ae9564ae373bae` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-279@sha256:cc907e2e9abf307aa0a4d684eb6273bc9252976fb13af7b678614c6a000c309b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-279@sha256:3e8646709f326091db11cb87736a39d00e7ed041633c7164ab2fb4e0b8abe27f` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-279@sha256:3e8646709f326091db11cb87736a39d00e7ed041633c7164ab2fb4e0b8abe27f` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-279@sha256:2d0ae5f19fad8ef0e9c3901c9e157af8ff07ea9fe9e0ab148c2c5b2c94f9b9e0` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-279@sha256:f160efa5edbeddfd1eb5d0c026ab650d4ff7e1cea393e4cb12cc365f83b23c34` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-279@sha256:8ceaccaa96c9dc7b6089bfcee4d1f28fc140ff0921e975ea228cdc2ff2fccb2b` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-279@sha256:f10d60601ea34fd5152fd5fbf77e0ed9a4b1ed561859daf8fc76cc65688154d5` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:c23273d0c79280dba3325ebb039f637f5fdf9417839ec5e656e5642eaef04a6a` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.513.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.512

<!-- source-commit: a0e7ca371f0b3b1d8769cd899dd43841eafcd903 version: 0.0.0-develop.512 -->
Published 2026-11-10. Archive SHA-256 `3b7f73ab4e892fb761c4ae34ff22c8f874e464b60ec8f0479d65995982ffe329`.

- Change: Give the disposable test database room and wait for real queries before each test module (#270)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@a0e7ca371f0b](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/a0e7ca371f0b3b1d8769cd899dd43841eafcd903)
- Changes since 0.0.0-develop.510: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/f2fa56046f5733f21771d77e06e679b3734a5008...a0e7ca371f0b3b1d8769cd899dd43841eafcd903

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-278@sha256:cffb66a6eeda085ba6e94b70500f8867ec1bb8c10174fee642a0709cf24fb1f3` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-278@sha256:8eac8c190a9f2aa39cd22845417e5cb182a7b9b86fa86e670abffce16e9aaf1a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-278@sha256:64dd67cd8b02cd208772a7246c24de2f592189d418f8c881a24db8b48ccae35b` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-278@sha256:64dd67cd8b02cd208772a7246c24de2f592189d418f8c881a24db8b48ccae35b` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-278@sha256:31bb736a1a19524ff690e38c30a0921cc0030f7898c3b7aabb9e275a284406a5` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-278@sha256:d72ce73a7b1d92bad5313b337e9d577df4c0c7d49758fc2a1627be0f7aa059f6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-278@sha256:f570883303e36cd2a039b92b6829f4c05305b7af551dd1f7f89711d10d8e5c1e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-278@sha256:02e07c01d4917e69ea11248110b962e7e74c48245795816c0f0832a41321d124` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:14c354a0a42e740240b846bb1fa590a9b61090d56b8577dd3e191be2ebc91476` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.512.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.510

<!-- source-commit: f2fa56046f5733f21771d77e06e679b3734a5008 version: 0.0.0-develop.510 -->
Published 2026-11-10. Archive SHA-256 `33d2f5cfd04f46d4cd33515698d484fe2c09da86ee2bd2186b055a97e4f90636`.

- Change: Staging connector: drop the admin-auth keys that commonEnv never renders (#266)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@f2fa56046f57](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/f2fa56046f5733f21771d77e06e679b3734a5008)
- Changes since 0.0.0-develop.508: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/7cd9b2c3dd5e238a105d760edc39f78fbacf86f5...f2fa56046f5733f21771d77e06e679b3734a5008

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-275@sha256:e1500b8c4782a462c83777409685d1491abb34edee9259a8bbafdc78028c6adc` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-275@sha256:b303af03dd7ccc828f9458a1ec02759b13e87c17e6dcecb61eb496ea1ad37ef7` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-275@sha256:9703ac51636ab9019310994b41b1d79fc6499e521f483b6225ca52ccfb318c8a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-275@sha256:9703ac51636ab9019310994b41b1d79fc6499e521f483b6225ca52ccfb318c8a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-275@sha256:5f8f262a40da880a600096d8260a52a941d8258589182ab8dc614d7d8999de61` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-275@sha256:f7f6ea1b5d0275ef9138abb2258c1979cd910b2b3e4372bb7b1c2d327fcd72c7` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-275@sha256:0ca823126d59ca8aab8493f406d7b3981f67638ec8812cf58f02c611e5c581d3` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-275@sha256:d4f9991e67fe41d7ac7afe7a7b07d46af4d1ac40312dcc3c5d800288b8f2b729` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:69c4d470e414a88726c541468a2d260711f17b66884d53dc79e1bfa26ce3ae0a` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.510.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.508

<!-- source-commit: 7cd9b2c3dd5e238a105d760edc39f78fbacf86f5 version: 0.0.0-develop.508 -->
Published 2026-11-10. Archive SHA-256 `de0140c5b43a7bdb6daaf279963182de5357a27ccb6d9ab823cdd015eb0a83e3`.

- Change: Crop Sown: plot registered question, record header lock, Afaan Oromoo/Tigrinya routes, intake ID label, ODK forms on Master Data (#248)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@7cd9b2c3dd5e](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/7cd9b2c3dd5e238a105d760edc39f78fbacf86f5)
- Changes since 0.0.0-develop.507: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/8db1a47c847519997f1c5f21c6fc97f2a96f9d9d...7cd9b2c3dd5e238a105d760edc39f78fbacf86f5

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-273@sha256:7aa2b5504a602b2dc83eb4d70f6ea2984448430e2ae9736bdf24a1264c857898` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-273@sha256:166939d8f1168f6d7205da98fe350f7f3e78f0a4e612009281c6339d1a1db2f5` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-273@sha256:c7ab9d28390ef652ecf8f0338d80a8fee38f6e39d4da28379bd1c834263f3d2d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-273@sha256:c7ab9d28390ef652ecf8f0338d80a8fee38f6e39d4da28379bd1c834263f3d2d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-273@sha256:2c7b0c7f0ade925041f1c4ec93940a29e27ed9dab1e33928d1085a167f06d9b7` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-273@sha256:9ee7d368e469ffcb62c855cf1437b5fd84ff6430063c65e6cc5a2ef4bf3f19b0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-273@sha256:16ee6d05937112ef6b4c26bb87773d60b45028ea71c5e5c19eea11d5f1782e06` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-273@sha256:2898752095e40aaffb1d96d3e69392b37c378cadc37f31ea3afcb5b75e146c54` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:61ee44951c2d1842b3454e5e5df82351cfa967ebbf3f377d092499787cc99943` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.508.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.507

<!-- source-commit: 8db1a47c847519997f1c5f21c6fc97f2a96f9d9d version: 0.0.0-develop.507 -->
Published 2026-11-10. Archive SHA-256 `7b36a4e2079ab6b614f4500f9bc23f6842200849a5f9e7de6e0d183a11d6579e`.

- Change: Staging connector: expect the staging Keycloak issuer (#263)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@8db1a47c8475](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/8db1a47c847519997f1c5f21c6fc97f2a96f9d9d)
- Changes since 0.0.0-develop.506: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/3a9b4df787dcfe30eba38a969cf4ac34fc3c90bd...8db1a47c847519997f1c5f21c6fc97f2a96f9d9d

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-270@sha256:988099c5d872a8f2733beafe1385c1de15dd494da768a71cb406d97183669cd0` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-270@sha256:148b58776eed7d072ddc6f621fd7282b43b62ae5c753edb65a65e59b0ce3237f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-270@sha256:1067fa46b08e2a702064d60c914f32dec5067f58cbecfaa376810c2c5feaa742` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-270@sha256:1067fa46b08e2a702064d60c914f32dec5067f58cbecfaa376810c2c5feaa742` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-270@sha256:cbc1c6e637031028d04b195e0c1a5321f972a0a7839d7d80e3f8bb8d98ccd5df` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-270@sha256:22b1898810c2785dd1981295a4c68c4e7c2b75946919a76c1f5418df5552e035` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-270@sha256:dc15203a17ee303ce6f1ac27b4550ffe5dfc27fad010a600514f73aa3fd2c29a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-270@sha256:6701e33f2b28fbe8f85526f4601de710b4c78c9e10a79b046b010ab486f8c211` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:9ac89fbf35bb645f761d7d1e5334ced71f5af2f59b6081ea71692e2703aa787f` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.507.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.506

<!-- source-commit: 3a9b4df787dcfe30eba38a969cf4ac34fc3c90bd version: 0.0.0-develop.506 -->
Published 2026-11-10. Archive SHA-256 `ed711ae94c447cd96deb87d2bbebe3d07751d04bf4f2628c8544636ddafb341a`.

- Change: Staging connector: accept admin tokens from the staging Keycloak issuer (#262)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@3a9b4df787dc](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/3a9b4df787dcfe30eba38a969cf4ac34fc3c90bd)
- Changes since 0.0.0-develop.505: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/2a96fa5136e033bfc030f096111f6ec5dddb617b...3a9b4df787dcfe30eba38a969cf4ac34fc3c90bd

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-268@sha256:3ba3a42d29c4b40fe951aed2c95821887a8ad5953de56760471a685b238db5ca` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-268@sha256:b267c1245f0b489ce8feea1f3ed4df6a4b76d8a8f20a9b00813b87641b895d00` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-268@sha256:7a186f0f0fa3183fc2f93613bc069b6c934b25e3a710e9b02e47c1bce4ea6fde` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-268@sha256:7a186f0f0fa3183fc2f93613bc069b6c934b25e3a710e9b02e47c1bce4ea6fde` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-268@sha256:a407f9282be9699984d8a62b8c8c891e0d5e363fee12493afbfd02b2c3568f47` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-268@sha256:c45dcd17bf3a00fc974687823562141cc0079cadfec985e9c019f72ca672feb6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-268@sha256:f72e1a37d8ad3756d8d8adea0f64d9306cf50c5a4242fc513a13a481f6c5cc95` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-268@sha256:2847af4548dba935b8e9c498a798b1d04058fdae5d0e5dca26b842d997b6661b` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:e409b894e68b02cb15f92f617024734d5230cc77e5ab73ecaa9865f571baf6c8` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.506.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

## 0.0.0-develop.505

<!-- source-commit: 2a96fa5136e033bfc030f096111f6ec5dddb617b version: 0.0.0-develop.505 -->
Published 2026-11-10. Archive SHA-256 `71c413fe84f4daff9d55f8618ded5b468cca28f6f65a73c2e68e6e004522951b`.

- Change: Add a load sample data option to the staging build (#261)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@2a96fa5136e0](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/2a96fa5136e033bfc030f096111f6ec5dddb617b)
- Changes since 0.0.0-develop.504: https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/compare/7880d51210c46b996070f8d8413c02bd284bf6b2...2a96fa5136e033bfc030f096111f6ec5dddb617b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:develop-267@sha256:d61a704cd3ade249f487b66c2b98c2cb8b57973eae0745f03603bfe264a4f100` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:develop-267@sha256:2bf3071e8fad12c92b5f3359da1cf0fc1fcdb0b53b0e51255dd1b8e30d2f6eb6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-267@sha256:e9db93628552c2935ec749d1193cd9993a769a3fc76bd1390b388c9a730bcd43` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:develop-267@sha256:e9db93628552c2935ec749d1193cd9993a769a3fc76bd1390b388c9a730bcd43` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:develop-267@sha256:0786a29d7467694afb6e55553c00e77b80198641c1b3e63bc379aa35cdfd3d95` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:develop-267@sha256:fce2e4470e4ece07f63590b3918f2362ac83492889e379ca7bf2c9b982e25744` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:develop-267@sha256:de06a5301153dfc6d41356188b95dbe30720c2197497cd231a50080eb1c7d50e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:develop-267@sha256:fd5fd8f4c355b3bf1500d426fba808f2408805c1e6ff772ce295f144c12e2ae6` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1027e7775505@sha256:64b202f0f92754b8c5d3122497ffb49036b98c7cc8d749df92fc52c83f95d990` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-cropsown-registry-0.0.0-develop.505.tgz -n crop --reset-values -f environments/dev/values/cropsown.yaml --wait --timeout 15m
```

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

