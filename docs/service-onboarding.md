# Add or enable a service in OAN dev

The environment uses `*.development.oanstaging.com`. Wildcard DNS and TLS are
installed once. Nginx forwards requests to Istio; Istio selects the application.
Adding a service does **not** require an individual Route 53 record, Nginx site
or certificate. It does require a route, runtime configuration and readiness checks.

## Add a new service

1. Choose an unused single-label hostname such as
   `new-service.development.oanstaging.com`. Keep it in the environment endpoint
   inventory. The wildcard certificate does not cover nested names such as
   `api.new-service.development.oanstaging.com`.
2. Select the component's owning chart/release and namespace. Upgrade an existing
   release rather than installing another owner over its resources. Supply a
   verified immutable image, its real service port, probes and resource settings.
3. Prepare namespace-local Secret references, database access and any persistent
   signing keys, catalog, policies or partner bindings. Keep values/passwords
   outside Git. Back up existing data and review migrations before first start.
4. Add a Helm-managed VirtualService using the explicit hostname and shared
   Gateway `istio-system/development`. Point it to the namespace-qualified
   Kubernetes Service and its Service port. Preserve required path prefixes and
   rewrites; a gateway alone does not create an application route.
5. Configure the application's public base URL, allowed origins and exact
   Keycloak redirects/web origins where needed. The canonical staff issuer is
   `https://keycloak.development.oanstaging.com/realms/staff`; application cookies
   use `.development.oanstaging.com`. Internal calls continue using Kubernetes
   service names. Retain existing authentication and authorization.
6. Render the combined chart/private values and review images, Secrets, route
   ownership and initialization Jobs. Upgrade the selected version through
   Rancher or Helm; inspect rollout status and run the component's acceptance
   checks. Save the previous chart/revision and values for recovery.

Example **route shape** (replace the sample hostname, namespace, Service and
port with the component's reviewed values; include it in the owning chart):

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: new-service
  namespace: commons
spec:
  hosts:
    - new-service.development.oanstaging.com
  gateways:
    - istio-system/development
  http:
    - route:
        - destination:
            host: new-service.commons.svc.cluster.local
            port:
              number: 80
```

## Enable a component already in a chart

Check [the service catalog](service-catalog.md) for its values key and image
availability. Setting `enabled: true` only renders resources; it does not create
credentials, usable database contents or an ingress for every optional workload.

| Component | Enablement and prerequisites |
| --- | --- |
| Registry dashboard API | `dashboardApi.enabled`; reporting views, database Secret and the source's access model. Existing unauthenticated/private APIs must remain private; do not attach their routes to the public Gateway. |
| Registry dashboard UI | `dashboardUi.enabled`; verified UI image, IAM/client roles, backend URL and an explicit authenticated public route. |
| OAN Aggregation | `aggregationApi.enabled`; select the published image overlay, complete [Consent/Aggregation prerequisites](consent-aggregation-prerequisites.md), prepare its own DB, signing key, registry catalog, bindings and authenticated Consent routing. Its chart currently creates a ClusterIP Service; add the reviewed VirtualService separately. `aggregation.development.oanstaging.com` is reserved and does not mean it is deployed. |
| DA registry | Verified backend images, confirmed namespace, DB/IAM initialization and routes. Remains disabled until those prerequisites are available. |
| Other Commons components | Preserve the shared release's settings; verify image, identity/database requirements and routes before enabling. |

Aggregation, DA and unavailable dashboard UIs are not enabled by this DNS migration.
Use the component's exact image digest and chart version. Helm rollback does not
reverse database migrations or external Keycloak/partner changes.

## Check and troubleshoot

- **DNS:** a new hostname should resolve through the wildcard to the environment
  address without adding a record. Existing exact records can override a wildcard.
- **TLS:** check certificate hostname coverage and validity with normal HTTPS
  verification. Do not work around failures with insecure TLS options.
- **Routing:** a hostname without a VirtualService should return 404. Check host,
  shared Gateway, Service endpoints, port and path rules. A 503 often indicates
  a missing or unready upstream; check Istio's route/cluster status.
- **Application:** verify the expected page/API behavior, auth redirects,
  issuer/JWKS, cookies/CORS and the component's own readiness checks. A generic
  root HTTP status alone does not establish readiness.
- **Renewal:** the Jenkins job `oan-development-wildcard-certificate-renewal`
  runs daily through `vpn-agent2`, using the existing protected AWS and SSH
  credential bindings. Check its latest result and the protected server renewal
  log. The certificate key never belongs in Git.

For recovery, restore the previous route/configuration and release values. If a
hostname or issuer changes, restore the corresponding identity settings too.
Management endpoints such as Rancher and Jenkins keep their existing URLs.

## Upgrade a release migrated from legacy charts

The live URL cutover retained installed chart versions using the compatibility
post-renderer. Before its next upgrade, merge the complete matching
`environments/dev/values/` overlay with saved private values, including Gateway
settings. Saved `gateway: internal` entries otherwise override new chart defaults.
Retain the compatibility renderer for an old chart, or review the dev.4 chart
render against live resources before removing it. Preserve runtime image and
manual configuration overrides now saved in Helm values. Do not run initialization
Jobs as part of a URL-only update.

In Rancher, select **Apps > Installed Apps > the existing release > Upgrade**,
choose the reviewed chart version, and reconcile these values in the YAML editor.
Confirm the namespace, image references and rendered route before upgrading.
Do not install a second release to change a hostname.

## Temporary old-URL compatibility

Old `*-development.oanstaging.com` links remain available until migration
completion is explicitly confirmed. Browser HTML GET/HEAD navigation redirects
with HTTP 307; API/JSON traffic and POSTs keep their methods, paths and bodies.
The old MinIO object API always proxies, including browser requests, so signed
download URLs retain the Host used by their signature.
Do not revert the canonical Keycloak issuer or application cookie domain.

Existing aliases use the separate environment-owned Gateway
`istio-system/development-legacy` and manifests under `environments/dev/legacy/`.
When an existing service's destination, port or path rules change, refresh its
legacy alias too. New services need only the new wildcard domain; do not create
new legacy DNS names by default. Preserve legacy certificate renewal while these
names are in use. Remove compatibility only after explicit completion, retaining
the private recovery snapshot.

For Keycloak authorization and IAM callbacks, preserve the ingress response
buffers (`proxy_buffer_size 16k`, `proxy_buffers 8 16k`, and
`proxy_busy_buffers_size 32k`). A 502 with `upstream sent too big header` indicates
these buffers are insufficient. Check the real authorization page as well as
OIDC discovery; `python scripts/check-keycloak-login.py` runs five live Postman
assertions with a synthetic large state/nonce and submits no credentials.
