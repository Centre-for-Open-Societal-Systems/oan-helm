# OAN Leads API

OpenAgriNet (OAN) Leads API, developed in the OAN
[leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api) repository:
a Spring Boot service (port 8080, Swagger at `/swagger-ui/index.html`) backed by
PostgreSQL, Elasticsearch and a Redis cache, with the A2C initiate webhook. Its
`telephony` dependency captures leads by phone and posts them to the API.

| Source | GitHub repository |
| --- | --- |
| OAN application | [leads-api](https://github.com/Centre-for-Open-Societal-Systems/leads-api) |
| Telephony (dependency) | [Telephony-Service](https://github.com/A5HW1NRA7AN/Telephony-Service/tree/freeswitch-kubernetes), branch `freeswitch-kubernetes` (same commit in the [COSS repository](https://github.com/Centre-for-Open-Societal-Systems/Telephony-Service/tree/freeswitch-kubernetes)) |
| OAN Helm sources | [oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-leads-api) |

The chart has no OpenG2P dependency and owns no existing release, so installing it
changes no other chart's resources. It replaces the raw manifests in leads-api
`terra/prod/k8` (`01`-`04`) and the Telephony-Service `deploy/helm/telephony` chart
with one release in one namespace (`leads`).

## What it installs

| Resource | Values key | Default |
| --- | --- | --- |
| API Deployment (2 replicas, rolling, TCP probes), Service, ConfigMap, PDB | `image`, `config` | Enabled; `eoan/leads-api/leads-api` (`develop-latest` until a digest is set) |
| ECR pull secret `leads-api-ecr`: pre-install/pre-upgrade hook Job + CronJob every 8 hours, node IAM role | `ecrPullSecret` | Enabled; the API pods pull with it |
| Credentials Secret `leads-secrets`, filled from the secret values file | `secret` | Referenced; created by the chart with `secret.create: true` |
| Redis cache Deployment + Service (`<release>-redis`), no persistence | `redis` | Enabled, no AUTH |
| `leads-postgres` / `leads-elasticsearch` Services + EndpointSlices to a private DB host | `externalDb` | Disabled |
| Istio VirtualService on the shared Gateway | `virtualService` | Disabled |
| HorizontalPodAutoscaler | `autoscaling` | Disabled |
| Telephony dependency (below): lead-service, event-publisher, FreeSWITCH, `lead_db` PostgreSQL | `telephony` | Enabled; `telephony.enabled: false` renders the API alone |

Rate limiting of `/leads/v1/initiate` (a Kong plugin in `terra/prod/k8/06-kong-to-app.yaml`)
is not part of this chart: apply it on the environment's gateway.

## Telephony dependency

`charts/telephony` is a subchart kept as source (declared in `Chart.yaml` with
`repository: file://charts/telephony`, `condition: telephony.enabled`; any generated
`charts/telephony-*.tgz` is ignored). Change it in place and its changes release with
this chart. The call flow, all inside the release namespace:

```
caller ─► SIP trunk ─► <release>-telephony-freeswitch (host network: answer, play greeting)
             └─ ESL outbound socket :8084 ─► <release>-telephony-event-publisher
                  └─ POST /api/v1/call-events ─► <release>-telephony-lead-service (lead_db)
                       └─ POST /leads/v1/initiate ─► <release> (this Leads API)
```

| Resource | Values key | Default |
| --- | --- | --- |
| lead-service Deployment (2) + Service :8080; posts to `http://<release>.<namespace>.svc.cluster.local/leads/v1/initiate` | `telephony.leadService`, `telephony.leadRegistry` | `freeswitch-lead-service` build 23 |
| event-publisher Deployment (2) + Service :8080/:8084, spool `emptyDir` | `telephony.eventPublisher` | `freeswitch-event-publisher` build 23 |
| FreeSWITCH Deployment (1, `Recreate`, host network, SIP 5060, RTP 16384-32768) + ConfigMap `freeswitch.xml` | `telephony.freeswitch` | `freeswitch-freeswitch` build 23, `extIp` auto-nat |
| `lead_db` PostgreSQL Deployment + Service + PVC (`helm.sh/resource-policy: keep`) | `telephony.postgres` | Enabled, 10Gi, default StorageClass |
| Credentials Secret `leads-telephony-secrets` (`DB_USER`, `DB_PASSWORD`, `ESL_PASSWORD`, optional `LEAD_REGISTRY_API_KEY_VALUE`) | `telephony.secret` | Referenced; created with `telephony.secret.create: true` |

- **Images.** The three telephony images are in `379220350808.dkr.ecr.ap-northeast-1.amazonaws.com`
  (`telephony.registry`), pinned by digest. The release's pull secret `leads-api-ecr` holds a
  token for that registry too, so the node role needs pull access in both regions.
- **Probes.** lead-service and event-publisher are probed on `/actuator/health/{readiness,liveness}`.
- **Spool.** event-publisher keeps events lead-service did not accept in
  `telephony.eventPublisher.spoolDir` (an `emptyDir`) and retries them every 30 seconds; they
  survive a container restart, not the pod's deletion.
- **ESL password.** FreeSWITCH reads it from the mounted Secret key `ESL_PASSWORD` at start
  (`exec-set` in `freeswitch.xml`); it is not in the ConfigMap.
- **FreeSWITCH node.** With the host network, one node answers the SIP trunk: pin it with
  `telephony.freeswitch.nodeSelector`, set `telephony.freeswitch.extIp` to its public IP and
  open UDP/TCP 5060 and UDP 16384-32768 to the trunk. `telephony.freeswitch.enabled: false`
  keeps the rest of the pipeline without a SIP endpoint.
- **External database.** `telephony.postgres.enabled: false` with `telephony.leadService.dbUrl`
  (`jdbc:postgresql://<host>:5432/<db>`) uses another PostgreSQL with the same credentials.
- **Upgrading telephony images.** Set `telephony.<component>.image.tag` and `.digest` to the
  reviewed Telephony-Service build (its Jenkinsfile pushes `<build>` and `latest`).

## Delivery

Nothing is created by hand in the namespace:

- **Image pull.** The release writes `leads-api-ecr` itself, before the pods start and
  every 8 hours after, with the node's IAM role (which needs pull access to
  `eoan/leads-api/leads-api` and, with telephony, the ap-northeast-1 telephony repositories).
  It holds one token per registry: the API registry, `ecrPullSecret.extraRegistries` and
  `telephony.registry`. Set `ecrPullSecret.enabled: false` only where another
  mechanism provides the pull secret, and list it in `imagePullSecrets` (and
  `telephony.imagePullSecrets`).
- **Credentials.** They arrive with the deploy as a secret values file, stored as a
  Jenkins secret-file credential (`dev-leads-api-secret-values` for dev), the same way
  `staging-commons-secret-values` delivers Commons' secrets. The file is passed after the
  environment values and is never committed:

  ```yaml
  secret:
    create: true
    values:
      SPRING_DATASOURCE_USERNAME: ...
      SPRING_DATASOURCE_PASSWORD: ...
      ELASTICSEARCH_USERNAME: ...
      ELASTICSEARCH_PASSWORD: ...
      A2C_WEBHOOK_API_KEY: ...
      A2C_WEBHOOK_API_SECRET: ...
      # SPRING_REDIS_PASSWORD: ...   # required with redis.auth.enabled
  config:
    SPRING_DATASOURCE_URL: jdbc:postgresql://<host>:5432/<db>
    ELASTICSEARCH_HOST: <host>
  # or: externalDb: {enabled: true, ip: <private DB host IP>}
  telephony:
    secret:
      create: true
      values:
        DB_USER: ...        # lead_db owner; the in-chart PostgreSQL is initialised with it
        DB_PASSWORD: ...
        ESL_PASSWORD: ...
    freeswitch:
      extIp: <public IP of the FreeSWITCH node>
  ```

  The chart refuses to render with `secret.create: true` when a required key is
  missing. A changed value rolls the pods (`checksum/secret`). With
  `secret.create: false` the Secret `secret.name` must be provided by another
  controller, such as External Secrets.

The release is installed and upgraded from `repository/` (Rancher, or Helm from the
Jenkins agent with the deployer kubeconfig):

```sh
helm upgrade --install leads-api oan/oan-leads-api -n leads --create-namespace \
  -f environments/dev/values/oan-leads-api.yaml -f "$LEADS_SECRET_VALUES"
```

After install: `kubectl -n leads rollout status deploy/leads-api` and
`deploy/leads-api-telephony-{lead-service,event-publisher,freeswitch,db}`, then
`https://<host>/swagger-ui/index.html` loads and a lead search answers from
Elasticsearch. A test call to the SIP number shows a `SENT` row in lead_db's lead ingest
log and the lead (its `phone_number`) in the API.

## Upgrading the image

The leads-api Jenkinsfile publishes
`379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/leads-api/leads-api:0.1.0-develop.<build>`
and `develop-latest`. Set `image.digest` to the reviewed build's digest (keep the
`0.1.0-develop.<build>` tag in the comment), `image.pullPolicy: IfNotPresent`, and run
`helm upgrade`.
