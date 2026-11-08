# openg2p-livestock-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

