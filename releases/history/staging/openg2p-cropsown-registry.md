# openg2p-cropsown-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.503

<!-- source-commit: 97e9a92e1fb86f20019efb1241102554074d2826 version: 1.0.0-rc.503 -->
Published 2026-11-08. Archive SHA-256 `aa5b6dbba51d4e41a90e83470576300eca39947398ea975338e048fa74c40988`.

- Change: Operator job: a parameter to accept a deliberate connector chart change (#253)
- Source: [Centre-for-Open-Societal-Systems/cropsown-regsitry@97e9a92e1fb8](https://github.com/Centre-for-Open-Societal-Systems/cropsown-regsitry/commit/97e9a92e1fb86f20019efb1241102554074d2826)

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api:1.0.0-rc.503@sha256:b5443b0e56c10e288200c21789dbcfe0ef2bd0ac7f24d59f1c740dc5197bd0b7` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/partner-api:1.0.0-rc.503@sha256:3a0b820e2ab6d44e9e3a69e8602a9f0d3f47d6949640bdfa8c77b3419f9794b8` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.503@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/celery:1.0.0-rc.503@sha256:eb1f5ddd05fad9a63f0cae4655428a7c46c5c95c87e254b7b27090cf661cbeee` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/db-seed:1.0.0-rc.503@sha256:c79eb58105666e937558f43724c12bcf617890b99524aabe2e1c309aecd50864` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-ui:1.0.0-rc.503@sha256:8e656d962a466803f02dc43442aac79cf73832b207149cd159080c25eeba3b57` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/sanity-tests:1.0.0-rc.503@sha256:f2eeada6551ff6be1b1b3d4edf07914b1e50f33b7679c53aa05392d4c86d593c` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-api:1.0.0-rc.503@sha256:2dfde9e664de3d1a8f61a8149daede9889e57e3914703d163027046693218739` |
| `dashboardUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/dashboard-ui:1.0.0-rc.503@sha256:77e5859ab4b343b897b0d6cfe3c84220e27a6261fba8acf9204e4b0d7565af8c` |

Return to this version:

```sh
helm upgrade cropsown-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-cropsown-registry-1.0.0-rc.503.tgz -n crop --reset-values -f environments/staging/values/cropsown.yaml --wait --timeout 15m
```

