# openg2p-da-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

