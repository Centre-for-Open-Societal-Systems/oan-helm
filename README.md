# COSS Helm repository

Start with the [service catalog](docs/service-catalog.md): it maps every included
COSS service to its chart, source/configuration and enablement status. The
[five editable source charts](charts/README.md) are Farmer, Crop Sown, Livestock,
DA and Commons Services, which contains COSS Consent and Aggregation.

Current chart version is **`1.0.0-dev.2`**, with the migrated new-dev URLs.
The original `1.0.0-dev.1` packages remain available unchanged. Component versions
and image digests are separate; automatic build-number synchronization is deferred.

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

Rancher repository URLs after Pages activation:

- COSS: `https://centre-for-open-societal-systems.github.io/oan-helm/`
- Fork preview: `https://asmitonweb.github.io/oan-helm/`

Enable **GitHub Pages → Source: GitHub Actions** before Rancher can consume
either URL. PR workflows validate only. Pages publication runs on `main` after
merge; this change does not activate Pages, merge the PR or deploy to Kubernetes.

Use the [Rancher guide](docs/rancher-dev.md) and
[new-dev URL migration guide](docs/dev-urls.md), plus the
[readiness table](docs/readiness.md). Published COSS core/Consent images are
pinned by digest. Optional dashboard APIs also have verified images but remain
opt-in for reporting/identity preparation. Dashboard UIs, DA backend/dashboard
workloads and Aggregation remain disabled pending images or configuration.
Private registry pull credentials and live values stay outside Git.
Unconfirmed public endpoints stay unset. Superset/Certify defaults match their
disabled state in the inspected dev release; notifications await confirmed routes.

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
require a new chart version and manifest. No application-repository CI changes
or cluster deployment are included.
