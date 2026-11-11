# openg2p-farmer-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.850

<!-- source-commit: ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d version: 1.0.0-rc.850 -->
Published 2026-11-11. Archive SHA-256 `5060c69a31ce0507ea96baadffa893f976725c2db59bec9ae65e63bf74f55e0f`.

- Change: AWE callback registration follows the registry's HMAC Secret (#266)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@ae21b3b8a4e2](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d)
- Changes since 1.0.0-rc.848: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/2681f31e6c2e77ed66e3143b622cc4c463ae6250...ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.850@sha256:0066dc0ca2f10220802b6744596a4fc4b715b00196bc38cbd00bfaf8b87ed662` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.850@sha256:004c945bb9257e0ad26bc4cced94beeddaf6a9ca0c6807b46507de174e10bab4` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.850@sha256:69bad1168153b351985b645396decbf667bb52d09e4baefed2d80823f9c98d4c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.850@sha256:1eae5fe8570c0bfc3faeca710c8385c22a7d6d09e227ba7208f5e5e211c484d4` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.850@sha256:1eae5fe8570c0bfc3faeca710c8385c22a7d6d09e227ba7208f5e5e211c484d4` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.850@sha256:7f23374fa84fb82e77c26c8b762d470cd2469f17f19a3f5e503596d99e3dfa42` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.850@sha256:037fd8eb7269ffe1f3f1f4fc847526317794e67f10b401c5b23b45638108dea3` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.850.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.848

<!-- source-commit: 2681f31e6c2e77ed66e3143b622cc4c463ae6250 version: 1.0.0-rc.848 -->
Published 2026-11-11. Archive SHA-256 `08ac61046aaa8b7e06f4e97eaf05f55db9693b59804d02eb934171d36a35d961`.

- Change: Sample loader: a failed load never fails the registry upgrade (#264)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@2681f31e6c2e](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/2681f31e6c2e77ed66e3143b622cc4c463ae6250)
- Changes since 1.0.0-rc.846: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/ac551813beb073b996f54cd51dcc18a9649ab567...2681f31e6c2e77ed66e3143b622cc4c463ae6250

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.848@sha256:170da3c35fc59d0bee124753921dd7af4ee885ce5b1252010e3360da6a1de3b9` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.848@sha256:a0fb2010db56b80a35761b5c7d214f994d426e9e2db301a62a0cbbb378617183` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.848@sha256:9c053c75a4714b8480190d33b9d591a777c29a81b222cf6c8521359707c5ff7b` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.848@sha256:6ff7a487a6911e94d9a88731eaf14a70fd7ebc3494ace9149b7bac7a9cd55910` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.848@sha256:6ff7a487a6911e94d9a88731eaf14a70fd7ebc3494ace9149b7bac7a9cd55910` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.848@sha256:2eff8c823d22663092f4f339112a97980ac5ee9dc658b53b895fe745c55d3dc8` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.848@sha256:539c91bc3409064944c05e73413d60a0e7ceace59f8dbf25c47fd9f8c4ba4090` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.848.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.846

<!-- source-commit: ac551813beb073b996f54cd51dcc18a9649ab567 version: 1.0.0-rc.846 -->
Published 2026-11-11. Archive SHA-256 `ce24871277a8f8345144a40ebe804abfd7f3a681608cbebbdb3934c63c79830b`.

- Change: Run the sample loader as the chart's own hook Job with its settings (#262)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@ac551813beb0](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/ac551813beb073b996f54cd51dcc18a9649ab567)
- Changes since 1.0.0-rc.844: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/72f2fa0903fe8c77601146d13509ac695ae6525f...ac551813beb073b996f54cd51dcc18a9649ab567

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.846@sha256:f108f7ac876be3f09fc1a9d9e05993e78c3aa581ff7f932c077c8d0e93dc2726` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.846@sha256:a0e047abc9b133e0c229789881de7e01b14a65215df1a7247c5d68881885c4a5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.846@sha256:3332a1e55243b719613963ea6a38d8dc12215d1cec7562a058aab6e4a9b5f082` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.846@sha256:4cd28e752d686f90160fac6925ad4f2b3dc2a68be7213826818fe7c94ebb5342` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.846@sha256:4cd28e752d686f90160fac6925ad4f2b3dc2a68be7213826818fe7c94ebb5342` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.846@sha256:20ef8a7811bca1d964b1f8bd51b0750a33f0fd3f0417c72b243dc9f630a0be78` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.846@sha256:9cb06ee7865fbd550f1ab44dba20a9d7127e084579ca7a92ad88bb157b49ac6c` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.846.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.844

<!-- source-commit: 72f2fa0903fe8c77601146d13509ac695ae6525f version: 1.0.0-rc.844 -->
Published 2026-11-11. Archive SHA-256 `cc33c7ec32aab5e8644f82c4ad101971ffc131e8db07c68fc69379121b118afd`.

- Change: CI: on-demand agents: retry on agent loss, real Postgres readiness (#258)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@72f2fa0903fe](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/72f2fa0903fe8c77601146d13509ac695ae6525f)
- Changes since 1.0.0-rc.839: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/72f2fa0903fe8c77601146d13509ac695ae6525f...72f2fa0903fe8c77601146d13509ac695ae6525f

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.844@sha256:bbfea215f2dcb82bcda88a947bdf143b2b1621c1fd3e0f14249012b15e9a35f6` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.844@sha256:56d8927bbe723bfc949e8e2070712df5c267fe7325da98f899c750c4d9dae22d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.844@sha256:4933d57d99cb307f0e3d0b87f8d68029a2080765d8afe635e636f5daa0bc59d4` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.844@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.844@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.844@sha256:493f92bfe9a20e9d92e02b928bc5528ed529371beda010b9c34f7964cdbcfec2` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.844@sha256:1513cff530766ea658527912a337f798078c21932738175093b5cf4c34b40a89` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.844.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.839

<!-- source-commit: 72f2fa0903fe8c77601146d13509ac695ae6525f version: 1.0.0-rc.839 -->
Published 2026-11-11. Archive SHA-256 `a3706c94abfe3efa5d66bd18a7d7eaba614f2371a96b567099cc27e3dce681d4`.

- Change: CI: on-demand agents: retry on agent loss, real Postgres readiness (#258)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@72f2fa0903fe](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/72f2fa0903fe8c77601146d13509ac695ae6525f)
- Changes since 1.0.0-rc.838: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4...72f2fa0903fe8c77601146d13509ac695ae6525f

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.839@sha256:bbfea215f2dcb82bcda88a947bdf143b2b1621c1fd3e0f14249012b15e9a35f6` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.839@sha256:56d8927bbe723bfc949e8e2070712df5c267fe7325da98f899c750c4d9dae22d` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.839@sha256:4933d57d99cb307f0e3d0b87f8d68029a2080765d8afe635e636f5daa0bc59d4` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.839@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.839@sha256:0d93d0efb9042469ef60b30c57222a6e1badaf48f65b90ecdb70d52808f29092` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.839@sha256:493f92bfe9a20e9d92e02b928bc5528ed529371beda010b9c34f7964cdbcfec2` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.839@sha256:1513cff530766ea658527912a337f798078c21932738175093b5cf4c34b40a89` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.839.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.838

<!-- source-commit: b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4 version: 1.0.0-rc.838 -->
Published 2026-11-10. Archive SHA-256 `ad961cc8974148d53d3b5b59a2e3fe94b30fda19ee3e2a64b6aaf684c6ae11fd`.

- Change: Add a load sample data option to the staging build (#253)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@b46a215b6731](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4)
- Changes since 1.0.0-rc.836: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/303596597adba08315502216488bea9b136cc376...b46a215b6731d0b8c24d1d2a0c4be522a5b7f2a4

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.838@sha256:85920aeed4529b9fcf630c67f6c3875f54a9ffdf29694edf8ec13869413a8e5e` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.838@sha256:45b5b667331132a6e70c1c2bcb0928bf7039ba3b3e800572f7f7365b62e36ad8` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.838@sha256:f699d8c7cc9014f9ff3817a77dff5fd8c0ab77489acdd8583dcddd98b3e45a0c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.838@sha256:2404f834d2bb51d4ca175a289b274c89a8fcddac481d52c3fcff400402967a0e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.838@sha256:2404f834d2bb51d4ca175a289b274c89a8fcddac481d52c3fcff400402967a0e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.838@sha256:a3337950770856e1c7bfa8edf8155652b3192dcd24539cf6ccd2989918ebdc9c` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.838@sha256:40a4f98b1a8a097f68a559ae8d2647d080d0793b67f64878db3f79e1fcd945f9` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.838.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.836

<!-- source-commit: 303596597adba08315502216488bea9b136cc376 version: 1.0.0-rc.836 -->
Published 2026-11-10. Archive SHA-256 `a6fa5b153f3cb793046e07be55adab595615df3a8531884a2b2c2cb5072583d4`.

- Change: Docs: use the .development New Dev hostnames (#251)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@303596597adb](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/303596597adba08315502216488bea9b136cc376)
- Changes since 1.0.0-rc.813: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/90b2649a7b10d8ba6db48164fdb478f49fcc878b...303596597adba08315502216488bea9b136cc376

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.836@sha256:9150e30f52e4a7cc1c2111d93bb6bf82baec365303adc3246ea2b6920265e1ef` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.836@sha256:81dfb799dbe72c62d9d697b47ba5ad221467a5b650fefb6748071d35d3fac75e` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.836@sha256:6e6fbca65d7484037fd3cd503d7de1470726e9da068b1e45501f925579c42bee` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.836@sha256:2aa5652e77c577cd89639c1ff588c0592aa25d1bb074c093d91a1271c4880824` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.836@sha256:2aa5652e77c577cd89639c1ff588c0592aa25d1bb074c093d91a1271c4880824` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.836@sha256:b042452d6e5062a011330469edf20289e4e58d5442303dc8f430334e18bca132` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.836@sha256:2967c5ec1d657b92f5e49e31ffaf3e19182135931554980d668a2ca13c506234` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.836.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.813

<!-- source-commit: 90b2649a7b10d8ba6db48164fdb478f49fcc878b version: 1.0.0-rc.813 -->
Published 2026-11-05. Archive SHA-256 `e333c92ec12bdb5e6672af07b62bf4502dcd7163840e33f74ef0807a33d4d5ed`.

- Change: Merge pull request #228 from asmitonweb/promote-staging-automatically
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@90b2649a7b10](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/90b2649a7b10d8ba6db48164fdb478f49fcc878b)

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.813@sha256:6092fc7a640a0074dac414584082eb608077a8aaeb7f2c30f3e8521a4dc83f14` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.813@sha256:cb47eea3ae977e5fd7b18ec5bb67c6ed96cfd275d4b6def7b709fce47d256351` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.813@sha256:c9aaecb15edc64432823824b7125593c3da020bb99afa7bc1719af98263e1b67` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.813@sha256:77c260d130c5bfc2e5cb36d41b29242f0b2dabc03aff7fe9dfff41287a4a9be0` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.813@sha256:77c260d130c5bfc2e5cb36d41b29242f0b2dabc03aff7fe9dfff41287a4a9be0` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.813@sha256:8529be9464b04716af761d40d5b0f70c1d6e1e1e142843ed11f68611f4e47de9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.813@sha256:4f5b5f2f3405ff6aaf4cf9761d106a06f683a39284f9e9624bf83c1dbeb09f5f` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.813.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

