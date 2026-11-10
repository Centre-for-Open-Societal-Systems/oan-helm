# openg2p-livestock-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

