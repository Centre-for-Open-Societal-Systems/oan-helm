# OAN Leads API

OpenAgriNet (OAN) Leads API, developed in the OAN
[leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api) repository:
a Spring Boot service (port 8080, Swagger at `/swagger-ui/index.html`) backed by
PostgreSQL, Elasticsearch and a Redis cache, with the A2C initiate webhook.

| Source | GitHub repository |
| --- | --- |
| OAN application | [leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api) |
| OAN Helm sources | [oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-leads-api) |

The chart has no OpenG2P dependency and owns no existing release, so installing it
changes no other chart's resources. It replaces the raw manifests in leads-api
`terra/prod/k8` (`01`-`04`) with one release.

## What it installs

| Resource | Values key | Default |
| --- | --- | --- |
| API Deployment (2 replicas, rolling, TCP probes), Service, ConfigMap, PDB | `image`, `config`, `secret` | Enabled; `oan/leads-api` by digest |
| Redis cache Deployment + Service (`<release>-redis`) | `redis` | Enabled, no AUTH |
| `leads-postgres` / `leads-elasticsearch` Services + EndpointSlices to a private DB host | `externalDb` | Disabled |
| Istio VirtualService on the shared Gateway | `virtualService` | Disabled |
| HorizontalPodAutoscaler | `autoscaling` | Disabled |

Rate limiting of `/leads/v1/initiate` (a Kong plugin in `terra/prod/k8/06-kong-to-app.yaml`)
is not part of this chart: apply it on the environment's gateway.

## Before installing

1. **Image.** The leads-api Jenkinsfile (`DEPLOY_ENV=staging`) pushes
   `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/leads-api:staging-ati-<build>`.
   Set `image.digest` to the reviewed build's digest and add the namespace-local ECR pull
   Secret to `imagePullSecrets`.
2. **Secret.** Create a Secret in the release namespace and set `secret.name`
   (default `leads-secrets`). Required keys: `SPRING_DATASOURCE_USERNAME`,
   `SPRING_DATASOURCE_PASSWORD`, `ELASTICSEARCH_USERNAME`, `ELASTICSEARCH_PASSWORD`,
   `A2C_WEBHOOK_API_KEY`, `A2C_WEBHOOK_API_SECRET`. Optional: `SPRING_REDIS_PASSWORD`
   (required with `redis.auth.enabled`; Redis and the app share it).
3. **Databases.** Point `config.SPRING_DATASOURCE_URL` and `config.ELASTICSEARCH_HOST` at
   the databases, or enable `externalDb` with the DB host's private `externalDb.ip` to
   keep the `leads-postgres` / `leads-elasticsearch` names.
4. **Route.** Set `virtualService.host` (a single-label wildcard name such as
   `leads.development.oanstaging.com`) and enable `virtualService`.

```sh
helm upgrade --install leads-api charts/oan-leads-api -n leads --create-namespace \
  -f environments/dev/values/oan-leads-api.yaml -f <private values>
```

After install: `kubectl -n leads rollout status deploy/leads-api`, then
`https://<host>/swagger-ui/index.html` loads and a lead search answers from
Elasticsearch.

## Upgrading the image

Change `image.digest` (keep the `staging-ati-<build>` tag in the comment) and run
`helm upgrade`. Changing a `config` value rolls the pods; a Secret change needs
`kubectl rollout restart deploy/<release>`.
