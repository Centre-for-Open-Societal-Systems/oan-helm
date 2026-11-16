# OAN Leads API

OpenAgriNet (OAN) Leads API from
[leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api): Spring Boot
service with a Redis cache, PostgreSQL/Elasticsearch access and an optional Istio route.

Before installing, create the `leads-secrets` Secret (database, Elasticsearch and A2C
webhook credentials) in the target namespace and set the image digest and ECR pull Secret.
See the [chart README](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-leads-api).
