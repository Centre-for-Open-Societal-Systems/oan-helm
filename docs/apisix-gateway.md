# APISIX gateway

The OAN API gateway is Apache APISIX, configured through the APISIX Ingress Controller.
This document is the design and the DevOps runbook for the development cluster.

**Status:** nothing here has been run against a cluster yet. Where a step depends on
something we could not confirm, it says **Confirm** and tells you how to check.

The grievance service runs on its own RKE2 cluster (`13.233.56.204`), separate from the
OpenG2P dev cluster (`server` in `environments/dev/endpoints.yaml`, `13.201.58.55`). Its
gateway values sit with the other dev values in `environments/dev/values/`, and each file
names its target cluster in its header. **Never install them into the OpenG2P cluster.**

## 1. Design

### What lives where

| Part                              | Source                                                                                                                                                                                                                                   | Values                                                                                         |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| APISIX and the Ingress Controller | Upstream chart `apisix/apisix` 2.18.2 (bundles `apisix-ingress-controller`) from `https://apache.github.io/apisix-helm-chart`. It is not vendored, repackaged or added to `releases/`                                                    | [dev/values/apisix.yaml](../environments/dev/values/apisix.yaml)                               |
| Grievance routes                  | Chart `oan-grievance-gateway` in [oan_grievance_service/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/tree/develop/apisix/k8s), generated from the service's OpenAPI spec. It is not copied here | [dev/values/oan-grievance-gateway.yaml](../environments/dev/values/oan-grievance-gateway.yaml) |
| A2C routes                        | Chart `oan-a2c-gateway` in [oan_a2c/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/tree/develop/apisix/k8s), generated from the A2C OpenAPI spec                                                                | [dev/values/oan-a2c-gateway.yaml](../environments/dev/values/oan-a2c-gateway.yaml)             |

This repository holds only the values. Each app's route chart lives with the app, because
the routes come from the app's OpenAPI spec and must change in the same PR as the code.
The grievance service will get its own chart repository and releases later; until then,
install its chart from a checkout of the service repository at the deployed commit.

oan_auth_service is a library installed into each app's bench, not a service of its own,
so it has no chart or values. Its endpoints (`/v1/auth/*`, `/v1/admin/*`,
`/v1/notifications/*`) are part of each app's chart, pointed at that app's Frappe.

Do not also run `adc sync` against this gateway. ADC and the Ingress Controller each
overwrite the other's routes.

### Traffic path

```
browser -> DNS grievance-backend-dev.oanstaging.com -> 13.233.56.204
        -> ingress-nginx (TLS, Let's Encrypt)            unchanged
        -> Service apisix-gateway (ns apisix)            NEW: routes, rate limits, CORS, metrics
        -> Frappe Services in ns develop (web, socket.io)
```

ingress-nginx keeps the public ports and the certificate. Only its backend for the
grievance host changes, from the Frappe Service to APISIX.

### Gateway-wide plugins

`request-id` (`X-Request-Id`, echoed in the response) and `prometheus` are global rules,
set as `gatewayProxy.plugins` in `apisix.yaml`, so they apply to every app's routes. Metrics
are served on port 9091 at `/apisix/prometheus/metrics`; enable
`metrics.serviceMonitor` once a Prometheus Operator scrapes the cluster. Per-app plugins
(CORS, body size, rate limits, authentication) stay in each app's chart.

## 2. Prerequisites

Run these from a machine with `kubectl` and `helm` (3.x) pointed at the grievance cluster.

```sh
kubectl config current-context        # must be the grievance cluster, not OpenG2P
kubectl get nodes -o wide             # expect the node 13.233.56.204
helm version --short
```

Collect these facts first. They are the values the install needs.

| Fact                                                                                                             | How to get it                                                                         | Goes in                                         |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Frappe web Service name and port (the Service in front of the `backend` Deployment, or the frappe nginx Service) | `kubectl get svc -n develop`                                                          | `web.serviceName`, `web.port`                   |
| socket.io Service name and port                                                                                  | same command                                                                          | `socket.serviceName`, `socket.port`             |
| A Redis reachable from the `apisix` namespace, for rate-limit counters                                           | `kubectl get svc -A \| grep -i redis`                                                 | `redis.host`                                    |
| Pod CIDR                                                                                                         | `kubectl cluster-info dump \| grep -m1 cluster-cidr` (RKE2 default is `10.42.0.0/16`) | `apisix.nginx.http.realIpFrom` in `apisix.yaml` |
| Which Ingress serves the grievance host today                                                                    | `kubectl get ingress -A \| grep grievance`                                            | section 6                                       |
| Ingress class and controller                                                                                     | `kubectl get pods -A \| grep -i ingress`                                              | section 6                                       |
| Browser origins of the grievance UI                                                                              | ask the UI team                                                                       | `corsOriginRegexes`, `realtimeAllowedOrigins`   |

Confirm that the cluster has no APISIX CRDs from another install:

```sh
kubectl get crd | grep apisix.apache.org || echo "none (expected on a fresh cluster)"
kubectl get ingressclass
```

## 3. Secrets and values

Create the secrets outside Git. Use random values (for example `openssl rand -hex 16`).

```sh
kubectl create namespace apisix
kubectl -n apisix create secret generic apisix-admin-credentials \
  --from-literal=admin="$(openssl rand -hex 16)" \
  --from-literal=viewer="$(openssl rand -hex 16)"
```

Keep the `admin` value in the team's secret manager. It is the gateway's Admin API key.

Then edit the values, in a branch of this repo, and get the change reviewed:

- `environments/dev/values/oan-grievance-gateway.yaml`: `web.serviceName`, `socket.serviceName`,
  `redis.host`, and the origin lists. `siteName` and `hosts` are already set from the
  service's Jenkinsfile. A missing required value stops `helm install` with
  "`<name>` is required".
- `environments/dev/values/apisix.yaml`: confirm the Pod CIDR in `realIpFrom`, and later
  narrow `ingressControllerExtraIpList` from `0.0.0.0/0` to the Pod CIDR.

## 4. Install the gateway

```sh
helm repo add apisix https://apache.github.io/apisix-helm-chart && helm repo update

# Read the plan first.
helm template apisix apisix/apisix --version 2.18.2 -n apisix \
  -f environments/dev/values/apisix.yaml | less

helm upgrade --install apisix apisix/apisix --version 2.18.2 -n apisix \
  -f environments/dev/values/apisix.yaml --wait --timeout 10m
```

The release name must be `apisix`: the Ingress Controller values point at the Service
`apisix-admin` that this name produces.

Check:

```sh
kubectl -n apisix get pods                       # apisix, etcd, apisix-ingress-controller: Running
kubectl -n apisix get svc                        # apisix-gateway, apisix-admin, apisix-prometheus-metrics
kubectl get ingressclass apisix
kubectl -n apisix get gatewayproxy               # apisix-config
kubectl get crd | grep apisix.apache.org         # apisixroutes, apisixupstreams, apisixconsumers ...
kubectl get crd apisixroutes.apisix.apache.org -o jsonpath='{.spec.versions[*].name}'   # includes v2
kubectl -n apisix logs deploy/apisix-ingress-controller | tail -20   # no "unauthorized" or "connection refused"
```

If the controller cannot reach the Admin API, check that `apisix-admin-credentials`
exists and that `allow.ipList` plus `ingressControllerExtraIpList` admit the controller Pod.

## 5. Install the grievance routes

Use the chart from the `oan_grievance_service` checkout at the **commit that is deployed**
(`git log -1` on the deployed branch), so routes match the running code.

```sh
CHART=<path to oan_grievance_service>/apisix/k8s
VALUES=environments/dev/values/oan-grievance-gateway.yaml

helm lint "$CHART" -f "$VALUES"
helm template oan-grievance-gateway "$CHART" -n develop -f "$VALUES" | less   # read it

helm upgrade --install oan-grievance-gateway "$CHART" -n develop -f "$VALUES" --atomic --wait
```

Check that the controller synced the routes:

```sh
kubectl -n develop get apisixroute,apisixupstream
kubectl -n develop describe apisixroute oan-grievance-service-v1 | tail -20   # status Accepted/Synced, no errors
kubectl -n apisix logs deploy/apisix-ingress-controller | grep -i -E 'error|fail' | tail
```

### Test through the gateway, before any traffic moves

Reach the gateway Service directly with a port-forward. The `Host` header must be the
public host.

```sh
kubectl -n apisix port-forward svc/apisix-gateway 9080:80 &
H='Host: grievance-backend-dev.oanstaging.com'

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
kubectl -n apisix port-forward svc/apisix-prometheus-metrics 9091:9091 &
curl -s http://localhost:9091/apisix/prometheus/metrics | grep -c apisix_http_status
```

Also test socket.io from a browser or `wscat` with a valid session (see Known open items).
If any test fails, stop here. Nothing public has changed yet.

## 6. Move public traffic

Before this step, make sure the old path stays available for rollback.

1. Back up the current Ingress for the grievance host, outside the repo:
   `kubectl -n develop get ingress -o yaml > /tmp/grievance-ingress.backup.yaml`
2. Add an ExternalName Service in `develop`. An Ingress can only send traffic to a Service
   in its own namespace.

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: apisix-gateway
     namespace: develop
   spec:
     type: ExternalName
     externalName: apisix-gateway.apisix.svc.cluster.local
     ports:
       - port: 80
   ```

3. Edit the existing grievance Ingress (kept outside this repository) so the backend for
   `grievance-backend-dev.oanstaging.com` is Service `apisix-gateway`, port 80. Keep its TLS
   section and certificate settings. Leave the other hosts alone.
4. Run the checks from section 5 again against `https://grievance-backend-dev.oanstaging.com`.
   Use `/v1/grievances/health` for the health check, not `/api/method/ping` (see Known open items).
5. Watch for a few minutes: `kubectl -n apisix logs deploy/apisix -f`, and the
   `apisix_http_status` metrics (look for 5xx and 429).

### Rollback

```sh
kubectl apply -f /tmp/grievance-ingress.backup.yaml      # old backend returns at once
helm -n develop rollback oan-grievance-gateway           # only if the routes themselves are bad
```

The `apisix` release can stay installed while traffic goes back to the old path.

## 7. After every later merge

The routes are generated from the service's OpenAPI spec, so they change whenever an
endpoint or tier changes. The order matters.

1. Merge the app PR. Its "OpenAPI and APISIX in sync" check guarantees `apisix/k8s` matches the code.
2. Deploy the new app image (Jenkins).
3. Run `helm upgrade` for `oan-grievance-gateway` from the checkout at the deployed commit
   (section 5), with `--atomic --wait`.
4. Run the smoke checks from section 5 (health plus one route that changed).
5. On failure: `helm -n develop rollback oan-grievance-gateway`.

Changes to the values in this repo (hosts, Service names, origins) need only step 3 and
the checks. Changes to `apisix.yaml` need `helm upgrade apisix ...` first.

## 8. A2C

A2C has no Kubernetes target yet. Dev runs on docker-compose, and staging_ati runs through
oan-kustomize and ArgoCD. Once it has one, install APISIX there, or reuse a gateway that
can reach it. Then install `oan-a2c-gateway` next to the A2C Frappe Service.

A2C needs secrets that grievance does not, all provisioned outside Git:

- One Secret per partner and dashboard consumer in the chart's namespace, named after the
  consumer, with key `key`: `a2c-openg2p-consent-webhook`, `a2c-telco-ivr-lead-gateway`,
  `a2c-oan-dashboards`.
- `A2C_FRAPPE_SERVICE_AUTHORIZATION` (`token <api_key>:<api_secret>` of the Frappe service
  user) in the APISIX pods' environment. Partner routes reference it as
  `$env://A2C_FRAPPE_SERVICE_AUTHORIZATION`. In the `apisix` values:

```yaml
extraEnvVars:
  - name: A2C_FRAPPE_SERVICE_AUTHORIZATION
    valueFrom:
      secretKeyRef:
        name: a2c-frappe-service-credential
        key: authorization
```

## 9. Known open items

- **Values to fill:** Frappe web and socket.io Service names, a Redis in the grievance
  cluster, and the UI origins for CORS and socket.io cookies (still the localhost
  defaults). For A2C: target cluster, public host, site name, Service name and partner
  egress CIDRs.
- **socket.io `Origin`.** The socket routes set `Origin: http://<siteName>:8000`. The socket.io
  server calls Frappe back at that address, and Frappe also requires `Origin` and `Host` to
  name the same host. `develop.grievance.test` probably does not resolve inside the cluster,
  so socket authentication may fail. Test a socket connection in section 5. If it fails, the
  fix is to make the origin a chart value (`frappeWebOrigin`) and make that host resolvable
  from the socket.io Pod (for example `hostAliases` or a CoreDNS entry). Not done yet.
- **`/api/...` paths.** Clients use `/v1/...`, which the gateway rewrites to `/api/v1/...`.
  `/api/...` is intentionally not routed, so Jenkins' verify URL (`/api/method/ping`) would
  return 404 after cutover. Use `/v1/grievances/health`, or keep a separate path to Frappe
  for ops checks.
- **Frappe `Host` handling.** The gateway rewrites `Host` to the site name
  (`develop.grievance.test`). Confirm Frappe answers for that site through the gateway
  (section 5, check 1).
- **Real client IP.** Rate limits are per client address. They only work if ingress-nginx passes
  `X-Real-IP` and the Pod CIDR in `realIpFrom` is right. If all requests share one limit
  bucket, check this. Also narrow `apisix.admin.allow.ingressControllerExtraIpList`
  from `0.0.0.0/0` to the Pod CIDR.
- **ingress-nginx.** We inferred it from the bare-IP 404 page and the default fake
  certificate. Confirm with `kubectl get pods -A | grep ingress`.
- **ADC and APISIX 3.19.** The Ingress Controller uses ADC internally, and ADC's documented
  support stops at APISIX 3.17. Watch the controller logs on the first sync.
- **etcd.** The bundled etcd is for development. Use `externalEtcd` before production.
- **Global plugins.** Confirm `request-id` and `prometheus` take effect: `X-Request-Id` in
  responses and the `apisix_http_status` metric.
