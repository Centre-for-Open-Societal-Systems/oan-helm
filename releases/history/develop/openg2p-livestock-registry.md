# openg2p-livestock-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.454

<!-- source-commit: b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f version: 0.0.0-develop.454 -->
Published 2026-11-12. Archive SHA-256 `a6668dd53c8b14e287c117b112b81e34e7733d728cb0c435ab2385c056c3fdad`.

- Change: Give the sample approvers their declared password after every deploy (#237)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b275e4c48b1f](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f)
- Changes since 0.0.0-develop.453: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc...b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b275e4c48b1f@sha256:5ba4bd8a5fe679e454b589a64dc6062ce033042a20352da0f1b32bea1339b65c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b275e4c48b1f@sha256:f0284b69101022a182ff5ebe95973e411be65f5568cadf0f0cefc223b612ab1e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b275e4c48b1f@sha256:9ee921d0017225a9e606653eeeb3d1755e3dfbed57c04d236434145479732d90` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b275e4c48b1f@sha256:9ee921d0017225a9e606653eeeb3d1755e3dfbed57c04d236434145479732d90` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b275e4c48b1f@sha256:456ce23705ad6acd7cbec368a0c23c8a62eeaee69e36df1975eeef84794aad54` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b275e4c48b1f@sha256:8ef3aa47038381bb5fbcbc546136244ee60d85f6e58bd431b4613d1724460d3f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b275e4c48b1f@sha256:83d8a357a95e166822188711fc599705b6056f06a0fc8e3908f960e40c15683e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b275e4c48b1f@sha256:8b9ccca84c65720e713ee2ac403c569c5fc72db31244dda5f11b5dd5a115417d` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.454.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.453

<!-- source-commit: b053d120c8e02c59a7db0b57ca66d52d67d3e6bc version: 0.0.0-develop.453 -->
Published 2026-11-12. Archive SHA-256 `523ede90ec9ed6807ce3e8e8c902ef4ea46dd071a1e6021b3dd36ac6945e3bf8`.

- Change: Staging connector moves to the qa.oanstaging.com scope (#234)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b053d120c8e0](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc)
- Changes since 0.0.0-develop.452: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/798ea765f01be019ced8737c33eb11f7254e4642...b053d120c8e02c59a7db0b57ca66d52d67d3e6bc

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b053d120c8e0@sha256:db862c5249f77ba0a8ebbd7acb81036fc797b62520cbc9a50dd86b41ded5e9a5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b053d120c8e0@sha256:491c55b1f9bfc35e840734f20a2a18b715d86b852a5d29d215d6a7f9f26edb4d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b053d120c8e0@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b053d120c8e0@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b053d120c8e0@sha256:29fdf78e002ccf469aaa232bffb30821d1edb4965aa4c8b84162c35fd32b9f72` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b053d120c8e0@sha256:234cb128c8c06f7e3b72e66121b3bf314bbe973cdd14e860168cdac319f720e3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b053d120c8e0@sha256:90cc503964e2c8f087ef7f3f651750a274832557478874e518c6ae46ef6d1574` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b053d120c8e0@sha256:815a6b14439e57e74c552470390dd793fe1050a565d15e8e37871bca8865f369` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.453.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.452

<!-- source-commit: 798ea765f01be019ced8737c33eb11f7254e4642 version: 0.0.0-develop.452 -->
Published 2026-11-11. Archive SHA-256 `690aefc39459e65f7b895d5a7203cc7d82aab9fe285bf5b0dbe55cfc671b1135`.

- Change: AWE callback registration follows the registry's HMAC Secret (#233)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@798ea765f01b](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/798ea765f01be019ced8737c33eb11f7254e4642)
- Changes since 0.0.0-develop.451: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/2eeb5e826da13a61179c6bcdd5499bc54cf1e275...798ea765f01be019ced8737c33eb11f7254e4642

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:798ea765f01b@sha256:a707980d756d167397e3c871518d48baae2dae50353acf376ef47a7e3dfd6532` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:798ea765f01b@sha256:97ad86249c40699117187531766c2b42df7775226d0bb46d84897a8ba3c023fd` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:798ea765f01b@sha256:ff8da996a62b4dc8fbf1e832ca4dba0564117a918e8000493a6c15bc09fb1f3e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:798ea765f01b@sha256:ff8da996a62b4dc8fbf1e832ca4dba0564117a918e8000493a6c15bc09fb1f3e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:798ea765f01b@sha256:27dcd1270c9770389b5079639fc9bc4789849b9ce2dcee7648c0275282e3dcdf` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:798ea765f01b@sha256:25e0d1241ff68498713faae3a96e04d305bbe7b7754fac80f73ee3329c65bf5d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:798ea765f01b@sha256:e433970fa45868454e74c17353d447e61eb346bac1f4a688675289158c132983` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:798ea765f01b@sha256:17b6b255e656bcc5b852bcecfea8e295be9c789c991b3e8d3eab5619d496ecbc` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.452.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.451

<!-- source-commit: 2eeb5e826da13a61179c6bcdd5499bc54cf1e275 version: 0.0.0-develop.451 -->
Published 2026-11-10. Archive SHA-256 `243d9e5a01812efaf4efc7d84041aa90dcacd8feac9071e79e5943a7da23e220`.

- Change: CI: on-demand agents: ECR layer cache, retry on agent loss, real Postgres readiness (#229)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@2eeb5e826da1](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/2eeb5e826da13a61179c6bcdd5499bc54cf1e275)
- Changes since 0.0.0-develop.450: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/c81f3f78b6c7102d20c4016edb4b919c1dc04cd3...2eeb5e826da13a61179c6bcdd5499bc54cf1e275

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:2eeb5e826da1@sha256:c42d5144faf5690ae7ee3b580a1a71e0bb496fad18ff3972bc4d064a84f3a820` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:2eeb5e826da1@sha256:d6755f06a57699a773f2043d77c1b79eec2350c9d4acf5ccf93d4f1f0c74717e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:2eeb5e826da1@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:2eeb5e826da1@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:2eeb5e826da1@sha256:ba79b19ce8e4121e7444a68e39ebd679312c77162a3b563472b35572ff0708b4` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:2eeb5e826da1@sha256:e748260b9eb06a14fccfdc603adae4da0e68f443c0b3fece1b0d52c884818fe0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:2eeb5e826da1@sha256:320daba33532080bb86ee7d103729bad9b4d289d4b8ff86d5f56e90e72b02358` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:2eeb5e826da1@sha256:50ea6bed9690fbc11ab8886b293e692d8123568e5638c34d678cd74b2b18620c` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.451.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.450

<!-- source-commit: c81f3f78b6c7102d20c4016edb4b919c1dc04cd3 version: 0.0.0-develop.450 -->
Published 2026-11-10. Archive SHA-256 `ca32fc106b231010f5b9c3680466f1e9e4229c1b7e05b8fe0892f22bbb2b3308`.

- Change: Give the disposable test database room and wait for real queries before each test module (#231)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@c81f3f78b6c7](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/c81f3f78b6c7102d20c4016edb4b919c1dc04cd3)
- Changes since 0.0.0-develop.449: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/4fd3dd7ce387d3a2d29eec06390f34f028791f7e...c81f3f78b6c7102d20c4016edb4b919c1dc04cd3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:c81f3f78b6c7@sha256:830aea1140257d00802e9c43c32882987cb73c38fdce94554c8196c7e2767901` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:c81f3f78b6c7@sha256:3844fa5ae0013ce1e06eb297e7c1851f4e13da3e48cb8a9854e3b35cbbc2adb3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:c81f3f78b6c7@sha256:11ce5c7e23d5750b0045d0f25d4f530138368b4bc5ef8bc7bf2eeb1eaedab352` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:c81f3f78b6c7@sha256:11ce5c7e23d5750b0045d0f25d4f530138368b4bc5ef8bc7bf2eeb1eaedab352` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:c81f3f78b6c7@sha256:248291df719defe3cc4a643ffc6e5b659050d5818583ff08c9954bb3ff311ab2` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:c81f3f78b6c7@sha256:065aa5c4a7b2b2a02fd62e66f4cad16ee36e5cbff1c6533a30bd07c3be0c70a9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:c81f3f78b6c7@sha256:cf59b788075f2a92dc89c70a86233298045a1b435a07f7a68dce3b788144ac95` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:c81f3f78b6c7@sha256:22326a3512d20154eb47a02d97ca9c25d1902e3f1255e259d47d3793e1330ffe` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.450.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.449

<!-- source-commit: 4fd3dd7ce387d3a2d29eec06390f34f028791f7e version: 0.0.0-develop.449 -->
Published 2026-11-10. Archive SHA-256 `c08c34e9af931d524a714297b5d2b5c601056be8b520c73a2f246520f329f840`.

- Change: Subscribe the staging livestock connector to Farmer profile changes (#230)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@4fd3dd7ce387](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/4fd3dd7ce387d3a2d29eec06390f34f028791f7e)
- Changes since 0.0.0-develop.448: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874...4fd3dd7ce387d3a2d29eec06390f34f028791f7e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:4fd3dd7ce387@sha256:83a9494879e02afff85cf550d7579296802c15686527cbd0a04f73e28441c827` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:4fd3dd7ce387@sha256:a912a478268e540a9e098632a43f7579f7e29841954250701fb816f5662aa698` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:4fd3dd7ce387@sha256:862083b546a05dc4478c24452d6245fcccf3154648b508eba52540fa2a2eaf70` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:4fd3dd7ce387@sha256:862083b546a05dc4478c24452d6245fcccf3154648b508eba52540fa2a2eaf70` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:4fd3dd7ce387@sha256:aeff067084fa8911d5bee62ca89c3f5bf6bfd63b574343ab671d4287018a98b4` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:4fd3dd7ce387@sha256:3c75e6ed91376851ebb8ac4882fa88b5b771b1b08c1d915448fb83664dbdc98c` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:4fd3dd7ce387@sha256:3839c9f6b5545b81a905b6d9b4dda4a96a6e374c29c90a941fbc9fb3abb08d53` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:4fd3dd7ce387@sha256:ca37af05225f9f65d564ee757f706bdbf98347319a46eb62466a2da1f3ec7a22` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.449.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.448

<!-- source-commit: 7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874 version: 0.0.0-develop.448 -->
Published 2026-11-10. Archive SHA-256 `a930418739239acf1aa2e39dee559df14d131f366581b444dd8c70c8b9c20dbc`.

- Change: Staging connector: drop the admin-auth keys that commonEnv never renders (#228)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@7e2729a7bf4e](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874)
- Changes since 0.0.0-develop.446: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/1c74138c15aaa4ba425cbb1a731295736797cd20...7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:7e2729a7bf4e@sha256:455117b1b45c3ec0128c43861bc334edbe1a934ba23d92e318ef9dd080937c95` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:7e2729a7bf4e@sha256:13fa05335272509992e4bf31ced7b82ee0a887e972771f61ed59c5d63789ab0e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:7e2729a7bf4e@sha256:ce4eae36fbd6ec67998fcb55df539db9df110614e8390f3b2f8b872ab875d940` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:7e2729a7bf4e@sha256:ce4eae36fbd6ec67998fcb55df539db9df110614e8390f3b2f8b872ab875d940` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:7e2729a7bf4e@sha256:136cce484d14d940f83eaf4cf75065bdabc562b090fbd15daa7750790f5aee1a` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:7e2729a7bf4e@sha256:41c444c85580ce863661b96fe6daacca59d81dca3c2566b448a10ec7846092fa` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:7e2729a7bf4e@sha256:0d7deb2697d2c1b9230d089489b99f8c496a07a522382c6432b380a0f5eb7534` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:7e2729a7bf4e@sha256:eaa6894b3557ccf6e4776f8d29b4b8879406890a0051711cfb427393aba2fc4c` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.448.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.446

<!-- source-commit: 1c74138c15aaa4ba425cbb1a731295736797cd20 version: 0.0.0-develop.446 -->
Published 2026-11-10. Archive SHA-256 `d21650d44e58d4174fcbd3c4ab7130f4f1f3db3c572b1a38df0d7165fa43aa44`.

- Change: Staging connector: expect the staging Keycloak issuer (#224)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@1c74138c15aa](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/1c74138c15aaa4ba425cbb1a731295736797cd20)
- Changes since 0.0.0-develop.444: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/684febd3b7730edba1a62a200970f91069cf770e...1c74138c15aaa4ba425cbb1a731295736797cd20

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1c74138c15aa@sha256:244de208699f7d1583310e24159281b9f61e68b349bbc11359b28ea7f410d5d6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1c74138c15aa@sha256:90724a2134898fd9b6aab30434a71dc2065ea454a289df176155fd13ce4b08c0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1c74138c15aa@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1c74138c15aa@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1c74138c15aa@sha256:6777b92d8a6750a8385cb04b57c0e4786bd506261b7e70e03241019377824194` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1c74138c15aa@sha256:0ff40275d527a8bd3c3c9f1dd02655e0de9c2d7b8e91cdc9a8487837cfb600fb` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1c74138c15aa@sha256:b64a9e31dbd07cba822f4b4d5abe70a181b578a846f91a6047e9bd9e4716e5dc` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1c74138c15aa@sha256:cd9510b560d92644563edc2bb690acbbb1b904dcc91e62dd881c1fc3c806101b` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.446.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.444

<!-- source-commit: 684febd3b7730edba1a62a200970f91069cf770e version: 0.0.0-develop.444 -->
Published 2026-11-10. Archive SHA-256 `5e8b23fa725b79110e3e060d42479b5e54ce27ad364b3d74f55c9945d23491c0`.

- Change: Add a load sample data option to the staging build (#222)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@684febd3b773](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/684febd3b7730edba1a62a200970f91069cf770e)
- Changes since 0.0.0-develop.443: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b6656cdfba74e284013b774d652daf626ad617f3...684febd3b7730edba1a62a200970f91069cf770e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:684febd3b773@sha256:8588a8673dc17667d4abde75ef25f03466e4a3c7dd656fe87b0b7aeeb0640a6b` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:684febd3b773@sha256:343327f45b0b6826847b8a723e57a252188656dbf098ca55a6829eeb52b02593` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:684febd3b773@sha256:96cf8f68236e6270dd3117ae5dc0ef27e04f978c1484ad521c86d521cdced4e1` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:684febd3b773@sha256:96cf8f68236e6270dd3117ae5dc0ef27e04f978c1484ad521c86d521cdced4e1` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:684febd3b773@sha256:2c32c27f17093d5b500069f0fde56d711a8cf895f7ebe941fa052ae13a03f209` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:684febd3b773@sha256:f80c1d98d313c2abb4d401410999fd1acead6e49a978f01843b9bbf243302ba4` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:684febd3b773@sha256:097da9d8ccc1336f6520484594cd711655a93bc3a482658edce989a5f4c89289` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:684febd3b773@sha256:87775242328412aad13ff80ee6ba1d996d5b66e2388f9e835b354faba352b45d` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.444.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.443

<!-- source-commit: b6656cdfba74e284013b774d652daf626ad617f3 version: 0.0.0-develop.443 -->
Published 2026-11-10. Archive SHA-256 `f056be27cd308247496ce612997434ac8b58b9059107a01202705e195c17a9b2`.

- Change: New Dev: point the ODK connectors at odk-central.development.oanstaging.com (#213)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b6656cdfba74](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b6656cdfba74e284013b774d652daf626ad617f3)
- Changes since 0.0.0-develop.441: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/418c8fab326cee99d08aaf59a914c6afb8ecf7a9...b6656cdfba74e284013b774d652daf626ad617f3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b6656cdfba74@sha256:e6726465d2941204f1a696944043fca0843d1ec3d3fcb97222f369adae0ee630` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b6656cdfba74@sha256:26c5fd89e500752631b758f303e7d2e8459d0fea682cbc93fd4704af72016fea` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b6656cdfba74@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b6656cdfba74@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b6656cdfba74@sha256:fd8837e565ebc8293dea3000847177016e3aef2d8e49df5f3830b452735de307` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b6656cdfba74@sha256:0e3313ef4acd39f150b3cfdef1d02e09dbb57d8b28a8882b3c910d337108c6ba` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b6656cdfba74@sha256:77564efdad743018f2683f08c935d92efae0cb7f5e889974e634df769706282a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b6656cdfba74@sha256:d0e0566f045079106cacebb8464d03e717974923c361daac1fea9fd1db1ab5f9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.443.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.441

<!-- source-commit: 418c8fab326cee99d08aaf59a914c6afb8ecf7a9 version: 0.0.0-develop.441 -->
Published 2026-11-09. Archive SHA-256 `dac25151b0beb31b0861a400aafe870071e6fc5a8b00a854983d7cb96fd8ffb3`.

- Change: Merge pull request #218 from simretyibeltal-commits/revert-app-publish-v2
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@418c8fab326c](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/418c8fab326cee99d08aaf59a914c6afb8ecf7a9)
- Changes since 0.0.0-develop.435: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/cd63c4c20c6302d2f4696e58cae97f958ce0cec6...418c8fab326cee99d08aaf59a914c6afb8ecf7a9

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:418c8fab326c@sha256:d1cc9759f3835d073270cb32e3a1dfa4686f4aa02374f8af96928b3cffca26f1` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:418c8fab326c@sha256:aea7c59bd4393613bca3291f57f89d9953dd08bdc996c3ef756bc3db280158a7` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:418c8fab326c@sha256:43a774ce42ecf7e5be28535e1cabe62182d90829351a3bde69679503d9681ae9` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:418c8fab326c@sha256:43a774ce42ecf7e5be28535e1cabe62182d90829351a3bde69679503d9681ae9` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:418c8fab326c@sha256:3431f13a6ab0b185465a7f20e1ace6b17accdebe53b87f7223a0400a1f17d29e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:418c8fab326c@sha256:ddb012e2efbed59200b55a07b5059fc8a9f04b9bab46985371a23fdf3ab00f16` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:418c8fab326c@sha256:33a01eab2e215ae8975b14494956e9700aa92abbaaf6418ad71ccdfd49f818af` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:418c8fab326c@sha256:88183b6ca403f1d46800cfed1ce524a3880ea92bc551c9866e03fcf8de9ced04` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.441.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.435

<!-- source-commit: cd63c4c20c6302d2f4696e58cae97f958ce0cec6 version: 0.0.0-develop.435 -->
Published 2026-11-08. Archive SHA-256 `27cf2432150601e5fc37fdfa4de8d0445276513ee1e9d7c9867c81837e04a2e7`.

- Change: Seed renames the Farmer-reference tables before it writes the archive (#210)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@cd63c4c20c63](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/cd63c4c20c6302d2f4696e58cae97f958ce0cec6)
- Changes since 0.0.0-develop.433: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/455e6ec2eac4e5e12a5719df558efb3a6d40b989...cd63c4c20c6302d2f4696e58cae97f958ce0cec6

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:cd63c4c20c63@sha256:4f690993e85241f81289acaa96f6c2f0c2cebcdd1bf61c4f9d25640c8b44c02c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:cd63c4c20c63@sha256:6a181e723f8cab172d0e12112370936d925f63ab70ac35c99b4edb0a278f8582` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cd63c4c20c63@sha256:054b7f32064b1cea9483c8ece0b06d69f6aa749ac2f907660fd7120e2c3b174d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cd63c4c20c63@sha256:054b7f32064b1cea9483c8ece0b06d69f6aa749ac2f907660fd7120e2c3b174d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:cd63c4c20c63@sha256:06a6a3cbbda0fa1c62ca55789596d077ab3c3ec7be2adf9b8b37881f72bfd56c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:cd63c4c20c63@sha256:743ef4dd7ef0beb4e54f67bb0d71877673f841e110b7daa93ab498479188dea6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:cd63c4c20c63@sha256:65d97767e053614f871eed9fd770d8d59e04c3893cca44a34c835e1160f068c9` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:cd63c4c20c63@sha256:b5c22bcd5e2caf546a67a098a96712f716b95d4a21d6a69fc31215f96e211da6` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.435.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.433

<!-- source-commit: 455e6ec2eac4e5e12a5719df558efb3a6d40b989 version: 0.0.0-develop.433 -->
Published 2026-11-08. Archive SHA-256 `b8eec5f698bd8d46c566309682b1cd655985854cb3647ce12896fbd62b1eac6d`.

- Change: Replace the stale parameter test with a check that the pipeline takes no parameters (#211)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@455e6ec2eac4](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/455e6ec2eac4e5e12a5719df558efb3a6d40b989)
- Changes since 0.0.0-develop.426: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/cc5b130f5aeab6e98d56e80cab9217ee68088f07...455e6ec2eac4e5e12a5719df558efb3a6d40b989

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:455e6ec2eac4@sha256:fa5204d32d9f150b2a0427c1ffb6ae30b4382caf19359819027f302e04dd7a47` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:455e6ec2eac4@sha256:c3ef43b3ccbe4a39add9792257cce2f51cc7e82c70bba580c147d755a714b02f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:455e6ec2eac4@sha256:3e417f0273beceea584f9fde6c0c45eb61d8b2d47dd84b58fe5f3a8c734bc24c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:455e6ec2eac4@sha256:3e417f0273beceea584f9fde6c0c45eb61d8b2d47dd84b58fe5f3a8c734bc24c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:455e6ec2eac4@sha256:0e29d432b49170be9aad7e7349e0d897da66882b3e5be2432e03a332c6b22166` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:455e6ec2eac4@sha256:9a579758a5eb3905a70c8953ec74ac8a83ab4dc8f33c15c4a649f5666a6f59fc` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:455e6ec2eac4@sha256:909bcd34cc1e7865d9d07de3f2c974a14a59883aae70279501b263a7cfeb5653` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:455e6ec2eac4@sha256:6d6bd625cc17e2f1ad087828d0a64eb9cce1d51ebf0bfce78219c06e895a1254` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.433.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.426

<!-- source-commit: cc5b130f5aeab6e98d56e80cab9217ee68088f07 version: 0.0.0-develop.426 -->
Published 2026-11-05. Archive SHA-256 `efb8a761dd304fbc7108ede269cff6c1a5866d020c910ebae37c358fcb892265`.

- Change: Merge pull request #199 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@cc5b130f5aea](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/cc5b130f5aeab6e98d56e80cab9217ee68088f07)
- Changes since 0.0.0-develop.424: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/e5082c54e7ab7404902c324d9ee86ae920a166d2...cc5b130f5aeab6e98d56e80cab9217ee68088f07

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:cc5b130f5aea@sha256:5c6c14ea7011cca09cace8f34d441dc5c1e1592a9fa8a1f3e6d504a71d58f123` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:cc5b130f5aea@sha256:7678c266d04b4a5d8f368af6a22067fe9281be11d8faae027066886b7151e555` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cc5b130f5aea@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cc5b130f5aea@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:cc5b130f5aea@sha256:8e2b12e2fcacb8de4b830fe8979630798218f8759daf92ad0e0382ec3460622d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:cc5b130f5aea@sha256:9e1a17531f33ae7b23312770c542e2073688324867860a61a0f72512efd24e8b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:cc5b130f5aea@sha256:c23f11a12c2e8b7d12edd2581cbfb927acd5174a99b80ee5e770cae88085a336` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:cc5b130f5aea@sha256:0e6a34e3413b317261a74f5dc878fec4573b173f435890ab957d170fc2a6120e@sha256:f105a023e2cf38149ae194eefae91d9d9a9d8ab8c6839a5b8d8c3a2d40958ce9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.426.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.424

<!-- source-commit: e5082c54e7ab7404902c324d9ee86ae920a166d2 version: 0.0.0-develop.424 -->
Published 2026-11-05. Archive SHA-256 `bbc15f61c8ed1081c6b56d814bbb1a6f843dff9f833d9bb5f6ff29fbd8b2a5d1`.

- Change: Move the Livestock chart into this repository and deploy the chart each build packages
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@e5082c54e7ab](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/e5082c54e7ab7404902c324d9ee86ae920a166d2)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:e5082c54e7ab@sha256:ff7100de2038fa19c2c8b2043021521f360fe106187610b81f5f7d65b91de5b7` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:e5082c54e7ab@sha256:5ad5d05addcf08c4a03ecfe5d17cac2244d7a309ca9c62f40970424bedd290bf` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:e5082c54e7ab@sha256:d839a0535588d7c9fe5bf79135a01d0fe12ceba351e9c6dcd2d145d4bd907783` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:e5082c54e7ab@sha256:d839a0535588d7c9fe5bf79135a01d0fe12ceba351e9c6dcd2d145d4bd907783` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:e5082c54e7ab@sha256:48ec19309180d11c993ac9be2c3df1cf0ef73764e699bed54c3a43545d274095` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:e5082c54e7ab@sha256:18b2b2885546c5c1c5929d93edf50159360efda95219a480890a00de290b1cd3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:e5082c54e7ab@sha256:84141e4a37c54f85de9ed52fa621e4e4bb6243d8dd802f56f56a61c0d444814c` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:e5082c54e7ab@sha256:b2d470d8a6e7f33a468dd09049e902ccc1015e2c386aabd0f694ae0e42825870@sha256:f105a023e2cf38149ae194eefae91d9d9a9d8ab8c6839a5b8d8c3a2d40958ce9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.424.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

