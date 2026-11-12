# PostgreSQL and the sites volume on NFS

The base values files for [grievance](grievance-service.md) and [A2C](a2c.md) use the
PostgreSQL of the `oan-frappe-common` release and an NFS server for the shared Frappe
`sites` volume. This guide sets both up. There is one set of values for every environment,
so a lab, dev and production differ only in addresses (the NFS server), names and sizes,
not in which components run. The gateway, routes and Secrets other than the database one
do not depend on this choice.

The NFS setup is the one on the OpenG2P dev cluster, which OpenG2P builds with
[openg2p-deployment](https://github.com/OpenG2P/openg2p-deployment) (`nfs-server/install-nfs-server.sh`,
`kubernetes/nfs-client/install-nfs-csi-driver.sh`, `automation/sandbox/lib/phase1.sh`).
Checked on that cluster on 2026-11-11:

- The NFS server runs on the cluster's only node and exports `/srv/nfs` to every address
  with `rw,sync,insecure,no_root_squash,no_all_squash`.
- Each cluster has its own directory, `/srv/nfs/<cluster name>` (`/srv/nfs/openg2p` there).
- `csi-driver-nfs` (driver v4.7.0) provides the default StorageClass `nfs-csi`: `Retain`,
  `subDir: ${pvc.metadata.namespace}-${pvc.metadata.name}-${pv.metadata.name}`,
  `mountPermissions: "0777"`.
- Every volume uses it, the commons PostgreSQL, Kafka and MinIO included.

OpenG2P's production layout keeps NFS and PostgreSQL on a separate storage node, with
PostgreSQL installed on the host ([persistent storage](https://docs.openg2p.org/operations/deployment/deployment-guide/persistent-storage.md)).
This guide is the dev layout.

Rendered and checked with `helm template` only. Nothing in this guide has been installed
against a real NFS server.

## 1. What runs where

| | Dev |
|---|---|
| NFS server | On the app node itself, exporting `/srv/nfs` (section 2) |
| StorageClass | `nfs-csi`, the default class, share `/srv/nfs/<cluster name>` ([nfs-csi.yaml](../environments/dev/values/nfs-csi.yaml)) |
| PostgreSQL | Release `oan-frappe-common-db` of [charts/oan-frappe-common](../charts/oan-frappe-common), namespace `frappe-common`, one per cluster, its volume on `nfs-csi` ([oan-frappe-common.yaml](../environments/dev/values/oan-frappe-common.yaml)). The apps reach it at `oan-frappe-common-db-postgresql-subchart.frappe-common.svc.cluster.local` (`frappe.dbHost` in the app values). |
| Database credential | The chart creates Secret `oan-frappe-common-db` (key `password`, the `postgres` password) on first install. Each app reads a copy of it in its own namespace (`dbExistingSecret`). No value on the command line, none in the Helm release record. |
| Sites volume (RWX) | `nfs-csi`, one per app release |
| APISIX etcd (gateway cluster) | external, three members on local SSD, never NFS ([apisix-gateway.md](apisix-gateway.md), section 10) |

Files:

- [nfs-csi.yaml](../environments/dev/values/nfs-csi.yaml): the NFS CSI driver and the `nfs-csi` StorageClass.
- [oan-frappe-common.yaml](../environments/dev/values/oan-frappe-common.yaml): the PostgreSQL volume.
- [oan-grievance-service.yaml](../environments/dev/values/oan-grievance-service.yaml) and [oan-a2c-service.yaml](../environments/dev/values/oan-a2c-service.yaml): `frappe.dbHost`, `dbRootUser: postgres` and the `nfs-csi` sites volume.

Everything in this table is installed once per cluster except the app releases. With
grievance and A2C in one cluster, they share the driver, the StorageClass and PostgreSQL.

## 2. The NFS server

On the app node, as root. The same steps as OpenG2P's `install-nfs-server.sh` (Ubuntu):

```sh
apt update && apt install -y nfs-kernel-server
useradd nfsnobody
mkdir -p /srv/nfs && chown -R nfsnobody:nfsnobody /srv/nfs && chmod 777 /srv/nfs
mkdir -p /srv/nfs/<cluster name> && chmod 777 /srv/nfs/<cluster name>
echo '/srv/nfs *(rw,sync,no_root_squash,no_all_squash,insecure,subtree_check)' >> /etc/exports
sort -u /etc/exports -o /etc/exports
systemctl enable --now nfs-kernel-server && exportfs -rav
```

The export is open to every address and keeps root (`no_root_squash`); OpenG2P's script
marks it as unsafe. It is acceptable only while TCP 2049 is reachable from the node network
alone: allow 2049 in the node's firewall or security group from the cluster's subnet only.

`/srv/nfs` on the root disk fills `/` when it fills. A dedicated disk or logical volume
mounted at `/srv/nfs` avoids that and can be resized.

Use one directory per cluster. With grievance and A2C in separate clusters, each node
serves its own `/srv/nfs/<cluster name>`.

## 3. The cluster side

Every node needs the NFS client (`nfs-common` on Debian and Ubuntu, `nfs-utils` on the
RHEL family). k3d nodes are containers built from the `rancher/k3s` image, which has no
`mount.nfs`, so NFS does not work on a local k3d cluster. Use VMs for NFS tests.

Install the driver and the StorageClass once per cluster. Pass the node's internal address
(from `kubectl get nodes -o wide`), not `localhost`: the CSI driver's Pod makes the mount,
and in its network `localhost` may not be the host.

```sh
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm repo update csi-driver-nfs
helm upgrade --install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --version 4.13.6 -n kube-system \
  -f environments/dev/values/nfs-csi.yaml \
  --set-string storageClass.parameters.server=<node internal address> \
  --set-string storageClass.parameters.share=/srv/nfs/<cluster name> --wait
kubectl get sc                 # nfs-csi (default)
```

OpenG2P's script installs driver v4.7.0 and applies the StorageClass with `kubectl`. This
uses chart 4.13.6, which creates the same StorageClass from the values file.

Test it before installing an app. A Pod in the test must write a file:

```sh
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: nfs-test}
spec:
  accessModes: [ReadWriteMany]
  resources: {requests: {storage: 1Gi}}
---
apiVersion: v1
kind: Pod
metadata: {name: nfs-test}
spec:
  containers:
    - name: t
      image: busybox
      command: [sh, -c, "echo ok > /d/f && cat /d/f && sleep 3600"]
      volumeMounts: [{name: d, mountPath: /d}]
  volumes: [{name: d, persistentVolumeClaim: {claimName: nfs-test}}]
EOF
kubectl get pvc nfs-test     # nfs-csi, Bound, with no class named in the claim
kubectl logs nfs-test        # ok
kubectl delete pod/nfs-test pvc/nfs-test
```

The class is `Retain`, so the test leaves a directory `default-nfs-test-pvc-...` on the
share; delete it on the node.

A `mount failed` event on the Pod means the node cannot mount NFS (client missing, export
or firewall wrong).

## 4. The database

```sh
helm upgrade --install oan-frappe-common-db charts/oan-frappe-common -n frappe-common --create-namespace \
  -f environments/dev/values/oan-frappe-common.yaml --wait
kubectl -n frappe-common get pvc     # nfs-csi, Bound
```

Use the release name `oan-frappe-common-db`. The Service name, and so `frappe.dbHost` in
the app values, is derived from it.

The password Secret is created once and kept on upgrade and uninstall. Copy it into each
app's namespace; a Pod cannot read a Secret from another namespace:

```sh
for ns in develop a2c-develop; do
  kubectl -n frappe-common get secret oan-frappe-common-db -o json \
    | jq 'del(.metadata.namespace,.metadata.uid,.metadata.resourceVersion,.metadata.creationTimestamp,.metadata.ownerReferences,.metadata.labels,.metadata.annotations)' \
    | kubectl -n "$ns" apply -f -
done
```

Run only the namespaces that exist in this cluster (`develop` for grievance, `a2c-develop`
for A2C). The create-site job logs in as `postgres` and creates one database and one
database user per site.

PostgreSQL on NFS is what OpenG2P runs on its dev cluster. It is slower than a local disk
and depends on the NFS server staying up; production moves it to a host install.

Back up with `pg_dump` from the PostgreSQL Pod, and the share with a disk snapshot of the
node. Frappe also keeps `encryption_key` in `sites/<site>/site_config.json`; back that up
with the database.

## 5. Install

Order in each app cluster: NFS server (section 2), `csi-driver-nfs` (section 3),
`oan-frappe-common-db` and the copied Secret (section 4), then the app. The database host
and user are in the base values, so nothing about the database is passed:

```sh
helm upgrade --install grievance charts/oan-grievance-service -n develop \
  -f environments/dev/values/oan-grievance-service.yaml \
  --set-string frappe.image.tag=<tag> \
  --wait --wait-for-jobs --timeout 20m
```

A2C is the same with `charts/oan-a2c-service`, namespace `a2c-develop` and
`oan-a2c-service.yaml`. Through Rancher, paste the base file into the values editor.

Check:

```sh
kubectl -n develop get pvc                       # sites volume: nfs-csi, Bound
kubectl -n develop logs job/<create-site job>    # no connection errors to the DB host
ls /srv/nfs/<cluster name>                        # on the node: develop-..., frappe-common-...
```

## 6. Not covered

- **Moving data.** The base values are for a fresh install. Moving an existing site to
  another database needs a dump and restore, then the site's `db_host` changed.
- **Database high availability.** One PostgreSQL Pod is one failure point. Use replication
  or a host install when that matters.
- **NFS high availability.** The NFS server is the node itself: the node and its storage
  fail together. Production keeps NFS on a separate node.
- **Frappe on NFS under load.** The `sites` volume holds assets, uploads and logs. Network
  filesystems are slower for many small files. Measure on dev before production.
- **A production environment directory.** The values sit in `environments/dev/values/`.
  Copy them into `environments/<env>/values/` with that environment's addresses when it
  exists.
