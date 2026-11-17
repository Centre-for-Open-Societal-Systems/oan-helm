# OAN Leads API

OpenAgriNet (OAN) Leads API from
[leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api): Spring Boot
service with a Redis cache, PostgreSQL/Elasticsearch access and an optional Istio route.

The release keeps its own ECR pull secret (`leads-api-ecr`). Pass the secret values file
(`secret.create: true` with the database, Elasticsearch and A2C webhook credentials) with
the install; nothing is created by hand in the namespace.
See the [chart README](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-leads-api).
