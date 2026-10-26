# Request flow, load balancing, logging and Rancher

How a request travels from a client to Frappe when the gateway and the app clusters have
several nodes and several Pods, which layer spreads the load at each step, where logs go,
and where Rancher sits.

Today each cluster has one node and one gunicorn Pod per app. The gateway chart takes a
list of nodes per app (`externalHosts`) with a health check, but only one node has been
tried. The diagram shows the target layout; "What exists today" at
the end separates what is installed from what is only planned.

Two nodes per cluster show the difference between one and many. etcd has three members,
because a majority is needed. Lines are coloured by what they carry:

| Colour | Carries |
|---|---|
| Blue, numbered 1 to 4 | The request path: client, DNS, APISIX, node port, Service, Pod |
| Purple | Gateway configuration: the `Apisix*` resources, the controller, the Admin API, etcd |
| Grey | Data: database, Valkey, the job queue, NFS |
| Yellow, dotted | Logs and errors |
| Red, dotted | Management: Rancher and operators |

The yellow note is a configuration object, not a running program. A Service is not a
machine: it is a virtual address that `kube-proxy` rules on every node implement, and a
NodePort Service opens its port on every node. Everything under "Operations, planned" and
the OTel and Rancher agents is not installed yet; see [What exists today](#what-exists-today). Sentry is left out of the pipeline for now.

```mermaid
flowchart LR

  client["Clients<br/>browser, partner, IVR"]
  dns["DNS or load balancer<br/>one address, 2 gateway nodes"]
  admin["Operators<br/>browser"]

  subgraph GW["Gateway cluster, 2 nodes"]
    direction TB
    apA["APISIX Pod A<br/>gateway node 1<br/>hostPort 80/443"]
    apB["APISIX Pod B<br/>gateway node 2<br/>hostPort 80/443"]
    pick(("routes by Host,<br/>picks a node"))
    valkey[("Valkey<br/>rate-limit counters")]
    cfg>"config objects: ApisixRoute,<br/>ApisixUpstream, ApisixTls"]
    ic["apisix-ingress-controller"]
    agGW["agents: OTel, Rancher"]
  end

  subgraph ETCD["etcd, 3 members"]
    e1[("member 1")]
    e2[("member 2")]
    e3[("member 3")]
  end

  subgraph GRV["Grievance cluster, 2 nodes"]
    direction TB
    svcG{{"Service grievance-gateway-web<br/>NodePort 30800, open on every node<br/>kube-proxy picks a Pod"}}
    svcS{{"Service grievance-gateway-socket<br/>NodePort 30900"}}
    subgraph g1["node 1"]
      pgA["gunicorn Pod A<br/>workers 1..n"]
    end
    subgraph g2["node 2"]
      pgB["gunicorn Pod B<br/>workers 1..n"]
    end
    sioG["socket.io Pod"]
    vcG[("Valkey cache Pod")]
    vqG[("Valkey queue Pod")]
    schedG["scheduler Pod"]
    wkG["Frappe workers<br/>default, short, long"]
    wcG["OAN workers<br/>routing, sla, scan, notifications"]
    clam["ClamAV Pod"]
    pvcG[/"PVC sites<br/>nfs-csi, ReadWriteMany"/]
    csiG["csi-driver-nfs"]
    agG["agents: OTel, Rancher"]
  end

  subgraph A2C["A2C cluster, 2 nodes"]
    direction TB
    svcA{{"Service a2c-gateway-web<br/>NodePort 30810, open on every node<br/>kube-proxy picks a Pod"}}
    subgraph a1["node 1"]
      paA["gunicorn Pod A<br/>workers 1..n"]
    end
    subgraph a2["node 2"]
      paB["gunicorn Pod B<br/>workers 1..n"]
    end
    vcA[("Valkey cache Pod")]
    vqA[("Valkey queue Pod")]
    wkA["scheduler, socket.io,<br/>Frappe workers"]
    pvcA[/"PVC sites<br/>nfs-csi, ReadWriteMany"/]
    csiA["csi-driver-nfs"]
    agA["agents: OTel, Rancher"]
  end

  db[("MariaDB<br/>external server")]
  nfs[("NFS server<br/>one subdirectory per PVC")]

  subgraph OPS["Operations, planned"]
    otelgw["OTel gateway<br/>batches, forwards"]
    loki[("Loki")]
    grafana["Grafana<br/>search the log lines"]
  end
  rancher["Rancher<br/>management cluster"]

  client -->|"1"| dns
  dns -->|"2"| apA
  dns --> apB
  apA --> pick
  apB --> pick
  pick -->|"3  Host = grievance, to a node, port 30800"| svcG
  pick -->|"/socket.io, port 30900"| svcS
  pick -->|"3  Host = A2C, to a node, port 30810"| svcA
  svcG -->|"4"| pgA
  svcG --> pgB
  svcS --> sioG
  svcA -->|"4"| paA
  svcA --> paB
  cfg -->|"watched"| ic
  ic -->|"pushes through the Admin API; APISIX writes etcd"| apA
  apA <-->|"store and watch"| e1
  e1 <-->|"vote"| e2
  e2 <--> e3
  e3 <--> e1
  apA -.->|"count"| valkey
  pgA --> db
  pgB --> db
  pgA --> vcG
  pgB --> vcG
  pgA -->|"enqueue jobs,<br/>publish realtime"| vqG
  pgB --> vqG
  vqG -->|"jobs, workers wait here"| wkG
  vqG --> wcG
  vqG -->|"realtime events"| sioG
  schedG -->|"enqueue due jobs"| vqG
  wkG --> db
  wcG --> db
  schedG -->|"every ~4 min: any due job?"| db
  wcG -->|"scan upload"| clam
  pgA -.->|"mount"| pvcG
  pgB -.-> pvcG
  wkG -.-> pvcG
  wcG -.-> pvcG
  schedG -.-> pvcG
  sioG -.-> pvcG
  pvcG --> csiG
  csiG -->|"provisions, mounts"| nfs
  paA --> db
  paB --> db
  paA --> vcA
  paB --> vcA
  paA --> vqA
  paB --> vqA
  vqA -->|"jobs"| wkA
  wkA --> db
  paA -.->|"mount"| pvcA
  paB -.-> pvcA
  wkA -.-> pvcA
  pvcA --> csiA
  csiA --> nfs
  agGW -.->|"logs"| otelgw
  agG -.-> otelgw
  agA -.-> otelgw
  otelgw -.-> loki
  loki -.-> grafana
  agGW -.->|"dials out"| rancher
  agG -.-> rancher
  agA -.-> rancher
  admin -.->|"manage"| rancher
  admin -.-> grafana
  %% request path (blue)
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12 stroke:#1f6feb,stroke-width:3px
  %% gateway config (purple)
  linkStyle 13,14,15,16,17,18 stroke:#8250df,stroke-width:2px
  %% data (grey)
  linkStyle 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54 stroke:#6e7781,stroke-width:1.5px
  %% logs (yellow)
  linkStyle 55,56,57,58,59 stroke:#bf8700,stroke-width:1.5px
  %% management (red)
  linkStyle 60,61,62,63,64 stroke:#cf222e,stroke-width:1.5px
  classDef note fill:#fff8c5,stroke:#bf8700
  class cfg note
```

## Pods in one app release

Both apps use the upstream chart's Deployments. Each one is its own Pod, so each scales
and fails on its own. Rendered with `helm template` from the dev values.

| Pod | Role | In |
|---|---|---|
| `gunicorn` | HTTP API, runs several worker processes inside one Pod | both |
| `socketio` | realtime, own node port (30900 for grievance) | both |
| `scheduler` | enqueues scheduled jobs; keep one replica | both |
| `worker-d`, `worker-s`, `worker-l` | Frappe background workers (default, short, long queues) | both |
| `worker-routing`, `worker-sla`, `worker-scan`, `worker-notifications` | OAN queue workers | grievance only |
| `clamav` | virus scanner for uploads | grievance only |
| `valkey-cache`, `valkey-queue` | Frappe cache and job queue (Deployments, not StatefulSets) | both |
| `mariadb-sts` | database; off, the server is external (`frappe.dbHost`) | both |
| `nginx` | present with 0 replicas; APISIX replaces it | both |
| jobs | `conf-bench`, `new-site`, `site-config` run on install and upgrade | both |

## Smallest layout: one node at most

One gateway node, one node per app, one Pod per Deployment, no load balancer. MariaDB and
the NFS server are external, as in the [overlay](external-db-and-nfs.md). The numbers on the lines
are the order of one request. Dotted lines are background work.

```mermaid
flowchart LR
  client["Client"]

  subgraph GW["Gateway cluster, 1 node"]
    apisix["APISIX<br/>hostPort 80/443<br/>routes by Host"]
    valkey[("Valkey<br/>rate limits")]
    etcd[("etcd<br/>routes")]
  end

  subgraph GRV["Grievance cluster, 1 node"]
    np_g["node port<br/>30800 / 30900"]
    gun_g["gunicorn Pod<br/>workers 1..n"]
    sio_g["socket.io"]
    work_g["workers, scheduler,<br/>OAN workers, ClamAV"]
    vk_g[("Valkey<br/>cache + queue")]
    pvc_g[/"PVC sites<br/>StorageClass nfs-csi"/]
    csi_g["csi-driver-nfs<br/>kube-system<br/>controller + node plugin"]
  end

  subgraph A2C["A2C cluster, 1 node"]
    np_a["node port<br/>30810"]
    gun_a["gunicorn Pod<br/>workers 1..n"]
    work_a["workers, scheduler,<br/>socket.io"]
    vk_a[("Valkey<br/>cache + queue")]
    pvc_a[/"PVC sites<br/>StorageClass nfs-csi"/]
    csi_a["csi-driver-nfs<br/>kube-system<br/>controller + node plugin"]
  end

  db[("MariaDB<br/>external server")]
  nfs[("NFS server<br/>sites volumes (nfs-csi)")]

  client -->|"1"| apisix
  apisix -.-> valkey
  apisix -.-> etcd
  apisix -->|"2 Host = grievance"| np_g
  apisix -->|"2 Host = A2C"| np_a
  np_g -->|"3"| gun_g
  np_g --> sio_g
  np_a -->|"3"| gun_a
  gun_g -->|"4"| db
  gun_g --> vk_g
  gun_g -.->|"mounts"| pvc_g
  gun_a -->|"4"| db
  gun_a --> vk_a
  gun_a -.->|"mounts"| pvc_a
  vk_g -.->|"jobs"| work_g
  work_g -.-> db
  vk_a -.->|"jobs"| work_a
  work_a -.-> db
  pvc_g -.->|"provisions"| csi_g
  csi_g -.->|"subdirectory per PVC"| nfs
  pvc_a -.-> csi_a
  csi_a -.-> nfs
```
The gateway still reaches each app cluster by node address and node port, because the
clusters are separate. Collapsing to one cluster is possible (APISIX could then use
Service names), but the charts and the Host-based routing are built for separate clusters.
Logging and Rancher are left out: logs stay in `kubectl logs`, and Rancher is optional.

## Who balances what

| Step | Layer | Spreads requests across | If one of them fails |
|---|---|---|---|
| 1 | DNS or a load balancer | gateway nodes | traffic goes to the other gateway nodes (needs health checks on the load balancer) |
| 2 | APISIX upstream (`externalNodes`) | the app cluster's nodes | APISIX marks the node unhealthy and stops sending to it |
| 3 | Service (`kube-proxy`) | Pods behind the Service, on any node | the Service stops using the Pod once it is not ready |
| 4 | gunicorn master | its own worker processes | the master restarts a dead worker |

A node port is open on every node of the cluster. A request that arrives at node 1's node
port can be forwarded to a Pod on node 2, one extra hop inside the cluster. Setting the
Service's `externalTrafficPolicy: Local` keeps traffic on the node that received it, but
then a node with no ready Pod must fail its health check so APISIX skips it.

APISIX picks the app by the `Host` header. Both apps serve `/v1/auth/*`, so the host name
is the only separator. An unknown host gets `404 Route Not Found`.

## etcd for APISIX

APISIX keeps its routes, upstreams and certificates in etcd. The ingress controller
writes them there from the `Apisix*` resources in the gateway cluster. APISIX reads them
at start and watches for changes. If etcd is down, running APISIX Pods keep serving the
routes they already hold; they cannot load new ones. I expect this from how APISIX works
and have not tested it here.

| | Dev and the lab | Production |
|---|---|---|
| Where | `externalEtcd`: three etcd processes on one VM, other ports | `externalEtcd`: three machines outside Kubernetes, one etcd service on each |
| Members | 3, but on one machine, so only a process can fail | 3, so one machine can fail and the other two still form a majority |
| Storage | the VM's disk | fast local SSD, never NFS or EFS |
| Security | a user and password (`externalEtcd.user`, `existingSecret`), no TLS | the same, plus TLS between members and from APISIX |
| Backup | none | scheduled `etcdctl snapshot save`, copied off the machine |
| Ports | cluster-internal | 2379 from the APISIX nodes only, 2380 between the members only |

- **Why three machines:** the members vote, and a change counts only when a majority
  agrees. Three services on one server would all fail together, so each member needs its
  own machine, in different availability zones.
- **Dedicated or shared:** three small dedicated servers are the cleaner choice. The
  fallback is one member on the host of each of three gateway nodes, outside Kubernetes.
  Then a gateway node failure takes an APISIX Pod and an etcd member together, and a
  reboot needs a health check first. Which one is used is a decision for whoever runs the
  platform.
- **Size:** small. The built-in single member used about 153 MiB on a laptop cluster. A
  small instance with 2 vCPU and a few GB per member is my estimate for production.
- **Not Kubernetes' own etcd.** RKE2 runs one for the cluster API, and it needs the same
  things (three server nodes, SSD, snapshots), but RKE2 sets up its TLS, joining and
  snapshot schedule itself. APISIX's etcd has none of that automation. Never point APISIX
  at the cluster's etcd: it holds every Secret.

## Walk through one request

1. The client resolves `grievance-backend-dev.oanstaging.com` and reaches one gateway
   node through DNS or the load balancer.
2. APISIX on that node terminates TLS and matches the route by `Host` and path. It checks
   the rate limit in Valkey (the same counters for every APISIX Pod), then CORS, API
   keys and IP rules.
3. APISIX picks a healthy node from the upstream's `externalNodes` and sends plain HTTP
   to that node's port 30800. It rewrites `Host` to the Frappe site name.
4. `kube-proxy` on that node hands the connection to one ready gunicorn Pod, possibly on
   another node.
5. A gunicorn worker handles it, reading the database and the shared sites volume.

## Logging

Every container writes to stdout and stderr; nothing is read from log files.

| Source | What it logs | How it reaches the collector |
|---|---|---|
| Frappe containers | `FRAPPE_STREAM_LOGGING=1` sends `frappe.logger()` to stdout. Outside the dev server only `ERROR` and above are logged. | container stdout |
| APISIX | access and error logs | container stdout |
| Workers, socket.io, jobs | same as Frappe | container stdout |
| Errors with stack traces | every 5xx in the API wrapper, through `frappe.log_error` | Sentry directly, when Secret `oan-<app>-sentry` (key `dsn`) exists |

The collection path, as OpenG2P describes it ([deployment guides](https://docs.openg2p.org)):

1. An OpenTelemetry agent runs on every node of every cluster as a DaemonSet and reads
   the container logs.
2. It redacts personal data on the node, before the logs leave it (OpenG2P's
   [system monitoring docs](https://docs.openg2p.org/platform/platform-services/system-monitoring.md)
   place redaction in the agent; they do not say whether it is a collector processor
   or custom code, or which fields it covers). It forwards the logs to an OpenTelemetry
   gateway, which batches them and sends them to Loki.
3. Loki stores them on object storage. Loki has no interface of its own.
4. Grafana searches them (LogQL), draws dashboards and sends alerts, for example to Slack.
5. Sentry is separate. It groups errors and keeps stack traces. It does not replace the
   log pipeline, and the log pipeline does not replace it.

Frappe puts request bodies into Sentry events. Add a scrubbing rule on the Sentry project
that removes `contexts."JSON Body"` and `contexts."Form Data"` before turning it on.

Logs and the request path never share a hop: if the collector is down, requests still
work and the container runtime keeps the most recent logs on the node until it rotates
them.

## Rancher

Rancher is a management console. It is not in the request path.

- It runs on a cluster of its own (the management cluster). Each other cluster is
  imported and runs a `cattle-cluster-agent` that connects outward to Rancher over HTTPS,
  so the clusters need no inbound port for Rancher.
- Operators use Rancher to see Pods, jobs, volumes and logs, open a shell in a Pod, and
  install or upgrade Helm releases from a chart repository. Grafana is reachable from its
  UI in the OpenG2P setup.
- Its own state is Kubernetes objects in the management cluster's datastore (etcd on
  RKE2, SQLite on single-node k3s). Back that cluster up (the `rancher-backup` operator)
  before relying on it.
- If Rancher is down, the apps and the gateway keep working. You lose the console, not
  the service. `kubectl` and `helm` still work.
- Anyone who can open a release in Rancher can read its values. Give each namespace its
  own Rancher project.

## What happens on failures

| Failure | Result |
|---|---|
| One gunicorn Pod dies | The Service drops it. The other Pods keep serving. Kubernetes starts a replacement. |
| One app node dies | APISIX health checks mark it down. Pods on the other nodes serve. Pods from the dead node are rescheduled if there is room. |
| One etcd member dies (production, 3 members) | The other two keep the majority. Routes keep working and can still change. A second failure stops route changes; running APISIX Pods are expected to keep serving (untested). |
| The only etcd dies (dev) | Routes cannot change. Running APISIX Pods are expected to keep their routes until restarted (untested). |
| One gateway node dies | The load balancer or DNS stops using it. The other gateway nodes serve. |
| The NFS server dies | Every Pod that needs the sites volume fails or hangs. NFS is a single point of failure until it is made redundant. |
| The database server dies | Every Pod fails its database calls. Same: redundancy is separate work. |
| The log collector or Loki dies | Requests are unaffected. Recent logs stay on the nodes until they rotate; older ones are lost for the gap. |
| Sentry is unreachable | Requests are unaffected. Error reports from that period are lost. |
| Rancher is down | No console. Apps, gateway and `kubectl`/`helm` keep working. |

## What exists today

| Part | Status |
|---|---|
| Gateway cluster with APISIX and Valkey, one node | built and tested on OrbStack |
| Grievance and A2C app clusters, one node, one Pod each | built and tested on OrbStack |
| Several gateway nodes, several app nodes | the gateway chart takes `externalHosts` (a list) and `healthCheck` per app, generated by `oan_auth_service/gateway_apisix.py`. Rendered, and accepted by a server-side dry run against the controller's CRD; not tried with real traffic. APISIX still needs one replica per node (`hostPort`) and a load balancer in front. |
| External MariaDB and NFS | the base app values use them ([external-db-and-nfs.md](external-db-and-nfs.md)); rendered with `helm template`, not installed against a real server. NFS on k3d is untested. |
| Several Pods per app | possible by raising replicas in the values. The sites volume is ReadWriteMany on NFS. socket.io needs sticky routing or websocket-only clients; I have not checked the realtime route. |
| Stdout logging | on (`FRAPPE_STREAM_LOGGING=1`) |
| OpenTelemetry, Loki, Grafana | not installed. Memory is the limit on a laptop. Placement is open: in the management cluster, or a cluster of its own. |
| Sentry | not installed. The Secret hook exists in both charts. |
| Rancher | tested locally on its own k3d cluster with the OrbStack cluster imported. Dev's Rancher version and install method are unconfirmed. |
| etcd | `apisix.yaml` sets `etcd.enabled: false` and `externalEtcd`; the three member URLs are passed at install. Rendered with `helm template`; no etcd cluster has been run against it. |
| Valkey | single instance. If it is down, the rate-limit plugin follows its `allow_degradation` setting. |
