# APISIX gateway

The OAN API gateway is Apache APISIX, configured through the APISIX Ingress Controller.
This document is the design and the DevOps runbook for the development clusters.

**Status:** nothing here has been run against a cluster yet. Where a step depends on
something we could not confirm, it says **Confirm** and tells you how to check.

One central gateway serves every OAN app. It runs alone in its own cluster (the gateway
cluster). Each app runs in its own cluster: grievance on RKE2 (`13.233.56.204`), A2C in
a cluster not provisioned yet. All are separate from the OpenG2P dev cluster (`server`
in `environments/dev/endpoints.yaml`, `13.201.58.55`). The values sit with the other dev
values in `environments/dev/values/`, and each file names its target cluster in its
header. **Never install them into the OpenG2P cluster.**

## 1. Design

### What lives where

| Part                              | Source                                                                                                                                                                                                                                   | Values                                                                                         |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| APISIX and the Ingress Controller | Chart `oan-apisix-gateway`, which vendors upstream `apisix/apisix` 2.18.2 (bundles `apisix-ingress-controller`) and releases like the other charts                                                    | [charts/oan-apisix-gateway/values.yaml](../charts/oan-apisix-gateway/values.yaml)                               |
| Rate-limit counters               | Dependency `bitnami/redis` 17.15.2 of `oan-apisix-gateway`, installed with APISIX in the same release                                                                                                                                      | [charts/oan-apisix-gateway/values.yaml](../charts/oan-apisix-gateway/values.yaml)            |
| Grievance routes                  | Chart `oan-grievance-gateway` in [oan_grievance_service/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/tree/develop/apisix/k8s), generated from the service's OpenAPI spec. It is not copied here | [dev/values/oan-grievance-gateway.yaml](../environments/dev/values/oan-grievance-gateway.yaml) |
| A2C routes                        | Chart `oan-a2c-gateway` in [oan_a2c/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/tree/develop/apisix/k8s), generated from the A2C OpenAPI spec                                                                | [dev/values/oan-a2c-gateway.yaml](../environments/dev/values/oan-a2c-gateway.yaml)             |
| Partner APIs (OAN sandbox apps)   | Chart `oan-partner-gateway` in [sandbox-platform deploy/apisix-partner-gateway/k8s](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform/tree/develop/deploy/apisix-partner-gateway), generated from the routes the sandbox is tested against | [dev/values/oan-partner-gateway.yaml](../environments/dev/values/oan-partner-gateway.yaml) |

This repository holds only the values. Each app's route chart lives with the app, because
the routes come from the app's OpenAPI spec and must change in the same PR as the code.
The grievance service will get its own chart repository and releases later; until then,
install its chart from a checkout of the service repository at the deployed commit.

All of these install into the gateway cluster: APISIX and Redis in namespace `api6-gateway`,
each app's routes in a namespace named after the app (`grievance`, `a2c`).

oan_auth_service is a library installed into each app's bench, not a service of its own,
so it has no chart or values. Its endpoints (`/v1/auth/*`, `/v1/admin/*`,
`/v1/notifications/*`) are part of each app's chart, pointed at that app's Frappe.

Do not also run `adc sync` against this gateway. ADC and the Ingress Controller each
overwrite the other's routes.

### Traffic path

```
browser -> DNS grievance-backend.development.oanstaging.com -> gateway node
        -> APISIX, hostPorts 80 and 443 on the node      TLS, routes, rate limits, CORS, metrics
        -> grievance node, private address               node ports 30800 (gunicorn), 30900 (socket.io)
```

APISIX is the edge. It binds the gateway node's ports 80 and 443 and terminates TLS with
the certificate each app's `ApisixTls` names. No nginx or ingress controller sits in
front of it, so clients connect directly and rate limits see their own address.

APISIX picks the app by the request's host: the TLS handshake (SNI) picks the
certificate, and each route matches its app's `hosts` and paths. Apps share paths such
as `/v1/auth/*` (oan_auth_service runs in each bench), so every app's chart must set
`hosts`. An empty list matches any host.

The Ingress Controller resolves only Services in its own cluster. An app chart therefore
points its ApisixUpstreams at the app cluster's private addresses (`web.externalHosts`,
`socket.externalHosts`, one entry per app node): the upstream lists each address as a
node, APISIX balances across them and drops one that fails its health check
(`web.healthCheck`), and the routes reference the upstream by name. With an empty list
the same chart targets an in-cluster Service, for a gateway in the app's own cluster. The app cluster exposes
Frappe on node ports that accept only the gateway cluster's addresses. That hop is plain
HTTP, so it must stay on a private network (one VPC, or peering).

The Frappe app itself is installed by `charts/oan-grievance-service`; its runbook is
[grievance-service.md](grievance-service.md), which installs this gateway as one of its
steps.

### Gateway-wide plugins

`request-id` (`X-Request-Id`, echoed in the response) and `prometheus` are global rules,
set as `gatewayProxy.plugins` in the chart's `values.yaml`, so they apply to every app's routes.
`gatewayProxy.pluginMetadata` holds a plugin's gateway-wide setting: for `http-logger`, the
record format of the partner routes' call log (section 8b). Metrics
are served on port 9091 at `/apisix/prometheus/metrics`; enable
`metrics.serviceMonitor` once a Prometheus Operator scrapes the cluster. Per-app plugins
(CORS, body size, rate limits, authentication) stay in each app's chart.

## 2. Prerequisites

Run these from a machine with `kubectl` and `helm` (3.x) pointed at the gateway cluster.

```sh
kubectl config current-context        # must be the gateway cluster, not OpenG2P or an app cluster
kubectl get nodes -o wide             # expect the gateway node
helm version --short
```

Collect these facts first. They are the values the install needs.

| Fact                                                                                                             | How to get it                                                                         | Goes in                                         |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| What holds ports 80 and 443 on the node today (APISIX needs them) | `kubectl get pods -A -o wide \| grep -i -E 'ingress\|nginx\|traefik'` | section 4 |
| Private address of each app node, reachable from the gateway cluster | the cloud console | `--set "web.externalHosts={...}"` (section 5) |
| Browser origins of the grievance UI | ask the UI team | `corsOriginRegexes`, `realtimeAllowedOrigins` |

The upstream names, node ports and the Redis for rate-limit counters are already in
`oan-grievance-gateway.yaml`. The node ports belong to `gatewayAccess` of the
`grievance` release of `charts/oan-grievance-service`.

Confirm that the cluster has no APISIX CRDs from another install:

```sh
kubectl get crd | grep apisix.apache.org || echo "none (expected on a fresh cluster)"
kubectl get ingressclass
```

## 3. Secrets and values

The chart creates the Admin API Secret `apisix-admin-credentials` (keys `admin` and `viewer`) with random
values on the first install and keeps it across upgrades. To provide your own, set `adminCredentials.create`
to `false`, or create the Secret before the first install (a Secret the chart does not own is left alone).
Create any other secrets outside Git, with random values (for example `openssl rand -hex 16`).

```sh
kubectl create namespace api6-gateway
# Only to provide the keys yourself:
kubectl -n api6-gateway create secret generic apisix-admin-credentials \
  --from-literal=admin="$(openssl rand -hex 16)" \
  --from-literal=viewer="$(openssl rand -hex 16)"
```

Keep the `admin` value in the team's secret manager. It is the gateway's Admin API key.

APISIX keeps its routes in an etcd outside the release (section 10). Create its
password Secret before the install, and have the etcd members running:

```sh
kubectl -n api6-gateway create secret generic apisix-etcd-credentials \
  --from-literal=etcd-root-password="$(openssl rand -hex 16)"
```

Then edit the values, in a branch of this repo, and get the change reviewed:

- `environments/dev/values/oan-grievance-gateway.yaml`: the origin lists. `siteName`,
  `hosts`, the upstream names and ports, and `tls.secretName` are already
  set. A missing required value stops `helm install` with "`<name>` is required".
- The certificate: Secret `oan-grievance-tls` in `grievance` (see
  [grievance-service.md](grievance-service.md), section 2, step 9).

## 4. Install the gateway

```sh
# Read the plan first.
helm template apisix charts/oan-apisix-gateway -n api6-gateway \
  --set 'apisix.externalEtcd.host={http://<m1>:2379,http://<m2>:2379,http://<m3>:2379}' | less

helm upgrade --install apisix charts/oan-apisix-gateway -n api6-gateway \
  --set 'apisix.externalEtcd.host={http://<m1>:2379,http://<m2>:2379,http://<m3>:2379}' \
  --wait --timeout 10m
```

The same release installs the Redis for rate-limit counters (the `redis` key of the
chart's `values.yaml`); its Service is `apisix-redis-master`.

The release name must be `apisix`: the Ingress Controller values point at the Service
`apisix-admin` that this name produces.

the chart's `values.yaml` binds the node's ports 80 and 443 (hostPort). While another Pod holds
them, the APISIX Pod stays `Pending`: turn off `rke2-ingress-nginx` first
([grievance-service.md](grievance-service.md), section 2, step 2).

Check:

```sh
kubectl -n api6-gateway get pods                       # apisix, etcd, apisix-ingress-controller, apisix-redis: Running
kubectl -n api6-gateway get svc                        # apisix-gateway, apisix-admin, apisix-prometheus-metrics
kubectl get ingressclass apisix
kubectl -n api6-gateway get gatewayproxy               # apisix-config
kubectl get crd | grep apisix.apache.org         # apisixroutes, apisixupstreams, apisixconsumers ...
kubectl get crd apisixroutes.apisix.apache.org -o jsonpath='{.spec.versions[*].name}'   # includes v2
kubectl -n api6-gateway logs deploy/apisix-ingress-controller | tail -20   # no "unauthorized" or "connection refused"
```

If the controller cannot reach the Admin API, check that `apisix-admin-credentials`
exists and that `allow.ipList` plus `ingressControllerExtraIpList` (the private address
ranges) admit the controller Pod.

## 5. Install the grievance routes

Use the chart from the `oan_grievance_service` checkout at the **commit that is deployed**
(`git log -1` on the deployed branch), so routes match the running code.

```sh
CHART=<path to oan_grievance_service>/apisix/k8s
VALUES=environments/dev/values/oan-grievance-gateway.yaml

APP_HOST=<grievance node private IP>
SET="--set web.externalHosts={$APP_HOST} --set socket.externalHosts={$APP_HOST}"

helm lint "$CHART" -f environments/dev/values/gateway-common.yaml -f "$VALUES" $SET
helm template oan-grievance-gateway "$CHART" -n grievance -f environments/dev/values/gateway-common.yaml -f "$VALUES" $SET | less   # read it

helm upgrade --install oan-grievance-gateway "$CHART" -n grievance -f environments/dev/values/gateway-common.yaml -f "$VALUES" $SET --atomic --wait
```

Check that the controller synced the routes:

```sh
kubectl -n grievance get apisixroute,apisixupstream
kubectl -n grievance describe apisixroute oan-grievance-service-v1 | tail -20   # status Accepted/Synced, no errors
kubectl -n api6-gateway logs deploy/apisix-ingress-controller | grep -i -E 'error|fail' | tail
```

### Test through the gateway

Reach the gateway Service directly with a port-forward, so the tests do not depend on
DNS or the certificate. The `Host` header must be the public host.

```sh
kubectl -n api6-gateway port-forward svc/apisix-gateway 9080:80 &
H='Host: grievance-backend.development.oanstaging.com'

# 1. Health: 200, with an X-Request-Id header.
curl -si -H "$H" http://localhost:9080/v1/grievances/health | head -20

# 2. A route that does not exist: 404 from the gateway, not Frappe.
curl -si -H "$H" http://localhost:9080/v1/does-not-exist | head -5

# 3. CORS preflight from an allowed origin: 200/204 with access-control-allow-origin.
curl -si -X OPTIONS -H "$H" -H 'Origin: http://localhost:3000' \
  -H 'Access-Control-Request-Method: GET' http://localhost:9080/v1/grievances | head -12

# 4. Rate limit: public-read tier is 120/min per client address; expect 429 after that.
for i in $(seq 1 130); do curl -s -o /dev/null -w '%{http_code}\n' -H "$H" \
  http://localhost:9080/v1/auth/health; done | sort | uniq -c

# 5. Auth through the gateway (oan_auth_service endpoints are in this chart).
curl -si -H "$H" -H 'Content-Type: application/json' \
  -d '{"identifier":"<test user>","password":"<password>"}' http://localhost:9080/v1/auth/login | head -5

# 6. Metrics.
kubectl -n api6-gateway port-forward svc/apisix-prometheus-metrics 9091:9091 &
curl -s http://localhost:9091/apisix/prometheus/metrics | grep -c apisix_http_status
```

Also test socket.io from a browser or `wscat` with a valid session (see Known open items).
If any test fails, stop here and fix it before using the public host.

## 6. Public traffic

Dev is built fresh, so there is no traffic to move: once APISIX holds ports 80 and 443,
the grievance host is served by it. Run the checks from section 5 against
`https://grievance-backend.development.oanstaging.com`, using `/v1/grievances/health` for health,
not `/api/method/ping` (see Known open items). Watch for a few minutes:
`kubectl -n api6-gateway logs deploy/apisix -f`, and the `apisix_http_status` metrics (look
for 5xx and 429).

## 7. After every later merge

The routes are generated from the service's OpenAPI spec, so they change whenever an
endpoint or tier changes. The order matters.

1. Merge the app PR. Its "OpenAPI and APISIX in sync" check guarantees `apisix/k8s` matches the code.
2. Deploy the new app image (Jenkins).
3. Run `helm upgrade` for `oan-grievance-gateway` in the gateway cluster, from the checkout
   at the deployed commit (section 5), with `--atomic --wait`.
4. Run the smoke checks from section 5 (health plus one route that changed).
5. On failure: `helm -n grievance rollback oan-grievance-gateway`.

Changes to the values in this repo (hosts, Service names, origins) need only step 3 and
the checks. Changes to the chart's `values.yaml` need `helm upgrade apisix ...` first.

## 8. A2C

A2C runs in an app cluster of its own and uses this gateway. Its install, secrets and
local setup are in [a2c.md](a2c.md). Its routes install into the gateway cluster,
namespace `a2c`, from the `oan_a2c` checkout at the deployed commit:

```sh
helm upgrade --install oan-a2c-gateway <oan_a2c>/apisix/k8s -n a2c --create-namespace \
  -f environments/dev/values/gateway-common.yaml -f environments/dev/values/oan-a2c-gateway.yaml \
  --set "web.externalHosts={<A2C node private IP>}" --atomic --wait
```

`hosts` is set in `oan-a2c-gateway.yaml` (confirm the real name): routes of both apps
share paths such as `/v1/auth/*`, and an empty `hosts` would match any host. Expose A2C's
Frappe web Service on node port 30810 to the gateway cluster only, and point the A2C
host's DNS at the gateway node.

A2C needs secrets that grievance does not, all provisioned outside Git:

- One Secret per partner and dashboard consumer in namespace `a2c`, named after the
  consumer, with key `key`: `a2c-openg2p-consent-webhook`, `a2c-oan-dashboards`.
- `A2C_FRAPPE_SERVICE_AUTHORIZATION` (`token <api_key>:<api_secret>` of the Frappe service
  user) in the APISIX pods' environment, in the gateway cluster. Partner routes reference it as
  `$env://A2C_FRAPPE_SERVICE_AUTHORIZATION`. the chart's `values.yaml` reads it from the optional Secret
  `a2c-frappe-service-credential` (key `authorization`) in namespace `api6-gateway`.

### Consumers shared by several apps

The telco IVR vendor calls A2C lead creation and the grievance IVR webhook with one key.
Its consumer, `oan-ivr-vendor`, belongs to neither app chart: the APISIX release creates it
(`extraDeploy` in the chart's `values.yaml`), so the controller names it `apisix_oan-ivr-vendor`. Both
app charts whitelist that name through `sharedConsumerNamespace: api6-gateway` in their values.
Each app's route still calls Frappe with its own credential, from the APISIX environment:
`A2C_FRAPPE_SERVICE_AUTHORIZATION` and `OAN_GRIEVANCE_IVR_FRAPPE_AUTHORIZATION`.

```sh
kubectl -n api6-gateway create secret generic oan-ivr-vendor --from-literal=key='<vendor key>'
kubectl -n api6-gateway create secret generic oan-grievance-ivr-frappe-credential \
  --from-literal=authorization='token <api_key>:<api_secret>'
```

To keep the vendor's current key, create `oan-ivr-vendor` with the value of the old
`a2c-telco-ivr-lead-gateway` Secret. Then upgrade the APISIX release and `oan-a2c-gateway`
back to back. Between the two upgrades both consumers hold the key, APISIX matches either,
and the old A2C chart accepts only the old one, so some IVR calls to A2C get 403 for that
moment. Delete the old Secret once the A2C chart no longer creates its consumer.

## 8b. Partner APIs (OAN sandbox)

Partners call OAN APIs with apps they create in the OAN sandbox: the Consent Manager, the
Partner Management key fetch API and the Aggregation Layer. Only what partners call is
routed: staff use their own portals, so no staff API (the registries' staff APIs, the
Partner Management admin API, the Consent Manager staff routes) is on this gateway. The
sandbox runs with `GATEWAY_PARTNER_AUTH=oauth`:

```
partner -> POST https://keycloak.development.oanstaging.com/realms/partner/protocol/openid-connect/token
           grant_type=client_credentials, client_id=<API key>, client_secret=<API secret>
        <- access token (claims participant_uid, oan_app, oan_environments, oan_routes)
partner -> https://<partner host>/consent-manager/... with header X-Partner-Token: <token>
        -> APISIX: openid-connect (realm JWKS, iss, exp), role `uat` in oan_environments,
           this route's id in oan_routes, limit-count per app -> Consent Manager
```

The routes are the chart `oan-partner-gateway` (sandbox-platform
`deploy/apisix-partner-gateway/k8s`), and an `ApisixTls` for the partner host. `hosts` is
required. Values: [dev/values/oan-partner-gateway.yaml](../environments/dev/values/oan-partner-gateway.yaml).

Each API is switched on by its own value and has three resources:

| Resource | Holds | Gateway path |
|---|---|---|
| `ApisixUpstream` | the API's public host (`externalNodes`, https) | |
| `ApisixPluginConfig` | the plugins every route of the API shares: the token check (`serverless-pre-function`, `openid-connect`, `serverless-post-function`), the path rewrite, `limit-count` and the call log | |
| `ApisixRoute` | one rule per operation, pointing at the plugin config (`plugin_config_name`); a plugin of its own only where it differs | |

| Value | API | Gateway path |
|---|---|---|
| `consentManager.portalApi` | Consent Manager partner portal API (the console host, `/consent/v1/partner-portal` only) | `/consent-manager/...` |
| `consentManager.partnerApi` | Consent Manager partner API (validate, status, receipts, JWKS) | `/consent-manager-partner/...` |
| `partnerManagement.keysApi` | Partner Management key fetch API | `/partner-management-keys/...` |
| `aggregationLayer` | Aggregation Layer (DCI search) | `/aggregation-layer/...` |

The prefix is removed before the call. `Authorization` is the API's own credential (the
partner's token, where the API asks for one) and is passed on untouched; the app token
travels only in `X-Partner-Token`.

**Not checked on a cluster:** that the Ingress Controller of this gateway resolves
`plugin_config_name`. Check after the install (step 4). If the token check does not apply,
set `inlineSharedPlugins: true`: the routes then carry a copy of the shared plugins, the
shape the chart had before.

What the sandbox does on the gateway: it **only reads** the routes through the Admin API
(`GATEWAY_ADMIN_URL`, key `GATEWAY_ADMIN_TOKEN`; the **viewer** key is enough). Their ids go
into the tokens' `oan_routes`. In oauth mode it writes nothing to the gateway (no consumers
or credentials): each app key is a Keycloak client instead, and the routes check the
token. So the Ingress Controller stays the only writer, as section 10 requires.

Install, in order:

1. **Partner host.** **Confirm** the name (values use `partner-api-dev.oanstaging.com`).
   DNS to the gateway node, and a certificate in Secret `oan-partner-gateway-tls`
   (`tls.crt`, `tls.key`) in namespace `api6-gateway`, as for grievance (section 11).
2. **Routes.** From a sandbox-platform checkout at the deployed commit:

```bash
helm upgrade --install oan-partner-gateway deploy/apisix-partner-gateway/k8s   -n api6-gateway -f <oan-helm>/environments/dev/values/gateway-common.yaml -f <oan-helm>/environments/dev/values/oan-partner-gateway.yaml
kubectl -n api6-gateway get apisixroutes,apisixupstreams,apisixtls -l app=oan-partner-gateway
```

3. **Admin API for the sandbox.** The sandbox runs in the OpenG2P dev cluster. The Admin
   API in the chart's `values.yaml` is a ClusterIP Service (`apisix-admin:9180`) that admits
   `10.0.0.0/8`, so the sandbox cannot reach it from another cluster. **Confirm** one way
   in: an Admin API route on a host with `ip-restriction` to the sandbox cluster's egress
   IP (the live dev gateway has `apisix-admin.oanstaging.com` this way), or a private
   network path. Then the sandbox's `config.gateway.sync.adminUrl` and the viewer key.
4. **Check, before telling partners:**

```bash
H=https://partner-api-dev.oanstaging.com
# No token: 401 {"message":"Missing app token (X-Partner-Token)"} from the gateway
curl -s $H/consent-manager-partner/ping
# A user's or a foreign realm's token: 401. An app token without this route: 403.
# An app token from the sandbox (try-it page "Get token"): passes the gateway (the API answers "pong").
```

The sandbox's own check: sign up and approve a participant, create and approve an app,
**Get token** on the try-it page, then **Run**: the call passes the gateway.

Rate limits count per app (`X-OAN-App`, set from the token) in the Redis at `redis.host`.

There are no consumers: what an app's consumer would hold travels in its token. The
sandbox writes the app's IP whitelist (`oan_ips`) and the limits of its API products
(`oan_limit_minute`, `oan_limit_day`; sandbox `config.gateway.rateLimit.enabled`) on the
app's Keycloak client, and the shared plugins check them: another caller address gets
`403`, a call over the limit `429`. The app's limits count per API, and a change applies
from the next token (five minutes at most). The caller address is the one APISIX sees
(section 9, "Real client IP").

### Call log (API history of direct calls)

With `callLog.enabled`, the shared plugin config carries `http-logger`: APISIX posts a
record of every call to the sandbox (`POST /oan/internal/gateway/logs`), and the sandbox
shows the calls of its apps in API history with source **Direct**. Three parts, all needed:

| Part | Where | What |
|---|---|---|
| The record format | `oan-apisix-gateway`, `gatewayProxy.pluginMetadata.http-logger` (already in the chart's `values.yaml`) | names the app (`app` = `X-OAN-App`); no credential header |
| The token | Secret `oan-sandbox-log-ingest-credential` in namespace `api6-gateway`, key `authorization`, value `Bearer <token>`; the APISIX pods get it as `OAN_SANDBOX_LOG_INGEST_AUTHORIZATION` and the plugin reads it at run time (`$env://`), so it is never written into a route | the sandbox's `GATEWAY_LOG_INGEST_TOKEN` |
| The switch | `callLog.enabled: true`, `callLog.url` in the partner values; in the sandbox `config.gateway.logIngest.enabled: true` | the URL is the sandbox API as APISIX reaches it |

```sh
kubectl -n api6-gateway create secret generic oan-sandbox-log-ingest-credential \
  --from-literal=authorization="Bearer <GATEWAY_LOG_INGEST_TOKEN>"
kubectl -n api6-gateway rollout restart deploy/apisix     # the pods read the Secret at start
```

A call the gateway refuses before it knows the app (no token, a bad token) is not stored;
a `403` (no API product for the route) and a `429` are. Check: one call with an app token,
then the sandbox access log shows `POST /oan/internal/gateway/logs -> 200`
(`401` = the token in the Secret differs, `404` = the sandbox has the callback off).

## 8c. A new gateway: UAT and production

UAT and production are two gateways, each with its own Keycloak. Each gets the same
installs, with its own values; nothing is copied by hand into APISIX.

1. **APISIX**: sections 2 to 4 (`oan-apisix-gateway`, release `apisix`). The global rules
   and the `http-logger` record format come with it.
2. **Values**: copy
   [examples/gateway/oan-partner-gateway.uat.yaml](../examples/gateway/oan-partner-gateway.uat.yaml)
   (or `.production.yaml`) to `environments/<env>/values/oan-partner-gateway.yaml` and fill
   in the hosts. `keycloak.issuer` is that environment's realm, exactly as in the tokens'
   `iss`; `environmentRole` is `uat` or `production`, so a UAT app's token is refused on
   the production gateway and the other way round.
3. **Secrets** in namespace `api6-gateway`: `oan-partner-gateway-tls` (the partner host's
   certificate) and, for the call log, `oan-sandbox-log-ingest-credential`.
4. **Routes**: section 8b, step 2, with that environment's values files.
5. **The sandbox** (one portal for both environments): UAT uses its main settings
   (`config.keycloak.url`, `config.gateway.uatUrl`, `config.gateway.sync.adminUrl`).
   Production has its own: `GATEWAY_PROD_URL`, `GATEWAY_PROD_ADMIN_URL` / `_TOKEN` (viewer
   key), `KEYCLOAK_PROD_URL`, `KEYCLOAK_PROD_PUBLIC_URL`, `KEYCLOAK_PROD_ADMIN_CLIENT_SECRET`
   (sandbox-platform `DEPLOYMENT.md`, "UAT and production apps").
6. **Keycloak** of that environment: realm `partner` with `oan-sandbox-provisioner`
   (sandbox-platform `backend/scripts/keycloak/setup_partner_realm.py`).
7. **Check**: section 8b, step 4, on that environment's host.

A new API: add it to the route generator in sandbox-platform (it regenerates the chart),
merge, then `helm upgrade` the routes release and switch the API on in the values.

## 9. Known open items

- **Values to fill:** the UI origins for CORS and socket.io cookies (still the
  localhost defaults). For A2C: public host, site name, its node's private address and
  port, and partner egress CIDRs.
- **Gateway cluster.** Not provisioned yet: its public IP (DNS for every app host), and
  a private network shared with each app cluster. The hop to the app node ports is plain
  HTTP; without a private network it needs a VPN or TLS on that hop.
- **Several nodes per app.** `web.externalHosts` takes one address per node. Adding or
  removing a node is an edit to that list and a `helm upgrade` of the routes release.
  Rendered, and accepted by a server-side dry run against the controller's CRD; not
  tried with real traffic. If nodes change often, put an internal load balancer in front
  of the node ports (`gatewayAccess.type: LoadBalancer`) and list its address once.
- **socket.io `Origin`.** The socket routes set `Origin: http://<siteName>:8000`. The socket.io
  server calls Frappe back at that address, and Frappe also requires `Origin` and `Host` to
  name the same host. `grievance-backend.development.oanstaging.com` is the public name, and
  may not resolve from the socket.io Pod, so socket authentication may fail. Test a socket connection in section 5. If it fails, the
  fix is to make the origin a chart value (`frappeWebOrigin`) and make that host resolvable
  from the socket.io Pod (for example `hostAliases` or a CoreDNS entry). Not done yet.
- **`/api/...` paths.** Clients use `/v1/...`, which the gateway rewrites to `/api/v1/...`.
  `/api/...` is intentionally not routed, so Jenkins' verify URL (`/api/method/ping`) would
  return 404 through the gateway. Use `/v1/grievances/health`, or keep a separate path to Frappe
  for ops checks.
- **Frappe `Host` handling.** The gateway rewrites `Host` to the site name
  (`grievance-backend.development.oanstaging.com`). Confirm Frappe answers for that site through the gateway
  (section 5, check 1).
- **Real client IP.** Rate limits are per client address, taken from the connection
  (no proxy in front, no `X-Real-IP` trusted). This holds only if the gateway node keeps
  the source address of hostPort traffic. Check the APISIX access log on the first requests. On a
  local OrbStack cluster it does not hold: every request shows the Pod gateway.
- **HTTP to HTTPS redirect.** Port 80 still serves the routes over plain HTTP. Once the
  first certificate is issued, add a `redirect` global rule (`http_to_https: true`) in
  the chart's `values.yaml`. Before the first issuance it would break the HTTP-01 challenge, since
  APISIX has no certificate to answer HTTPS with yet.
- **ADC and APISIX 3.19.** The Ingress Controller uses ADC internally, and ADC's documented
  support stops at APISIX 3.17. Watch the controller logs on the first sync.
- **Partner APIs:** the partner host name, DNS and certificate; how the sandbox reaches
  the Admin API (read only) from the OpenG2P cluster (section 8b). `plugin_config_name`
  and `gatewayProxy.pluginMetadata` are rendered but not tried on a cluster.
- **etcd.** the chart's `values.yaml` uses `externalEtcd`; see section 10. Not yet installed against
  a real etcd.
- **Global plugins.** Confirm `request-id` and `prometheus` take effect: `X-Request-Id` in
  responses and the `apisix_http_status` metric.

## 10. etcd

APISIX keeps its routes, upstreams and certificates in etcd. The Ingress Controller does
not write to etcd: it translates the `Apisix*` resources (through ADC, which runs inside
the controller Pod) and pushes them to APISIX's Admin API (`apisix-admin`, port 9180),
and APISIX stores them. The controller is the source of truth, so a lost etcd is rebuilt
from the resources at the next sync (not tried here). Never edit the gateway by hand with
the Admin API or `adc sync`.

the chart's `values.yaml` sets `etcd.enabled: false` and `externalEtcd`, the same shape in every
environment:

| | Value |
|---|---|
| Members | three, each on its own machine, in different availability zones. The members vote, and a change counts only when a majority agrees, so one can fail. Three services on one machine would fail together. |
| URLs | `--set 'apisix.externalEtcd.host={...}'` at install. Use `https` when TLS is on. |
| Authentication | `externalEtcd.user: root`, password in Secret `apisix-etcd-credentials`, key `etcd-root-password`. |
| Storage | fast local SSD, never NFS or EFS. |
| Ports | 2379 (clients) from the APISIX nodes only, 2380 (peers) between the members only. |
| Backup | scheduled `etcdctl snapshot save`, copied off the machine. Not set up. |

The chart's built-in etcd is a single member and is for development only. In the lab,
run the three members as separate processes on one VM with different ports
(`homelab-fedora-rke2.local.md`). That tests the configuration and one member failing,
not a machine failing. RKE2 runs its own etcd on 2379 to 2381, so use other ports there.
Never point APISIX at the cluster's own etcd: it holds every Secret.

Who runs the production members, on which machines, and where snapshots go is not
decided. Dedicated small servers are cleaner than one member on each gateway node, where
a node failure takes an APISIX Pod and a member together.

Not checked: that chart `apisix/apisix` 2.18.2 and controller 1.3.0 run cleanly against
a three-member external etcd. `helm template` renders the three URLs into APISIX's
configuration.

## 11. TLS

There are four separate jobs. None is automated by this repository.

| Job | Today | In production |
|---|---|---|
| Public certificate, clients to APISIX | Secret `oan-grievance-tls` (and `oan-a2c-tls`), referenced by `ApisixTls`. Lab: a local CA, made by hand. The dev values say cert-manager writes the Secret in dev; that is not in this repository and I have not seen it. | Whoever issues the certificate (an ACME service such as Let's Encrypt, a company CA, or a bought certificate) writes the Secret before it expires, and the controller syncs the new one into APISIX without a restart. Let's Encrypt certificates last 90 days, so renewal must be automatic. Expiry needs an alert. |
| APISIX to the apps, port 30800, 30900, 30810 | Plain HTTP over a private network, node ports open to the gateway's addresses only | Same, if the network is private. If this hop must be encrypted, it needs certificates from an internal CA on both sides (mutual TLS). Not set up, and not yet required by anyone I know of. |
| APISIX to etcd | Plain HTTP in the lab | `https` URLs with certificates from an internal CA, reissued on a schedule. |
| Kubernetes internals (RKE2) | RKE2 creates and rotates them itself. As I recall they last a year and rotate when the server restarts near expiry; I have not checked the current numbers. | Same. |

Open questions for the platform owners: who issues the public certificate in dev and
production, who owns renewal and the expiry alert, and whether the hop to the apps must
be encrypted. No certificate manager is added to `oan-helm` until that is decided and
the first releases of grievance and A2C are in place.
