# Public dev checklists

These are incomplete checklists, not replacement live values or upgrade
overlays. Registry core and Consent images are pinned to verified ECR manifests
in chart defaults. Supply private environment settings/pull credentials outside
Git. Never apply these files blindly over an existing release.

Farmer and Crop examples enable their verified dashboard APIs, matching observed
dev deployments. Preserve existing authentication/Secret configuration. Farmer
requires its reporting views; Crop's example enables `reporting.views`. Livestock
has a verified API image but remains disabled until reporting/schema preparation.
DA backend/dashboard components, all current standalone dashboard UIs and
Aggregation remain disabled because appropriate images are unavailable.

The three public hosts match the recorded 16 October 2026 dev route inventory.
Shared PostgreSQL is an example; confirm saved private values. DA's host and
namespace remain unconfirmed. Reconcile actual DB/IAM/AWE endpoints privately.

Optional workloads support `image.digest`, `imagePullSecrets`, resources,
`envFrom` and runtime configuration. UI/DA/Aggregation `env` uses Kubernetes
EnvVar objects, including `valueFrom.secretKeyRef`. Existing Farmer/Crop/Livestock
API `env` remains its upstream name/value map. DB passwords stay in existing
namespace-local Secrets. No new Secret is automatically created.

The UI defaults to `<release>-dashboard-ui`; the API retains
`<release>-dashboard-api`. Existing standalone dashboards keep their owners.
New Services are ClusterIP. Prepare public routing/authentication separately.
Aggregation uses port `8100`; `volumes`/`volumeMounts` can mount its registry
catalog and signing key. Prepare its DB, Consent/Partner bindings and migration
procedure before enabling it.

Consent retains nested values under `openg2p-consent-manager`:
`consentManagerApi.image`, `ui.image` and `sanity.image`. Partner API and expiry
jobs inherit the API image. Existing `extraApis` list settings/names are retained.
Valid `tag@sha256` references let upstream tag-only templates use verified digests.

Public upstream demo defaults are not private environment credentials. Keep
actual approver-resolver/API/seed authentication in private values or Secrets
through existing `envVarsFrom` settings. Preserve matching values on API and
seed sides when changing that wiring.
