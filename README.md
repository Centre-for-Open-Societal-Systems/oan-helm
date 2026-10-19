# OpenAgriNet (OAN) Helm repository

Start with the [service catalog](docs/service-catalog.md): it maps every included
COSS service to its chart, source/configuration and enablement status. The
[five editable source charts](charts/README.md) are Farmer, Crop Sown, Livestock,
DA and Commons Services, which contains COSS Consent and Aggregation.

For those two components, start at
[where COSS Consent Manager and Aggregation are included](docs/service-catalog.md#where-are-coss-consent-manager-and-aggregation).
Consent reuses the `openg2p-consent-manager` child chart with COSS image overrides;
Aggregation is a local Commons template, disabled pending runtime preparation.
The current chart pins new Consent and Aggregation images from the recorded
COSS commits by ECR digest. See [the current setup guide](docs/consent-aggregation-prerequisites.md).

Current chart version is **`1.0.0-dev.5`**, using
`<service>.development.oanstaging.com` and the shared Istio Gateway. It retains
OAN display names and direct COSS source links. Earlier packages remain unchanged.
Component image versions are independent; automatic synchronization is deferred.
Old application URLs remain compatible until explicit migration completion;
browser navigations redirect temporarily and API requests retain their methods.

Use the [service onboarding guide](docs/service-onboarding.md) to add or enable a
service without an individual Route 53 record, Nginx site or certificate.

| Location | Contents |
| --- | --- |
| `charts/` | Five editable source trees; start at [charts/README.md](charts/README.md) |
| `docs/service-catalog.md` | Every included service, its COSS repository, owning chart and status |
| `environments/dev/` | Canonical endpoint inventory and public URL migration overlays |
| `examples/dev/` | Public dev configuration checklists; no private live values |
| `releases/` | Release manifest, provenance, deployment comparison and validation evidence |
| `repository/` | Generated Rancher downloads, SHA256SUMS and cumulative Helm index, including historical versions |
| `docs/` | Readable service catalog, URL migration and Rancher guides |
| `scripts/validate.py` | Dependency, render, packaging and repository validation |

Rancher repository URLs served directly by GitHub:

- COSS after merge: `https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/`
- Current fork preview: `https://raw.githubusercontent.com/asmitonweb/oan-helm/feat/consent-aggregation-rancher/repository/`

GitHub serves the committed `repository/index.yaml` and archives directly;
GitHub Pages is not required. Validation runs on PRs and pushes. Merging the
reviewed files into `main` makes the COSS URL available; this change does not
merge the PR. Live URL cutover evidence is recorded separately from chart publication.

Use the [Rancher guide](docs/rancher-dev.md) and
[new-dev URL migration guide](docs/dev-urls.md), plus the
[readiness table](docs/readiness.md). Published COSS core/Consent images are
pinned by digest. Optional dashboard APIs also have verified images but remain
opt-in for reporting/identity preparation. Dashboard UIs, DA backend/dashboard
workloads and Aggregation remain disabled pending images or configuration.
Private registry pull credentials and live values stay outside Git.
Unconfirmed public endpoints stay unset. Superset/Certify defaults match their
disabled state in the inspected dev release; notifications await confirmed routes.

Follow the [Consent and Aggregation prerequisites](docs/consent-aggregation-prerequisites.md)
before enabling Aggregation. The 19 October code is stateless and uses the split
Consent partner API directly; it needs no Aggregation database, queue or worker.
Consent uses per-binding `consent_method` settings; the older global
`subject_consent_*` flags are absent. OTP remains unavailable pending SMS;
neither OTP logging nor bucket publishing is enabled. Historical integration
reports apply only to their recorded image pairs, not these new images.

Commons Services was imported from the latest published OpenG2P package at
verification time, `2.3.4-rc.247`, with its published SHA-256 verified. All registry
charts retain their source pins to platform `1.2.2-rc.544`. Commons Base remains a
separate upstream installation, pinned to `2.3.4-rc.245` for new preparations;
the current dev release is `2.3.3` and upgrading it requires separate preparation.
Connectors, the shared OAN dashboard and existing independent dashboards keep
their Helm owners.

```sh
python -m pip install -r requirements.txt
python scripts/validate.py --package
# Also verify locked dependencies against upstream repositories:
python scripts/validate.py --online
```

Requires Helm `3.19.0`; set `HELM` if the executable is not on PATH. Validation
uses no Kubernetes credentials. It resolves locks through a local HTTP mirror of
bundled sources, strictly lints all charts, compares original resource names,
selectors and Secret references, renders two namespaces and optional workloads,
and verifies package rendering plus relative index/archive URLs over HTTP.
Synthetic render fixtures use `example.invalid`; installation examples never do.

Archives are immutable. Packaging rejects changed source bytes for an existing
archive/version. Keep historical archives and index entries; future releases
require a new chart version and manifest. The separate 19 October dev URL cutover retains installed chart/image versions;
see `releases/live-domain-migration.json`. No application-repository CI changes
are included.
