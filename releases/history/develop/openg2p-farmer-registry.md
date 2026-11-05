# openg2p-farmer-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.801

<!-- source-commit: 3337c093d42e4f9f7d1e87cb2b558adcce91ab74 version: 0.0.0-develop.801 -->
Published 2026-11-05. Archive SHA-256 `6e9e40d9ea48ce5cd21c573e97ea2a86bd2c4efec01914f715d86ac227a95cfe`.

- Change: Deploy the chart each develop build packages, and publish that same archive
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@3337c093d42e](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/3337c093d42e4f9f7d1e87cb2b558adcce91ab74)
- Changes since 0.0.0-develop.800: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/a9128872b86d01b86f2174357dceb0230df35090...3337c093d42e4f9f7d1e87cb2b558adcce91ab74

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:3337c093d42e@sha256:02f1918129ff6fd2e4bee08ae215166d2aedf54853e74c868e6c1cff2257f603` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:3337c093d42e@sha256:36e421a7269399f35fc1e9269851b1440e1704bb72cd25cf33e509da821df255` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:3337c093d42e@sha256:bc729ecf854fd000f4cf6c8a97320cebae78b8eb8ced257757175b72b10f38df` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:3337c093d42e@sha256:b24f187eb83b52a176a01bc24576ac05e27b3ed27f7bec73a528058979c9bc89` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:3337c093d42e@sha256:b24f187eb83b52a176a01bc24576ac05e27b3ed27f7bec73a528058979c9bc89` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:3337c093d42e@sha256:14a83b1e4898c681f4f2e97882f173881c35b91e3247377ba5ca0dec35fcd5e0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:3337c093d42e@sha256:89072bd9a741375aaf51645dcfb4471bf70e927a95aa6d3cb87894abe0f868e9` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.801.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.800

<!-- source-commit: a9128872b86d01b86f2174357dceb0230df35090 version: 0.0.0-develop.800 -->
Published 2026-11-05. Archive SHA-256 `d4e2b0634a58e0e3ca15422fb548a8acdd8b5ff9d1d361738a297ffb49c559ab`.

- Change: Publish the Farmer chart from this repository after each deploy (#226)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@a9128872b86d](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/a9128872b86d01b86f2174357dceb0230df35090)

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:a9128872b86d@sha256:e4032a6d92d6dc703044d68f727c446af97381e92fc6fe9d2262ae766a1c8c09` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:a9128872b86d@sha256:d425e7f3a8df88dc17be59e52c8cc43474d1522d7f51036bd8106096aab1783c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:a9128872b86d@sha256:242c6af17c68dc03e5f8a728ff66e00cdcb58c4496a6a3eb8469db7423b34d51` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:a9128872b86d@sha256:594552e833467acabbedd13803b4c7615f1e2cf818b4514897fbf771ce0fe9c5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:a9128872b86d@sha256:594552e833467acabbedd13803b4c7615f1e2cf818b4514897fbf771ce0fe9c5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:a9128872b86d@sha256:d36ac3d26494e7229911cabb30acf33e1aeb4ab4c5e898373c8f141374a7a57d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:a9128872b86d@sha256:88a635cdf3a8776a6853ff9ea8411a20eadbf9d6e5427546755db4bfbbf64384` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.800.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

