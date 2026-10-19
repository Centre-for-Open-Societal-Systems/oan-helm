# APISIX gateway

The OAN API gateway is Apache APISIX, configured through the APISIX Ingress Controller.
No cluster deployment has been performed.

The grievance service runs on its own RKE2 cluster (`13.233.56.204`), separate from the
OpenG2P dev cluster in `environments/dev` (`13.201.58.55`). Its values live in
[environments/grievance-dev](../environments/grievance-dev/). Never install them into the
OpenG2P cluster.

| Part | Source | Values |
| --- | --- | --- |
| APISIX and the Ingress Controller | Upstream chart `apisix/apisix` 2.18.2 (bundles `apisix-ingress-controller`) from `https://apache.github.io/apisix-helm-chart`. It is not vendored, repackaged or added to `releases/` | [grievance-dev/values/apisix.yaml](../environments/grievance-dev/values/apisix.yaml) |
| Grievance routes | [gateway/oan-grievance-gateway](../gateway/oan-grievance-gateway/), whose templates are generated in `oan_grievance_service/apisix/k8s` | [grievance-dev/values/oan-grievance-gateway.yaml](../environments/grievance-dev/values/oan-grievance-gateway.yaml) |

The grievance chart sits under `gateway/`, not `charts/`, so it stays outside the five
packaged Rancher charts and `scripts/validate.py`. The grievance service will get its own
chart repository and releases later.

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
  -n apisix --create-namespace -f environments/grievance-dev/values/apisix.yaml

helm upgrade --install oan-grievance-gateway gateway/oan-grievance-gateway \
  -n develop -f environments/grievance-dev/values/oan-grievance-gateway.yaml
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

## Open items

- Frappe web and socket.io Service names in `develop` (`kubectl get svc -n develop`).
- A Redis for rate-limit counters in the grievance cluster.
- Grievance UI origins for CORS and socket.io cookies. They are still the localhost defaults.
- Confirm the Pod CIDR in `apisix.nginx.http.realIpFrom`, and narrow
  `apisix.admin.allow.ingressControllerExtraIpList` to it.
- Built-in etcd is for development only. Use `externalEtcd` beyond dev.
