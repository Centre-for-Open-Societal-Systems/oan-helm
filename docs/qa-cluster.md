# QA cluster (`qa.oanstaging.com`)

One RKE2 node runs every OAN service in its own namespace, with the shared PostgreSQL and the UIs in the cluster:
the oan_dev layout. APISIX is the only edge, as on dev. This page installs the cluster-level releases, which need a
cluster admin; Jenkins then deploys the services from their repositories with the deployer installed here.
Values: `environments/qa/`.

Not installed yet. Every step below is the same command the automation in
[arnavam/oan-deployment](https://github.com/arnavam/oan-deployment) runs.

## Before

- An RKE2 node with the NFS CSI driver (StorageClass `nfs-csi`) and a `local-path` StorageClass for etcd.
- Nothing on the node's ports 80 and 443: no nginx, no istio, no other ingress controller.
- The wildcard certificate for `qa.oanstaging.com` and `*.qa.oanstaging.com` as TLS Secret
  `oan-qa-wildcard-tls` in namespace `api6-gateway`.
- A central OTel gateway the node can reach. Set it in `environments/qa/values/oan-logging.yaml`.

## Order

```sh
helm repo add oan-helm https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/
helm repo update oan-helm

# 1. Namespaces, Pod Security and NetworkPolicies. api6-gateway already exists (the certificate): adopt it first,
#    as the values file shows.
helm -n kube-system upgrade --install oan-namespace-guard oan-helm/oan-namespace-guard --devel \
  -f environments/qa/values/oan-namespace-guard.yaml

# 2. APISIX: its etcd, then the gateway with the wildcard certificate.
kubectl apply -f environments/qa/manifests/apisix-etcd.yaml
helm -n api6-gateway upgrade --install apisix oan-helm/oan-apisix-gateway --devel \
  -f environments/qa/values/oan-apisix-gateway.yaml

# 3. The shared PostgreSQL of the Frappe services.
helm -n frappe-common upgrade --install oan-frappe-common-db oan-helm/oan-frappe-common --devel \
  -f environments/qa/values/oan-frappe-common.yaml

# 4. The Jenkins deployer (docs/cluster-access.md).
helm -n a2c upgrade --install oan-cluster-access oan-helm/oan-cluster-access --devel \
  -f environments/qa/values/oan-cluster-access.yaml

# 5. The node log agent, shipping to the central Loki and Grafana (docs/logging.md).
helm -n observability upgrade --install oan-logging oan-helm/oan-logging --devel \
  -f environments/qa/values/oan-logging.yaml
```

Pin `--version` to the chart versions you tested instead of `--devel` once they are released.

## Namespaces

| Namespace | Holds | Accepts traffic from | Pod Security |
|---|---|---|---|
| `api6-gateway` | APISIX, its etcd and Redis | anywhere (the edge) | `privileged`: hostPort 80/443 |
| `observability` | the oan-logging agent | its own pods and Prometheus | `privileged`: hostPath `/var/log/pods` |
| `frappe-common` | the shared PostgreSQL | a2c, grievance, da-app, farmer-app, sandbox, leads | `baseline` |
| `a2c`, `grievance`, `da-app`, `farmer-app`, `leads`, `sandbox` | the services (Jenkins) | APISIX | `baseline` |

Every guarded namespace also accepts its own pods and `cattle-monitoring-system`. Egress is open.

## Edge

The wildcard ApisixTls comes from `edge` in the APISIX values without `edge.upstream.host`: the certificate, no
catch-all. A host without a route of its own gets APISIX's 404. To send the remaining hosts to an OpenG2P server,
set `edge.upstream` as `environments/dev/values/oan-apisix-gateway.yaml` does.
