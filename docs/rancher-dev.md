# Manual Rancher installation and upgrade

Complete [readiness prerequisites](readiness.md) for components being enabled.
For Consent/Aggregation, follow the [component preparation guide](consent-aggregation-prerequisites.md).
Use the five packages after repository publication. No
cluster deployment or ownership migration has been performed.

## Add the repository

1. After the upstream PR is merged, confirm the committed
   `repository/index.yaml` and archives are readable from GitHub's raw URLs.
2. Open the intended Rancher cluster and **Apps → Repositories → Create**.
   Use the Helm repository URL
   `https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/`.
   For the current fork preview, use
   `https://raw.githubusercontent.com/asmitonweb/oan-helm/feat/coss-rancher-charts/repository/`.
   The preview uses the same relative archive paths. GitHub Pages is not required.
   Enter the raw directory URL, not GitHub's HTML `tree`/`blob` URL or the index filename.
3. Confirm `/index.yaml` and its `.tgz` archive URLs are available, refresh the
   repository, and select exact version **`1.0.0-dev.3`**, including its prerelease
   suffix. Version `1.0.0-dev.1` is retained for history and has old URL defaults.

## New releases

Use **Apps → Charts**, select the chart and exact version, then set its release
name and namespace deliberately. The dev candidates use Farmer
`farmer-registry/farmer`, Crop `cropsown-registry/crop`, Livestock
`livestock-registry/livestock`, and Commons `commons-services/commons`.
DA's namespace needs confirmation before installation.

Use the public example as a checklist, then supply private values in Rancher's
values editor or a separately managed private values file. Existing PostgreSQL,
Keycloak, IAM, AWE, Master Data, object storage and queue settings must match the
environment. Secret references resolve within the workload's namespace: an
ExternalName Service can alias a shared Service, but it cannot alias a Secret.
Provision required namespace-local Secrets through the environment's existing
secret process. Supply pull Secrets for private images and preserve their refresh
mechanism. Never commit exported Helm values, kubeconfig, tokens or passwords.

Dashboard API configuration retains the database Secret references in each
registry chart. Farmer needs its `analytics.reportingViews`; Crop/Livestock need
`reporting.views`. Use authenticated service-to-service access for dashboard APIs.
The optional UI needs its public URL, IAM URL/cookie domain/provider, dashboard
client role and any client Secret supplied through `env` valueFrom or `envFrom`.
These charts do not silently create IAM clients or grant roles. The generic DA
API and Aggregation API additionally require confirmed runtime contracts.

Aggregation uses port `8100`. Supply its own database credentials and persistent
signing key through Secret references. Mount its reviewed registry catalog and
signing material with `volumes`/`volumeMounts`. Its entrypoint migrates the
database before serving; prepare that migration and Partner Management/Consent
bindings separately before enabling it.

The optional UI and Aggregation resources expose ClusterIP Services only. Supply
environment-owned ingress/TLS routing after confirming hosts and authentication.

Commons Base stays a separate release installed directly from the pinned
OpenG2P repository: `openg2p-commons-base` version `2.3.4-rc.245` for new preparations.
Current dev `commons/commons` is `2.3.3`; its upgrade needs separate preparation.
Do not add it as a
dependency or reinstall it over existing infrastructure. Connectors and existing
standalone dashboards remain separate releases.

## Existing releases: upgrade the current owner

In **Apps → Installed Apps**, select the existing release in its existing
namespace and choose **Upgrade**. Select the new repository/chart and exact
version. Preserve the current private values and enabled-service settings, then
apply only reviewed changes. Public examples are incomplete and are not upgrade
overlays. Do not install a second release over existing resource names.

For this URL migration, explicitly merge the matching public overlay under
`environments/dev/values/`; saved literal URLs otherwise override new defaults.
See [the URL migration guide](dev-urls.md) for canonical hosts and list handling.

Before upgrade, record the current release name, namespace, chart/version and
Helm revision; retain its package and privately exported values. Back up affected
databases and storage. Review schema/seed jobs, platform version changes,
reporting migrations and shared IAM configuration. For Commons Services, compare
all shared service settings and coordinate the shared-platform change separately.

An equivalent CLI upgrade, once those checks are complete, is:

```sh
helm upgrade farmer-registry coss/openg2p-farmer-registry \
  --namespace farmer --version 1.0.0-dev.3 \
  --reuse-values -f /private/reviewed-changes.yaml \
  -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

Substitute the **actual current** release/namespace from the installed app. This
command assumes `coss` points to the published Helm repository and that reviewed
private values have been reconciled with the new schema. Do not add `--install`
to this existing-release procedure.

If an existing dashboard or Consent component belongs to another release, keep
that owner. Enabling a new registry UI with the same name does not transfer Helm
ownership. Moving ownership requires a separately reviewed resource/annotation
and rollback plan; do not use `--take-ownership`, delete resources, or uninstall
the old release as part of these chart upgrades.

## Verify and retain a rollback path

After a manual install/upgrade, inspect Rancher workloads, ready replicas, Jobs,
events, image digests and logs. Check image pulls, namespace-local Secret names
and keys, database connections, IAM login/roles/cookies, dashboard charts and
expected private routing. Check that disabled components remain absent and
connectors/other releases still have their original owners. Packaging checks do
not replace these runtime checks.

Retain the previous package, private values, Helm revision and data backups. Use
the existing app's rollback action only after assessing compatibility.
**Helm rollback does not reverse database migrations, seed-data changes, external
IAM changes or ownership transfers.** Restore data only through the separately
prepared recovery procedure.

## OAN names and GitHub sources in Rancher

Refresh the repository and select exact version `1.0.0-dev.3` to see the OAN
metadata and embedded README. Older versions retain their original metadata.
Rancher may show either a display name or the Helm identifier depending on its
view; the chart Home, Sources and README link directly to the COSS repositories.

| OAN display name | Retained Helm chart identifier |
| --- | --- |
| OAN Farmer Registry | `openg2p-farmer-registry` |
| OAN Crop Sown Registry | `openg2p-cropsown-registry` |
| OAN Livestock Registry | `openg2p-livestock-registry` |
| OAN DA Registry | `openg2p-da-registry` |
| OAN Commons Services (Consent Manager & Aggregation) | `openg2p-commons-services` |

Consent Manager's dependency URL continues to point to OpenG2P because those
are the reused Helm templates. Its OAN application source is
[COSS/consent-management](https://github.com/Centre-for-Open-Societal-Systems/consent-management).
Aggregation is a template in the Commons chart, with source
[COSS/oan-aggregation-api](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api).
Changing these labels does not enable Aggregation or select newer candidate
images. Use the explicit candidate overlays only after the prerequisites.
