# openg2p-farmer-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.844

<!-- source-commit: fd9d33ce18fd3ff6cc2b0becac75304900839a55 version: 0.0.0-develop.844 -->
Published 2026-11-11. Archive SHA-256 `c6de10dbc4f724e5d3d0c4cc7d8b07de92cea887ad18c890bfdc84740760cfb1`.

- Change: Sample loader: a failed head's members don't stop the load; no samples is SKIPPED (#269)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@fd9d33ce18fd](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/fd9d33ce18fd3ff6cc2b0becac75304900839a55)
- Changes since 0.0.0-develop.843: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/3e841ba3e9f53dd08a3a276accb5c3de1552c32c...fd9d33ce18fd3ff6cc2b0becac75304900839a55

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:fd9d33ce18fd@sha256:63de1bec53aae52f4a03785f4717f867fcacb0eae2d97e841821465d2672ce76` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:fd9d33ce18fd@sha256:f56af7f2af1453413be76334c41e350583fbcfeaa99014d0d82f92597ce3b7d0` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:fd9d33ce18fd@sha256:032f10ac3686aff4a23fc0f51962e6c3eff958c3d511ae46aa7d5745529bb470` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:fd9d33ce18fd@sha256:ff9ee7f10078c70ad15ba81a4419b9345dd5303d4ef78c8d99473711af12f438` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:fd9d33ce18fd@sha256:ff9ee7f10078c70ad15ba81a4419b9345dd5303d4ef78c8d99473711af12f438` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:fd9d33ce18fd@sha256:441b7f6af55323ce4c0a1dac315c3f7b583624ba7e1d2ba11eaf65f467f7242d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:fd9d33ce18fd@sha256:85fe11ffbcb410e526cb98d76a142ea51e4cad6c64d70bf4eaf4373af0d971c6` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.844.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.843

<!-- source-commit: 3e841ba3e9f53dd08a3a276accb5c3de1552c32c version: 0.0.0-develop.843 -->
Published 2026-11-11. Archive SHA-256 `e3fd2d9a4ef759bab3bdb1baba8441802693b9a966b9984d935a54373852903a`.

- Change: Sample loader: one stuck intake no longer stops the load; staging shows the summary (#268)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@3e841ba3e9f5](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/3e841ba3e9f53dd08a3a276accb5c3de1552c32c)
- Changes since 0.0.0-develop.842: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d...3e841ba3e9f53dd08a3a276accb5c3de1552c32c

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:3e841ba3e9f5@sha256:816bade6f3b15bcca7dc6a46803d0cd147874c738fbce3d8ff0063581b9a7b17` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:3e841ba3e9f5@sha256:947a234b3c5249d1c6bcfa1affdee05382b844c00e669ac5189fff8352798629` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:3e841ba3e9f5@sha256:3ccdc838058ec667c78120cbeec08b1ed2f57c634f65dfac7ffe6bf51f991fac` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:3e841ba3e9f5@sha256:1046f27c1733ad2fc9d9596b16c229a755b2c953097f9caa8b5831768c4a714b` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:3e841ba3e9f5@sha256:1046f27c1733ad2fc9d9596b16c229a755b2c953097f9caa8b5831768c4a714b` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:3e841ba3e9f5@sha256:b120a514eff2fbb6a5ca421c9ba45ab0be94076a0655831acbad6fabed6ef2c8` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:3e841ba3e9f5@sha256:638514fb01341056e5180be4cd548ba405b517ed5d8052c1e9c073674b4be65e` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.843.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.842

<!-- source-commit: ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d version: 0.0.0-develop.842 -->
Published 2026-11-11. Archive SHA-256 `95b99f78b525160d0a0435fd701400d47a853a31b08e86fd28c6eb46f704293d`.

- Change: AWE callback registration follows the registry's HMAC Secret (#266)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@ae21b3b8a4e2](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d)
- Changes since 0.0.0-develop.841: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/2681f31e6c2e77ed66e3143b622cc4c463ae6250...ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:ae21b3b8a4e2@sha256:0066dc0ca2f10220802b6744596a4fc4b715b00196bc38cbd00bfaf8b87ed662` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:ae21b3b8a4e2@sha256:004c945bb9257e0ad26bc4cced94beeddaf6a9ca0c6807b46507de174e10bab4` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:ae21b3b8a4e2@sha256:69bad1168153b351985b645396decbf667bb52d09e4baefed2d80823f9c98d4c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:ae21b3b8a4e2@sha256:1eae5fe8570c0bfc3faeca710c8385c22a7d6d09e227ba7208f5e5e211c484d4` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:ae21b3b8a4e2@sha256:1eae5fe8570c0bfc3faeca710c8385c22a7d6d09e227ba7208f5e5e211c484d4` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:ae21b3b8a4e2@sha256:7f23374fa84fb82e77c26c8b762d470cd2469f17f19a3f5e503596d99e3dfa42` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:ae21b3b8a4e2@sha256:037fd8eb7269ffe1f3f1f4fc847526317794e67f10b401c5b23b45638108dea3` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.842.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.841

<!-- source-commit: 2681f31e6c2e77ed66e3143b622cc4c463ae6250 version: 0.0.0-develop.841 -->
Published 2026-11-11. Archive SHA-256 `5221df42ed94e9af0d519c4f3c2f8b676e285ef5a75146b78a711c9b9b912fcb`.

- Change: Sample loader: a failed load never fails the registry upgrade (#264)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@2681f31e6c2e](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/2681f31e6c2e77ed66e3143b622cc4c463ae6250)
- Changes since 0.0.0-develop.840: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/ac551813beb073b996f54cd51dcc18a9649ab567...2681f31e6c2e77ed66e3143b622cc4c463ae6250

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:2681f31e6c2e@sha256:170da3c35fc59d0bee124753921dd7af4ee885ce5b1252010e3360da6a1de3b9` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:2681f31e6c2e@sha256:a0fb2010db56b80a35761b5c7d214f994d426e9e2db301a62a0cbbb378617183` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:2681f31e6c2e@sha256:9c053c75a4714b8480190d33b9d591a777c29a81b222cf6c8521359707c5ff7b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:2681f31e6c2e@sha256:6ff7a487a6911e94d9a88731eaf14a70fd7ebc3494ace9149b7bac7a9cd55910` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:2681f31e6c2e@sha256:6ff7a487a6911e94d9a88731eaf14a70fd7ebc3494ace9149b7bac7a9cd55910` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:2681f31e6c2e@sha256:2eff8c823d22663092f4f339112a97980ac5ee9dc658b53b895fe745c55d3dc8` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:2681f31e6c2e@sha256:539c91bc3409064944c05e73413d60a0e7ceace59f8dbf25c47fd9f8c4ba4090` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.841.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.840

<!-- source-commit: ac551813beb073b996f54cd51dcc18a9649ab567 version: 0.0.0-develop.840 -->
Published 2026-11-11. Archive SHA-256 `56777904fbff4fd7b104726c2ec60dffffa11dcb449dae192905960267869903`.

- Change: Run the sample loader as the chart's own hook Job with its settings (#262)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@ac551813beb0](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/ac551813beb073b996f54cd51dcc18a9649ab567)
- Changes since 0.0.0-develop.839: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/72f2fa0903fe8c77601146d13509ac695ae6525f...ac551813beb073b996f54cd51dcc18a9649ab567

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:ac551813beb0@sha256:f108f7ac876be3f09fc1a9d9e05993e78c3aa581ff7f932c077c8d0e93dc2726` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:ac551813beb0@sha256:a0e047abc9b133e0c229789881de7e01b14a65215df1a7247c5d68881885c4a5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:ac551813beb0@sha256:3332a1e55243b719613963ea6a38d8dc12215d1cec7562a058aab6e4a9b5f082` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:ac551813beb0@sha256:4cd28e752d686f90160fac6925ad4f2b3dc2a68be7213826818fe7c94ebb5342` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:ac551813beb0@sha256:4cd28e752d686f90160fac6925ad4f2b3dc2a68be7213826818fe7c94ebb5342` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:ac551813beb0@sha256:20ef8a7811bca1d964b1f8bd51b0750a33f0fd3f0417c72b243dc9f630a0be78` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:ac551813beb0@sha256:9cb06ee7865fbd550f1ab44dba20a9d7127e084579ca7a92ad88bb157b49ac6c` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.840.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.839

<!-- source-commit: 72f2fa0903fe8c77601146d13509ac695ae6525f version: 0.0.0-develop.839 -->
Published 2026-11-10. Archive SHA-256 `0640aa144f9f5192fd1b1ceb9c2361f371f75b5610067443511e237bd69b015e`.

- Change: CI: on-demand agents: retry on agent loss, real Postgres readiness (#258)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@72f2fa0903fe](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/72f2fa0903fe8c77601146d13509ac695ae6525f)
- Changes since 0.0.0-develop.838: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/c2efce305864d1407da74e1af5cc082e552be564...72f2fa0903fe8c77601146d13509ac695ae6525f

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:72f2fa0903fe@sha256:bbfea215f2dcb82bcda88a947bdf143b2b1621c1fd3e0f14249012b15e9a35f6` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:72f2fa0903fe@sha256:56d8927bbe723bfc949e8e2070712df5c267fe7325da98f899c750c4d9dae22d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:72f2fa0903fe@sha256:4933d57d99cb307f0e3d0b87f8d68029a2080765d8afe635e636f5daa0bc59d4` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:72f2fa0903fe@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:72f2fa0903fe@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:72f2fa0903fe@sha256:493f92bfe9a20e9d92e02b928bc5528ed529371beda010b9c34f7964cdbcfec2` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:72f2fa0903fe@sha256:1513cff530766ea658527912a337f798078c21932738175093b5cf4c34b40a89` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.839.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.838

<!-- source-commit: c2efce305864d1407da74e1af5cc082e552be564 version: 0.0.0-develop.838 -->
Published 2026-11-10. Archive SHA-256 `2b1169746becb70b46720c0567ccc6fa148d17e4e35c019401ca2fa079537c66`.

- Change: Declare the Farmer connector definitions in git and apply them after every services deploy (#259)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@c2efce305864](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/c2efce305864d1407da74e1af5cc082e552be564)
- Changes since 0.0.0-develop.837: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/4c5d8c3ff558a560afaed8ba03d9ad5208c7e25d...c2efce305864d1407da74e1af5cc082e552be564

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:c2efce305864@sha256:f7c9f7c3bb447ba04738a1728f75e029cc1359dea02b7796f6081233389ce886` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:c2efce305864@sha256:a13f9ecd292b68881712b1440bedbae5c5287f4b6826c4a78b9197c1e57c7e75` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:c2efce305864@sha256:7fbcfae2612d0e4366dd317f45497928fd06a8f8757512ca44c7c7089de2ca63` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:c2efce305864@sha256:935e588c8cd021effe076b8fef9ee5925b95c390f3a1e3f58659f775911eadcb` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:c2efce305864@sha256:935e588c8cd021effe076b8fef9ee5925b95c390f3a1e3f58659f775911eadcb` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:c2efce305864@sha256:b8f739761b85ea7e9db289fbfcc42760901c62dfdf2b8362c94d2087ad460c1f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:c2efce305864@sha256:b1eed642cb87cc9c9a3be9810a0ca8b4fe0f328fe9dc8728efc4da0fd0440c4e` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.838.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.837

<!-- source-commit: 4c5d8c3ff558a560afaed8ba03d9ad5208c7e25d version: 0.0.0-develop.837 -->
Published 2026-11-10. Archive SHA-256 `ba118b12fcc0a1a1b86cca38d23f9e559103649a6119be6efedfc8826bb35843`.

- Change: Give the sample loader its Master Data settings and skip cleanly without them (#257)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@4c5d8c3ff558](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/4c5d8c3ff558a560afaed8ba03d9ad5208c7e25d)
- Changes since 0.0.0-develop.836: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/2e61eec84e35f92b9a3f246c87b4ed875c87f211...4c5d8c3ff558a560afaed8ba03d9ad5208c7e25d

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:4c5d8c3ff558@sha256:fafcc767a79439865527678d822acc9b9857ed9c50f5bea69f5781f223f983bf` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:4c5d8c3ff558@sha256:66008b26fa7eac4f5ec453132b1f503ef31c9ab412d3c3741e6c5a3954bfaeaa` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:4c5d8c3ff558@sha256:e6d27561279c8b301b00b65da6f14e1ee2d8c7b1970ebebddaa9cf5607bc4f74` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:4c5d8c3ff558@sha256:40946f2e88876b69b518b9c647e18f7a6538f9b2bfcc83c7258e19b129f5bc6a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:4c5d8c3ff558@sha256:40946f2e88876b69b518b9c647e18f7a6538f9b2bfcc83c7258e19b129f5bc6a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:4c5d8c3ff558@sha256:30644e675b8e597b5acfb909200979883e193f4ebe5f76de773b60cc8ff9c175` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:4c5d8c3ff558@sha256:84eb8871f2f05b04b875bca269e1985420b0c0296954cabb77ad0437da8dcecb` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.837.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.836

<!-- source-commit: 2e61eec84e35f92b9a3f246c87b4ed875c87f211 version: 0.0.0-develop.836 -->
Published 2026-11-10. Archive SHA-256 `6f6837f76b610c9765566ea549f91fc4a1b3e747f28956770b09bdfb5e89fa07`.

- Change: Run deploy stages on the oan-ci-deploy label (#255)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@2e61eec84e35](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/2e61eec84e35f92b9a3f246c87b4ed875c87f211)
- Changes since 0.0.0-develop.835: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4...2e61eec84e35f92b9a3f246c87b4ed875c87f211

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:2e61eec84e35@sha256:d28976b2cdda654debad4b26a02b6097eee4ee61f339b7c43a1ddfcc4ab4699a` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:2e61eec84e35@sha256:66d161ce02aed4aee4cda5b8ea0d1be8071805a4ca27f26e79d83141102ae8c9` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:2e61eec84e35@sha256:ba93de71caad96d821a601f7be59daac4405deaeafad6bb5d14f9da91dc7c765` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:2e61eec84e35@sha256:f19b3d6e3c897711a05ea2175c0f93adb4a7509081bb664845dbe6a1b71f666f` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:2e61eec84e35@sha256:f19b3d6e3c897711a05ea2175c0f93adb4a7509081bb664845dbe6a1b71f666f` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:2e61eec84e35@sha256:85f98e18ecb205ddb09513b11f5147ccf4c98d5d72acbf3db55830e20c8b128b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:2e61eec84e35@sha256:56777330c10dfd428f670c607d2886e9d9a295c6ae6c8da55326d50989520ed4` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.836.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.835

<!-- source-commit: b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4 version: 0.0.0-develop.835 -->
Published 2026-11-10. Archive SHA-256 `6acca71971d9aaa093822c5d22be92719b0dfbb3c34a0f5a5d41f659a7a593b0`.

- Change: Add a load sample data option to the staging build (#253)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@b46a215b6731](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4)
- Changes since 0.0.0-develop.834: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/303596597adba08315502216488bea9b136cc376...b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:b46a215b6731@sha256:85920aeed4529b9fcf630c67f6c3875f54a9ffdf29694edf8ec13869413a8e5e` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:b46a215b6731@sha256:45b5b667331132a6e70c1c2bcb0928bf7039ba3b3e800572f7f7365b62e36ad8` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:b46a215b6731@sha256:f699d8c7cc9014f9ff3817a77dff5fd8c0ab77489acdd8583dcddd98b3e45a0c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:b46a215b6731@sha256:2404f834d2bb51d4ca175a289b274c89a8fcddac481d52c3fcff400402967a0e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:b46a215b6731@sha256:2404f834d2bb51d4ca175a289b274c89a8fcddac481d52c3fcff400402967a0e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:b46a215b6731@sha256:a3337950770856e1c7bfa8edf8155652b3192dcd24539cf6ccd2989918ebdc9c` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:b46a215b6731@sha256:40a4f98b1a8a097f68a559ae8d2647d080d0793b67f64878db3f79e1fcd945f9` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.835.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.834

<!-- source-commit: 303596597adba08315502216488bea9b136cc376 version: 0.0.0-develop.834 -->
Published 2026-11-10. Archive SHA-256 `8ff2dcd701f2efd8f485796555dfd1c2bb3f0181ee43ee20de09be34af97dbcf`.

- Change: Docs: use the .development New Dev hostnames (#251)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@303596597adb](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/303596597adba08315502216488bea9b136cc376)
- Changes since 0.0.0-develop.833: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/0101d51c6ef6f2482b6a91697b39e9aaac390a38...303596597adba08315502216488bea9b136cc376

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:303596597adb@sha256:9150e30f52e4a7cc1c2111d93bb6bf82baec365303adc3246ea2b6920265e1ef` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:303596597adb@sha256:81dfb799dbe72c62d9d697b47ba5ad221467a5b650fefb6748071d35d3fac75e` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:303596597adb@sha256:6e6fbca65d7484037fd3cd503d7de1470726e9da068b1e45501f925579c42bee` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:303596597adb@sha256:2aa5652e77c577cd89639c1ff588c0592aa25d1bb074c093d91a1271c4880824` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:303596597adb@sha256:2aa5652e77c577cd89639c1ff588c0592aa25d1bb074c093d91a1271c4880824` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:303596597adb@sha256:b042452d6e5062a011330469edf20289e4e58d5442303dc8f430334e18bca132` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:303596597adb@sha256:2967c5ec1d657b92f5e49e31ffaf3e19182135931554980d668a2ca13c506234` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.834.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.833

<!-- source-commit: 0101d51c6ef6f2482b6a91697b39e9aaac390a38 version: 0.0.0-develop.833 -->
Published 2026-11-09. Archive SHA-256 `c4bcdb7abcb2b6c31b0342837e8f957056c60ee434dfccdcf38e8d5c66fe2d8a`.

- Change: Use the New Dev wildcard host names (#250)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@0101d51c6ef6](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/0101d51c6ef6f2482b6a91697b39e9aaac390a38)
- Changes since 0.0.0-develop.828: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/b7b0f527f04ccdaf21dc3d74390227d5288da3ed...0101d51c6ef6f2482b6a91697b39e9aaac390a38

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:0101d51c6ef6@sha256:df9b54da2b99c234cee75f84f259cd15f70204f94889176b4aebda348e4076e7` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:0101d51c6ef6@sha256:d1370d153b76df5e5c5ed24ba0a1bd15f8627abaf45608c16ba30e0c961dade4` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:0101d51c6ef6@sha256:4a9e6012774dd38b81db96d80fbf8687b77424ef5aef24a0303afb95f1903267` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:0101d51c6ef6@sha256:fbfb9ff73a522a9596a58c0655999d1e1df9a5f03d1cba67a8eeff030ebf1a76` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:0101d51c6ef6@sha256:fbfb9ff73a522a9596a58c0655999d1e1df9a5f03d1cba67a8eeff030ebf1a76` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:0101d51c6ef6@sha256:8b0adab14e232a3560416326b25bb8aa1aa108da9705e489030dd4441d1ce4fe` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:0101d51c6ef6@sha256:160fda6641d7aa5ad97bd3fbf84b02d03813c15a2ad4891e428fcaa4e1853cfb` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.833.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.828

<!-- source-commit: b7b0f527f04ccdaf21dc3d74390227d5288da3ed version: 0.0.0-develop.828 -->
Published 2026-11-09. Archive SHA-256 `d93cf51dbd00263815075c9772dbed26a2950bac344fd0bac2430b3889656e77`.

- Change: Roll an active connector's images automatically with a smoke check and rollback (#245)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@b7b0f527f04c](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/b7b0f527f04ccdaf21dc3d74390227d5288da3ed)
- Changes since 0.0.0-develop.827: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/d4d3042bb15188a7d71f999627883bb4253bbf71...b7b0f527f04ccdaf21dc3d74390227d5288da3ed

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:b7b0f527f04c@sha256:0ea13856e12daa8e9c9c4a50cdb2e3a0523926bf33001274b8120660e79be2a1` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:b7b0f527f04c@sha256:0219a05803b0a5294cf2206617ea3c54336e9e018693e854795adaf912366256` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:b7b0f527f04c@sha256:14c93ded3c690bec404387760d9aac67d5457507e666a6ca4004fa76bfedf8b9` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:b7b0f527f04c@sha256:516cbf79b2091fefe424a07e47e5fc17d8e513303cfaf5d19e6b784a2391598a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:b7b0f527f04c@sha256:516cbf79b2091fefe424a07e47e5fc17d8e513303cfaf5d19e6b784a2391598a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:b7b0f527f04c@sha256:7d328518d0c09ee982349e0e2dd191614d5697d64a8467ee675d27ff4e0fc671` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:b7b0f527f04c@sha256:1e7f8e7873b44036902b1fb5758437844898cd8aad1c757e041b0a71673cc71b` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.828.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.827

<!-- source-commit: d4d3042bb15188a7d71f999627883bb4253bbf71 version: 0.0.0-develop.827 -->
Published 2026-11-08. Archive SHA-256 `dc56bb25df910d4cfbdd4fed8088e62c1374ce99642c54c50a8c62e10c6d953b`.

- Change: Carry the connector UI overlay into the services deploy stage (#244)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@d4d3042bb151](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/d4d3042bb15188a7d71f999627883bb4253bbf71)
- Changes since 0.0.0-develop.826: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/969866646703fc964ebb1af28422fe1b68212eeb...d4d3042bb15188a7d71f999627883bb4253bbf71

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:d4d3042bb151@sha256:83efc392ad316e4bbaad41c6b9a2a3844746c759d9c23676eda17837abe50f2c` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:d4d3042bb151@sha256:4e73ba129ea446301f0a56dd39a336b8e34c55cc6db56170ab58c39ad3b93581` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:d4d3042bb151@sha256:f722458a00d5ab5303b8567ab19002d52ea8c91dbb35164c1333d8ea6f7e9245` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:d4d3042bb151@sha256:9da31685eefa107d9237656c9683d795293baea32ba577c597aeaeb707e5210a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:d4d3042bb151@sha256:9da31685eefa107d9237656c9683d795293baea32ba577c597aeaeb707e5210a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:d4d3042bb151@sha256:ee76d022545255f199773b972eef2c57dc56c52f0549f97a5921c62a98b0552c` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:d4d3042bb151@sha256:baf7aaccc7e49c09fabc3a35638a7910e6e28dd38dcaad342fbe513f92c4ea0c` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.827.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.826

<!-- source-commit: 969866646703fc964ebb1af28422fe1b68212eeb version: 0.0.0-develop.826 -->
Published 2026-11-08. Archive SHA-256 `1722d07a3121c788a6a1381e9a51547dbfd0a1ffc4f8ea33fce3ee7bd51f2966`.

- Change: Run the connector schema rehearsal on the API image only (#243)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@969866646703](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/969866646703fc964ebb1af28422fe1b68212eeb)
- Changes since 0.0.0-develop.825: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/eeafa8593de134b3113eb746e9350b332b74ad1f...969866646703fc964ebb1af28422fe1b68212eeb

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:969866646703@sha256:f6da3eaebcdd9ef359f6c82542398116e0c7727a30df9135502d5472d1e7620c` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:969866646703@sha256:7a30e4c19d4de35933df79bccb5d158b38862cf80513a07e1ee39d23a38705e3` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:969866646703@sha256:bfa40b57e6d3169f969e57d0cb19c541c9aca12a030844b9650e09d6e07f98d0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:969866646703@sha256:5b9db84db499e01634761eb2e89a7c915853e6fee674538ae9b0394b1afe06f1` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:969866646703@sha256:5b9db84db499e01634761eb2e89a7c915853e6fee674538ae9b0394b1afe06f1` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:969866646703@sha256:8ee09d0d233cfaf054717b38d0b4b941c30015b53e90b929a8b7083f043a32f6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:969866646703@sha256:ee641591fc4016f45f3749eb88e3c9c7384a7a2edad443fdde2fbc44a876b7db` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.826.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.825

<!-- source-commit: eeafa8593de134b3113eb746e9350b332b74ad1f version: 0.0.0-develop.825 -->
Published 2026-11-08. Archive SHA-256 `f38bbabe7eb605d5d7ce852bb3e6952af97feb9db3c61b77db0445beb50fccdd`.

- Change: Create a missing role image repository like the component's own, then push again (#242)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@eeafa8593de1](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/eeafa8593de134b3113eb746e9350b332b74ad1f)
- Changes since 0.0.0-develop.824: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/a7a37ef1d37aa9e79ab1fcd5fbe697ee8f280f83...eeafa8593de134b3113eb746e9350b332b74ad1f

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:eeafa8593de1@sha256:5792d5dc75d0ebf54c6fde83438895d70dfb03264d5053ae209b76d93c136b78` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:eeafa8593de1@sha256:30214ae401b75a42c44b1d0c4efecffe3f36584a1cd736f00f4f36b26b341748` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:eeafa8593de1@sha256:b17daf89f0ff3d35f98ede3cf52d6988ad0e8cdbb0ba9df5b7f3eb61a4dfe446` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:eeafa8593de1@sha256:5dd83d58ce4659678851ff5d4437778a8103204009d8beec736785287ae5b93c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:eeafa8593de1@sha256:5dd83d58ce4659678851ff5d4437778a8103204009d8beec736785287ae5b93c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:eeafa8593de1@sha256:f3bafaf517ea0b4cd00bf7d5580f33ed2fc8f7fb621e4443bff006ae9aa67bf5` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:eeafa8593de1@sha256:9e6f4edf437437a718c96b166a4b41b87222f13172e5a7f9d89ebc6c8a24c44d` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.825.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.824

<!-- source-commit: a7a37ef1d37aa9e79ab1fcd5fbe697ee8f280f83 version: 0.0.0-develop.824 -->
Published 2026-11-08. Archive SHA-256 `9225f60a079740b2e84cefcdfaf90923570471129763e9a58649d909d26ba96f`.

- Change: Name the docker step that failed and catch a missing ECR repository on push (#241)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@a7a37ef1d37a](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/a7a37ef1d37aa9e79ab1fcd5fbe697ee8f280f83)
- Changes since 0.0.0-develop.823: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/60169129495d95f4922fb0a5ce23c660614d4df4...a7a37ef1d37aa9e79ab1fcd5fbe697ee8f280f83

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:a7a37ef1d37a@sha256:e731e0d24b89d8528b4a96032d5ad9bdaa0e5f8ae2cb2613407756c14b60360e` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:a7a37ef1d37a@sha256:91392ddc67f4fa595d06770685bb63ab7b8dd7857d9813aec500f9fb65cd0d2c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:a7a37ef1d37a@sha256:ca56755b252130b1da95fab1c13aabfae19f82998a2d883dafbcf246e4d11a37` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:a7a37ef1d37a@sha256:629c674633e91c9631e42fbff7e4323ee216825bf824b6c77426e8282649b4aa` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:a7a37ef1d37a@sha256:629c674633e91c9631e42fbff7e4323ee216825bf824b6c77426e8282649b4aa` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:a7a37ef1d37a@sha256:d14e3a5cfd7ec5f55dacc758231e13b134c44de39715643d7f96c39796a74f3e` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:a7a37ef1d37a@sha256:dd4ff0c9bdde4a61f47c6f283ee246b2959c649207118dd9bbcdeae0c4032c86` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.824.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.823

<!-- source-commit: 60169129495d95f4922fb0a5ce23c660614d4df4 version: 0.0.0-develop.823 -->
Published 2026-11-08. Archive SHA-256 `e58190984d647344513eda80021bc628ccf24d6122a59121830a80fbd90a081d`.

- Change: Keep publishing the earlier farmer change topic until the receivers move (#240)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@60169129495d](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/60169129495d95f4922fb0a5ce23c660614d4df4)
- Changes since 0.0.0-develop.822: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/14982326968d46e5733d29cc32516b9e98f0316d...60169129495d95f4922fb0a5ce23c660614d4df4

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:60169129495d@sha256:98e720805feceae36e6e34c62541054fe691c8daec643ed6ce71c4f15512c5d1` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:60169129495d@sha256:2f367b60728ece7fa338c46f7a8b10311a1266f7b4bab9aa415add45dd46ac5a` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:60169129495d@sha256:e7abbbec608f254e1bfecc457ebf208bb79703de59a5b3b0512002fa5d9b0c44` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:60169129495d@sha256:82d5a0f65ef446f667b68d49698ea4db25793603d67b1c24c4af843c5776fdec` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:60169129495d@sha256:82d5a0f65ef446f667b68d49698ea4db25793603d67b1c24c4af843c5776fdec` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:60169129495d@sha256:5d95113f206977db219ace596bc2e9bc71bf76afc046c66aa07d66fa52b66f4b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:60169129495d@sha256:9986f046d932bf399df3880c320a1ea2485d67bc5981a592d2a228d0f9e8089d` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.823.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.822

<!-- source-commit: 14982326968d46e5733d29cc32516b9e98f0316d version: 0.0.0-develop.822 -->
Published 2026-11-08. Archive SHA-256 `2bad41c735da0f1c89e58dbb003ee45eaf00abfbbd8927efa494e850232a1884`.

- Change: Publish the farmer change notice as farmer-registry.farmer-profile.changed.v1 (#236)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@14982326968d](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/14982326968d46e5733d29cc32516b9e98f0316d)
- Changes since 0.0.0-develop.819: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/c15d5c18f2ccfdfbce08da447cc0c594fe9d6af6...14982326968d46e5733d29cc32516b9e98f0316d

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:14982326968d@sha256:21d2c256935dd6491c569806ca66ecc577d2f167bd747abb1926ed86b3e116c9` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:14982326968d@sha256:ba1efc2bc38694246032d2dd1e921e595beab4a29d6e7d358857135965b286bf` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:14982326968d@sha256:b1fa5747a32a40c6634bf506f36aff4b56be2fa0da62014bfeee2aac12f9256a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:14982326968d@sha256:806ac4f1e5e87ce6a2a59f1197bf89fdd544e75ae213192df70120c6f58f2ea5` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:14982326968d@sha256:806ac4f1e5e87ce6a2a59f1197bf89fdd544e75ae213192df70120c6f58f2ea5` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:14982326968d@sha256:2f42d9383c34fc7a5b6853db2994e3af8ce6ff1cb7be0aaba28c732318d21626` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:14982326968d@sha256:0e7ecdc737370e5a67c27afcce3c4bb562b2713a3b3abf26ed37f8574ca15b2a` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.822.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.819

<!-- source-commit: c15d5c18f2ccfdfbce08da447cc0c594fe9d6af6 version: 0.0.0-develop.819 -->
Published 2026-11-08. Archive SHA-256 `aab302f3fe3f0360722860ac12c937e5a96a6f56a04bcbb6cd9408d2a5fdd16c`.

- Change: Add required chart check and failure mail on staging builds (#237)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@c15d5c18f2cc](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/c15d5c18f2ccfdfbce08da447cc0c594fe9d6af6)
- Changes since 0.0.0-develop.818: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/7daff6e3d2a5bb9150661e71345d6465f8114f09...c15d5c18f2ccfdfbce08da447cc0c594fe9d6af6

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:c15d5c18f2cc@sha256:4c226252d0c9f31b7141c50ef56f6d3a43a1666c27aff7447d1634f15e86f913` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:c15d5c18f2cc@sha256:40e222624ce736cb07b7a78da3e353e82d56f2579560d6d2404852e53fd7fe9b` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:c15d5c18f2cc@sha256:38cb79ee461a8e70fa4cf3ea61e383ca578c6b4d0c1d72e9ee28e7a6845fa316` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:c15d5c18f2cc@sha256:94a84d1648d3be607ff644885b0be4695f2701853af3f561a72352f38b3f9bc3` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:c15d5c18f2cc@sha256:94a84d1648d3be607ff644885b0be4695f2701853af3f561a72352f38b3f9bc3` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:c15d5c18f2cc@sha256:92a7577a07fcc194b76267b852643adea87bbac8bc5d4e78dd4ac1d0e677b365` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:c15d5c18f2cc@sha256:0c9a52f97238f26672c7d58ffd50a0a7aa383286fcef809a1f90ec96029c6327` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.819.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.818

<!-- source-commit: 7daff6e3d2a5bb9150661e71345d6465f8114f09 version: 0.0.0-develop.818 -->
Published 2026-11-08. Archive SHA-256 `b262161388167f9414b44148232948b99143828613127d2ac7e966538bc3ab66`.

- Change: Deploy on merge without Build with Parameters (#235)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@7daff6e3d2a5](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/7daff6e3d2a5bb9150661e71345d6465f8114f09)
- Changes since 0.0.0-develop.803: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/90b2649a7b10d8ba6db48164fdb478f49fcc878b...7daff6e3d2a5bb9150661e71345d6465f8114f09

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:7daff6e3d2a5@sha256:77f45d46f17049eceb7b1495e05f47efe7cb91750902766aedd813edc4085e5e` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:7daff6e3d2a5@sha256:f32eb02dcf70d6bbd0078ebf51272dbeb89417ab113b94afe0cc849d53806b56` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:7daff6e3d2a5@sha256:74d92e85aa0971f394e491bb4a577226830ebe687a4ba6de9f461fbde6657a83` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:7daff6e3d2a5@sha256:501ba0bc06e90f785006b518dcdbb42283c7f372fa3aef730ea2fb4cadbf7ee7` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:7daff6e3d2a5@sha256:501ba0bc06e90f785006b518dcdbb42283c7f372fa3aef730ea2fb4cadbf7ee7` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:7daff6e3d2a5@sha256:7ea50d29b05ddc68c2be868dd74d8033160239b9e81a9fc757b34e62f44751a1` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:7daff6e3d2a5@sha256:5224daf5d41a1c87933448b9f2459ba0e22e089277eee9dca53d532ed96220b9` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.818.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

## 0.0.0-develop.803

<!-- source-commit: 90b2649a7b10d8ba6db48164fdb478f49fcc878b version: 0.0.0-develop.803 -->
Published 2026-11-05. Archive SHA-256 `5a912d7a7b6c692a3fb9fcf1e9ac3c1933296d091b1e6430e908f3ef39397842`.

- Change: Merge pull request #228 from asmitonweb/promote-staging-automatically
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@90b2649a7b10](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/90b2649a7b10d8ba6db48164fdb478f49fcc878b)
- Changes since 0.0.0-develop.801: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/3337c093d42e4f9f7d1e87cb2b558adcce91ab74...90b2649a7b10d8ba6db48164fdb478f49fcc878b

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:90b2649a7b10@sha256:6092fc7a640a0074dac414584082eb608077a8aaeb7f2c30f3e8521a4dc83f14` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:90b2649a7b10@sha256:cb47eea3ae977e5fd7b18ec5bb67c6ed96cfd275d4b6def7b709fce47d256351` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:90b2649a7b10@sha256:c9aaecb15edc64432823824b7125593c3da020bb99afa7bc1719af98263e1b67` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:90b2649a7b10@sha256:77c260d130c5bfc2e5cb36d41b29242f0b2dabc03aff7fe9dfff41287a4a9be0` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:90b2649a7b10@sha256:77c260d130c5bfc2e5cb36d41b29242f0b2dabc03aff7fe9dfff41287a4a9be0` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:90b2649a7b10@sha256:8529be9464b04716af761d40d5b0f70c1d6e1e1e142843ed11f68611f4e47de9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:90b2649a7b10@sha256:4f5b5f2f3405ff6aaf4cf9761d106a06f683a39284f9e9624bf83c1dbeb09f5f` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-farmer-registry-0.0.0-develop.803.tgz -n farmer --reset-values -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

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

