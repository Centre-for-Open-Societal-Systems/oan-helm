# Vendored service chart

Source: `deploy/helm/oan-messaging/` of Centre-for-Open-Societal-Systems/oan_messaging_service
(`staging` at c4af3ba; the chart directory last changed in 453a42f, and the copy is identical to it), without its `ci/` directory. Only change: `name` in `Chart.yaml`
is `oan-messaging-service` (the parent chart is `oan-messaging`). Its values live under the key
`oan-messaging-service` in the parent's values. Refresh by copying the directory again and re-applying
that one change.
