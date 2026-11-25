# openg2p-da-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-develop.91

<!-- source-commit: 490f2e20f673b533579bb83e9546093840ecf601 version: 1.0.0-develop.91 -->
Published 2026-11-25. Archive SHA-256 `7d83e3fbb2b0a014be3c05630b2e8b7e015c5d0d7927f1cc3caf9f747421e89d`.

- Change: Merge pull request #87 from simretyibeltal-commits/ci/coverage-and-lint
- Source: [Centre-for-Open-Societal-Systems/da-registry@490f2e20f673](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/490f2e20f673b533579bb83e9546093840ecf601)
- Changes since 1.0.0-develop.90: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/4db8e7dafe9811be74020f2d9dada319e14615f7...490f2e20f673b533579bb83e9546093840ecf601

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.91@sha256:b3b83aa8799f44e43ff64d36d6e0e7a2eadb8965042319433169c485e3505041` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.91@sha256:1bab2b5b0abbceb88f5fb97e6d517d4eb411dcc7576773d438597f95495e8fc0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.91@sha256:cc4780b494d85b7115253ed8a1caa17c08e6244d5a0608fe517ae7336a9d6d7e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.91@sha256:cc4780b494d85b7115253ed8a1caa17c08e6244d5a0608fe517ae7336a9d6d7e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.91@sha256:d71e4b372951252c2156cde7266e1c8905e3ae6dc440aed915dedadb45f60ca3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.91@sha256:5a873773797bd04c5156e1e384c003857e15534f4d0ddbd7e798a1f8f20995a0` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.91@sha256:c8317867cd19b989b8b7281d5b07f30c2395a4e7ade52e191a942119f815bac8` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.91.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 1.0.0-develop.90

<!-- source-commit: 4db8e7dafe9811be74020f2d9dada319e14615f7 version: 1.0.0-develop.90 -->
Published 2026-11-25. Archive SHA-256 `6aec7d2e7a62eced67d5c5f37ca25b676f0631cfeae7ed725d6b7cf4a0cde701`.

- Change: Merge pull request #86 from simretyibeltal-commits/test/guard-tests
- Source: [Centre-for-Open-Societal-Systems/da-registry@4db8e7dafe98](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/4db8e7dafe9811be74020f2d9dada319e14615f7)
- Changes since 1.0.0-develop.89: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/41a30cd0157ab60be8ba43e39a91ed2a6a78d2ad...4db8e7dafe9811be74020f2d9dada319e14615f7

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.90@sha256:b8807112c65640ade3ee24b1dcb805eb99456e586d49da30a9020945579026cf` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.90@sha256:9f351004d4799161652881659c41fbce4b1158817ce5f408a6661f1748bad05c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.90@sha256:888adb79a556983fd699bde31dd6cf523a1b220df44fd54fe449fa6a15e49ace` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.90@sha256:888adb79a556983fd699bde31dd6cf523a1b220df44fd54fe449fa6a15e49ace` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.90@sha256:fbc0187d85ea8b87666405fb084868308faf9a0068019dff9b4bf2862505eb5a` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.90@sha256:ee4ed4037a61a6e0276a81279afbf8809f2883947e98198049feb30575b0d37f` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.90@sha256:3994a5a61bbf20c6fa2189cd9d819b09e0d352516b2f3cb1723e1a39dbf6e38d` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.90.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 1.0.0-develop.89

<!-- source-commit: 41a30cd0157ab60be8ba43e39a91ed2a6a78d2ad version: 1.0.0-develop.89 -->
Published 2026-11-25. Archive SHA-256 `2a8683ee506a79d7cdd2233ea03af41f85f6065bcbd2e74b142a151e24e8141b`.

- Change: Merge pull request #85 from simretyibeltal-commits/ci/validate-runs-all-tests
- Source: [Centre-for-Open-Societal-Systems/da-registry@41a30cd0157a](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/41a30cd0157ab60be8ba43e39a91ed2a6a78d2ad)
- Changes since 1.0.0-develop.88: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/91c10fcf21b7bcfe0b930c1a8d393b2afd2542c8...41a30cd0157ab60be8ba43e39a91ed2a6a78d2ad

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.89@sha256:ffd341cb07a46fc241a89d41d99723a2de0cc8a56788e9756d4efc29ddf58272` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.89@sha256:16b1aad7eba9fb4279e968b47fc6c80c1c0d7b66a0a1686c7f6714dc4a3d6c1f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.89@sha256:a26f33438cae82f423c674fe8a891041d6c0eaeb1752cfb7d95aab01c75bd8d4` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.89@sha256:a26f33438cae82f423c674fe8a891041d6c0eaeb1752cfb7d95aab01c75bd8d4` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.89@sha256:5743a95df07f6df4c6e85ebc7104cbfa114a00003bf2792f54cae366a9b0feac` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.89@sha256:6abf55e84752bb135efa36548f00ce080964b4ca0070f83a411797b984ee6d36` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.89@sha256:c8f0e81b490e82f5e5b2bca735ec4fdc1f6d343456a4379ac1e5b4cfd898d6d2` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.89.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 1.0.0-develop.88

<!-- source-commit: 91c10fcf21b7bcfe0b930c1a8d393b2afd2542c8 version: 1.0.0-develop.88 -->
Published 2026-11-24. Archive SHA-256 `2837a87a339ba4d48b3b1484f787c95b936a386f27e25ddfc198636667e26bdd`.

- Change: DA dev: object links for the Garage host, staff UI image CSP checked on every deploy (G2R-614) (#84)
- Source: [Centre-for-Open-Societal-Systems/da-registry@91c10fcf21b7](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/91c10fcf21b7bcfe0b930c1a8d393b2afd2542c8)
- Changes since 1.0.0-develop.87: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/6fba7b111ff9cd7c2805906ce00ca65c8cd63385...91c10fcf21b7bcfe0b930c1a8d393b2afd2542c8

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.88@sha256:11819cc0e2d132a29a71394e8122dcc24062f5a75a0355862af67b37d5e1eb89` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.88@sha256:e2f3d3a90cdef331fc44f5789b70b9fa8652d8a2a9e43d7c0152a0b084a915c6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.88@sha256:5aa586d02b7362e412fccf47d85fb79eb7b6afeb4f04693c4dca56ff0050b7f5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.88@sha256:5aa586d02b7362e412fccf47d85fb79eb7b6afeb4f04693c4dca56ff0050b7f5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.88@sha256:69da69f50b5174bb9a3774003db4e2ffcc6c7abb33e457580cfbb42210c91772` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.88@sha256:7b1bf36da96f7ef6b263ce74345ae84acae091780820386fafbee1106476f269` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.88@sha256:bb01666fba0c991b0055d4cc7218d786dd1db4d6ad953b538181c652474e10a7` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.88.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 1.0.0-develop.87

<!-- source-commit: 6fba7b111ff9cd7c2805906ce00ca65c8cd63385 version: 1.0.0-develop.87 -->
Published 2026-11-20. Archive SHA-256 `8ce4beb8723f60487b393daa3b66ca84197bbe58ef997cfa407b552bca0dba47`.

- Change: DA intake: a required field the form leaves out is refused on Next (#83)
- Source: [Centre-for-Open-Societal-Systems/da-registry@6fba7b111ff9](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/6fba7b111ff9cd7c2805906ce00ca65c8cd63385)
- Changes since 1.0.0-develop.86: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/c161f2db1699c3656d017e57eae2e8594e072866...6fba7b111ff9cd7c2805906ce00ca65c8cd63385

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.87@sha256:2c36c9a5b68e00313840a723b03c90dfecfa67d03c86da1d7db8f0b63ebd04b2` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.87@sha256:dd929f6b3312d06d2c73e732cde679014b6b43cd115710cd5821fe5faa31dcbe` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.87@sha256:1d5bb73fb0db2f71affd778c0ffc185f8d7f06418b7e861d6a57841864bdb073` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.87@sha256:1d5bb73fb0db2f71affd778c0ffc185f8d7f06418b7e861d6a57841864bdb073` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.87@sha256:927fc50fdfdf23b68a88ee90a485af26dd74e74260e00af50d7f3c7729f08847` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.87@sha256:c0f44a715e73208223d94371faa33472deb619c8b9bc8a559dd5c1bb1d35a66e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.87@sha256:b0ce9c31dbc0b3c552bc16b2dfac22c20a8987bc655b3edab4c91c30b1298f66` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.87.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 1.0.0-develop.86

<!-- source-commit: c161f2db1699c3656d017e57eae2e8594e072866 version: 1.0.0-develop.86 -->
Published 2026-11-20. Archive SHA-256 `f5356cc047e6f8af1b48260236c1956777a49125b94f21403e97ceb853a0a153`.

- Change: Name and version DA images from init.yaml; every eoan repository immutable (#82)
- Source: [Centre-for-Open-Societal-Systems/da-registry@c161f2db1699](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/c161f2db1699c3656d017e57eae2e8594e072866)
- Changes since 0.0.0-develop.131: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/81651c21e3478f23c07cc83e1e33eaef5a71a747...c161f2db1699c3656d017e57eae2e8594e072866

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-api-1.2.2-rc.614:1.0.0-develop.86@sha256:a9f001bda5bd8afe75f49f1fc0bff0d9359b102e659b2580414075ac649495c5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/partner-api-1.2.2-rc.614:1.0.0-develop.86@sha256:f2479e7872946f78927aadf567556229a913f16388f2542a418f65f7ce59590a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.86@sha256:f9be561302a2fe753febe00f599300f4f8502b75edf91f7ddf019c75e122097c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/celery-1.2.2-rc.614:1.0.0-develop.86@sha256:f9be561302a2fe753febe00f599300f4f8502b75edf91f7ddf019c75e122097c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/db-seed-1.2.2-rc.614:1.0.0-develop.86@sha256:d8b296867021df9d927c1b97f5e715ee34b82815d939b0152d1c80e0d6d5d7ab` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.86@sha256:b9235cec3bbb36f702a95603d16ea925fbbb4163bd4d8ee21fae2e4adbbec2e5` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/da-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.86@sha256:f3e97fb4072d1d4f2374bec4006c62e4b8e602bbeed7f8460494d72103e5705f` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-1.0.0-develop.86.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.131

<!-- source-commit: 81651c21e3478f23c07cc83e1e33eaef5a71a747 version: 0.0.0-develop.131 -->
Published 2026-11-19. Archive SHA-256 `2778c23a16650a30accbf3a5a8eda80c0d40c49f0d69039e571c1fbbd96d722c`.

- Change: Reporting views for the DA register: da_rpt_da and da_rpt_da_qualification (#81)
- Source: [Centre-for-Open-Societal-Systems/da-registry@81651c21e347](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/81651c21e3478f23c07cc83e1e33eaef5a71a747)
- Changes since 0.0.0-develop.130: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/0d6c6a29fcabe84bd03da8286f3490c59e7684d3...81651c21e3478f23c07cc83e1e33eaef5a71a747

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:81651c21e347@sha256:b0ebd9859dbf260a7d6a9a2b3772c208464ff1fa4690d4174579bc42b5378375` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:81651c21e347@sha256:e472496113e23f170e03536537831036732f2fa18f2e2eab83e4494936a6bea0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:81651c21e347@sha256:cb16286df40b92c8caa917bdf2f6b28f928ffd7b9adeb2157c83264f95a80715` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:81651c21e347@sha256:cb16286df40b92c8caa917bdf2f6b28f928ffd7b9adeb2157c83264f95a80715` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:81651c21e347@sha256:0c0c92a6b616925127e5c329debf3d790c8e4578e1d3a6f7299796c332b8743d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/sanity-tests:81651c21e347@sha256:2e1794d1ceaa579310d8ef2fcfcc66d18b7d8bd817ea8e47ce3970bac5eb9487` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:81651c21e347@sha256:4907bc45e1216721ce296bfe92dd1eba7ae70b4aefa8fa4c59679c2774be2d49` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.131.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.130

<!-- source-commit: 0d6c6a29fcabe84bd03da8286f3490c59e7684d3 version: 0.0.0-develop.130 -->
Published 2026-11-19. Archive SHA-256 `28fc32ef1bd822b487f3f9181ff01305f89f6d933241718c0b8c456b2ce15394`.

- Change: Pipeline wiring test: the Checks green stage comes before the deploy (#80)
- Source: [Centre-for-Open-Societal-Systems/da-registry@0d6c6a29fcab](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/0d6c6a29fcabe84bd03da8286f3490c59e7684d3)
- Changes since 0.0.0-develop.126: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/1ab7e247d74aa96be317d41f61667547db9fbb73...0d6c6a29fcabe84bd03da8286f3490c59e7684d3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:0d6c6a29fcab@sha256:1a8e401dff4a82f831863da975e01cc9edae94bf4a6281025a681559f5d930de` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:0d6c6a29fcab@sha256:83db8fbcd41188902d7ec7a827730c5c9746cff11f7212a10832c653750aa32d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:0d6c6a29fcab@sha256:356b4c482590f03f3523ab550f3e62126fb0691e119fa13a74af6b35e6610a44` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:0d6c6a29fcab@sha256:356b4c482590f03f3523ab550f3e62126fb0691e119fa13a74af6b35e6610a44` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:0d6c6a29fcab@sha256:131f22a87fa85a1c08f392ccaffb3c5b7c696dbbbc37c8e35d515e8d7fd983ec` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/sanity-tests:0d6c6a29fcab@sha256:96d8b2410621d973727b3f354af7ccaf863a82e5b06cd1666ff407da58941eee` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:0d6c6a29fcab@sha256:fbcddef0f82018d59990a096628ef599c9eebf6346d6a5026aaed98c7a363cec` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.130.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.126

<!-- source-commit: 1ab7e247d74aa96be317d41f61667547db9fbb73 version: 0.0.0-develop.126 -->
Published 2026-11-18. Archive SHA-256 `e56eea54acacac13b21ba64d56584e049c1a03acfea171276c796f54b8ff16f4`.

- Change: Merge pull request #78 from yash7473/feat/da-reports-to-marital
- Source: [Centre-for-Open-Societal-Systems/da-registry@1ab7e247d74a](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/1ab7e247d74aa96be317d41f61667547db9fbb73)
- Changes since 0.0.0-develop.123: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/d291007fcb7c32eb9ed536399705045916b40f4e...1ab7e247d74aa96be317d41f61667547db9fbb73

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:1ab7e247d74a@sha256:0fbd5abac8a4e457294202f44dbd427ede53105a32d8e30af3bdf86ff1d530d0` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:1ab7e247d74a@sha256:70df12e3ab773d53bae01a83dfde2e999694481fe13aae2883b9d20f4d411dc2` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1ab7e247d74a@sha256:f676a92a5baac2db7030bedc381596740be978aa3bf9356dc09626054d23fa96` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:1ab7e247d74a@sha256:f676a92a5baac2db7030bedc381596740be978aa3bf9356dc09626054d23fa96` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:1ab7e247d74a@sha256:bb4d4020cb5a5dd6988c9de531ad46011cf04bb73efcb2dd82dff391d0dad361` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:1ab7e247d74a@sha256:ed8e82066e1e62df59601d28a3ac2cb58ce5514d12d9cdfcb2dc226f99e22c54` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.126.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.123

<!-- source-commit: d291007fcb7c32eb9ed536399705045916b40f4e version: 0.0.0-develop.123 -->
Published 2026-11-18. Archive SHA-256 `f94bdc0443bfba8d7bf4fddbb43121a03777030537f1eed88b85b2e5e592c91e`.

- Change: Merge pull request #77 from yash7473/feat/da-professional-details
- Source: [Centre-for-Open-Societal-Systems/da-registry@d291007fcb7c](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/d291007fcb7c32eb9ed536399705045916b40f4e)
- Changes since 0.0.0-develop.119: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/3ed1d9ed8d494c14b6370e3c1f0e1543d8ceb7d6...d291007fcb7c32eb9ed536399705045916b40f4e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:d291007fcb7c@sha256:ff48c2ace0309999197f3685dad59bb58c7a13d5d408c5afbed82f6356177d89` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:d291007fcb7c@sha256:f2f17624d35a8e8c19b16b91ced940409ec392fb0bf7cd994f1fa7f1a4e0f33b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:d291007fcb7c@sha256:fbef0fbf4703577994d7d3b77b062def6fb508386ad32b42c76c058956c71732` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:d291007fcb7c@sha256:fbef0fbf4703577994d7d3b77b062def6fb508386ad32b42c76c058956c71732` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:d291007fcb7c@sha256:300c9ff5cc01e9a8f4d3199ea1eb4fa43a6a05e99b5b6086ccd055f205287055` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:d291007fcb7c@sha256:5fd77037584a0c5eedd977184146b8a29f0f62deb3b22e931915d33eda181144` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.123.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.119

<!-- source-commit: 3ed1d9ed8d494c14b6370e3c1f0e1543d8ceb7d6 version: 0.0.0-develop.119 -->
Published 2026-11-17. Archive SHA-256 `e469055c86451077bec8fe26dc438fd7b5b8fc2f08e71bca693ef68892b48864`.

- Change: Merge pull request #76 from yash7473/fix/da-home-address-layout
- Source: [Centre-for-Open-Societal-Systems/da-registry@3ed1d9ed8d49](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/3ed1d9ed8d494c14b6370e3c1f0e1543d8ceb7d6)
- Changes since 0.0.0-develop.117: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/61387b620acbf0b8ef0dd4c3ecb3f895d88975a9...3ed1d9ed8d494c14b6370e3c1f0e1543d8ceb7d6

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:3ed1d9ed8d49@sha256:f3cc9e0a8d27f66333ecadb5d969a0f628ad0df1cc3ea65f2fd3f526772c0add` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:3ed1d9ed8d49@sha256:355b603f162216570ef49e6f0a41838d20467bea1ac0a7c38f7c5f29d16f39c3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:3ed1d9ed8d49@sha256:9edcf31df050134e8a9be85fa9a2ad57565a36296c01d0a71b5b6566b281f694` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:3ed1d9ed8d49@sha256:9edcf31df050134e8a9be85fa9a2ad57565a36296c01d0a71b5b6566b281f694` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:3ed1d9ed8d49@sha256:76198a30acd4ca4188f468c1adefb41b3a38e271466eb190988be6e8735161e8` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:3ed1d9ed8d49@sha256:6fa6f6a9c99d40cdb98deaf0a3cf4f4cb8de515701538e19ad01b4f167a38371` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.119.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.117

<!-- source-commit: 61387b620acbf0b8ef0dd4c3ecb3f895d88975a9 version: 0.0.0-develop.117 -->
Published 2026-11-17. Archive SHA-256 `38738dfc5e911864871b9c594d029ed6e27f75c1db1f1eef2b0e56f9fcb6a554`.

- Change: Merge pull request #75 from yash7473/fix/da-location-names
- Source: [Centre-for-Open-Societal-Systems/da-registry@61387b620acb](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/61387b620acbf0b8ef0dd4c3ecb3f895d88975a9)
- Changes since 0.0.0-develop.115: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/bf099136e6881a4cb7cb34de1d415b4ebceae2fd...61387b620acbf0b8ef0dd4c3ecb3f895d88975a9

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:61387b620acb@sha256:9228df806bed02251c208264584a83015fc8751790a77310398163a095119f0b` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:61387b620acb@sha256:6f426f6abff076f680840fe3e0721da3bca74c08d4db7d671f45c461cfd2e156` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:61387b620acb@sha256:4bccf9103be4151cdd45da7296b6706b6c81652b9d9528db1602777d5c48d0b9` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:61387b620acb@sha256:4bccf9103be4151cdd45da7296b6706b6c81652b9d9528db1602777d5c48d0b9` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:61387b620acb@sha256:0ede815401ef1404de13e210e19eda39b7894699d4ca04145d1a562f960bf1e5` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:61387b620acb@sha256:03d4c6ac314d2499ddc3da39ddbfb75aed78109f8a91c483a0a21da9e08ab584` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.117.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.115

<!-- source-commit: bf099136e6881a4cb7cb34de1d415b4ebceae2fd version: 0.0.0-develop.115 -->
Published 2026-11-16. Archive SHA-256 `6375109cb78b9c5b67cd7cd92d35a9094644e1d35a97454864410ad2c7e1a317`.

- Change: Add contracts and chart checks (#72)
- Source: [Centre-for-Open-Societal-Systems/da-registry@bf099136e688](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/bf099136e6881a4cb7cb34de1d415b4ebceae2fd)
- Changes since 0.0.0-develop.114: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/b0fb8b85de0798940ca3223ebd979307e8c313a1...bf099136e6881a4cb7cb34de1d415b4ebceae2fd

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:bf099136e688@sha256:93c4aeb1c3d1e1b1fb107d0580d9b49b78de0c4d2177ee763e68f309f6a10af6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:bf099136e688@sha256:e365fcb456d5c8eaac060950a99062806568712efe6ea1921b15f305b25e24f6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:bf099136e688@sha256:10582dfc6831b69475719b1feba8c2954dafc19ccb1088b448741a429fa96956` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:bf099136e688@sha256:10582dfc6831b69475719b1feba8c2954dafc19ccb1088b448741a429fa96956` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:bf099136e688@sha256:f1139313b35f17c8e00dcd1cb1e3e7b422c73e97011e516a730071cb76ccdcd5` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:bf099136e688@sha256:121fc3038af52c68618d2e6d8655f9a27de927d7966d42702f66a042c81af670` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.115.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.114

<!-- source-commit: b0fb8b85de0798940ca3223ebd979307e8c313a1 version: 0.0.0-develop.114 -->
Published 2026-11-16. Archive SHA-256 `1db2831bdb3bb7854d624e0f0f915770b124186a00f79ce918cc7e7af2a42287`.

- Change: Merge pull request #71 from yash7473/feat/view-record-files
- Source: [Centre-for-Open-Societal-Systems/da-registry@b0fb8b85de07](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/b0fb8b85de0798940ca3223ebd979307e8c313a1)
- Changes since 0.0.0-develop.111: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/e623b553eff2770a6bf5f45b85e938dfa87711cb...b0fb8b85de0798940ca3223ebd979307e8c313a1

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:b0fb8b85de07@sha256:cfcb0f1b0786eb86b850948beda8f6d7d127db5eec960c7d5fcefa6d46f5ca98` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:b0fb8b85de07@sha256:af21a181a2b9ec6f89d2354725273a30b0a546cf1a7bc83c1111089ace2b6a34` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:b0fb8b85de07@sha256:6376f26f7a2af7550981622fe5f2f62d50dfb7f03c73475e0693d5a35b9c4103` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:b0fb8b85de07@sha256:6376f26f7a2af7550981622fe5f2f62d50dfb7f03c73475e0693d5a35b9c4103` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:b0fb8b85de07@sha256:a5e84eeec9702ef953eae7d2aa88bd28f6345d3bb1049261bfec771ccb536965` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:b0fb8b85de07@sha256:215c575b678ff16fe0b052d2ac8dcfc2aacd3edc9493e3981dc979dc8f4ea21a` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.114.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.111

<!-- source-commit: e623b553eff2770a6bf5f45b85e938dfa87711cb version: 0.0.0-develop.111 -->
Published 2026-11-16. Archive SHA-256 `9bc35f49941c73e6971f2827e09974344688553120e780cc076c9abfede410ca`.

- Change: Merge pull request #70 from yash7473/fix/da-id-copy-one-row
- Source: [Centre-for-Open-Societal-Systems/da-registry@e623b553eff2](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/e623b553eff2770a6bf5f45b85e938dfa87711cb)
- Changes since 0.0.0-develop.96: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/ffbe64bf583dd9ee3993e27caeaa88f4dfe4eb5c...e623b553eff2770a6bf5f45b85e938dfa87711cb

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:e623b553eff2@sha256:fea3fdb402eea385e607f538f9b6f3e6be3135eae6f1850a8ce1901c461b69fc` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:e623b553eff2@sha256:486bc251d8a5738526e19123980dfa107adae5904dd85ccf488560857ffa32b9` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:e623b553eff2@sha256:16cd70c1310ca11d4c00c9f8705f3fe3b94262d167daca8276af2717d8db3770` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:e623b553eff2@sha256:16cd70c1310ca11d4c00c9f8705f3fe3b94262d167daca8276af2717d8db3770` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:e623b553eff2@sha256:e40f104fcf46b07dab24639aaaa755e5a5d7385bcf258a0583a737853d00fff5` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:e623b553eff2@sha256:d56cad61d2f3e6346a3725dbc2a21a0183fb12caac37faa806e6427eee20ab4f` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.111.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.96

<!-- source-commit: ffbe64bf583dd9ee3993e27caeaa88f4dfe4eb5c version: 0.0.0-develop.96 -->
Published 2026-11-12. Archive SHA-256 `7b28fee8ea6752d86136ffc9e5d9286f463cd7a64f86aed2d498446a46d0cf66`.

- Change: New Dev: pin oan-helm 488d505 (DA dev values load the sample agents) (#63)
- Source: [Centre-for-Open-Societal-Systems/da-registry@ffbe64bf583d](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/ffbe64bf583dd9ee3993e27caeaa88f4dfe4eb5c)
- Changes since 0.0.0-develop.95: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/f9a4aabe4080e8ac60829f2629565339f768d4a4...ffbe64bf583dd9ee3993e27caeaa88f4dfe4eb5c

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:ffbe64bf583d@sha256:0034b0030ae659ab7100aed35f4c8bfbf0f85a4fd1200495804bb801694d0f5f` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:ffbe64bf583d@sha256:dff558c7ebaf8ced181cac37cbb24851d3796fb903a603b7bba97643c99a033d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:ffbe64bf583d@sha256:a5818492dab6daec2a7e0b5378ea02a8e92c9db7ce9da75ebfd49f67d00d4c7a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:ffbe64bf583d@sha256:a5818492dab6daec2a7e0b5378ea02a8e92c9db7ce9da75ebfd49f67d00d4c7a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:ffbe64bf583d@sha256:362397096b05f7cd774bae88f9b45294b17773eccd3ded8d5f13a201349de9d6` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:ffbe64bf583d@sha256:c5ed88b52de57c296a66195cd5d6ec44aa344ffd29efa287ce8740edcac0195f` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.96.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.95

<!-- source-commit: f9a4aabe4080e8ac60829f2629565339f768d4a4 version: 0.0.0-develop.95 -->
Published 2026-11-12. Archive SHA-256 `c576963c7b5545c2ee423d0717dc11ee69d4ae9b318e5a5f010917d42102453c`.

- Change: Enter sample DAs as the signed-in submit user (#61)
- Source: [Centre-for-Open-Societal-Systems/da-registry@f9a4aabe4080](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/f9a4aabe4080e8ac60829f2629565339f768d4a4)
- Changes since 0.0.0-develop.94: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/620d6c87af94d9cf95e14de6c01fe4af2e711e9c...f9a4aabe4080e8ac60829f2629565339f768d4a4

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:f9a4aabe4080@sha256:70c7b38ea95006e5397893ebba0cc81f0c60ad99cf1a6bf10c0cfbb0245776f7` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:f9a4aabe4080@sha256:26a2e0ddc0af44d596b7d83d0e95486f9b8f23530ca589b4603be46ffd1d3ced` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:f9a4aabe4080@sha256:30e1ac7ee1fd7bb8169c3b504c77ab9cbfe7d5bff867c71bf22467bcd13a052d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:f9a4aabe4080@sha256:30e1ac7ee1fd7bb8169c3b504c77ab9cbfe7d5bff867c71bf22467bcd13a052d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:f9a4aabe4080@sha256:afc15f5ccb8fa2c5a27243ffc742b44587aedf9b6c0455a39f227810ae1a9e41` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:f9a4aabe4080@sha256:bc33f76efe83c4b61bd05b381e8c7b25abc3d7e490181334954be6aa38d62231` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.95.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.94

<!-- source-commit: 620d6c87af94d9cf95e14de6c01fe4af2e711e9c version: 0.0.0-develop.94 -->
Published 2026-11-12. Archive SHA-256 `f4a60455b7f923c544911e4936afd2d6cdc2bb3e94c2b79c6ba2293e96edf63b`.

- Change: Run the sample loader tests in the dev pipeline (#60)
- Source: [Centre-for-Open-Societal-Systems/da-registry@620d6c87af94](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/620d6c87af94d9cf95e14de6c01fe4af2e711e9c)
- Changes since 0.0.0-develop.93: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/cba80649ebcdf7210aafdb80fdf90d855f9bfec4...620d6c87af94d9cf95e14de6c01fe4af2e711e9c

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:620d6c87af94@sha256:3fa9dc8cb9d3e10a8c7790098f30c62bafd16b46f1145c51376770afc6bc5485` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:620d6c87af94@sha256:1a73e06ab8e06cda8daf7533e2f4ba059e9a79ea30418e7296f1edb0254656bd` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:620d6c87af94@sha256:2079d9afff625d8907b0b55d6e93c0667632f2bd5774db3788949d1b9c22486a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:620d6c87af94@sha256:2079d9afff625d8907b0b55d6e93c0667632f2bd5774db3788949d1b9c22486a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:620d6c87af94@sha256:3fbb74a592dad810455c2734c1ecf249e729e71d2eae6f5a299f41b74e1c4b5e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:620d6c87af94@sha256:83e0bfe01484394d7a67f407425df2764572f383ae22a92d0d01b05e66549f0a` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.94.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.93

<!-- source-commit: cba80649ebcdf7210aafdb80fdf90d855f9bfec4 version: 0.0.0-develop.93 -->
Published 2026-11-12. Archive SHA-256 `e1dc8e1ce948acf8a91974c15f4168c53673f835145333b2447ba97e45f437a9`.

- Change: Give the sample approvers their declared password after every deploy (#57)
- Source: [Centre-for-Open-Societal-Systems/da-registry@cba80649ebcd](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/cba80649ebcdf7210aafdb80fdf90d855f9bfec4)
- Changes since 0.0.0-develop.92: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/2fb048e4f5f63e5004cdc88092535096d807367b...cba80649ebcdf7210aafdb80fdf90d855f9bfec4

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:cba80649ebcd@sha256:adf86df169bf5c9fe2d2e24162436903f03a0dda2e90a3422b4c04868348cbc4` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:cba80649ebcd@sha256:c00cf1520cc980956e147b0c74c4f6005542b8f43a090aa1d7bd96cdcc12b9e5` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:cba80649ebcd@sha256:483f06670c8baa141e9cd0fb25b2941e019b3f6fd2ded3fb25b1dfe323e3a9a4` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:cba80649ebcd@sha256:483f06670c8baa141e9cd0fb25b2941e019b3f6fd2ded3fb25b1dfe323e3a9a4` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:cba80649ebcd@sha256:aa83582590b0428c8d42e7313beef401b59bc41f11defae730549d6384e86d4e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:cba80649ebcd@sha256:940dcd356dbd5c6a563cf86ffbd7837ecd8e522bd3be9cdea976a13514d08ea7` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.93.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.92

<!-- source-commit: 2fb048e4f5f63e5004cdc88092535096d807367b version: 0.0.0-develop.92 -->
Published 2026-11-12. Archive SHA-256 `b08d8a5aba81d1a3decd8c5c34d2bacc4c9d2f709e71f51a217e096c9339f703`.

- Change: Sample DA loader: sign the approvers in again (#58)
- Source: [Centre-for-Open-Societal-Systems/da-registry@2fb048e4f5f6](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/2fb048e4f5f63e5004cdc88092535096d807367b)
- Changes since 0.0.0-develop.91: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/9602fb22623994a5e760ae2c2c108712bcb0d0a7...2fb048e4f5f63e5004cdc88092535096d807367b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:2fb048e4f5f6@sha256:7b2fa585607c276d1f1015a91d34939b302841b192dcf85aaca7f81d02f39103` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:2fb048e4f5f6@sha256:b402b4463b4397fd16c39ccac4518322d6cd5633e6169c5ecbf916f9d97af26c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:2fb048e4f5f6@sha256:9fb1a2e82d7a8416a736722febbe4037c53de5d3d79d8abab2775006d1ad0978` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:2fb048e4f5f6@sha256:9fb1a2e82d7a8416a736722febbe4037c53de5d3d79d8abab2775006d1ad0978` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:2fb048e4f5f6@sha256:fe4bb519e56829293feb52249cfc211d584cdee55d7006eb9de5855a70510d6a` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:2fb048e4f5f6@sha256:2e9775f55f12875fb0d8b683c71ff8e289d9941f9542d50b45fd05c1bef30282` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.92.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.91

<!-- source-commit: 9602fb22623994a5e760ae2c2c108712bcb0d0a7 version: 0.0.0-develop.91 -->
Published 2026-11-12. Archive SHA-256 `5ba1ff36e34fbcc18e494757aaf2246a892787ca28c47215fae8d732d8f1e4c8`.

- Change: Merge pull request #56 from yash7473/fix/da-id-on-intake-submission
- Source: [Centre-for-Open-Societal-Systems/da-registry@9602fb226239](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/9602fb22623994a5e760ae2c2c108712bcb0d0a7)
- Changes since 0.0.0-develop.89: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/e275ed0fbe0436f1d44d7348dc29d4da6f756b55...9602fb22623994a5e760ae2c2c108712bcb0d0a7

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:9602fb226239@sha256:9c27737797b5936cd995e930c441666629ac1e34b15f11cb04d1657ea546e4f6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:9602fb226239@sha256:86d74f5a7bfcd9d418b6bea8903ae77ae5ca28f66830321aaf836ca83f65c9e8` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:9602fb226239@sha256:a081cb78ad77f61306b2a71fd9bea5639fe830faacb9cf9ce751aed4c1102eec` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:9602fb226239@sha256:a081cb78ad77f61306b2a71fd9bea5639fe830faacb9cf9ce751aed4c1102eec` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:9602fb226239@sha256:086ff67ffeb749c2a0da32253e6d0e25a1df3cb7e542d157f8edf6af501a9365` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:9602fb226239@sha256:c3993763e32dd74846dc847b0c35c194cc71098a39652b4c8792eef257610d08` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.91.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.89

<!-- source-commit: e275ed0fbe0436f1d44d7348dc29d4da6f756b55 version: 0.0.0-develop.89 -->
Published 2026-11-10. Archive SHA-256 `582e5d7c1d56bb71dbf1aff2560b08449b166694aca3296ecbaaadea5fc4e6ab`.

- Change: CI: ECR layer cache and retry on agent loss for on-demand agents (#55)
- Source: [Centre-for-Open-Societal-Systems/da-registry@e275ed0fbe04](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/e275ed0fbe0436f1d44d7348dc29d4da6f756b55)
- Changes since 0.0.0-develop.88: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/4cb243d9ef73d0dcb8ffe901e40be343cfad20d4...e275ed0fbe0436f1d44d7348dc29d4da6f756b55

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:e275ed0fbe04@sha256:dd1b8082e8c0ea1fab12193128de24e3e569ea77085804935ebfd85217725512` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:e275ed0fbe04@sha256:566fa0a79b27176a7a3a41b6051e58e92b6a7a87eb4b844bff45df07160e9a3b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:e275ed0fbe04@sha256:eca91f6bf149cb9449d6d0edffc9f0482d58c2632fbffc194653105e71a02503` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:e275ed0fbe04@sha256:eca91f6bf149cb9449d6d0edffc9f0482d58c2632fbffc194653105e71a02503` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:e275ed0fbe04@sha256:946f2e26232f6dcdae89f6e5f1949d3feb950a32c1d35882f202ca3ccb7c12dd` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:e275ed0fbe04@sha256:7cab8477f7e9438bb5ab613f71524c179025f26d898298d1c34749f8fa65d467` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.89.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

## 0.0.0-develop.88

<!-- source-commit: 4cb243d9ef73d0dcb8ffe901e40be343cfad20d4 version: 0.0.0-develop.88 -->
Published 2026-11-10. Archive SHA-256 `4c87cbd0a66c9d3bb9bde7bc14030eb384ba7fd70541ba12cbb628b9743ddbbd`.

- Change: Run deploy stages on the oan-ci-deploy label (#54)
- Source: [Centre-for-Open-Societal-Systems/da-registry@4cb243d9ef73](https://github.com/Centre-for-Open-Societal-Systems/da-registry/commit/4cb243d9ef73d0dcb8ffe901e40be343cfad20d4)
- Changes since 0.0.0-develop.87: https://github.com/Centre-for-Open-Societal-Systems/da-registry/compare/b2eea8171fadc4c9dcb1c953e2511cc70ff87530...4cb243d9ef73d0dcb8ffe901e40be343cfad20d4

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-api:4cb243d9ef73@sha256:7ce600adbf660147823e90bf5f340a26e09fb7273f266a1f07b3e32d46894c5d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/partner-api:4cb243d9ef73@sha256:b4dabf064e520a2395e62ccd4a157d148fa82ffbbe0a11c3a33b8f96d219343d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:4cb243d9ef73@sha256:4851d0e0b9c83d1bcc6804d465ddaffba699f5ca6768549c450defe1be5c52a9` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/celery:4cb243d9ef73@sha256:4851d0e0b9c83d1bcc6804d465ddaffba699f5ca6768549c450defe1be5c52a9` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/db-seed:4cb243d9ef73@sha256:5bde406269eb28cb18e51f6d2afbb843e630d66a4908e6e002b02b8e1571276b` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/da-registry/staff-ui:4cb243d9ef73@sha256:7d191c315c4043bc68a0fd70bc387d9a1258f2eb1d753b5db61aebc350f31a50` |

Return to this version:

```sh
helm upgrade da-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-da-registry-0.0.0-develop.88.tgz -n da-registry --reset-values -f environments/dev/values/da.yaml --wait --timeout 15m
```

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

