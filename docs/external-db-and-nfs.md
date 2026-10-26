# MariaDB outside the cluster and the sites volume on NFS

The base values files for [grievance](grievance-service.md) and [A2C](a2c.md) use a
MariaDB server outside the cluster and an NFS server for the shared Frappe `sites`
volume. This guide sets both up. There is one set of values for every environment, so a
lab, dev and production differ only in addresses (the database host, the NFS server),
names and sizes, not in which components run. The gateway, routes and Secrets other than
the database one do not depend on this choice.

OpenG2P's production layout is the same idea: persistent volumes come from an NFS server
on a storage node through the `nfs-csi` StorageClass, and PostgreSQL runs on that
host, outside Kubernetes ([persistent storage](https://docs.openg2p.org/operations/deployment/deployment-guide/persistent-storage.md)).

Rendered and checked with `helm template` only. Nothing in this guide has been installed
against a real NFS or MariaDB server.

## 1. What changes

| | Earlier setup (in-chart database, single-node storage) | Base values now |
|---|---|---|
| MariaDB | StatefulSet `mariadb-sts` in the release | A server you run: `frappe.dbHost` |
| Root credential | `--set-string frappe.mariadb-sts.rootPassword=...` | Read from Secret `oan-<app>-db`, key `password`, by the create-site job (`dbExistingSecret`). No value on the command line, none in the Helm release record. |
| Sites volume (RWX) | `local-path-shared` | `nfs-csi` |
| APISIX etcd (gateway cluster) | built-in single member on `local-path-shared` | external, three members on local SSD, never NFS ([apisix-gateway.md](apisix-gateway.md), section 10) |

Files:

- [oan-grievance-service.yaml](../environments/dev/values/oan-grievance-service.yaml) and [oan-a2c.yaml](../environments/dev/values/oan-a2c.yaml): the base files already hold the external-database and `nfs-csi` settings.
- [nfs-csi.yaml](../environments/dev/values/nfs-csi.yaml): the NFS CSI driver and the `nfs-csi` StorageClass.

The charts only require that `frappe.dbHost` or `frappe.mariadb-sts` is set. The upstream
chart can still run MariaDB inside the release, but we no longer provide values for it.
To run without an NFS or MariaDB server of your own, set up both on the same machine
(a VM or the host), as in the homelab notes.

## 2. The database server

Run MariaDB on a host the cluster nodes can reach on port 3306, and keep it off the public
network. Frappe 16 accepts 10.6 to 11.8 (it warns outside that range, in
`check_compatible_versions`); the in-chart database used 11.8, and a distribution package
such as Ubuntu 24.04's 10.11 is inside the range.

Configuration, from the in-chart `myCnf`:

```ini
[mysqld]
skip-character-set-client-handshake
skip-innodb-read-only-compressed
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci
bind-address=0.0.0.0
```

Require TLS. The MariaDB client in the Frappe image (11.8) uses TLS by default and verifies the
server certificate. Without TLS on the server, `bench new-site` fails with `ERROR 2026 (HY000):
TLS/SSL error: SSL is required, but the server does not support it`, and the upstream
create-site job still ends as `Completed` (it reads the exit status of `tee`). Give the server
a certificate from your CA, whose subject alternative name is the address in `frappe.dbHost`:

```ini
[mysqld]
ssl-ca=/etc/mysql/ssl/ca.pem
ssl-cert=/etc/mysql/ssl/server-cert.pem
ssl-key=/etc/mysql/ssl/server-key.pem
tls_version=TLSv1.2,TLSv1.3
require_secure_transport=ON
max_connect_errors=100000
```

Raise `max_connect_errors`: all Pods on a node share the node's address, and Pods that start before
`db_ssl_ca` is written are refused and counted, so the default of 100 blocks the node.

The clients need the CA. Add it to the image's system trust store at build time
(`update-ca-certificates`) and point the client at it with `/etc/mysql/conf.d/oan-tls.cnf`
(`[client]` `ssl-ca=/etc/ssl/certs/ca-certificates.crt`, `ssl-verify-server-cert`). Frappe's own
connections use `db_ssl_ca` and `db_ssl_check_hostname` in `common_site_config.json`; the
environment values set both through `frappe.jobs.configure.args`.

Create the administrator that `bench new-site` uses. It creates one database and one
database user per site, so it needs `CREATE USER` and `GRANT OPTION`. Allow it from the
cluster nodes' addresses only. Pod traffic usually leaves a node with the node's
address:

```sql
CREATE USER 'frappe_admin'@'10.0.0.%' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON *.* TO 'frappe_admin'@'10.0.0.%' WITH GRANT OPTION;
```

The job creates the site's own database user with host `%`, so also restrict port 3306 in
the host's firewall or security group to the cluster nodes. Both apps can share one
server: each site gets its own database.

Backups run on the database host (`mariadb-backup` or `mysqldump`), not in Kubernetes.
Frappe also keeps `encryption_key` in `sites/<site>/site_config.json`; back that up with
the database.

## 3. The NFS server

Any Linux host works. NFS needs no special format: it exports a directory from a local
filesystem. Use a dedicated disk or logical volume, so the share cannot fill `/` and can
be resized:

```sh
sudo mkfs.xfs /dev/<disk-or-lv>                      # ext4 also works
sudo mkdir -p /srv/nfs
echo '/dev/<disk-or-lv> /srv/nfs xfs defaults 0 0' | sudo tee -a /etc/fstab && sudo mount -a
sudo mkdir -p /srv/nfs/k8s && sudo chown 1000:1000 /srv/nfs/k8s
```

Export it to the cluster nodes only, mapping every client to the Frappe user (UID and GID
1000 in the image), so files created by any Pod are writable by all of them:

```sh
sudo dnf install -y nfs-utils                         # apt install nfs-kernel-server on Debian
echo '/srv/nfs/k8s 10.0.0.0/24(rw,sync,no_subtree_check,all_squash,anonuid=1000,anongid=1000)' | sudo tee -a /etc/exports
sudo systemctl enable --now nfs-server && sudo exportfs -rav
sudo firewall-cmd --permanent --add-service=nfs && sudo firewall-cmd --reload
```

Use NFSv4 so only TCP 2049 is needed. SELinux can block exports on Fedora and RHEL; test
a write from a node before adding booleans.

Do not put MariaDB or etcd on this share.

## 4. The cluster side

Every node needs the NFS client (`nfs-utils` on the RHEL family, `nfs-common` on Debian).
I did not confirm that the CSI driver needs it on the host; install it anyway. k3d nodes
are containers built from the `rancher/k3s` image, which has no `mount.nfs`, so test an
NFS volume there before relying on it. Use VMs for NFS tests.

```sh
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm repo update csi-driver-nfs
helm upgrade --install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --version 4.13.6 -n kube-system \
  -f environments/dev/values/nfs-csi.yaml \
  --set-string storageClass.parameters.server=<nfs server address> --wait
kubectl get sc nfs-csi
```

Test it before installing an app. A Pod in the test must write a file:

```sh
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: nfs-test}
spec:
  accessModes: [ReadWriteMany]
  storageClassName: nfs-csi
  resources: {requests: {storage: 1Gi}}
---
apiVersion: v1
kind: Pod
metadata: {name: nfs-test}
spec:
  securityContext: {supplementalGroups: [1000]}
  containers:
    - name: t
      image: busybox
      command: [sh, -c, "echo ok > /d/f && cat /d/f && sleep 3600"]
      volumeMounts: [{name: d, mountPath: /d}]
  volumes: [{name: d, persistentVolumeClaim: {claimName: nfs-test}}]
EOF
kubectl logs nfs-test        # ok
kubectl delete pod/nfs-test pvc/nfs-test
```

A `mount failed` event on the Pod means the node cannot mount NFS (client missing, export
or firewall wrong).

## 5. Install

Create the Secret first. `oan-<app>-db` now holds the password of `frappe_admin` on the
external server:

```sh
kubectl -n develop create secret generic oan-grievance-db --from-literal=password='<frappe_admin password>'
```

Then install. No `rootPassword` is passed:

```sh
helm upgrade --install grievance charts/oan-grievance-service -n develop \
  -f environments/dev/values/oan-grievance-service.yaml \
  --set-string frappe.image.tag=<tag> \
  --set-string frappe.dbHost=<mariadb host> \
  --wait --wait-for-jobs --timeout 20m
```

A2C is the same with `charts/oan-a2c`, namespace `a2c-develop`, `oan-a2c.yaml` and
Secret `oan-a2c-db`. Through Rancher, paste the base file into the values editor and set
`frappe.dbHost`.

Check:

```sh
kubectl -n develop get pvc                       # sites volume: nfs-csi, Bound
kubectl -n develop get pods                      # no mariadb-sts Pod
kubectl -n develop logs job/<create-site job>    # no connection errors to the DB host
```

## 6. Not covered

- **Moving data.** The base values are for a fresh install. A running in-chart database
  needs a dump and restore, then the site's `db_host` changed.
- **Database high availability.** One server is one failure point. Use replication or a
  managed service when that matters.
- **NFS high availability.** The same applies to the NFS server.
- **Frappe on NFS under load.** The `sites` volume holds assets, uploads and logs. Network
  filesystems are slower for many small files. Measure on dev before production.
- **A production environment directory.** The values sit in `environments/dev/values/`.
  Copy them into `environments/<env>/values/` with that environment's addresses when it
  exists.
