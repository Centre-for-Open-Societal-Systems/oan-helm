# frappe-common: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.47

<!-- source-commit: 0 version: 0.0.0-develop.47 -->
Published 2026-11-27. Archive SHA-256 `0f2cc3094a56b5b232840b1799d87fc54b48282eba7d99dbee5fd06b37d77dc2`.

- Change: No description recorded.

| Values path | Image |
| --- | --- |
| `mariadb-sts.image` | `mariadb:10.6` |
| `mariadb-subchart.image` | `bitnamilegacy/mariadb:10.6.17-debian-11-r10` |
| `postgresql-sts.image` | `postgres:15` |
| `postgresql-subchart.image` | `bitnamilegacy/postgresql:16.4.0-debian-12-r14` |

Return to this version:

```sh
helm upgrade <release> https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/frappe-common-0.0.0-develop.47.tgz -n <namespace> --reset-values -f helm/environments/dev/values.yaml --wait --timeout 15m
```

