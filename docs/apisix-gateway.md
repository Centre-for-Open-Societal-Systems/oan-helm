# APISIX gateway

The OAN API gateway is Apache APISIX, configured through the APISIX Ingress Controller.
No cluster deployment has been performed.

The grievance service runs on its own RKE2 cluster (`13.233.56.204`), separate from the
OpenG2P dev cluster (`server` in `environments/dev/endpoints.yaml`, `13.201.58.55`). Its
gateway values sit with the other dev values in `environments/dev/values/`, and each file
names its target cluster in its header. Never install them into the OpenG2P cluster.

| Part | Source | Values |
| --- | --- | --- |
| APISIX and the Ingress Controller | Upstream chart `apisix/apisix` 2.18.2 (bundles `apisix-ingress-controller`) from `https://apache.github.io/apisix-helm-chart`. It is not vendored, repackaged or added to `releases/` | [dev/values/apisix.yaml](../environments/dev/values/apisix.yaml) |
| Grievance routes | Chart `oan-grievance-gateway` in [oan_grievance_service/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/tree/develop/apisix/k8s), generated from the service's OpenAPI spec. It is not copied here | [dev/values/oan-grievance-gateway.yaml](../environments/dev/values/oan-grievance-gateway.yaml) |
| A2C routes | Chart `oan-a2c-gateway` in [oan_a2c/apisix/k8s](https://github.com/Centre-for-Open-Societal-Systems/oan_a2c/tree/develop/apisix/k8s), generated from the A2C OpenAPI spec | [dev/values/oan-a2c-gateway.yaml](../environments/dev/values/oan-a2c-gateway.yaml) |

This repository holds only the values for both charts. The grievance service will get its
own chart repository and releases later; until then, install its chart from a checkout of
the service repository at the deployed commit.

## Traffic path

```
DNS grievance-backend-dev.oanstaging.com -> 13.233.56.204
  -> ingress-nginx (TLS, Let's Encrypt; unchanged)
  -> apisix-gateway Service (namespace apisix): routes, rate limits, CORS
  -> grievance Frappe Services (namespace develop)
```

ingress-nginx keeps the public ports and the certificate. Only its backend for the
grievance host changes, from the Frappe Service to APISIX.

## Prerequisites

- Namespace `apisix` with Secret `apisix-admin-credentials`, keys `admin` and `viewer`,
  provisioned through the environment's secret process. Never commit the keys.
- The confirmed Frappe Service names and a Redis in the grievance cluster, set in
  `oan-grievance-gateway.yaml`. `helm install` fails until they are set.

## Install

```sh
helm repo add apisix https://apache.github.io/apisix-helm-chart
helm upgrade --install apisix apisix/apisix --version 2.18.2 \
  -n apisix --create-namespace -f environments/dev/values/apisix.yaml

helm upgrade --install oan-grievance-gateway <oan_grievance_service>/apisix/k8s \
  -n develop -f environments/dev/values/oan-grievance-gateway.yaml
```

The release name `apisix` matters: the Ingress Controller values point at the
`apisix-admin` Service it creates.

## Cut over from ingress-nginx

An Ingress can only send traffic to a Service in its own namespace. So add an
ExternalName Service in `develop` that points at APISIX:

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

Then, in the existing grievance Ingress (kept outside this repository), change the
backend for `grievance-backend-dev.oanstaging.com` to `apisix-gateway:80`. Keep its TLS
and cert settings. To roll back, point the backend at the Frappe Service again.

Do not also run `adc sync` against this gateway. ADC and the Ingress Controller each
overwrite the other's routes.

## oan_auth_service

oan_auth_service is a library installed into each app's bench, not a service of its own,
so it has no chart or values here. Its endpoints (`/v1/auth/*`, `/v1/admin/*`,
`/v1/notifications/*`) are part of each app's chart, pointed at that app's Frappe.

## Gateway-wide plugins

`request-id` (`X-Request-Id`, echoed in the response) and `prometheus` are global rules,
set as `gatewayProxy.plugins` in `apisix.yaml`, so they apply to every app's routes. Metrics
are served on port 9091 at `/apisix/prometheus/metrics`; enable
`metrics.serviceMonitor` once a Prometheus Operator scrapes the cluster. Per-app plugins
(CORS, body size, rate limits, authentication) stay in each app's chart.

## A2C

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

## Open items

- Frappe web and socket.io Service names in `develop` (`kubectl get svc -n develop`).
- A2C: target cluster, public host, site name, Service name and partner egress CIDRs.
- A Redis for rate-limit counters in the grievance cluster.
- Grievance UI origins for CORS and socket.io cookies. They are still the localhost defaults.
- Confirm the Pod CIDR in `apisix.nginx.http.realIpFrom`, and narrow
  `apisix.admin.allow.ingressControllerExtraIpList` to it.
- Built-in etcd is for development only. Use `externalEtcd` beyond dev.
