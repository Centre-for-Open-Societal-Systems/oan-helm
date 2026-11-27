# oan-grievance-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.125

<!-- source-commit: 05fc0c373c99e863845f602af2f27a5c217a3c3a version: 0.0.1-develop.125 -->
Published 2026-11-27. Archive SHA-256 `8856f77f3cffdc8e07b85f82c9589e134b70a6f8860481dee52f75e9d9ae32ed`.

- Change: Merge pull request #163 from dhruvbhatt701/feature/STG-518-guest-link-pin-access
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@05fc0c373c99](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/05fc0c373c99e863845f602af2f27a5c217a3c3a)
- Changes since 0.0.1-develop.124: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/1810153fedf82b6945cbee93400faa31dacc13b7...05fc0c373c99e863845f602af2f27a5c217a3c3a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.125` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.125.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.124

<!-- source-commit: 1810153fedf82b6945cbee93400faa31dacc13b7 version: 0.0.1-develop.124 -->
Published 2026-11-26. Archive SHA-256 `281f34cc6d3912ed5d27bf1342262370c926a321a3a1907a91b49979e5136658`.

- Change: Merge pull request #162 from dhruvbhatt701/STG-521-reopen-escalation-assign-senior-officer
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@1810153fedf8](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/1810153fedf82b6945cbee93400faa31dacc13b7)
- Changes since 0.0.1-develop.123: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/08c341978b516b4ed01d40feb622d6371859a855...1810153fedf82b6945cbee93400faa31dacc13b7

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.124` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.124.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.123

<!-- source-commit: 08c341978b516b4ed01d40feb622d6371859a855 version: 0.0.1-develop.123 -->
Published 2026-11-26. Archive SHA-256 `a74e4cc4128d312b1e8b230ee9a8c9d186862c71eb879c1fd8bb0572eb2e7207`.

- Change: Merge pull request #161 from arnavam/chore/iam-application-grievance-service
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@08c341978b51](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/08c341978b516b4ed01d40feb622d6371859a855)
- Changes since 0.0.1-develop.122: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/4a4997c704468f60bf32102512743a430eabe3ae...08c341978b516b4ed01d40feb622d6371859a855

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.123` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.123.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.122

<!-- source-commit: 4a4997c704468f60bf32102512743a430eabe3ae version: 0.0.1-develop.122 -->
Published 2026-11-26. Archive SHA-256 `3a48b7153fbf8d066cfb5eff897f69193147bfe54874be696b17adc474f4af4c`.

- Change: Merge pull request #160 from arnavam/chore/helm-install-oan-messaging-connector
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@4a4997c70446](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/4a4997c704468f60bf32102512743a430eabe3ae)
- Changes since 0.0.1-develop.121: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/634cebba7dcb20e2452330182cd42dd8c736c1bb...4a4997c704468f60bf32102512743a430eabe3ae

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.122` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.122.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.121

<!-- source-commit: 634cebba7dcb20e2452330182cd42dd8c736c1bb version: 0.0.1-develop.121 -->
Published 2026-11-26. Archive SHA-256 `68eb34bde856e323434f648b68438e3a10262ccfe04d486fb840a98062a27bd3`.

- Change: Merge pull request #159 from arnavam/fix/expose-external-area-code
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@634cebba7dcb](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/634cebba7dcb20e2452330182cd42dd8c736c1bb)
- Changes since 0.0.1-develop.120: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/87d14cd768a7fedf421799ea53b1506d4021a4f5...634cebba7dcb20e2452330182cd42dd8c736c1bb

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.121` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.121.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.120

<!-- source-commit: 87d14cd768a7fedf421799ea53b1506d4021a4f5 version: 0.0.1-develop.120 -->
Published 2026-11-26. Archive SHA-256 `449b1989114ae4783428be8de96b8cdfabd2a2094d8e5a795144f4f92a813c94`.

- Change: Merge pull request #158 from arnavam/oan-messaging
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@87d14cd768a7](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/87d14cd768a7fedf421799ea53b1506d4021a4f5)
- Changes since 0.0.1-develop.119: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/028ee11d5945417ebccbb9341a05e19b13675c82...87d14cd768a7fedf421799ea53b1506d4021a4f5

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.120` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.120.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.119

<!-- source-commit: 028ee11d5945417ebccbb9341a05e19b13675c82 version: 0.0.1-develop.119 -->
Published 2026-11-25. Archive SHA-256 `3af8c3c9980756c88875a86f83ead17ee04aeef86c31f6c243ed34a496e070fd`.

- Change: Merge pull request #157 from arnavam/feat/helm-clamav
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@028ee11d5945](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/028ee11d5945417ebccbb9341a05e19b13675c82)
- Changes since 0.0.1-develop.118: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/a4360c79413b3d2220f4d17ea910b6a1ce22d1b6...028ee11d5945417ebccbb9341a05e19b13675c82

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.119` |
| `clamav.image` | `clamav/clamav:stable` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.119.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.118

<!-- source-commit: a4360c79413b3d2220f4d17ea910b6a1ce22d1b6 version: 0.0.1-develop.118 -->
Published 2026-11-25. Archive SHA-256 `0d7fd928d752c5e2b103bf84beb2774ec37418a29231f4e6a09515c7190d7bc5`.

- Change: Merge pull request #156 from arnavam/feat/ivr-credential-secret
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@a4360c79413b](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/a4360c79413b3d2220f4d17ea910b6a1ce22d1b6)
- Changes since 0.0.1-develop.117: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/115d0566d4a1f7472c775ff12485a9da15aaeb51...a4360c79413b3d2220f4d17ea910b6a1ce22d1b6

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.118` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.118.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.117

<!-- source-commit: 115d0566d4a1f7472c775ff12485a9da15aaeb51 version: 0.0.1-develop.117 -->
Published 2026-11-25. Archive SHA-256 `c14ee8da07f1153a2cce0e5c98b4e632817fa0bbafb7c0d1cf075f09686758f3`.

- Change: Merge pull request #152 from arnavam/feat/sla-rule-clusters
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@115d0566d4a1](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/115d0566d4a1f7472c775ff12485a9da15aaeb51)
- Changes since 0.0.1-develop.116: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/27f48ae8e6bd394d40777aeda7b468584cf13b5a...115d0566d4a1f7472c775ff12485a9da15aaeb51

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.117` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.117.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.116

<!-- source-commit: 27f48ae8e6bd394d40777aeda7b468584cf13b5a version: 0.0.1-develop.116 -->
Published 2026-11-24. Archive SHA-256 `e46a74b65867cc0e48302258f243c3de310e8420388c80c54f5fada85bd9ec5f`.

- Change: Merge pull request #154 from arnavam/fix/qa-desk-public
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@27f48ae8e6bd](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/27f48ae8e6bd394d40777aeda7b468584cf13b5a)
- Changes since 0.0.1-develop.115: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/673d96c61f039a708175b6b8fb2daaab7ac57e5e...27f48ae8e6bd394d40777aeda7b468584cf13b5a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.116` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.116.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.115

<!-- source-commit: 673d96c61f039a708175b6b8fb2daaab7ac57e5e version: 0.0.1-develop.115 -->
Published 2026-11-24. Archive SHA-256 `26189c075502a5918e9369bc73a7b4b20cffcf88e767e63f310fdc7532e089ea`.

- Change: Merge pull request #153 from arnavam/feat/grievance-admin-role
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@673d96c61f03](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/673d96c61f039a708175b6b8fb2daaab7ac57e5e)
- Changes since 0.0.1-develop.114: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93...673d96c61f039a708175b6b8fb2daaab7ac57e5e

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.115` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.115.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.114

<!-- source-commit: f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93 version: 0.0.1-develop.114 -->
Published 2026-11-24. Archive SHA-256 `6703a880cced7b8af073d6fcf76836f375b9a8763357df7f01a411966bd4ce6e`.

- Change: Merge pull request #151 from arnavam/resync/staging-into-develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@f4b2bda4b44a](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93)
- Changes since 0.0.1-develop.113: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/a4a551b714ceebe1ba7901aef380e0889df86cbc...f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.114` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.114.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.113

<!-- source-commit: a4a551b714ceebe1ba7901aef380e0889df86cbc version: 0.0.1-develop.113 -->
Published 2026-11-24. Archive SHA-256 `2841e049d2570bce2fe08a8f309359ec94ae71f45527ba0f562ed679fbdf24cd`.

- Change: Merge pull request #148 from arnavam/ci/promote-staging-workflow
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@a4a551b714ce](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/a4a551b714ceebe1ba7901aef380e0889df86cbc)
- Changes since 0.0.1-develop.112: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/e1687d2746733a1b4f1562e973871de9602d7b1a...a4a551b714ceebe1ba7901aef380e0889df86cbc

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.113` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.113.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.112

<!-- source-commit: e1687d2746733a1b4f1562e973871de9602d7b1a version: 0.0.1-develop.112 -->
Published 2026-11-24. Archive SHA-256 `19a7cfbd5d7b49523dd19d18876bec0ac8eb96b883e6db10cddd3f1a75f3508c`.

- Change: Merge pull request #139 from arnavam/feat/retire-sla-configuration
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@e1687d274673](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/e1687d2746733a1b4f1562e973871de9602d7b1a)
- Changes since 0.0.1-develop.111: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/0bbae7676cc5024397a97576d51a09a84b13001f...e1687d2746733a1b4f1562e973871de9602d7b1a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.112` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.112.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.111

<!-- source-commit: 0bbae7676cc5024397a97576d51a09a84b13001f version: 0.0.1-develop.111 -->
Published 2026-11-24. Archive SHA-256 `9692b9df7e3ce024f4025f643c655a8287350a39a1a6eb1b7bdc5616c259647d`.

- Change: fix(helm): drop CAP_CHOWN and disable privilege escalation for PodSecurity baseline (#146)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@0bbae7676cc5](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/0bbae7676cc5024397a97576d51a09a84b13001f)
- Changes since 0.0.1-develop.110: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/91e5db4e6de5762c30a1c970e88efd386363bf8a...0bbae7676cc5024397a97576d51a09a84b13001f

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.111` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.111.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.110

<!-- source-commit: 91e5db4e6de5762c30a1c970e88efd386363bf8a version: 0.0.1-develop.110 -->
Published 2026-11-24. Archive SHA-256 `2914721268696feb644f0af2642650a849e564a060b677eb79339c67085633dd`.

- Change: fix(STG-516): devtest bug fixes for SLA, deferral, attachments and officer pickers (#130)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@91e5db4e6de5](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/91e5db4e6de5762c30a1c970e88efd386363bf8a)
- Changes since 0.0.1-develop.109: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/e0e06dccb56d11dd9cc861b76306b5da2c808fb6...91e5db4e6de5762c30a1c970e88efd386363bf8a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.110` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.110.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.109

<!-- source-commit: e0e06dccb56d11dd9cc861b76306b5da2c808fb6 version: 0.0.1-develop.109 -->
Published 2026-11-24. Archive SHA-256 `d7962ea4c6a32898da416756a7c693e47464e887955393359e3aae57784df8e1`.

- Change: feat(helm): add the staff login option, with the agent's provider (#145)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@e0e06dccb56d](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/e0e06dccb56d11dd9cc861b76306b5da2c808fb6)
- Changes since 0.0.1-develop.108: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/b1e82d09eb253e7b0e0bfbc4966f0b15964b1ced...e0e06dccb56d11dd9cc861b76306b5da2c808fb6

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.109` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.109.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.108

<!-- source-commit: b1e82d09eb253e7b0e0bfbc4966f0b15964b1ced version: 0.0.1-develop.108 -->
Published 2026-11-24. Archive SHA-256 `436dd972d1b4848f8f0670ee27e79654f153a5bbbe0fb7b0595021a17543cd59`.

- Change: fix(ci): fetch develop so the staging promote can read the chart's source trees (#142)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@b1e82d09eb25](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/b1e82d09eb253e7b0e0bfbc4966f0b15964b1ced)
- Changes since 0.0.1-develop.106: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/c9aee7c3f26aa19d4c04824136ba65c1bbc140ff...b1e82d09eb253e7b0e0bfbc4966f0b15964b1ced

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.108` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.108.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.106

<!-- source-commit: c9aee7c3f26aa19d4c04824136ba65c1bbc140ff version: 0.0.1-develop.106 -->
Published 2026-11-23. Archive SHA-256 `9edf87a15b965cfe47367e5c4a6ee0f5f275b9ad01f84b2860c0587402908ef0`.

- Change: Merge pull request #138 from arnavam/feat/sla-rule-levels
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@c9aee7c3f26a](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/c9aee7c3f26aa19d4c04824136ba65c1bbc140ff)
- Changes since 0.0.1-develop.105: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/029eae42ce2b06e5dab516bf35eefb7d6c0a12d5...c9aee7c3f26aa19d4c04824136ba65c1bbc140ff

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.106` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.106.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.105

<!-- source-commit: 029eae42ce2b06e5dab516bf35eefb7d6c0a12d5 version: 0.0.1-develop.105 -->
Published 2026-11-23. Archive SHA-256 `74a76c0e7c55e4a0152db03fcd73e5dbb4d806999406d4ea2c1c18d76f4310d5`.

- Change: Merge pull request #137 from arnavam/feat/position-assignments
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@029eae42ce2b](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/029eae42ce2b06e5dab516bf35eefb7d6c0a12d5)
- Changes since 0.0.1-develop.104: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/511c3e23ce24471656e8ac79f49449403c73eeb0...029eae42ce2b06e5dab516bf35eefb7d6c0a12d5

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.105` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.105.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.104

<!-- source-commit: 511c3e23ce24471656e8ac79f49449403c73eeb0 version: 0.0.1-develop.104 -->
Published 2026-11-21. Archive SHA-256 `c0f9965498ce3f91f6f0dc751ea2a7a3bb6966fc349ffc552babf9df93f454b2`.

- Change: Merge pull request #134 from arnavam/feat/shared-openapi-generator
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@511c3e23ce24](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/511c3e23ce24471656e8ac79f49449403c73eeb0)
- Changes since 0.0.1-develop.103: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/0d170098627340875985337151a4f3fdff07b8a8...511c3e23ce24471656e8ac79f49449403c73eeb0

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.104` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.104.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.103

<!-- source-commit: 0d170098627340875985337151a4f3fdff07b8a8 version: 0.0.1-develop.103 -->
Published 2026-11-21. Archive SHA-256 `f0173e9b29a8de31293197326d55caf5befa42ffda3e2a91f27a81e03402e315`.

- Change: Merge pull request #135 from dhruvbhatt701/feature/STG-514-sensitive-urgent-grievance-flags
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@0d1700986273](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/0d170098627340875985337151a4f3fdff07b8a8)
- Changes since 0.0.1-develop.102: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/67fbee832f12851e3ca38ce3bd6fcef11bcb335d...0d170098627340875985337151a4f3fdff07b8a8

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.103` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.103.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.102

<!-- source-commit: 67fbee832f12851e3ca38ce3bd6fcef11bcb335d version: 0.0.1-develop.102 -->
Published 2026-11-20. Archive SHA-256 `cbba9b18ce04148f4fbff7ae9fd3b7576dc0302ec0a5d47c244bb00f26532769`.

- Change: Merge pull request #124 from dhruvbhatt701/feature/STG-514-sensitive-urgent-flags
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@67fbee832f12](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/67fbee832f12851e3ca38ce3bd6fcef11bcb335d)
- Changes since 0.0.1-develop.101: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/a08caa29ce905ba57a66a72210fea020b33fc573...67fbee832f12851e3ca38ce3bd6fcef11bcb335d

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.102` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.102.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.101

<!-- source-commit: a08caa29ce905ba57a66a72210fea020b33fc573 version: 0.0.1-develop.101 -->
Published 2026-11-20. Archive SHA-256 `5d9d246f9732e296320423e543126cfeadae1c64107942a2db54a4a2ec0d1006`.

- Change: Merge pull request #133 from arnavam/fix/gateway-deploy-every-build
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@a08caa29ce90](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/a08caa29ce905ba57a66a72210fea020b33fc573)
- Changes since 0.0.1-develop.100: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/a962e29b911cb5f31c9247a8db665acc5358c7dc...a08caa29ce905ba57a66a72210fea020b33fc573

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.101` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.101.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.100

<!-- source-commit: a962e29b911cb5f31c9247a8db665acc5358c7dc version: 0.0.1-develop.100 -->
Published 2026-11-20. Archive SHA-256 `c1bac4bd4b0e46837e7907db80b6ea9d841b4dec865cb318f98bdaf235ecfded`.

- Change: Merge pull request #132 from arnavam/fix/dev-forcecreate-stop-workloads
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@a962e29b911c](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/a962e29b911cb5f31c9247a8db665acc5358c7dc)
- Changes since 0.0.1-develop.96: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/68fdbc3949680a1e6a50d386fa336481bbe36e8a...a962e29b911cb5f31c9247a8db665acc5358c7dc

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.100` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.100.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.96

<!-- source-commit: 68fdbc3949680a1e6a50d386fa336481bbe36e8a version: 0.0.1-develop.96 -->
Published 2026-11-19. Archive SHA-256 `944b1b277df7cb1a2996beff9669666f343ff779431d43ebedb3e0b93d9b18bd`.

- Change: Merge pull request #128 from arnavam/fix/auth-service-prefix
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@68fdbc394968](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/68fdbc3949680a1e6a50d386fa336481bbe36e8a)
- Changes since 0.0.1-develop.95: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/61e4e2057a21c14394de47605ab31c27e87c8917...68fdbc3949680a1e6a50d386fa336481bbe36e8a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.96` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.96.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.95

<!-- source-commit: 61e4e2057a21c14394de47605ab31c27e87c8917 version: 0.0.1-develop.95 -->
Published 2026-11-19. Archive SHA-256 `cdc2709f6f128c0b193f97eeabc36ce30b76bf43c933bb9515a5d0eafe73d022`.

- Change: Merge pull request #127 from arnavam/fix/ci-gateway-deploy-chart-selection
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@61e4e2057a21](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/61e4e2057a21c14394de47605ab31c27e87c8917)
- Changes since 0.0.1-develop.89: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/6b17aa28b6ad0c241c015e88f8920ee8cf824beb...61e4e2057a21c14394de47605ab31c27e87c8917

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.95` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.95.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.89

<!-- source-commit: 6b17aa28b6ad0c241c015e88f8920ee8cf824beb version: 0.0.1-develop.89 -->
Published 2026-11-17. Archive SHA-256 `8552aad06282f1d7c9fea2333238bf0a387769fb405234059227c822730562de`.

- Change: Merge pull request #119 from Centre-for-Open-Societal-Systems/perf/grievance-dev-resource-requests
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@6b17aa28b6ad](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/6b17aa28b6ad0c241c015e88f8920ee8cf824beb)
- Changes since 0.0.1-develop.87: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/5afb43d83bc80418bcc841fee101cd9ec7aaa0df...6b17aa28b6ad0c241c015e88f8920ee8cf824beb

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.89` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.89.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.87

<!-- source-commit: 5afb43d83bc80418bcc841fee101cd9ec7aaa0df version: 0.0.1-develop.87 -->
Published 2026-11-15. Archive SHA-256 `1b05ba7268991b112b45c9b6eaf74a40ebccb703385ab2c9d94c1d8e65ec2da6`.

- Change: Merge pull request #117 from arnavam/feat/frappe-desk-host
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@5afb43d83bc8](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/5afb43d83bc80418bcc841fee101cd9ec7aaa0df)
- Changes since 0.0.1-develop.86: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/4d0341200dcbf66697824198c659e39643c5a22d...5afb43d83bc80418bcc841fee101cd9ec7aaa0df

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.87` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.87.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.86

<!-- source-commit: 4d0341200dcbf66697824198c659e39643c5a22d version: 0.0.1-develop.86 -->
Published 2026-11-15. Archive SHA-256 `6f3d985f132687f5fb219ae95aded6df59ca59896aa1f846874ec2fc55ad5f1c`.

- Change: Merge pull request #116 from arnavam/feat/iam-agent-beneficiary-rows
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@4d0341200dcb](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/4d0341200dcbf66697824198c659e39643c5a22d)
- Changes since 0.0.1-develop.85: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/d8e7c9097ff1c3beb8d00e3bdc7b0173cea2ba4a...4d0341200dcbf66697824198c659e39643c5a22d

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.86` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.86.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.85

<!-- source-commit: d8e7c9097ff1c3beb8d00e3bdc7b0173cea2ba4a version: 0.0.1-develop.85 -->
Published 2026-11-14. Archive SHA-256 `7172fc3840b050616387ea12a9a7690634dd73b9a186dd309636a126b3327b09`.

- Change: Merge pull request #114 from arnavam/chore/gateway-wildcard-tls
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@d8e7c9097ff1](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/d8e7c9097ff1c3beb8d00e3bdc7b0173cea2ba4a)
- Changes since 0.0.1-develop.84: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/7118e820e48709714b01ba6b7a8c8eae2f8eaa03...d8e7c9097ff1c3beb8d00e3bdc7b0173cea2ba4a

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.85` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.85.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.84

<!-- source-commit: 7118e820e48709714b01ba6b7a8c8eae2f8eaa03 version: 0.0.1-develop.84 -->
Published 2026-11-13. Archive SHA-256 `417e6b59a6dfb913b4911c746eff932ac31acde67121e14a4e3f734c9c778436`.

- Change: Merge pull request #112 from arnavam/fix/gateway-limit-count-no-group
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@7118e820e487](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/7118e820e48709714b01ba6b7a8c8eae2f8eaa03)
- Changes since 0.0.1-develop.83: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/9718a2878d4f3296a9630897716f2789c571dd58...7118e820e48709714b01ba6b7a8c8eae2f8eaa03

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.84` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.84.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.83

<!-- source-commit: 9718a2878d4f3296a9630897716f2789c571dd58 version: 0.0.1-develop.83 -->
Published 2026-11-13. Archive SHA-256 `76de8c7b4ba888cf79f90c0cb225fa689754794b9bb23ecc04b9157d994b960a`.

- Change: Merge pull request #115 from dhruvbhatt701/fix/category-admin-duplicate-message
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@9718a2878d4f](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/9718a2878d4f3296a9630897716f2789c571dd58)
- Changes since 0.0.1-develop.82: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25...9718a2878d4f3296a9630897716f2789c571dd58

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.83` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.83.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.82

<!-- source-commit: 031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25 version: 0.0.1-develop.82 -->
Published 2026-11-13. Archive SHA-256 `26a57ef8e1d1c21fa8d808f06f0a2cf2bfb16b12ce90c33b48480006724642ad`.

- Change: Merge pull request #111 from arnavam/feat/publish-gateway-chart
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@031d425de8bf](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25)
- Changes since 0.0.1-develop.81: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/6c6922f765acf9a30c0361fb9b05ace2e9f4b631...031d425de8bf4bd4f8b6c2bc9d5ec68f9be12c25

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.82` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.82.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.1-develop.81

<!-- source-commit: 6c6922f765acf9a30c0361fb9b05ace2e9f4b631 version: 0.0.1-develop.81 -->
Published 2026-11-13. Archive SHA-256 `57941a67c9bfed97a49b36a01f2fd0ad3da0afc8d006258b66b0833751aee710`.

- Change: Merge pull request #110 from arnavam/chore/trigger-gateway-deploy
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@6c6922f765ac](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/6c6922f765acf9a30c0361fb9b05ace2e9f4b631)
- Changes since 0.0.0-develop.79: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/compare/c84d8e9af2eee60773b0346581af810a49125859...6c6922f765acf9a30c0361fb9b05ace2e9f4b631

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-service/grievance-service:0.0.1-develop.81` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.1-develop.81.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

## 0.0.0-develop.79

<!-- source-commit: c84d8e9af2eee60773b0346581af810a49125859 version: 0.0.0-develop.79 -->
Published 2026-11-12. Archive SHA-256 `251af7392ec29c4225dfd6c0ffd0b5c6111e2e1f5b588dd3cedfe892ccbabb95`.

- Change: Merge pull request #108 from arnavam/fix/grievance-develop-chart-version
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@c84d8e9af2ee](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/c84d8e9af2eee60773b0346581af810a49125859)

| Values path | Image |
| --- | --- |
| `frappe.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan-grievance-service/grievance-service:0.0.0-develop.79` |

Return to this version:

```sh
helm upgrade grievance https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-service-0.0.0-develop.79.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-service.yaml --wait --timeout 15m
```

