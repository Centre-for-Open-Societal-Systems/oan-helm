# openg2p-livestock-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

