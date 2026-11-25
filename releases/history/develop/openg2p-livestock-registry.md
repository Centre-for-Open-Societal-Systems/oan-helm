# openg2p-livestock-registry: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 1.0.0-develop.234

<!-- source-commit: 7be7a46f8745d58213349f140f6247f3d013628b version: 1.0.0-develop.234 -->
Published 2026-11-25. Archive SHA-256 `cd9c2d07ef5c1dee6241a0f938c936a244ca171a1096a5842ea3b078e9d219cf`.

- Change: Merge pull request #267 from simretyibeltal-commits/docs/deployment-release-changelog
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@7be7a46f8745](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/7be7a46f8745d58213349f140f6247f3d013628b)
- Changes since 1.0.0-develop.233: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/36c9cffa6aae40dc50896581ea150fd56b146e7b...7be7a46f8745d58213349f140f6247f3d013628b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.234@sha256:42e063fd53ecb3fe7b6608e7c39192d2e6d619668872fb8cebf9a6775938581c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.234@sha256:3031587e7faf770d74c6260f4ce5cb471e9f7e62fbd3ffede2f80609942a6369` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.234@sha256:8dfa812731a9762f19d8336ba74b5c2c030384da794f9fc31a853296f44f7728` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.234@sha256:8dfa812731a9762f19d8336ba74b5c2c030384da794f9fc31a853296f44f7728` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.234@sha256:86c2f6486c2a787a7a785f3f6aa42d59198b5616d1e3d103fda591502c15711b` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.234@sha256:b9a9259d96f75fee581232eab3ccaf109eb230abf8c800aed22764e7d785e063` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.234@sha256:88a1668837a6834e950cb43ee68d8ba96ffe2484ba1c0260cd4f89470d51106b` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.234@sha256:249c5e636b48bc8005c4a0164a489d3e72f4d43a62b177bdad1033231004d874` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.234.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.233

<!-- source-commit: 36c9cffa6aae40dc50896581ea150fd56b146e7b version: 1.0.0-develop.233 -->
Published 2026-11-25. Archive SHA-256 `e8eae2faa31b57461c55c1dd679ccc34dd536b5c7d75d8b0146d74964f527475`.

- Change: Merge pull request #266 from simretyibeltal-commits/ci/coverage-and-lint
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@36c9cffa6aae](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/36c9cffa6aae40dc50896581ea150fd56b146e7b)
- Changes since 1.0.0-develop.232: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/abbea8883c93e403589bea68fcd00648c91cb6d0...36c9cffa6aae40dc50896581ea150fd56b146e7b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.233@sha256:dfa45a85c87c2d67d7caa4e74d22558de3f00f9b835a00240c99d631688b3c1e` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.233@sha256:67938b2179d399d2f04d7e2cc6ebc045d5280a98415f2b0a5f1525f006644ddf` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.233@sha256:1711fd6ee8e30da50697b69b2b2ba00c764906fd2b2f01d315f7dbed74679bcc` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.233@sha256:1711fd6ee8e30da50697b69b2b2ba00c764906fd2b2f01d315f7dbed74679bcc` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.233@sha256:6112edafd8c280d374accf69f4dd4d3c1b9f86d51ca841f7a04e9cfa8667d44d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.233@sha256:a76f63c01e3b43358d76f7018ebedb72ec2903cda6da594b402e53641d9f84c4` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.233@sha256:3fd93bc5e984b03c398536d5a25b45eebf459373fe72831fadf3918b6aa80a9e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.233@sha256:46859ae27129b0b66c4f348f2fd40e76a6a200c3b44e4e4a22767c244eaf4b1f` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.233.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.232

<!-- source-commit: abbea8883c93e403589bea68fcd00648c91cb6d0 version: 1.0.0-develop.232 -->
Published 2026-11-25. Archive SHA-256 `68052eb9dd9e2ec25bfad85b8b9faec50c32f93265e086295fc416fe27ab9293`.

- Change: Merge pull request #265 from simretyibeltal-commits/test/guard-tests
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@abbea8883c93](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/abbea8883c93e403589bea68fcd00648c91cb6d0)
- Changes since 1.0.0-develop.231: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/fc9d205a409945c378d09a31a15dc1acd31aa049...abbea8883c93e403589bea68fcd00648c91cb6d0

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.232@sha256:3d4c2e7c5cdaa05898d17278a64e49cdcac7d402f309fe62d3561e3a33f64dbf` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.232@sha256:399eae90eb116c7498e333379ab228f634102f55ed8530d07fd199a3f3a4654c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.232@sha256:5e95a359e132952e71908d1d84d233ce800e08b7bbf0a4d0f5fd8c83f5a0db8a` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.232@sha256:5e95a359e132952e71908d1d84d233ce800e08b7bbf0a4d0f5fd8c83f5a0db8a` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.232@sha256:a97857daa046dbced05f4e638b8146a2e57a54f44ffd5a49492e0026a805ba95` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.232@sha256:6173e1ec773b465d16624a3d1305ba206ca01fa03acfde75d0baa8c8974a2dcc` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.232@sha256:60e0f4c63ac1dbb4ad4bc516a4fc17ce09032dab917135f8a4e99967970a66c7` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.232@sha256:5826e201260878592432dc4232972a8291495f48ed5991cdc9062a7d2b243b77` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.232.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.231

<!-- source-commit: fc9d205a409945c378d09a31a15dc1acd31aa049 version: 1.0.0-develop.231 -->
Published 2026-11-25. Archive SHA-256 `0c95ed999fb31ea482c3f86199e57feabd358187fdbb2fa8aa32475b99d5c15b`.

- Change: Merge pull request #264 from simretyibeltal-commits/ci/validate-runs-all-tests
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@fc9d205a4099](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/fc9d205a409945c378d09a31a15dc1acd31aa049)
- Changes since 1.0.0-develop.230: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/906d8588bb43c8340ca13679a5dbe1f3d843ce20...fc9d205a409945c378d09a31a15dc1acd31aa049

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.231@sha256:14c7ca093918cd399dcc8bc2461c4b7dd9d25243d54634205c00a621ac72fe74` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.231@sha256:521364e6ee63e8ea6d25f96db3d9648559118c8a313cc66a3e19c64807320a1a` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.231@sha256:19af81b0fbf6db33ad27cd53d1f7015bb33d8a416cf571530aecec313a01c3f9` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.231@sha256:19af81b0fbf6db33ad27cd53d1f7015bb33d8a416cf571530aecec313a01c3f9` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.231@sha256:ab694d2c533cb2169cdfd9693fceafca730b173da40697ba66850fd61741f2ac` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.231@sha256:08f4a9675ccc9bfec8dfaf45d345832bd32bc1eea90618d40f845a8f0196cf45` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.231@sha256:084998f75b374647e0237f4c08562f90a24041d2e4853cf44c62a69be0ee2e1a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.231@sha256:1eaff6b8fd337b9214023fd32b30f28bb74141bdb2730d27eaa89731433db245` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.231.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.230

<!-- source-commit: 906d8588bb43c8340ca13679a5dbe1f3d843ce20 version: 1.0.0-develop.230 -->
Published 2026-11-20. Archive SHA-256 `4ae573506536e9b668da7c0be53d80f2fe889627882c4fccb59affe6714e53cd`.

- Change: fix(deploy): pin the dev values that use the Garage host (#263)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@906d8588bb43](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/906d8588bb43c8340ca13679a5dbe1f3d843ce20)
- Changes since 1.0.0-develop.229: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/6ab83b200bd7ce187f75f7f99d002e0a16b1a315...906d8588bb43c8340ca13679a5dbe1f3d843ce20

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.230@sha256:3b5b649dd61464950724bc4b96c8575be2515677b23bc9447f7d8b41e75dfd53` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.230@sha256:bf763dceb185c55f169547cb70e09b5192189532da853a49b463955a7c6a1e94` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.230@sha256:a9f2208a1916c6b33f421dbf0462ff80ab657d7adf825f06784e5df9521dda1b` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.230@sha256:a9f2208a1916c6b33f421dbf0462ff80ab657d7adf825f06784e5df9521dda1b` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.230@sha256:317c8ff0c98ef10fb0501f9ee23e456e0e5d681aed19ae2966dca2c01d981e44` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.230@sha256:7562aded764a785a39476f324825d95891d1df412772b7e36a12fd3963203e07` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.230@sha256:b29e05127e2528fb27f983fdf511a5f98a429fc9dd0a6761c4d30100786e62f8` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.230@sha256:02a45216baa87b73e73294e2378b174d2f724c3cbbc36fbbae0abdb46abed0ae` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.230.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.229

<!-- source-commit: 6ab83b200bd7ce187f75f7f99d002e0a16b1a315 version: 1.0.0-develop.229 -->
Published 2026-11-20. Archive SHA-256 `04a977e53a18a8131b62a4b1523fed89fdb7e434c579b166a9c96a2e0e2693a9`.

- Change: New Dev Livestock dashboard: sample approvers get Dashboard Viewer (dashboard pin at oan-helm 18f5bca) (#262)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@6ab83b200bd7](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/6ab83b200bd7ce187f75f7f99d002e0a16b1a315)
- Changes since 1.0.0-develop.228: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/d5c133bebbb4a4a55dbf3464713bee0ab1f20a77...6ab83b200bd7ce187f75f7f99d002e0a16b1a315

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.229@sha256:69fca19635e707894203ed629160faf01ee333bc386459e025a5c743fdb91270` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.229@sha256:789a1ede76885ada20aa1dc64bd8a4c755a1afad7772a055a1e7e0311b13d1fc` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.229@sha256:f3799cd46fec54057e93ed14af5e2ce7398307010f0ba5743661d6c8004d5496` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.229@sha256:f3799cd46fec54057e93ed14af5e2ce7398307010f0ba5743661d6c8004d5496` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.229@sha256:58b0c00e23a329e685c8c8b8c2df60721f6ca1d92bdf53c4b0a49a7f6ff57b35` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.229@sha256:e46209e2a7e858f403dc267744f35c3616ea97a697b26881a68266357281d3ba` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.229@sha256:324f5110f2925f14922aba005b9eed4542ff52b00ec30d79faa8acd93336e440` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.229@sha256:491de959778844adb35efba41b476ccb80745377922ac38fc63a5448fc7391e7` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.229.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.228

<!-- source-commit: d5c133bebbb4a4a55dbf3464713bee0ab1f20a77 version: 1.0.0-develop.228 -->
Published 2026-11-20. Archive SHA-256 `25bdd75e6c92a75fb4804c1fdb3459b4d007c5e463bf6f32dc532c65d4a773fa`.

- Change: Livestock ODK: AI technician name question in form v9, and a v8 answer used as the name only when it is one (#261)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@d5c133bebbb4](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/d5c133bebbb4a4a55dbf3464713bee0ab1f20a77)
- Changes since 1.0.0-develop.227: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/0742c0e5dde3de8dad2394eb9d98f376d652860c...d5c133bebbb4a4a55dbf3464713bee0ab1f20a77

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.228@sha256:d9c489eaf109b9207dfa5843cc83f7eef39476c06cd357afb324ec6bcde6fcd9` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.228@sha256:941eaf656626a9812a3a59d545c88c422a7711e7628f5bc9f420e545ead362e1` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.228@sha256:cea358bc80f011125e870e805499ea7e309d5ad68c93c8502456c65724e6321e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.228@sha256:cea358bc80f011125e870e805499ea7e309d5ad68c93c8502456c65724e6321e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.228@sha256:45a657ae2cd467e1cdd79e537f85acbc086cafe87a43c7c94b62788e638bb318` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.228@sha256:1495b0f8719b5981012ea101ddbba1de276dfca21ec490b8ba93d6fd43160f57` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.228@sha256:4a32aa3c19b15d5315a326b5ee7ed74c7d9d5515ccaa071dffa4ab53b7763402` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.228@sha256:d14ac60b1aac794ec1a41494882bcb779a13a157ba9febd0f549eea905eb8b54` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.228.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.227

<!-- source-commit: 0742c0e5dde3de8dad2394eb9d98f376d652860c version: 1.0.0-develop.227 -->
Published 2026-11-20. Archive SHA-256 `d2dfe2d5c4510a225998998d82fbd434f33f326e9fa5d5db2e2dbab28a5ab10a`.

- Change: New Dev connector and dashboard UI on the eoan names of develop build 226 (#260)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@0742c0e5dde3](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/0742c0e5dde3de8dad2394eb9d98f376d652860c)
- Changes since 1.0.0-develop.226: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/4101ce0bb566cb7db93d9f6290d7e92ef80d6a7f...0742c0e5dde3de8dad2394eb9d98f376d652860c

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.227@sha256:afc9b1f72862c9c9df267250d4704cf8eed43e4f91be76731b95295ffe9f7080` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.227@sha256:6a1718cbe821a77c3338ae69810aee6dcbab2892fa0c818fa84de65ef8299c02` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.227@sha256:18bb39f8ed2c12a7bca12d2dff38c8aeaa753c8dabbe4789fe7fedb663c21286` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.227@sha256:18bb39f8ed2c12a7bca12d2dff38c8aeaa753c8dabbe4789fe7fedb663c21286` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.227@sha256:832abee41c9f95d45860c207287beb727d3307e7d5495dd31bacd57cad402f0e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.227@sha256:d2e25ebb85f1720eeefefe6065b28c79433b7dca13e4346b0a6981954c1538b0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.227@sha256:65fc79a8347bbc8570073e22cc788723d2e03ed3ace794e24bac15530af4efad` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.227@sha256:8972ceba3cf57fcdc94154f62d477f8bfcc1b3f3f5279b5715a49b3449fb80cc` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.227.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 1.0.0-develop.226

<!-- source-commit: 4101ce0bb566cb7db93d9f6290d7e92ef80d6a7f version: 1.0.0-develop.226 -->
Published 2026-11-20. Archive SHA-256 `48e81306d89ac7c8f37ca8ac22c0174476c797d0a7aec130e12ec938139f9fa7`.

- Change: staff-ui: read @openg2p/notification from the last commit that has it (#259)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@4101ce0bb566](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/4101ce0bb566cb7db93d9f6290d7e92ef80d6a7f)
- Changes since 0.0.0-develop.469: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/5e57e7a297186dea544f0fd0ce71ff5547acfd41...4101ce0bb566cb7db93d9f6290d7e92ef80d6a7f

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:1.0.0-develop.226@sha256:3ca9c650ab9d26c206beccf31cadbf341029218211eb043df16ece5c03b771e3` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:1.0.0-develop.226@sha256:5294ad990ed5a9c831397a8b86dbea1a24a72d0643aba033afea138dee3dee08` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.226@sha256:4ff1ce013ca93c62871944ce3fc596e0ee59984378c42e05ccb578fc166f61c8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:1.0.0-develop.226@sha256:4ff1ce013ca93c62871944ce3fc596e0ee59984378c42e05ccb578fc166f61c8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:1.0.0-develop.226@sha256:ca64869922ebf67c39b4e6d8e87c3d9c82f130ebc138820922d5cc874277764e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:1.0.0-develop.226@sha256:b672866b44da7b3487d58b1a0002fd5412ad39f3b829695dbc2477c332315022` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:1.0.0-develop.226@sha256:1162e75ead5e71ee29059820443db14343516461a80bb6eac0f8387c663925ab` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/dashboard-api:1.0.0-develop.226@sha256:06c9be5c9b35e0ae9ada24bde2c61df25be98ffb660b5a4438805aae62f7e4cf` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-1.0.0-develop.226.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.469

<!-- source-commit: 5e57e7a297186dea544f0fd0ce71ff5547acfd41 version: 0.0.0-develop.469 -->
Published 2026-11-17. Archive SHA-256 `54eaa103a6cd07c2605fce57363e85ef6042c9ee9d2783b02d3210d5f93b9ec4`.

- Change: ODK: a vet's or AI technician's ID is never sent as their name (#254)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@5e57e7a29718](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/5e57e7a297186dea544f0fd0ce71ff5547acfd41)
- Changes since 0.0.0-develop.468: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/6c3a0bddbb99701ef143cf3e57fb3630e7b7146c...5e57e7a297186dea544f0fd0ce71ff5547acfd41

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.222@sha256:eaf7ca1ca7adaa3d918290f8b3a1aaa9c5635081db3335232bcf1f12477b7288` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.222@sha256:09e831201fdbee2dbd2172db53cf823b91aa9343b85d145661d41fc4220860b3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.222@sha256:51fd6ff3f6a5fd44daa084923ee0bd03936257db27201504bc54cbe0fbb3aba2` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.222@sha256:51fd6ff3f6a5fd44daa084923ee0bd03936257db27201504bc54cbe0fbb3aba2` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.222@sha256:7afcc2596e24e67308f8435f15f83e4658b2af19eca9db7481a32194ebbce25c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.222@sha256:14edaf32ff3357d15e10349f4fccbb514d5b577d4f6a42f9d9dbdf05157f4157` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.222@sha256:2895e96e5f49a1112681761693751628d02244c95f2439f5b62d8400697a49c0` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.222@sha256:476897aa65b269e07cc82179ea78be4d45ddc37ee7cbfa14a481563c485ae453` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.469.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.468

<!-- source-commit: 6c3a0bddbb99701ef143cf3e57fb3630e7b7146c version: 0.0.0-develop.468 -->
Published 2026-11-17. Archive SHA-256 `9bdedb01855268d1827f3aa324890a475b0bfdeee089d02715b5b8c3f79700a6`.

- Change: Postman: check generated answers against Master Data choice lists (#255)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@6c3a0bddbb99](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/6c3a0bddbb99701ef143cf3e57fb3630e7b7146c)
- Changes since 0.0.0-develop.466: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/978a84b5cca01e569b2ba51e2a0c420b8febcd67...6c3a0bddbb99701ef143cf3e57fb3630e7b7146c

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.221@sha256:c1405f19a2b7710acaa4047808e2e7cbc1d1cf645d525500e85f02301ba39a1f` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.221@sha256:d726fcfb6650a0cd59a8dc06bda124d2ee17fa978932b7393a8f52987fbf5498` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.221@sha256:454432caa470b5d2549166185e09bfc4e0fc0b525c752b71cb7d2cb06d4957e0` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.221@sha256:454432caa470b5d2549166185e09bfc4e0fc0b525c752b71cb7d2cb06d4957e0` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.221@sha256:e9800199ced8a3b52e8a987683551d7cc0db32ac9fe06cd9a769ecba53a0e576` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.221@sha256:a15d4ad75bd19a955efaf714e1a33b0900248fafe744528499d086b6581e1c17` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.221@sha256:637e408e45bf3e0118ee3d29f3560dfd166d53604621bc78cbf11533b8a1f857` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.221@sha256:37513c9cf9e96115b7f9d2f30a98a271b10b566bfdef3f9eae478a1dc281e22b` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.468.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.466

<!-- source-commit: 978a84b5cca01e569b2ba51e2a0c420b8febcd67 version: 0.0.0-develop.466 -->
Published 2026-11-16. Archive SHA-256 `51bfd51708b097c443f5b76bdcf79a8cb9b00c9b772355cd2eb74241c5cb651d`.

- Change: One Postman collection for the three registries, passing on New Dev (#253)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@978a84b5cca0](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/978a84b5cca01e569b2ba51e2a0c420b8febcd67)
- Changes since 0.0.0-develop.465: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/93d20e48ca35a78bc289a030a332646dab312ecd...978a84b5cca01e569b2ba51e2a0c420b8febcd67

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.220@sha256:ea158f2d7987d430de45f48d2b785f7a3c4e276842751be572cbbe931b40353e` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.220@sha256:bfe81433614daeed9a41cbe98cae22a8749742fac57dd088d3ae833c4ecef00c` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.220@sha256:66bb0a920bb470fb9782e27e22863ccb9eb702b49324e93d3ea2897894a297e8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.220@sha256:66bb0a920bb470fb9782e27e22863ccb9eb702b49324e93d3ea2897894a297e8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.220@sha256:2ab0cad0d426b5eb6174b47b53d137958187f313df393bf963e9e83c01d8a360` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.220@sha256:ab980951aaceb20079611cbc52be1ff241c3acb4cf8efcc85e4c548de4a2fb12` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.220@sha256:26bc72a5970a89751ad1c58230ac5df30ea5d2f6016eb57901e534899d74089f` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.220@sha256:130431c31c06f3965aa79232305a2077b775e035a0b6a119baf1cee315786a36` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.466.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.465

<!-- source-commit: 93d20e48ca35a78bc289a030a332646dab312ecd version: 0.0.0-develop.465 -->
Published 2026-11-16. Archive SHA-256 `197fb817caef4fa455208f5d64ebf7b2618ce97fa5934af61541495e5fc4f110`.

- Change: Pin the dev values at oan-helm 3ff2453 (farmer reference setting names) (#250)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@93d20e48ca35](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/93d20e48ca35a78bc289a030a332646dab312ecd)
- Changes since 0.0.0-develop.464: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/10298fdc8b3dc52e9921a776ce714809fafc9569...93d20e48ca35a78bc289a030a332646dab312ecd

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.219@sha256:c723c28343ab1de35ef5a5566586d86dc3990701f58f5944adb013f5a07e8594` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.219@sha256:5fc4333efc95e73ae9edc374a78158e7e53c5f7d652f5a3d9209e0583ceda1f3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.219@sha256:5b34943b9e1595e2426360d7e3d8d5fc138e6a26c47b3bd0f6525732a0bb469d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.219@sha256:5b34943b9e1595e2426360d7e3d8d5fc138e6a26c47b3bd0f6525732a0bb469d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.219@sha256:ed739c44ac709be6fae817ec5f12c85313be446f27c645dcff7c0f9db8bec8db` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.219@sha256:6d278ddb70eee82351e6b9ebef94f1ac835b73d7fd38f829bad77e2e50273501` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.219@sha256:3165a9fd596d2d882669b100a1442ff7a6f81648eb67930bb3b212c8494453b8` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.219@sha256:c67869f43cb18b21b166be12c1b6695fa3cc7a26ace4126971bcf948f227668e` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.465.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.464

<!-- source-commit: 10298fdc8b3dc52e9921a776ce714809fafc9569 version: 0.0.0-develop.464 -->
Published 2026-11-16. Archive SHA-256 `27c30c82f1763dce7834eff89de5ad3b2e1580f2cacb67ee7f829df7a538f126`.

- Change: Staging Livestock connector: pull with the refreshed livestock-registry-ecr-pull-secret (#248)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@10298fdc8b3d](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/10298fdc8b3dc52e9921a776ce714809fafc9569)
- Changes since 0.0.0-develop.463: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/07d9bbd40b25fb7ecf8b891afe2010d6a05365b1...10298fdc8b3dc52e9921a776ce714809fafc9569

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.218@sha256:42399a508fe931c61938549b42aac7262e7b63df7b9b6d090c74b6a5440c3db8` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.218@sha256:3057d1a0b1d7ccd1c9ce1ef1c55ad201deb88ee0e3806e49727d098a98b0df20` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.218@sha256:96f788b14db333456a6fd3f3676f0afe59a7434adf30aa345e663815ce370124` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.218@sha256:96f788b14db333456a6fd3f3676f0afe59a7434adf30aa345e663815ce370124` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.218@sha256:a773286fd3d27273508c9bb3bcd5207f3ba64f10c5dcdecd2969c00568360142` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.218@sha256:43ca3c898cbbd26fcb01a804b11d06eed9a3f8cf755093159b62514367348564` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.218@sha256:b975459d003a69fdf7c398d7c7957f50af263a32187e4dc7cc9b38aefd30e77b` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.218@sha256:162cc5eb8d4d871227f8c4b25d0f589ba7312ac6d2a3b2a869ae77b162473964` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.464.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.463

<!-- source-commit: 07d9bbd40b25fb7ecf8b891afe2010d6a05365b1 version: 0.0.0-develop.463 -->
Published 2026-11-16. Archive SHA-256 `41a575cf5fda78ed86c0a3914512c4e948eb26969137b8f407185c0a5ff6b965`.

- Change: Merge pull request #247 from simretyibeltal-commits/ci/eoan-image-names
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@07d9bbd40b25](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/07d9bbd40b25fb7ecf8b891afe2010d6a05365b1)
- Changes since 0.0.0-develop.461: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/e8bef753094f2502ea353d85fcca72677cc2c5f4...07d9bbd40b25fb7ecf8b891afe2010d6a05365b1

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-api-1.2.2-rc.614:0.0.0-develop.217@sha256:b536bfd91c1da30d5aba7dbd4791a1279d19e3f683dd73ee7bfd1d0a16856f76` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/partner-api-1.2.2-rc.614:0.0.0-develop.217@sha256:db891ce6f375e414042742b8d7846741bde917206d7d606e36a66b872e5db4fc` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.217@sha256:c56e7c248fcaf27f323976db7fbbaa783b466da422571cf8228a010a8e49e44f` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/celery-1.2.2-rc.614:0.0.0-develop.217@sha256:c56e7c248fcaf27f323976db7fbbaa783b466da422571cf8228a010a8e49e44f` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/db-seed-1.2.2-rc.614:0.0.0-develop.217@sha256:5f4bf3369fb57a5fb15127197de3c4aabc3af219c8911ef87719fc0e3f1f254b` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/staff-ui-1.2.2-rc.614:0.0.0-develop.217@sha256:37035e975c9f6f9dc74cbffa26ea5d9abd09277bbbfca9324df1a1e30a87ac1e` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/livestock-registry/sanity-tests-1.2.2-rc.614:0.0.0-develop.217@sha256:68e6f4116c17cf07d71b9216fb20369960a7fd1ac83f7d8b3a27557a1b9362fd` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0.0.0-develop.217@sha256:5263ff73bde7a41fcf760e489d90749febabd94db448eb23fb2016186973f19b` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.463.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.461

<!-- source-commit: e8bef753094f2502ea353d85fcca72677cc2c5f4 version: 0.0.0-develop.461 -->
Published 2026-11-12. Archive SHA-256 `6b7f349dddf49b6a587c63587e1529b27b811675f3b817b0b20c723f7c8660c2`.

- Change: ci(refactor): add password protection to disposable database probe connections (S2115) (#236)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@e8bef753094f](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/e8bef753094f2502ea353d85fcca72677cc2c5f4)
- Changes since 0.0.0-develop.458: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/61a63c3ab4866ec51154bc6b22f44f7ab6621454...e8bef753094f2502ea353d85fcca72677cc2c5f4

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:e8bef753094f@sha256:de4acf7bc749ac659a9b8e0acfd5cf9a502d32ad6d654bab6b2d7e8613c27bc9` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:e8bef753094f@sha256:d45cb7339ad6977487186876ccc31cff6693db502fd8e024532e6c82916481fb` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:e8bef753094f@sha256:81bccb61cf6e849affee2718c013f0f181e186837f17b0d994f443dafdaa50d8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:e8bef753094f@sha256:81bccb61cf6e849affee2718c013f0f181e186837f17b0d994f443dafdaa50d8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:e8bef753094f@sha256:bf321f99012df8a64fdea2f2088950fb72a98f326b62649bc42e05d9eecdada3` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:e8bef753094f@sha256:2b4bedd83b22a0a9c2347f8e68492ad3dad7f79bec7c1968092711f109c0518f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:e8bef753094f@sha256:1643a7c7214e6c7b14f33d7ee7fb68ee293a69fae9dc99b4a8c2444c5472f7f3` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:e8bef753094f@sha256:807875b08011f72a3b6881f6bc99f951ef6dd969697679862e4c2ee286f3794a` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.461.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.458

<!-- source-commit: 61a63c3ab4866ec51154bc6b22f44f7ab6621454 version: 0.0.0-develop.458 -->
Published 2026-11-12. Archive SHA-256 `c9c9ce8ef013aff51bfb3ff13c55b85e5ac426040ecadd38ac206c650de21f3c`.

- Change: Chart: the release keeps its own ECR pull secret, refreshed by a CronJob (#245)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@61a63c3ab486](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/61a63c3ab4866ec51154bc6b22f44f7ab6621454)
- Changes since 0.0.0-develop.457: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/0b74fcd3436fe3949c2b65ed174eb31b9b972233...61a63c3ab4866ec51154bc6b22f44f7ab6621454

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:61a63c3ab486@sha256:c7eaf74d5bc203075b965e4483c833b267feacefbc9cc5c73bc70e409c1479bb` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:61a63c3ab486@sha256:1aeb1e609f28b386a046a990a17e1cef5239f94a87d61cd54f1a9e23a6f7f7db` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:61a63c3ab486@sha256:9541bb93154edad10c057674ccce942fadf6600f47558cb10ee08c771ab72f8c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:61a63c3ab486@sha256:9541bb93154edad10c057674ccce942fadf6600f47558cb10ee08c771ab72f8c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:61a63c3ab486@sha256:ee7d6d9dba4535aae59d245476b3d99fd05285d31c575cc44c615388d0447738` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:61a63c3ab486@sha256:1efb8e77e47b8f58546531fb3b2f8413f222c3b4cc97fd430634d1245a9785d6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:61a63c3ab486@sha256:abd7307c7e3babd8c5055e4084567bc5b04bb046b26068158d60dd196fa42e30` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:61a63c3ab486@sha256:be4a72eacbd3d02218dd496bc3081ce852058aa24b27906db1c6642f5999ce50` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.458.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.457

<!-- source-commit: 0b74fcd3436fe3949c2b65ed174eb31b9b972233 version: 0.0.0-develop.457 -->
Published 2026-11-12. Archive SHA-256 `7be2afa0f001dbd9d91f599c0118f4d9ea5f462332c0ce858a1a429503571747`.

- Change: Staging Livestock: connector on the staging Gateway; pipeline delivers the dashboard UI (#243)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@0b74fcd3436f](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/0b74fcd3436fe3949c2b65ed174eb31b9b972233)
- Changes since 0.0.0-develop.456: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/abc345bfc6ff010eb0fc55a329ed5bc685aae008...0b74fcd3436fe3949c2b65ed174eb31b9b972233

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:0b74fcd3436f@sha256:8f294796442415896af56248a944f6add98a67f1f4b5aa9c2607090a9be0b187` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:0b74fcd3436f@sha256:9963d6383f6d95ae4179cfea54c833e508744b0294382db40127b934828bac83` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:0b74fcd3436f@sha256:ebad9b91247aab303790a884873039582af5beb9c67d3bccf7365aafea079234` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:0b74fcd3436f@sha256:ebad9b91247aab303790a884873039582af5beb9c67d3bccf7365aafea079234` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:0b74fcd3436f@sha256:662c753c81ce2761287b730824a589842887719e3f269403a37749ab917f6153` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:0b74fcd3436f@sha256:132cb1c44abd71da1de5e5474df805ef291b3753f7ec9ff148322f0e91b3303e` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:0b74fcd3436f@sha256:0776894c02167975c5e5a77939629c1bc4d2af73e013413a6272a9d85a09d44e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:0b74fcd3436f@sha256:892df8bd31ebdd41858843304055c8823fc92918fe28af85daa545b3715c9bb2` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.457.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.456

<!-- source-commit: abc345bfc6ff010eb0fc55a329ed5bc685aae008 version: 0.0.0-develop.456 -->
Published 2026-11-12. Archive SHA-256 `ee35f79bbef965a9c628f1862f03876af4ca852dbf45c2bb15b12d92f36e9d19`.

- Change: New Dev: let livestock-ci read the connector client secret for the connector upgrade check (#242)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@abc345bfc6ff](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/abc345bfc6ff010eb0fc55a329ed5bc685aae008)
- Changes since 0.0.0-develop.455: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/602aed8dd912068fb3ebf08288a948abcfaaaf8b...abc345bfc6ff010eb0fc55a329ed5bc685aae008

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:abc345bfc6ff@sha256:d344064d8dc51fdff4ef8a1a1777916553aac25efb017ffd32662da28bb3c471` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:abc345bfc6ff@sha256:be9ca380038473dc9e04627bea68f7ebad8b95aafb71b5190fe0beefdeeaa4d8` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:abc345bfc6ff@sha256:8c03c392968840ba349d407ab30e970be4585214c41db8e8a1c606ee55c43b55` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:abc345bfc6ff@sha256:8c03c392968840ba349d407ab30e970be4585214c41db8e8a1c606ee55c43b55` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:abc345bfc6ff@sha256:fdea0df5de0007d534d4d1e1b5793e807e91c08b272b2b7bc8171b89e1379539` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:abc345bfc6ff@sha256:04dcd5a33aeab5f1ae239faeb1d174842a41e7df6762b3733e455294a0881e7f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:abc345bfc6ff@sha256:5b4011307e0eaa91d2b2d3938527c896271634d2ad515611152909aa61787f41` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:abc345bfc6ff@sha256:c63d58fc930e4ee1c653889edf797747bd66f3a1ec3a1c117bb533c130cd5a16` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.456.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.455

<!-- source-commit: 602aed8dd912068fb3ebf08288a948abcfaaaf8b version: 0.0.0-develop.455 -->
Published 2026-11-12. Archive SHA-256 `057e6cd148b7a7cae0f8eb68dbe2b768c1eeb2599e1baa21e757deff3ac2ec01`.

- Change: Staging connector: name the build by the promoted chart's commit (#239)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@602aed8dd912](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/602aed8dd912068fb3ebf08288a948abcfaaaf8b)
- Changes since 0.0.0-develop.454: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f...602aed8dd912068fb3ebf08288a948abcfaaaf8b

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:602aed8dd912@sha256:8f7f1473505939b043361c650de9b17d623302ec580adae77a8da3a48b3f8ce6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:602aed8dd912@sha256:5cc06dd5fbe39ba08b3c7cc181e4eece8acd0306b7c77f890ba01bcf24a219b6` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:602aed8dd912@sha256:29df3c5cdfb19e6347a50e544cf91dbf77bbb2efcb8f17ea408fad0e0cfb074c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:602aed8dd912@sha256:29df3c5cdfb19e6347a50e544cf91dbf77bbb2efcb8f17ea408fad0e0cfb074c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:602aed8dd912@sha256:fd815b41bc68d4feba34a05916f4f0ddc7ba976e9e69b916c592bfeb4f25002d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:602aed8dd912@sha256:caa79694f169db384620324f31cbb04a1370de3deb5047e09e043d266e1b1663` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:602aed8dd912@sha256:528c2fdf369bb32c5fa98b973d2180470a63314065f64e69d80674cfddd9c326` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:602aed8dd912@sha256:db71e0579ce05954f6582b575eb191acbeab8ce036337ee230dbddca4ddd40dc` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.455.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.454

<!-- source-commit: b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f version: 0.0.0-develop.454 -->
Published 2026-11-12. Archive SHA-256 `a6668dd53c8b14e287c117b112b81e34e7733d728cb0c435ab2385c056c3fdad`.

- Change: Give the sample approvers their declared password after every deploy (#237)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b275e4c48b1f](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f)
- Changes since 0.0.0-develop.453: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc...b275e4c48b1f7b5b1b0b5ebcb67c03bb734e391f

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b275e4c48b1f@sha256:5ba4bd8a5fe679e454b589a64dc6062ce033042a20352da0f1b32bea1339b65c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b275e4c48b1f@sha256:f0284b69101022a182ff5ebe95973e411be65f5568cadf0f0cefc223b612ab1e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b275e4c48b1f@sha256:9ee921d0017225a9e606653eeeb3d1755e3dfbed57c04d236434145479732d90` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b275e4c48b1f@sha256:9ee921d0017225a9e606653eeeb3d1755e3dfbed57c04d236434145479732d90` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b275e4c48b1f@sha256:456ce23705ad6acd7cbec368a0c23c8a62eeaee69e36df1975eeef84794aad54` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b275e4c48b1f@sha256:8ef3aa47038381bb5fbcbc546136244ee60d85f6e58bd431b4613d1724460d3f` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b275e4c48b1f@sha256:83d8a357a95e166822188711fc599705b6056f06a0fc8e3908f960e40c15683e` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b275e4c48b1f@sha256:8b9ccca84c65720e713ee2ac403c569c5fc72db31244dda5f11b5dd5a115417d` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.454.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.453

<!-- source-commit: b053d120c8e02c59a7db0b57ca66d52d67d3e6bc version: 0.0.0-develop.453 -->
Published 2026-11-12. Archive SHA-256 `523ede90ec9ed6807ce3e8e8c902ef4ea46dd071a1e6021b3dd36ac6945e3bf8`.

- Change: Staging connector moves to the qa.oanstaging.com scope (#234)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b053d120c8e0](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b053d120c8e02c59a7db0b57ca66d52d67d3e6bc)
- Changes since 0.0.0-develop.452: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/798ea765f01be019ced8737c33eb11f7254e4642...b053d120c8e02c59a7db0b57ca66d52d67d3e6bc

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b053d120c8e0@sha256:db862c5249f77ba0a8ebbd7acb81036fc797b62520cbc9a50dd86b41ded5e9a5` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b053d120c8e0@sha256:491c55b1f9bfc35e840734f20a2a18b715d86b852a5d29d215d6a7f9f26edb4d` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b053d120c8e0@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b053d120c8e0@sha256:fa8eb00299d7279a554ce418e01e3dfcde47e844df0d1dcdec8d0c36d0483b43` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b053d120c8e0@sha256:29fdf78e002ccf469aaa232bffb30821d1edb4965aa4c8b84162c35fd32b9f72` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b053d120c8e0@sha256:234cb128c8c06f7e3b72e66121b3bf314bbe973cdd14e860168cdac319f720e3` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b053d120c8e0@sha256:90cc503964e2c8f087ef7f3f651750a274832557478874e518c6ae46ef6d1574` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b053d120c8e0@sha256:815a6b14439e57e74c552470390dd793fe1050a565d15e8e37871bca8865f369` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.453.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.452

<!-- source-commit: 798ea765f01be019ced8737c33eb11f7254e4642 version: 0.0.0-develop.452 -->
Published 2026-11-11. Archive SHA-256 `690aefc39459e65f7b895d5a7203cc7d82aab9fe285bf5b0dbe55cfc671b1135`.

- Change: AWE callback registration follows the registry's HMAC Secret (#233)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@798ea765f01b](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/798ea765f01be019ced8737c33eb11f7254e4642)
- Changes since 0.0.0-develop.451: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/2eeb5e826da13a61179c6bcdd5499bc54cf1e275...798ea765f01be019ced8737c33eb11f7254e4642

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:798ea765f01b@sha256:a707980d756d167397e3c871518d48baae2dae50353acf376ef47a7e3dfd6532` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:798ea765f01b@sha256:97ad86249c40699117187531766c2b42df7775226d0bb46d84897a8ba3c023fd` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:798ea765f01b@sha256:ff8da996a62b4dc8fbf1e832ca4dba0564117a918e8000493a6c15bc09fb1f3e` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:798ea765f01b@sha256:ff8da996a62b4dc8fbf1e832ca4dba0564117a918e8000493a6c15bc09fb1f3e` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:798ea765f01b@sha256:27dcd1270c9770389b5079639fc9bc4789849b9ce2dcee7648c0275282e3dcdf` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:798ea765f01b@sha256:25e0d1241ff68498713faae3a96e04d305bbe7b7754fac80f73ee3329c65bf5d` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:798ea765f01b@sha256:e433970fa45868454e74c17353d447e61eb346bac1f4a688675289158c132983` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:798ea765f01b@sha256:17b6b255e656bcc5b852bcecfea8e295be9c789c991b3e8d3eab5619d496ecbc` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.452.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.451

<!-- source-commit: 2eeb5e826da13a61179c6bcdd5499bc54cf1e275 version: 0.0.0-develop.451 -->
Published 2026-11-10. Archive SHA-256 `243d9e5a01812efaf4efc7d84041aa90dcacd8feac9071e79e5943a7da23e220`.

- Change: CI: on-demand agents: ECR layer cache, retry on agent loss, real Postgres readiness (#229)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@2eeb5e826da1](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/2eeb5e826da13a61179c6bcdd5499bc54cf1e275)
- Changes since 0.0.0-develop.450: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/c81f3f78b6c7102d20c4016edb4b919c1dc04cd3...2eeb5e826da13a61179c6bcdd5499bc54cf1e275

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:2eeb5e826da1@sha256:c42d5144faf5690ae7ee3b580a1a71e0bb496fad18ff3972bc4d064a84f3a820` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:2eeb5e826da1@sha256:d6755f06a57699a773f2043d77c1b79eec2350c9d4acf5ccf93d4f1f0c74717e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:2eeb5e826da1@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:2eeb5e826da1@sha256:f81455935ac1c5ec6c9d538ef9d5dc58aee21794f0d7fd66d7fca49938fc3cf8` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:2eeb5e826da1@sha256:ba79b19ce8e4121e7444a68e39ebd679312c77162a3b563472b35572ff0708b4` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:2eeb5e826da1@sha256:e748260b9eb06a14fccfdc603adae4da0e68f443c0b3fece1b0d52c884818fe0` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:2eeb5e826da1@sha256:320daba33532080bb86ee7d103729bad9b4d289d4b8ff86d5f56e90e72b02358` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:2eeb5e826da1@sha256:50ea6bed9690fbc11ab8886b293e692d8123568e5638c34d678cd74b2b18620c` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.451.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.450

<!-- source-commit: c81f3f78b6c7102d20c4016edb4b919c1dc04cd3 version: 0.0.0-develop.450 -->
Published 2026-11-10. Archive SHA-256 `ca32fc106b231010f5b9c3680466f1e9e4229c1b7e05b8fe0892f22bbb2b3308`.

- Change: Give the disposable test database room and wait for real queries before each test module (#231)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@c81f3f78b6c7](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/c81f3f78b6c7102d20c4016edb4b919c1dc04cd3)
- Changes since 0.0.0-develop.449: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/4fd3dd7ce387d3a2d29eec06390f34f028791f7e...c81f3f78b6c7102d20c4016edb4b919c1dc04cd3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:c81f3f78b6c7@sha256:830aea1140257d00802e9c43c32882987cb73c38fdce94554c8196c7e2767901` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:c81f3f78b6c7@sha256:3844fa5ae0013ce1e06eb297e7c1851f4e13da3e48cb8a9854e3b35cbbc2adb3` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:c81f3f78b6c7@sha256:11ce5c7e23d5750b0045d0f25d4f530138368b4bc5ef8bc7bf2eeb1eaedab352` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:c81f3f78b6c7@sha256:11ce5c7e23d5750b0045d0f25d4f530138368b4bc5ef8bc7bf2eeb1eaedab352` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:c81f3f78b6c7@sha256:248291df719defe3cc4a643ffc6e5b659050d5818583ff08c9954bb3ff311ab2` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:c81f3f78b6c7@sha256:065aa5c4a7b2b2a02fd62e66f4cad16ee36e5cbff1c6533a30bd07c3be0c70a9` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:c81f3f78b6c7@sha256:cf59b788075f2a92dc89c70a86233298045a1b435a07f7a68dce3b788144ac95` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:c81f3f78b6c7@sha256:22326a3512d20154eb47a02d97ca9c25d1902e3f1255e259d47d3793e1330ffe` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.450.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.449

<!-- source-commit: 4fd3dd7ce387d3a2d29eec06390f34f028791f7e version: 0.0.0-develop.449 -->
Published 2026-11-10. Archive SHA-256 `c08c34e9af931d524a714297b5d2b5c601056be8b520c73a2f246520f329f840`.

- Change: Subscribe the staging livestock connector to Farmer profile changes (#230)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@4fd3dd7ce387](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/4fd3dd7ce387d3a2d29eec06390f34f028791f7e)
- Changes since 0.0.0-develop.448: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874...4fd3dd7ce387d3a2d29eec06390f34f028791f7e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:4fd3dd7ce387@sha256:83a9494879e02afff85cf550d7579296802c15686527cbd0a04f73e28441c827` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:4fd3dd7ce387@sha256:a912a478268e540a9e098632a43f7579f7e29841954250701fb816f5662aa698` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:4fd3dd7ce387@sha256:862083b546a05dc4478c24452d6245fcccf3154648b508eba52540fa2a2eaf70` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:4fd3dd7ce387@sha256:862083b546a05dc4478c24452d6245fcccf3154648b508eba52540fa2a2eaf70` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:4fd3dd7ce387@sha256:aeff067084fa8911d5bee62ca89c3f5bf6bfd63b574343ab671d4287018a98b4` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:4fd3dd7ce387@sha256:3c75e6ed91376851ebb8ac4882fa88b5b771b1b08c1d915448fb83664dbdc98c` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:4fd3dd7ce387@sha256:3839c9f6b5545b81a905b6d9b4dda4a96a6e374c29c90a941fbc9fb3abb08d53` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:4fd3dd7ce387@sha256:ca37af05225f9f65d564ee757f706bdbf98347319a46eb62466a2da1f3ec7a22` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.449.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.448

<!-- source-commit: 7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874 version: 0.0.0-develop.448 -->
Published 2026-11-10. Archive SHA-256 `a930418739239acf1aa2e39dee559df14d131f366581b444dd8c70c8b9c20dbc`.

- Change: Staging connector: drop the admin-auth keys that commonEnv never renders (#228)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@7e2729a7bf4e](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874)
- Changes since 0.0.0-develop.446: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/1c74138c15aaa4ba425cbb1a731295736797cd20...7e2729a7bf4ea6bcdb88ec1b2eba21b89a643874

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:7e2729a7bf4e@sha256:455117b1b45c3ec0128c43861bc334edbe1a934ba23d92e318ef9dd080937c95` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:7e2729a7bf4e@sha256:13fa05335272509992e4bf31ced7b82ee0a887e972771f61ed59c5d63789ab0e` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:7e2729a7bf4e@sha256:ce4eae36fbd6ec67998fcb55df539db9df110614e8390f3b2f8b872ab875d940` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:7e2729a7bf4e@sha256:ce4eae36fbd6ec67998fcb55df539db9df110614e8390f3b2f8b872ab875d940` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:7e2729a7bf4e@sha256:136cce484d14d940f83eaf4cf75065bdabc562b090fbd15daa7750790f5aee1a` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:7e2729a7bf4e@sha256:41c444c85580ce863661b96fe6daacca59d81dca3c2566b448a10ec7846092fa` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:7e2729a7bf4e@sha256:0d7deb2697d2c1b9230d089489b99f8c496a07a522382c6432b380a0f5eb7534` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:7e2729a7bf4e@sha256:eaa6894b3557ccf6e4776f8d29b4b8879406890a0051711cfb427393aba2fc4c` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.448.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.446

<!-- source-commit: 1c74138c15aaa4ba425cbb1a731295736797cd20 version: 0.0.0-develop.446 -->
Published 2026-11-10. Archive SHA-256 `d21650d44e58d4174fcbd3c4ab7130f4f1f3db3c572b1a38df0d7165fa43aa44`.

- Change: Staging connector: expect the staging Keycloak issuer (#224)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@1c74138c15aa](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/1c74138c15aaa4ba425cbb1a731295736797cd20)
- Changes since 0.0.0-develop.444: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/684febd3b7730edba1a62a200970f91069cf770e...1c74138c15aaa4ba425cbb1a731295736797cd20

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:1c74138c15aa@sha256:244de208699f7d1583310e24159281b9f61e68b349bbc11359b28ea7f410d5d6` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:1c74138c15aa@sha256:90724a2134898fd9b6aab30434a71dc2065ea454a289df176155fd13ce4b08c0` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1c74138c15aa@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:1c74138c15aa@sha256:bd65af5e3d3b4b732a7f634e27efa608343ce1af1cf04eb21851cfbebb428fd3` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:1c74138c15aa@sha256:6777b92d8a6750a8385cb04b57c0e4786bd506261b7e70e03241019377824194` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:1c74138c15aa@sha256:0ff40275d527a8bd3c3c9f1dd02655e0de9c2d7b8e91cdc9a8487837cfb600fb` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:1c74138c15aa@sha256:b64a9e31dbd07cba822f4b4d5abe70a181b578a846f91a6047e9bd9e4716e5dc` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:1c74138c15aa@sha256:cd9510b560d92644563edc2bb690acbbb1b904dcc91e62dd881c1fc3c806101b` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.446.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.444

<!-- source-commit: 684febd3b7730edba1a62a200970f91069cf770e version: 0.0.0-develop.444 -->
Published 2026-11-10. Archive SHA-256 `5e8b23fa725b79110e3e060d42479b5e54ce27ad364b3d74f55c9945d23491c0`.

- Change: Add a load sample data option to the staging build (#222)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@684febd3b773](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/684febd3b7730edba1a62a200970f91069cf770e)
- Changes since 0.0.0-develop.443: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/b6656cdfba74e284013b774d652daf626ad617f3...684febd3b7730edba1a62a200970f91069cf770e

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:684febd3b773@sha256:8588a8673dc17667d4abde75ef25f03466e4a3c7dd656fe87b0b7aeeb0640a6b` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:684febd3b773@sha256:343327f45b0b6826847b8a723e57a252188656dbf098ca55a6829eeb52b02593` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:684febd3b773@sha256:96cf8f68236e6270dd3117ae5dc0ef27e04f978c1484ad521c86d521cdced4e1` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:684febd3b773@sha256:96cf8f68236e6270dd3117ae5dc0ef27e04f978c1484ad521c86d521cdced4e1` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:684febd3b773@sha256:2c32c27f17093d5b500069f0fde56d711a8cf895f7ebe941fa052ae13a03f209` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:684febd3b773@sha256:f80c1d98d313c2abb4d401410999fd1acead6e49a978f01843b9bbf243302ba4` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:684febd3b773@sha256:097da9d8ccc1336f6520484594cd711655a93bc3a482658edce989a5f4c89289` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:684febd3b773@sha256:87775242328412aad13ff80ee6ba1d996d5b66e2388f9e835b354faba352b45d` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.444.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.443

<!-- source-commit: b6656cdfba74e284013b774d652daf626ad617f3 version: 0.0.0-develop.443 -->
Published 2026-11-10. Archive SHA-256 `f056be27cd308247496ce612997434ac8b58b9059107a01202705e195c17a9b2`.

- Change: New Dev: point the ODK connectors at odk-central.development.oanstaging.com (#213)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@b6656cdfba74](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/b6656cdfba74e284013b774d652daf626ad617f3)
- Changes since 0.0.0-develop.441: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/418c8fab326cee99d08aaf59a914c6afb8ecf7a9...b6656cdfba74e284013b774d652daf626ad617f3

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:b6656cdfba74@sha256:e6726465d2941204f1a696944043fca0843d1ec3d3fcb97222f369adae0ee630` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:b6656cdfba74@sha256:26c5fd89e500752631b758f303e7d2e8459d0fea682cbc93fd4704af72016fea` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b6656cdfba74@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:b6656cdfba74@sha256:128c360c0fe59607a8a30315e57102ec313d06badc9fe540fcfdca9d52ad7dbc` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:b6656cdfba74@sha256:fd8837e565ebc8293dea3000847177016e3aef2d8e49df5f3830b452735de307` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:b6656cdfba74@sha256:0e3313ef4acd39f150b3cfdef1d02e09dbb57d8b28a8882b3c910d337108c6ba` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:b6656cdfba74@sha256:77564efdad743018f2683f08c935d92efae0cb7f5e889974e634df769706282a` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:b6656cdfba74@sha256:d0e0566f045079106cacebb8464d03e717974923c361daac1fea9fd1db1ab5f9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.443.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.441

<!-- source-commit: 418c8fab326cee99d08aaf59a914c6afb8ecf7a9 version: 0.0.0-develop.441 -->
Published 2026-11-09. Archive SHA-256 `dac25151b0beb31b0861a400aafe870071e6fc5a8b00a854983d7cb96fd8ffb3`.

- Change: Merge pull request #218 from simretyibeltal-commits/revert-app-publish-v2
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@418c8fab326c](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/418c8fab326cee99d08aaf59a914c6afb8ecf7a9)
- Changes since 0.0.0-develop.435: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/cd63c4c20c6302d2f4696e58cae97f958ce0cec6...418c8fab326cee99d08aaf59a914c6afb8ecf7a9

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:418c8fab326c@sha256:d1cc9759f3835d073270cb32e3a1dfa4686f4aa02374f8af96928b3cffca26f1` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:418c8fab326c@sha256:aea7c59bd4393613bca3291f57f89d9953dd08bdc996c3ef756bc3db280158a7` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:418c8fab326c@sha256:43a774ce42ecf7e5be28535e1cabe62182d90829351a3bde69679503d9681ae9` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:418c8fab326c@sha256:43a774ce42ecf7e5be28535e1cabe62182d90829351a3bde69679503d9681ae9` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:418c8fab326c@sha256:3431f13a6ab0b185465a7f20e1ace6b17accdebe53b87f7223a0400a1f17d29e` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:418c8fab326c@sha256:ddb012e2efbed59200b55a07b5059fc8a9f04b9bab46985371a23fdf3ab00f16` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:418c8fab326c@sha256:33a01eab2e215ae8975b14494956e9700aa92abbaaf6418ad71ccdfd49f818af` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:418c8fab326c@sha256:88183b6ca403f1d46800cfed1ce524a3880ea92bc551c9866e03fcf8de9ced04` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.441.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.435

<!-- source-commit: cd63c4c20c6302d2f4696e58cae97f958ce0cec6 version: 0.0.0-develop.435 -->
Published 2026-11-08. Archive SHA-256 `27cf2432150601e5fc37fdfa4de8d0445276513ee1e9d7c9867c81837e04a2e7`.

- Change: Seed renames the Farmer-reference tables before it writes the archive (#210)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@cd63c4c20c63](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/cd63c4c20c6302d2f4696e58cae97f958ce0cec6)
- Changes since 0.0.0-develop.433: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/455e6ec2eac4e5e12a5719df558efb3a6d40b989...cd63c4c20c6302d2f4696e58cae97f958ce0cec6

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:cd63c4c20c63@sha256:4f690993e85241f81289acaa96f6c2f0c2cebcdd1bf61c4f9d25640c8b44c02c` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:cd63c4c20c63@sha256:6a181e723f8cab172d0e12112370936d925f63ab70ac35c99b4edb0a278f8582` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cd63c4c20c63@sha256:054b7f32064b1cea9483c8ece0b06d69f6aa749ac2f907660fd7120e2c3b174d` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cd63c4c20c63@sha256:054b7f32064b1cea9483c8ece0b06d69f6aa749ac2f907660fd7120e2c3b174d` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:cd63c4c20c63@sha256:06a6a3cbbda0fa1c62ca55789596d077ab3c3ec7be2adf9b8b37881f72bfd56c` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:cd63c4c20c63@sha256:743ef4dd7ef0beb4e54f67bb0d71877673f841e110b7daa93ab498479188dea6` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:cd63c4c20c63@sha256:65d97767e053614f871eed9fd770d8d59e04c3893cca44a34c835e1160f068c9` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:cd63c4c20c63@sha256:b5c22bcd5e2caf546a67a098a96712f716b95d4a21d6a69fc31215f96e211da6` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.435.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.433

<!-- source-commit: 455e6ec2eac4e5e12a5719df558efb3a6d40b989 version: 0.0.0-develop.433 -->
Published 2026-11-08. Archive SHA-256 `b8eec5f698bd8d46c566309682b1cd655985854cb3647ce12896fbd62b1eac6d`.

- Change: Replace the stale parameter test with a check that the pipeline takes no parameters (#211)
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@455e6ec2eac4](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/455e6ec2eac4e5e12a5719df558efb3a6d40b989)
- Changes since 0.0.0-develop.426: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/cc5b130f5aeab6e98d56e80cab9217ee68088f07...455e6ec2eac4e5e12a5719df558efb3a6d40b989

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:455e6ec2eac4@sha256:fa5204d32d9f150b2a0427c1ffb6ae30b4382caf19359819027f302e04dd7a47` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:455e6ec2eac4@sha256:c3ef43b3ccbe4a39add9792257cce2f51cc7e82c70bba580c147d755a714b02f` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:455e6ec2eac4@sha256:3e417f0273beceea584f9fde6c0c45eb61d8b2d47dd84b58fe5f3a8c734bc24c` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:455e6ec2eac4@sha256:3e417f0273beceea584f9fde6c0c45eb61d8b2d47dd84b58fe5f3a8c734bc24c` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:455e6ec2eac4@sha256:0e29d432b49170be9aad7e7349e0d897da66882b3e5be2432e03a332c6b22166` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:455e6ec2eac4@sha256:9a579758a5eb3905a70c8953ec74ac8a83ab4dc8f33c15c4a649f5666a6f59fc` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:455e6ec2eac4@sha256:909bcd34cc1e7865d9d07de3f2c974a14a59883aae70279501b263a7cfeb5653` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:455e6ec2eac4@sha256:6d6bd625cc17e2f1ad087828d0a64eb9cce1d51ebf0bfce78219c06e895a1254` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.433.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

## 0.0.0-develop.426

<!-- source-commit: cc5b130f5aeab6e98d56e80cab9217ee68088f07 version: 0.0.0-develop.426 -->
Published 2026-11-05. Archive SHA-256 `efb8a761dd304fbc7108ede269cff6c1a5866d020c910ebae37c358fcb892265`.

- Change: Merge pull request #199 from asmitonweb/promote-staging-without-rebuilding
- Source: [Centre-for-Open-Societal-Systems/livestock-registry@cc5b130f5aea](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/commit/cc5b130f5aeab6e98d56e80cab9217ee68088f07)
- Changes since 0.0.0-develop.424: https://github.com/Centre-for-Open-Societal-Systems/livestock-registry/compare/e5082c54e7ab7404902c324d9ee86ae920a166d2...cc5b130f5aeab6e98d56e80cab9217ee68088f07

| Values path | Image |
| --- | --- |
| `registry.staffApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-api:cc5b130f5aea@sha256:5c6c14ea7011cca09cace8f34d441dc5c1e1592a9fa8a1f3e6d504a71d58f123` |
| `registry.partnerApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/partner-api:cc5b130f5aea@sha256:7678c266d04b4a5d8f368af6a22067fe9281be11d8faae027066886b7151e555` |
| `registry.celeryWorker.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cc5b130f5aea@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.celeryBeat.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/celery:cc5b130f5aea@sha256:a3378894d49cb3267ef0364a25452428c6779f5a0793e0b55a87ff3907be3fba` |
| `registry.dbSeed.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/db-seed:cc5b130f5aea@sha256:8e2b12e2fcacb8de4b830fe8979630798218f8759daf92ad0e0382ec3460622d` |
| `registry.staffUi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/staff-ui:cc5b130f5aea@sha256:9e1a17531f33ae7b23312770c542e2073688324867860a61a0f72512efd24e8b` |
| `registry.sanity.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/sanity-tests:cc5b130f5aea@sha256:c23f11a12c2e8b7d12edd2581cbfb927acd5174a99b80ee5e770cae88085a336` |
| `dashboardApi.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/openg2p/livestock-registry/dashboard-api:cc5b130f5aea@sha256:0e6a34e3413b317261a74f5dc878fec4573b173f435890ab957d170fc2a6120e@sha256:f105a023e2cf38149ae194eefae91d9d9a9d8ab8c6839a5b8d8c3a2d40958ce9` |

Return to this version:

```sh
helm upgrade livestock-registry https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/openg2p-livestock-registry-0.0.0-develop.426.tgz -n livestock --reset-values -f environments/dev/values/livestock.yaml --wait --timeout 15m
```

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

