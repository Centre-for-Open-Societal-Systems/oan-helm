# oan-aggregation-api: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

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

