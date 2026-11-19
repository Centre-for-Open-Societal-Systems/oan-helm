# OAN Leads API

OpenAgriNet (OAN) Leads API from
[leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api): Spring Boot
service with a Redis cache, PostgreSQL/Elasticsearch access and an optional Istio route,
plus its telephony dependency from
[Telephony-Service `freeswitch-kubernetes`](https://github.com/A5HW1NRA7AN/Telephony-Service/tree/freeswitch-kubernetes)
(FreeSWITCH, event publisher, lead-service and its lead_db), which posts every call lead
to the API. Both install in the `leads` namespace.

The release keeps its own ECR pull secret (`leads-api-ecr`) for both the API and telephony
registries. Pass the secret values file (`secret.create: true` with the database,
Elasticsearch and A2C webhook credentials, and `telephony.secret.create: true` with
`DB_USER`, `DB_PASSWORD`, `ESL_PASSWORD`) with the install; nothing is created by hand in
the namespace. Set `telephony.enabled: false` to install the API alone.
See the [chart README](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-leads-api).
