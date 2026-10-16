# COSS Helm repository

Five versioned charts for manual Rancher installation and upgrades: Farmer,
Crop Sown, Livestock, DA and customized Commons Services. Initial chart version
is `1.0.0-dev.1`. Component versions and verified image digests are recorded
separately; automatic build-number synchronization is deferred.

| Location | Contents |
| --- | --- |
| `charts/` | Chart sources and bundled locked dependencies |
| `examples/dev/` | Public dev configuration checklists; no private live values |
| `releases/` | Release manifest, provenance, deployment comparison and validation evidence |
| `docs/` | Five archives, SHA256SUMS and cumulative Helm index for Pages |
| `guides/` | Rancher installation, upgrades and component prerequisites |
| `scripts/validate.py` | Dependency, render, packaging and repository validation |

Rancher repository URLs after Pages activation:

- COSS: `https://centre-for-open-societal-systems.github.io/oan-helm/`
- Fork preview: `https://asmitonweb.github.io/oan-helm/`

Enable **GitHub Pages → Source: GitHub Actions** before Rancher can consume
either URL. PR workflows validate only. Pages publication runs on `main` after
merge; this change does not activate Pages, merge the PR or deploy to Kubernetes.

Use the [Rancher guide](guides/rancher-dev.md) and
[readiness table](guides/readiness.md). Published COSS core/Consent images are
pinned by digest. Optional dashboard APIs also have verified images but remain
opt-in for reporting/identity preparation. Dashboard UIs, DA backend/dashboard
workloads and Aggregation remain disabled pending images or configuration.
Private registry pull credentials and live values stay outside Git.

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
