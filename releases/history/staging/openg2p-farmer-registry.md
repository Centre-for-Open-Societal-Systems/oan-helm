# openg2p-farmer-registry: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-rc.868

<!-- source-commit: e7b12a88065c60c17a9dfbf5b50b1f1d5792c05a version: 1.0.0-rc.868 -->
Published 2026-11-12. Archive SHA-256 `e3892737bee3bac3e353af6a4efafd74045077c588a8aed93fd6931487db1307`.

- Change: Staging: the promotion delivers the Farmer dashboard UI from oan-helm (#286)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@e7b12a88065c](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/e7b12a88065c60c17a9dfbf5b50b1f1d5792c05a)
- Changes since 1.0.0-rc.866: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/1e21bd9c1c57cc22fff206d2aed7019a7d8389a2...e7b12a88065c60c17a9dfbf5b50b1f1d5792c05a

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.868@sha256:3192c067c474e9b43ba229b3e105758050b2930e69ee061129026fe0b9d4a4fe` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.868@sha256:f1b289926341a682a97cc8b67370a066dfd2a5df984e95f2720875a73815366f` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.868@sha256:a314e93f2583b2b29518a4c8d3d3fcb227da5543fee639d0684dcdae79efe00f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.868@sha256:4e8bc804691f4d6d2c22a0c753a9f2f0836ac0569db35fdc919690a93b3bd0b8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.868@sha256:4e8bc804691f4d6d2c22a0c753a9f2f0836ac0569db35fdc919690a93b3bd0b8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.868@sha256:281cd76bbbe0c704494214a4bc94730683e16595a7abe99fc958822bcf865e16` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.868@sha256:df846582bb6dce97835a0149d89476d2ab8bd1dd35c8a5070f2337891f0e5134` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.868.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.866

<!-- source-commit: 1e21bd9c1c57cc22fff206d2aed7019a7d8389a2 version: 1.0.0-rc.866 -->
Published 2026-11-12. Archive SHA-256 `f9467a3f1713316f9dd38fa45ea1d3848a134336c54c3b153832317d6aa15852`.

- Change: New Dev deploy check: allow the sample loader there (#284)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@1e21bd9c1c57](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/1e21bd9c1c57cc22fff206d2aed7019a7d8389a2)
- Changes since 1.0.0-rc.862: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/35c4c97bf1d708989adf68eee8b8c598a86c2112...1e21bd9c1c57cc22fff206d2aed7019a7d8389a2

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.866@sha256:1b051eef395c2a895f717f82bd32fc9c9c852025dc7f512541de75cad7985195` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.866@sha256:8feaf32b918d10e1a700e1eaf86ab6a3ab82739108188be3fa2203f65c89c87a` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.866@sha256:3ec720ec75b983c17a48f37e27c01a47255967d7d1387e3aa2790a533b106b55` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.866@sha256:b0d59f39ef6474e5c6987b0f09ee415e50b500800943d828e3493e02513d61af` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.866@sha256:b0d59f39ef6474e5c6987b0f09ee415e50b500800943d828e3493e02513d61af` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.866@sha256:815963508372966d7a5cefd534ec353491566e9785863712f0405bb12bf8ce41` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.866@sha256:b7401c033d227e825c02064a70c8651a3a60cd2b5881065ffe669fc9fe8e1cd0` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.866.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.862

<!-- source-commit: 35c4c97bf1d708989adf68eee8b8c598a86c2112 version: 1.0.0-rc.862 -->
Published 2026-11-12. Archive SHA-256 `32d9f3d4b28d34fd28464256db3de2f1bc30e7a58112536c443e384c009f31ac`.

- Change: Staging promotion upgrades the Farmer connector to oan-helm's staging values (#279)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@35c4c97bf1d7](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/35c4c97bf1d708989adf68eee8b8c598a86c2112)
- Changes since 1.0.0-rc.859: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/d1b420dc667b17d74ea588d0e225fc7eac0757e8...35c4c97bf1d708989adf68eee8b8c598a86c2112

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.862@sha256:5e5a0ca4b9deeca3f1c58c93f7acf7b4c8efea4e863a95ab56790c5609a605c5` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.862@sha256:c91570766c811357f536f2d799b05825d13b48ffcb8880edf6b57f992f341f92` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.862@sha256:71db82071059ed52c2eefd61530b979375e3a690320df4335054cde72b32b41a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.862@sha256:7ac442424c6e2a95de1f8991650ef73adc78fd6c623aa1c6e2fd6d2a8388db6b` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.862@sha256:7ac442424c6e2a95de1f8991650ef73adc78fd6c623aa1c6e2fd6d2a8388db6b` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.862@sha256:b924af00e2bcf53b8deeb0c9f7c97934364f1a298efc517e419d9cc8d0175733` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.862@sha256:bfac253bddb0779469e71dbda593163ae350701689854fbcc33968483c24969a` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.862.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.859

<!-- source-commit: d1b420dc667b17d74ea588d0e225fc7eac0757e8 version: 1.0.0-rc.859 -->
Published 2026-11-12. Archive SHA-256 `03170ec106790f9c1c6bdc80b1cf15dc276bf6147d934424d8fca94e19c593e0`.

- Change: Staging Farmer moves to the qa.oanstaging.com scope (#273)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@d1b420dc667b](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/d1b420dc667b17d74ea588d0e225fc7eac0757e8)
- Changes since 1.0.0-rc.856: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/83049b98b473162e9f8c50b400f990983d69a197...d1b420dc667b17d74ea588d0e225fc7eac0757e8

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.859@sha256:20c70a841acbef01209864229e63518b936c0dcb2b81dde7163c5336df38aae4` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.859@sha256:a16ca1792974c11834e9a51930ae74221275be4f77093580f8cd0e16a9a3a14e` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.859@sha256:6ab5af40ab7118b53a62f1c9429484d3f31843925e28e93b92485c1fc0a6c0da` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.859@sha256:1167186a26a72999f7a1a4d0af0856c5099ef436753023b605a865fb32414411` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.859@sha256:1167186a26a72999f7a1a4d0af0856c5099ef436753023b605a865fb32414411` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.859@sha256:3fdcada2dbf85948e4f101350bc2da05e52cca2f59c527c27077f955408bee03` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.859@sha256:fb6558c1c46a0dc2b3187204378207c412cbb4ded1a3f47c8f255bbdc960c695` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.859.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.856

<!-- source-commit: 83049b98b473162e9f8c50b400f990983d69a197 version: 1.0.0-rc.856 -->
Published 2026-11-11. Archive SHA-256 `0846c21bfe89d92453c72395fe0dd2f05587ac20fa37d71d70fb89ea301bc92c`.

- Change: Re-publish farmers whose first notice carried the TEMP- placeholder (#272)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@83049b98b473](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/83049b98b473162e9f8c50b400f990983d69a197)
- Changes since 1.0.0-rc.853: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/fd9d33ce18fd3ff6cc2b0becac75304900839a55...83049b98b473162e9f8c50b400f990983d69a197

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.856@sha256:be712dc85c6db7a13abe3e0a94cfd504fb73168657f7dee1871bdfb684563e67` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.856@sha256:d874f25953b6ac2b2e3cad23fd8be7c51b3ff048155d260f4f8e2ec29106117c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.856@sha256:6954c34296f0fbd71fbd57f4897d45183001be33d45594341e5417d8d316009f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.856@sha256:d316886298b2cb82107c240293d948e1cc87c627e640d95931d1a3126454119b` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.856@sha256:d316886298b2cb82107c240293d948e1cc87c627e640d95931d1a3126454119b` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.856@sha256:9b1de2e604a38ecb95f0314b3ff2b4807980dd5720d06c11a443b8679f40292d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.856@sha256:692d81d2fae5aeba49f3a34f6897eb3982e9d7364e7f8a176d15ace9acd57a22` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.856.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

## 1.0.0-rc.853

<!-- source-commit: fd9d33ce18fd3ff6cc2b0becac75304900839a55 version: 1.0.0-rc.853 -->
Published 2026-11-11. Archive SHA-256 `2d1b2c6d0cd7f8326184dcf423c4afeb5a03d06ef8403a24fe2a6c872990dac0`.

- Change: Sample loader: a failed head's members don't stop the load; no samples is SKIPPED (#269)
- Source: [Centre-for-Open-Societal-Systems/farmer-registry@fd9d33ce18fd](https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/commit/fd9d33ce18fd3ff6cc2b0becac75304900839a55)
- Changes since 1.0.0-rc.850: https://github.com/Centre-for-Open-Societal-Systems/farmer-registry/compare/ae21b3b8a4e240d8cae65b1f4e5542a1b2fcc40d...fd9d33ce18fd3ff6cc2b0becac75304900839a55

| Values path | Image |
| --- | --- |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-ui:1.0.0-rc.853@sha256:63de1bec53aae52f4a03785f4717f867fcacb0eae2d97e841821465d2672ce76` |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api:1.0.0-rc.853@sha256:f56af7f2af1453413be76334c41e350583fbcfeaa99014d0d82f92597ce3b7d0` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/partner-api:1.0.0-rc.853@sha256:032f10ac3686aff4a23fc0f51962e6c3eff958c3d511ae46aa7d5745529bb470` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.853@sha256:ff9ee7f10078c70ad15ba81a4419b9345dd5303d4ef78c8d99473711af12f438` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/celery:1.0.0-rc.853@sha256:ff9ee7f10078c70ad15ba81a4419b9345dd5303d4ef78c8d99473711af12f438` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/db-seed:1.0.0-rc.853@sha256:441b7f6af55323ce4c0a1dac315c3f7b583624ba7e1d2ba11eaf65f467f7242d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/sanity-tests:1.0.0-rc.853@sha256:85fe11ffbcb410e526cb98d76a142ea51e4cad6c64d70bf4eaf4373af0d971c6` |
| `analytics.dashboards.image` | `apachesuperset.docker.scarf.sh/apache/superset:4.0.1` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/dashboard-api:85fd0a3c2518@sha256:66934adc8a6f5effb3334c8bd80d5afa7eed76486ad8b0ceaf1638a24bc6e6c2` |
| `dciSigning.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `dciSigning.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |
| `registrantAuth.images.kubectl` | `docker.io/alpine/k8s@sha256:b0523f0a244ddc4c8e055aa335c040d3d78b3ead5528f4544395f7f9f69c7b68` |
| `registrantAuth.images.postgres` | `docker.io/openg2p/postgresql@sha256:65b6faa9f30de7dc89f63f055a3dd3e4ba0334172ee95c8badf49da0d08ef1c0` |

Return to this version:

```sh
helm upgrade farmer-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/openg2p-farmer-registry-1.0.0-rc.853.tgz -n farmer --reset-values -f environments/staging/values/farmer.yaml --wait --timeout 15m
```

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

