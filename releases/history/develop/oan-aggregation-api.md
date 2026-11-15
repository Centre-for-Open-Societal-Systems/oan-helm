# oan-aggregation-api: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.20

<!-- source-commit: 125ba647acb5bf3a0290b023793a9f6f32d93162 version: 0.0.0-develop.20 -->
Published 2026-11-15. Archive SHA-256 `56381c700884866ec9c307dad990fae4bb2409533a9f3a169073bbf53e3d85da`.

- Change: Merge pull request #9 from simretyibeltal-commits/ci/helm-pipeline
- Source: [Centre-for-Open-Societal-Systems/oan-aggregation-api@125ba647acb5](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api/commit/125ba647acb5bf3a0290b023793a9f6f32d93162)
- Changes since 0.0.0-develop.1: https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api/compare/99e42e03070f9232a48dcf3219d087e49290584d...125ba647acb5bf3a0290b023793a9f6f32d93162

| Values path | Image |
| --- | --- |
| `image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-aggregation-api/aggregation-api:0.0.0-develop.1@sha256:d24d3579f154fd80acda251974cb9a6a3c87c2e516b24c35215218ca89eac961` |

Return to this version:

```sh
helm upgrade commons-services https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-aggregation-api-0.0.0-develop.20.tgz -n commons --reset-values -f helm/oan-aggregation-api/values-dev.yaml --wait --timeout 15m
```

## 0.0.0-develop.1

<!-- source-commit: 99e42e03070f9232a48dcf3219d087e49290584d version: 0.0.0-develop.1 -->
Published 2026-11-15. Archive SHA-256 `cdf3fc1bdad92de74c324ee67bf14d8d5974a0800a71bbc53d0fe9c03dcff848`.

- Change: Bootstrap: aggregation-api as a commons-services subchart, image of the inline template (dev-a5fa17fd7e7f)
- Source: [Centre-for-Open-Societal-Systems/oan-aggregation-api@99e42e03070f](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api/commit/99e42e03070f9232a48dcf3219d087e49290584d)

| Values path | Image |
| --- | --- |
| `image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/commons/aggregation-api:dev-a5fa17fd7e7f@sha256:3bd17245a75252bdf497cc1bab22b9e1148d0fedce376e7892a9e551bcefb7b4` |

Return to this version:

```sh
helm upgrade commons-services https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-aggregation-api-0.0.0-develop.1.tgz -n commons --reset-values -f helm/oan-aggregation-api/values-dev.yaml --wait --timeout 15m
```

