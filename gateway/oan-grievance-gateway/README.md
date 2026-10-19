# oan-grievance-gateway

`ApisixRoute` and `ApisixUpstream` resources that expose the OAN Grievance Service through
the APISIX Ingress Controller. See [the APISIX gateway guide](../../docs/apisix-gateway.md).

`templates/` is generated in
[oan_grievance_service](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/tree/develop/apisix/k8s)
from its OpenAPI spec. Do not edit it here. When the service's routes change, copy
`apisix/k8s/*.yaml` from the matching service release into `templates/` and bump `version`.
Only `Chart.yaml` and `values.yaml` are maintained here.
