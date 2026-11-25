# Vendored service chart

Source: `deploy/helm/oan-messaging/` of Centre-for-Open-Societal-Systems/oan_messaging_service
(`develop`, merge commit e4f7dfb), without its `ci/` directory. Only change: `name` in `Chart.yaml`
is `oan-messaging-service` (the parent chart is `oan-messaging`). Its values live under the key
`oan-messaging-service` in the parent's values. Refresh by copying the directory again and re-applying
that one change.
