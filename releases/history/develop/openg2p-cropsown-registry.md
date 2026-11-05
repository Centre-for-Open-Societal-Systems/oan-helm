# openg2p-cropsown-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

