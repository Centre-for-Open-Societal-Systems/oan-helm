# openg2p-farmer-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

