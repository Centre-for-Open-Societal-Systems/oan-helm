# frappe-service: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.47

<!-- source-commit: 0 version: 0.0.0-develop.47 -->
Published 2026-11-27. Archive SHA-256 `2d31be592820ea9d04cb6829570141bc4a1863a2a78c707b48fc2fe9eec9555b`.

- Change: No description recorded.

| Values path | Image |
| --- | --- |
| `mariadb-sts.image` | `mariadb:10.6` |
| `postgresql-sts.image` | `postgres:15` |
| `redis-cache.image` | `bitnamilegacy/redis:7.0` |
| `redis-queue.image` | `bitnamilegacy/redis:7.0` |
| `valkey-cache.image` | `valkey/valkey:7.2` |
| `valkey-queue.image` | `valkey/valkey:7.2` |

Return to this version:

```sh
helm upgrade <release> https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/frappe-service-0.0.0-develop.47.tgz -n <namespace> --reset-values -f helm/environments/dev/values.yaml --wait --timeout 15m
```

## 0.0.0-develop.28

<!-- source-commit: 0 version: 0.0.0-develop.28 -->
Published 2026-11-12. Archive SHA-256 `aa1196e933b217162437d5830e00699e8d63d52c55aba0e51ca107403b18acd0`.

- Change: No description recorded.

| Values path | Image |
| --- | --- |
| `mariadb-sts.image` | `mariadb:10.6` |
| `postgresql-sts.image` | `postgres:15` |
| `redis-cache.image` | `bitnamilegacy/redis:7.0` |
| `redis-queue.image` | `bitnamilegacy/redis:7.0` |
| `valkey-cache.image` | `valkey/valkey:7.2` |
| `valkey-queue.image` | `valkey/valkey:7.2` |

Return to this version:

```sh
helm upgrade <release> https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/frappe-service-0.0.0-develop.28.tgz -n <namespace> --reset-values -f helm/environments/dev/values.yaml --wait --timeout 15m
```

