# CI deploy identity

Jenkins deploys the OAN Frappe services (A2C, grievance) and their APISIX routes with one
ServiceAccount per cluster. The chart [oan-cluster-access](../charts/oan-cluster-access) holds
everything that identity may do, so a new cluster gets the same access from Git:

| Namespace | Access | Used for |
| --- | --- | --- |
| each of `deployNamespaces` | built-in `admin` role | the service's Helm release, Secrets, Jobs and APISIX routes |
| `readSecret.namespace` (`frappe-common`) | `get` on Secret `oan-frappe-common-db` only | copy the shared PostgreSQL password |
| `gatewayNamespace` (`api6-gateway`) | get/list Services | find the APISIX release's Redis |

`admin` covers the APISIX custom resources only because the gateway chart aggregates them into
it ([apisix-gateway.md](apisix-gateway.md#who-may-manage-routes)). Install the gateway first.

The chart creates no namespace: every namespace it binds in must exist. It stores no
credential either. Kubernetes writes the token into the Secret `<serviceAccount.name>-token`,
and the script `cluster/write-kubeconfig.sh` in
[oan-service-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-service-helm) turns
it into the kubeconfig Jenkins keeps as the Secret file credential `oan-dev-kubeconfig`.

## Install or add a namespace

As a cluster admin:

```sh
helm upgrade --install oan-cluster-access charts/oan-cluster-access -n a2c \
  -f environments/dev/values/oan-cluster-access.yaml

kubectl auth can-i create deployments -n grievance --as=system:serviceaccount:a2c:jenkins-a2c-deployer   # yes
kubectl auth can-i get secret oan-frappe-common-db -n frappe-common --as=system:serviceaccount:a2c:jenkins-a2c-deployer  # yes
kubectl auth can-i list secrets -n frappe-common --as=system:serviceaccount:a2c:jenkins-a2c-deployer      # no
```

A new service: create its namespace, add it to `deployNamespaces` and upgrade. The kubeconfig
does not change.

## Taking over the oan_dev objects made by hand

oan_dev got this identity from a script before the chart existed. Hand the ServiceAccount, its
token Secret and the `a2c` RoleBinding to the release first, so the token Jenkins holds stays
valid:

```sh
for obj in serviceaccount/jenkins-a2c-deployer secret/jenkins-a2c-deployer-token rolebinding/jenkins-a2c-deployer; do
  kubectl -n a2c label "$obj" app.kubernetes.io/managed-by=Helm --overwrite
  kubectl -n a2c annotate "$obj" meta.helm.sh/release-name=oan-cluster-access meta.helm.sh/release-namespace=a2c --overwrite
done
```

Install as above, check with `kubectl auth can-i`, then delete the hand-made grants the chart
replaced under new names:

```sh
kubectl -n grievance delete rolebinding jenkins-a2c-deployer-grievance
kubectl -n frappe-common delete rolebinding jenkins-read-db-secret
kubectl -n frappe-common delete role jenkins-read-db-secret
kubectl -n api6-gateway delete rolebinding jenkins-read-services
kubectl -n api6-gateway delete role jenkins-read-services
```

## Rotating or revoking the token

Delete the Secret `jenkins-a2c-deployer-token` and upgrade the release: Kubernetes issues a new
token and the old one stops working. Write a new kubeconfig and replace the Jenkins credential.
Uninstalling the release removes every grant and the token.
