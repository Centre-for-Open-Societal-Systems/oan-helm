# APISIX gateway

The OAN API gateway is Apache APISIX, configured through the APISIX Ingress Controller.
No cluster deployment has been performed.

| Part | Source | Values |
| --- | --- | --- |
| APISIX and the Ingress Controller | Upstream chart `apisix/apisix` 2.18.2 (bundles `apisix-ingress-controller`) from `https://apache.github.io/apisix-helm-chart`. It is not vendored, repackaged or added to `releases/` | [environments/dev/values/apisix.yaml](../environments/dev/values/apisix.yaml) |
| Grievance routes | [gateway/oan-grievance-gateway](../gateway/oan-grievance-gateway/), whose templates are generated in `oan_grievance_service/apisix/k8s` | [environments/dev/values/oan-grievance-gateway.yaml](../environments/dev/values/oan-grievance-gateway.yaml) |

The grievance chart sits under `gateway/`, not `charts/`, so it stays outside the five
packaged Rancher charts and `scripts/validate.py`. The grievance service will get its own
chart repository and releases later.

## Prerequisites

- Namespace `apisix` with Secret `apisix-admin-credentials`, keys `admin` and `viewer`,
  provisioned through the environment's secret process. Never commit the keys.
- The grievance Frappe web and socket.io Services, in the namespace the routes are installed in.
- Decide the north-south placement: behind the Istio ingress gateway, or the APISIX
  Service exposed directly. The dev values keep APISIX `ClusterIP` until then.

## Install

```sh
helm repo add apisix https://apache.github.io/apisix-helm-chart
helm upgrade --install apisix apisix/apisix --version 2.18.2 \
  -n apisix -f environments/dev/values/apisix.yaml

helm upgrade --install oan-grievance-gateway gateway/oan-grievance-gateway \
  -n <grievance namespace> -f environments/dev/values/oan-grievance-gateway.yaml \
  --set siteName=<frappe site name>
```

The release name `apisix` matters: the Ingress Controller values point at the
`apisix-admin` Service it creates.

Do not also run `adc sync` against this gateway. ADC and the Ingress Controller each
overwrite the other's routes.

## Open items

- Grievance public host, Frappe site name and Service names: set in
  `oan-grievance-gateway.yaml` once confirmed. Add the host to `environments/dev/endpoints.yaml` too.
- `apisix.admin.allow.ingressControllerExtraIpList`: narrow from `0.0.0.0/0` to the Pod CIDR.
- Built-in etcd is for development only. Use `externalEtcd` beyond dev.
