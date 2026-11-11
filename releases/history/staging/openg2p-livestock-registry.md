# openg2p-livestock-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

