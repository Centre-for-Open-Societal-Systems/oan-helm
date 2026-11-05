# openg2p-cropsown-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

