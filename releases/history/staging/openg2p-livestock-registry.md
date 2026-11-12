# openg2p-livestock-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.472

<!-- source-commit: 61a63c3ab4866ec51154bc6b22f44f7ab6621454 version: 1.0.0-rc.472 -->
Published 2026-11-12. Archive SHA-256 `e48041703e50862bde48168777bf892c268bb9f89006b8e55825073a392740d7`.

- Change: Chart: the release keeps its own ECR pull secret, refreshed by a CronJob (#245)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@61a63c3ab486](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/61a63c3ab4866ec51154bc6b22f44f7ab6621454)
- Changes since 1.0.0-rc.470: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/0b74fcd3436fe3949c2b65ed174eb31b9b972233...61a63c3ab4866ec51154bc6b22f44f7ab6621454

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.472@sha256:c7eaf74d5bc203075b965e4483c833b267feacefbc9cc5c73bc70e409c1479bb` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.472@sha256:1aeb1e609f28b386a046a990a17e1cef5239f94a87d61cd54f1a9e23a6f7f7db` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.472@sha256:9541bb93154edad10c057674ccce942fadf6600f47558cb10ee08c771ab72f8c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.472@sha256:9541bb93154edad10c057674ccce942fadf6600f47558cb10ee08c771ab72f8c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.472@sha256:ee7d6d9dba4535aae59d245476b3d99fd05285d31c575cc44c615388d0447738` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.472@sha256:1efb8e77e47b8f58546531fb3b2f8413f222c3b4cc97fd430634d1245a9785d6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.472@sha256:abd7307c7e3babd8c5055e4084567bc5b04bb046b26068158d60dd196fa42e30` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.472@sha256:be4a72eacbd3d02218dd496bc3081ce852058aa24b27906db1c6642f5999ce50` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.472.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.470

<!-- source-commit: 0b74fcd3436fe3949c2b65ed174eb31b9b972233 version: 1.0.0-rc.470 -->
Published 2026-11-12. Archive SHA-256 `cb7e3fbea406d34707d3f83f5f1e5024d234ed88c6c6a557813b48380c0e3804`.

- Change: Staging Livestock: connector on the staging Gateway; pipeline delivers the dashboard UI (#243)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@0b74fcd3436f](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/0b74fcd3436fe3949c2b65ed174eb31b9b972233)
- Changes since 1.0.0-rc.467: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/602aed8dd912068fb3ebf08288a948abcfaaaf8b...0b74fcd3436fe3949c2b65ed174eb31b9b972233

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.470@sha256:8f294796442415896af56248a944f6add98a67f1f4b5aa9c2607090a9be0b187` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.470@sha256:9963d6383f6d95ae4179cfea54c833e508744b0294382db40127b934828bac83` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.470@sha256:ebad9b91247aab303790a884873039582af5beb9c67d3bccf7365aafea079234` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.470@sha256:ebad9b91247aab303790a884873039582af5beb9c67d3bccf7365aafea079234` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.470@sha256:662c753c81ce2761287b730824a589842887719e3f269403a37749ab917f6153` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.470@sha256:132cb1c44abd71da1de5e5474df805ef291b3753f7ec9ff148322f0e91b3303e` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.470@sha256:0776894c02167975c5e5a77939629c1bc4d2af73e013413a6272a9d85a09d44e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.470@sha256:892df8bd31ebdd41858843304055c8823fc92918fe28af85daa545b3715c9bb2` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.470.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.467

<!-- source-commit: 602aed8dd912068fb3ebf08288a948abcfaaaf8b version: 1.0.0-rc.467 -->
Published 2026-11-12. Archive SHA-256 `813e7da2b5b7d3a140c02d2b092e8b8e5d9e2cd219a3ea3a46ccb516c817796c`.

- Change: Staging connector: name the build by the promoted chart's commit (#239)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@602aed8dd912](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/602aed8dd912068fb3ebf08288a948abcfaaaf8b)
- Changes since 1.0.0-rc.464: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc...602aed8dd912068fb3ebf08288a948abcfaaaf8b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.467@sha256:8f7f1473505939b043361c650de9b17d623302ec580adae77a8da3a48b3f8ce6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.467@sha256:5cc06dd5fbe39ba08b3c7cc181e4eece8acd0306b7c77f890ba01bcf24a219b6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.467@sha256:29df3c5cdfb19e6347a50e544cf91dbf77bbb2efcb8f17ea408fad0e0cfb074c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.467@sha256:29df3c5cdfb19e6347a50e544cf91dbf77bbb2efcb8f17ea408fad0e0cfb074c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.467@sha256:fd815b41bc68d4feba34a05916f4f0ddc7ba976e9e69b916c592bfeb4f25002d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.467@sha256:caa79694f169db384620324f31cbb04a1370de3deb5047e09e043d266e1b1663` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.467@sha256:528c2fdf369bb32c5fa98b973d2180470a63314065f64e69d80674cfddd9c326` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.467@sha256:db71e0579ce05954f6582b575eb191acbeab8ce036337ee230dbddca4ddd40dc` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.467.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.464

<!-- source-commit: b053d120c8e02c59a7db0b57ca66d52d67d3e6bc version: 1.0.0-rc.464 -->
Published 2026-11-12. Archive SHA-256 `9eb3d18b645a7fa755dd10dda75bfa10800692e4d9d74961d23b25fed8f18a06`.

- Change: Staging connector moves to the qa.oanstaging.com scope (#234)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b053d120c8e0](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc)
- Changes since 1.0.0-rc.461: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/2eeb5e826da13a61179c6bcdd5499bc54cf1e275...b053d120c8e02c59a7db0b57ca66d52d67d3e6bc

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.464@sha256:db862c5249f77ba0a8ebbd7acb81036fc797b62520cbc9a50dd86b41ded5e9a5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.464@sha256:491c55b1f9bfc35e840734f20a2a18b715d86b852a5d29d215d6a7f9f26edb4d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.464@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.464@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.464@sha256:29fdf78e002ccf469aaa232bffb30821d1edb4965aa4c8b84162c35fd32b9f72` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.464@sha256:234cb128c8c06f7e3b72e66121b3bf314bbe973cdd14e860168cdac319f720e3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.464@sha256:90cc503964e2c8f087ef7f3f651750a274832557478874e518c6ae46ef6d1574` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.464@sha256:815a6b14439e57e74c552470390dd793fe1050a565d15e8e37871bca8865f369` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.464.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.461

<!-- source-commit: 2eeb5e826da13a61179c6bcdd5499bc54cf1e275 version: 1.0.0-rc.461 -->
Published 2026-11-11. Archive SHA-256 `7040a1fba0170fc9ddaa33b2baa5252de1a6a80fb2482b9cb5cf6a14188f8fd7`.

- Change: CI: on-demand agents: ECR layer cache, retry on agent loss, real Postgres readiness (#229)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@2eeb5e826da1](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/2eeb5e826da13a61179c6bcdd5499bc54cf1e275)
- Changes since 1.0.0-rc.455: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/1c74138c15aaa4ba425cbb1a731295736797cd20...2eeb5e826da13a61179c6bcdd5499bc54cf1e275

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.461@sha256:c42d5144faf5690ae7ee3b580a1a71e0bb496fad18ff3972bc4d064a84f3a820` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.461@sha256:d6755f06a57699a773f2043d77c1b79eec2350c9d4acf5ccf93d4f1f0c74717e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.461@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.461@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.461@sha256:ba79b19ce8e4121e7444a68e39ebd679312c77162a3b563472b35572ff0708b4` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.461@sha256:e748260b9eb06a14fccfdc603adae4da0e68f443c0b3fece1b0d52c884818fe0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.461@sha256:320daba33532080bb86ee7d103729bad9b4d289d4b8ff86d5f56e90e72b02358` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.461@sha256:50ea6bed9690fbc11ab8886b293e692d8123568e5638c34d678cd74b2b18620c` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.461.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.455

<!-- source-commit: 1c74138c15aaa4ba425cbb1a731295736797cd20 version: 1.0.0-rc.455 -->
Published 2026-11-10. Archive SHA-256 `cdf168866a4fe9098c2470e0b1b8d19767574ede35de1b6f25c912fdba50b9b9`.

- Change: Staging connector: expect the staging Keycloak issuer (#224)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@1c74138c15aa](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/1c74138c15aaa4ba425cbb1a731295736797cd20)
- Changes since 1.0.0-rc.451: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b6656cdfba74e284013b774d652daf626ad617f3...1c74138c15aaa4ba425cbb1a731295736797cd20

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.455@sha256:244de208699f7d1583310e24159281b9f61e68b349bbc11359b28ea7f410d5d6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.455@sha256:90724a2134898fd9b6aab30434a71dc2065ea454a289df176155fd13ce4b08c0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.455@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.455@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.455@sha256:6777b92d8a6750a8385cb04b57c0e4786bd506261b7e70e03241019377824194` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.455@sha256:0ff40275d527a8bd3c3c9f1dd02655e0de9c2d7b8e91cdc9a8487837cfb600fb` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.455@sha256:b64a9e31dbd07cba822f4b4d5abe70a181b578a846f91a6047e9bd9e4716e5dc` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.455@sha256:cd9510b560d92644563edc2bb690acbbb1b904dcc91e62dd881c1fc3c806101b` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.455.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.451

<!-- source-commit: b6656cdfba74e284013b774d652daf626ad617f3 version: 1.0.0-rc.451 -->
Published 2026-11-10. Archive SHA-256 `82bf650eef37248ce5f0985506977613aa51b462c11fd370b14c4c48bbfa8e6b`.

- Change: New Dev: point the ODK connectors at odk-central.development.oanstaging.com (#213)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b6656cdfba74](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b6656cdfba74e284013b774d652daf626ad617f3)
- Changes since 1.0.0-rc.432: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/cc5b130f5aeab6e98d56e80cab9217ee68088f07...b6656cdfba74e284013b774d652daf626ad617f3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.451@sha256:e6726465d2941204f1a696944043fca0843d1ec3d3fcb97222f369adae0ee630` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.451@sha256:26c5fd89e500752631b758f303e7d2e8459d0fea682cbc93fd4704af72016fea` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.451@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.451@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.451@sha256:fd8837e565ebc8293dea3000847177016e3aef2d8e49df5f3830b452735de307` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.451@sha256:0e3313ef4acd39f150b3cfdef1d02e09dbb57d8b28a8882b3c910d337108c6ba` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.451@sha256:77564efdad743018f2683f08c935d92efae0cb7f5e889974e634df769706282a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.451@sha256:d0e0566f045079106cacebb8464d03e717974923c361daac1fea9fd1db1ab5f9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.451.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-rc.432

<!-- source-commit: cc5b130f5aeab6e98d56e80cab9217ee68088f07 version: 1.0.0-rc.432 -->
Published 2026-11-05. Archive SHA-256 `48e069106a4a2bb0477d99a57d151acbb129ffcfaafdb128109b6d8553e5502d`.

- Change: Merge pull request #199 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@cc5b130f5aea](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/cc5b130f5aeab6e98d56e80cab9217ee68088f07)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1.0.0-rc.432@sha256:5c6c14ea7011cca09cace8f34d441dc5c1e1592a9fa8a1f3e6d504a71d58f123` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1.0.0-rc.432@sha256:7678c266d04b4a5d8f368af6a22067fe9281be11d8faae027066886b7151e555` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.432@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1.0.0-rc.432@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1.0.0-rc.432@sha256:8e2b12e2fcacb8de4b830fe8979630798218f8759daf92ad0e0382ec3460622d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1.0.0-rc.432@sha256:9e1a17531f33ae7b23312770c542e2073688324867860a61a0f72512efd24e8b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1.0.0-rc.432@sha256:c23f11a12c2e8b7d12edd2581cbfb927acd5174a99b80ee5e770cae88085a336` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1.0.0-rc.432@sha256:0e6a34e3413b317261a74f5dc878fec4573b173f435890ab957d170fc2a6120e@sha256:f105a023e2cf38149ae194eefae91d9d9a9d8ab8c6839a5b8d8c3a2d40958ce9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-livestock-registry-1.0.0-rc.432.tgz -n live --reset-values -f environments/staging/values/livestock.yaml --wait --timeout 15m
```

