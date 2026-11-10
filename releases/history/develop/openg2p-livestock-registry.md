# openg2p-livestock-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

