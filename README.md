# OpenAgriNet (OAN) Helm charts

Helm charts for the OpenAgriNet services that COSS deploys: the Farmer, Crop Sown,
Livestock and DA registries, Commons Services (the shared OpenG2P services plus the
COSS Consent Manager and Aggregation API), the OAN Sandbox, the Grievance service,
A2C and the per-registry dashboards.

This repository is also the Helm repository Rancher installs from. Chart sources live
under `charts/` and `addons/`. A GitHub Actions workflow versions, packages and
publishes them to `repository/` after every merge, so the only way to change what
Rancher sees is a reviewed pull request.

- **Helm repository URL:** `https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/`
- **Latest version of each chart:** [`releases/current.yaml`](releases/current.yaml)
- **What changed in each release:** [`CHANGELOG.md`](CHANGELOG.md)
- **How to contribute:** [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Contents

- [Charts](#charts)
- [How a change reaches a cluster](#how-a-change-reaches-a-cluster)
- [Changing a chart through a pull request](#changing-a-chart-through-a-pull-request)
- [Creating a new chart](#creating-a-new-chart)
- [Versions and releases](#versions-and-releases)
- [Deploying with Rancher or Helm](#deploying-with-rancher-or-helm)
- [Validating locally](#validating-locally)
- [Repository layout and ownership](#repository-layout-and-ownership)
- [Further documentation](#further-documentation)

## Charts

| Chart | Source | Deploys | Dev release / namespace |
| --- | --- | --- | --- |
| `openg2p-farmer-registry` | [charts/openg2p-farmer-registry](charts/openg2p-farmer-registry) | Farmer registry (OpenG2P registry platform with the OAN extension) | `farmer-registry` / `farmer` |
| `openg2p-cropsown-registry` | [charts/openg2p-cropsown-registry](charts/openg2p-cropsown-registry) | Crop Sown registry | `cropsown-registry` / `crop` |
| `openg2p-livestock-registry` | [charts/openg2p-livestock-registry](charts/openg2p-livestock-registry) | Livestock registry | `livestock-registry` / `livestock` |
| `openg2p-da-registry` | [charts/openg2p-da-registry](charts/openg2p-da-registry) | Development Agent registry | not installed |
| `openg2p-commons-services` | [charts/openg2p-commons-services](charts/openg2p-commons-services) | Shared services: IAM, Master Data, AWE, ODK, Partner Management, Consent Manager, Aggregation | `commons-services` / `commons` |
| `oan-sandbox` | [charts/oan-sandbox](charts/oan-sandbox) | OAN Sandbox developer portal (disabled until its images exist) | not installed |
| `oan-grievance-service` | [charts/oan-grievance-service](charts/oan-grievance-service) | Grievance service (Frappe) | `grievance` / `develop`, see [the guide](docs/grievance-service.md) |
| `oan-a2c` | [charts/oan-a2c](charts/oan-a2c) | Access to Credit (Frappe) | `a2c` / `a2c-develop`, see [the guide](docs/a2c.md) |
| `farmer-registry-dashboard`, `cropsown-registry-dashboard`, `livestock-registry-dashboard` | [addons/registry-dashboards](addons/registry-dashboards) | Per-registry dashboard UI and API | per registry |

Farmer, Crop Sown and Livestock were **refactor candidates** whose charts failed
every render at a promotion gate until their refactors were accepted; all three
now install like any other chart. [docs/registry-refactor.md](docs/registry-refactor.md)
describes the gate, kept for the next candidate.
Commons Services passed that gate with Master Data (MDS) `0.0.0-develop.118`: its
catalogue migration was rehearsed against a copy of the new-dev `master_data` database.

[docs/service-catalog.md](docs/service-catalog.md) maps every COSS service to its
chart, values key and source repository.

## How a change reaches a cluster

```
pull request ──► CI: protected paths, unit tests, lint/render/package validation
     │
  review + merge to main
     │
     ▼
release workflow ──► next version for each changed chart, .tgz in repository/,
     │               index.yaml, SHA256SUMS, CHANGELOG.md, tag <chart>-<version>
     ▼
Rancher: refresh repository ──► upgrade the installed app to the new version
```

Merging publishes a chart but **never deploys it**. Every cluster change is a separate,
deliberate Rancher or Helm upgrade by an operator.

## Changing a chart through a pull request

1. **Branch** from `main`, in this repository or a fork.
2. **Edit the chart source**: `values.yaml`, `templates/`, `Chart.yaml` dependencies or
   the chart's `README.md`, under `charts/<chart>/` or `addons/registry-dashboards/<chart>/`.
   - **Image update:** set the new `tag` and `digest` in `values.yaml`. Pin images by digest.
   - **Dependency update:** change the version in `Chart.yaml`, run
     `helm dependency update charts/<chart>` and commit `Chart.lock` together with the
     new `charts/<chart>/charts/<dependency>-<version>.tgz`; delete the old archive.
     Helm re-downloads every dependency, so restore unrelated archives whose bytes
     changed (`git checkout -- charts/<chart>/charts/<other>.tgz`).
   - **Behaviour that installed releases depend on** (resource names, selectors,
     Secret references): if the change is intentional, update
     `releases/resource-baselines-current.json` in the same PR, and explain the
     upgrade impact in the PR and the chart's README.
3. **Leave the version alone.** The release workflow sets it after merge. Set
   `version:` yourself only to choose a different step, such as a minor, `rc` or
   stable version.
4. **Do not touch release outputs:** `repository/`, `releases/artifacts.json`,
   `releases/current.yaml` and `CHANGELOG.md`. CI rejects any PR that does.
5. **Validate locally** (see [Validating locally](#validating-locally)), then open the
   PR. Its commit subjects become the chart's changelog lines, so make them describe
   the behaviour.
6. **Merge** once the `protected-paths` and `validate` checks pass and the change is
   reviewed. The release follows within minutes; watch
   [Actions → Release Helm charts](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/actions/workflows/release.yaml).

## Creating a new chart

1. Create `charts/<name>/`, with the directory name equal to the chart `name` and a
   first version such as `0.1.0-dev.1` in `Chart.yaml`.
2. Add `home`, `sources` and the OAN annotations (`oan.org/owner`,
   `oan.org/chart-source` and, for Rancher, `catalog.cattle.io/display-name`), plus a
   `README.md` that links the application's source repository.
3. Vendor dependencies with `helm dependency update` and commit `Chart.lock` and the
   archives.
4. Add the public dev overlay at `environments/dev/values/<name>.yaml` and, for
   anything non-obvious, a guide under `docs/`.
5. Contract checks: `scripts/validate.py` deep-checks the registry, Commons and Sandbox
   charts (strict lint, two-namespace renders, resource and Secret baselines).
   Register a new chart there when it needs the same guarantees. Every chart must at
   least package with `helm package`.
6. Merge. The first release publishes the version from `Chart.yaml` as it is.

## Versions and releases

Each chart is versioned on its own: changing Farmer releases only Farmer. The release
workflow (`.github/workflows/release.yaml` running `scripts/release.py`):

- compares each chart's source fingerprint with the one sealed for its current version
  in `releases/artifacts.json`;
- raises the version of every changed chart: `1.0.0-dev.16` becomes `1.0.0-dev.17`,
  stable `1.0.0` becomes `1.0.1`; a version already raised in the PR is kept;
- packages the chart into `repository/` and adds only the new entry to `index.yaml`;
- updates `SHA256SUMS`, `releases/artifacts.json`, `releases/current.yaml` and
  `CHANGELOG.md`;
- reruns the full validation, then commits `chore(release): …` to `main` as
  `github-actions[bot]` and pushes the tag `<chart>-<version>`.

Published archives are immutable: validation fails if an existing `.tgz` changes.
`python scripts/release.py --dry-run` shows what a merge would release. Version
rules (when to choose minor, major or stable) are in [docs/versioning.md](docs/versioning.md).

## Deploying with Rancher or Helm

Merging does not deploy anything. Apply a published version to an environment
deliberately, using its current release name, namespace and private values.

### Add the repository (once per cluster)

- **Rancher:** Apps → Repositories → Create → *http(s) URL to an index generated by Helm* →
  the Helm repository URL above (the raw directory URL, not a GitHub `tree` or `blob` page).
- **Helm CLI:**
  ```sh
  helm repo add oan https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/
  helm repo update oan
  ```

After a release, refresh the repository in Rancher (Repositories → ⋮ → Refresh) or run
`helm repo update oan`.

### Install a new release

1. Rancher: Apps → Charts → choose the chart and the **exact version**, including any
   `-dev.N` suffix.
2. Set the release name and namespace deliberately (see the table above).
3. Values: start from `examples/dev/<chart>.yaml`, merge
   `environments/dev/values/<chart>.yaml`, and supply credentials and other private
   settings from the environment's secret process. Never commit private values,
   kubeconfigs or tokens.
4. Make sure the required namespace-local Secrets and image pull Secrets exist, then install.

### Upgrade an existing release

1. Read the chart's [CHANGELOG](CHANGELOG.md) entries and README between the installed
   version and the target, looking for migrations and new required values.
2. Record the release's current version and Helm revision, export its values to a
   private location, and back up the databases and storage it uses:
   ```sh
   helm -n <namespace> history <release>
   helm -n <namespace> get values <release> -o yaml > /private/<release>-values.yaml
   ```
3. Rancher: Apps → Installed Apps → the release → ⋮ → **Upgrade** → the exact target
   version. Keep the saved values and merge in only reviewed changes. Saved literal
   values override new chart defaults, so remove stale overrides (old image tags, old
   hosts) on purpose. Never install a second release over existing resources.
4. Helm CLI equivalent:
   ```sh
   helm upgrade <release> oan/<chart> -n <namespace> --version <version> \
     --reuse-values -f /private/reviewed-changes.yaml -f environments/dev/values/<chart>.yaml \
     --wait --timeout 15m
   ```
5. Commons Services upgrades are one click in Rancher: every Job and hook is safe
   to repeat, following OpenG2P's initialization standard. Follow
   [docs/commons-upgrades.md](docs/commons-upgrades.md). Releases still on older
   charts keep their recorded procedure in
   [docs/rancher-consent-aggregation-status.md](docs/rancher-consent-aggregation-status.md).
   The Farmer dev Jenkins deployment is pinned in
   [`environments/dev/farmer-jenkins.json`](environments/dev/farmer-jenkins.json); a PR
   that updates the pin moves it ([docs/farmer-jenkins-dev.md](docs/farmer-jenkins-dev.md)).

### Verify and roll back

- Check workloads and Jobs, image digests, logs, database connections, IAM login and
  the application's own health endpoints. Confirm that disabled components stay absent.
- Roll back with Rancher (Installed Apps → ⋮ → Rollback) or `helm rollback <release> <revision>`.
  **A rollback does not undo database migrations, seed data or IAM changes**; restore
  those from the backup taken before the upgrade.

The detailed Rancher procedure, with ownership and safety rules, is in
[docs/rancher-dev.md](docs/rancher-dev.md).

## Validating locally

Requires Helm `3.19.0` (set `HELM` if it is not on `PATH`), Python 3.12 and Git. No
Kubernetes access is needed.

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/validate.py --package             # lint, render, baselines, package checks
python scripts/validate_registry_addons.py --package
python scripts/validate.py --online              # also resolve locks against upstream repositories
python scripts/release.py --dry-run              # what a merge would release
python scripts/check_protected_paths.py --base origin/main
```

`validate.py --package` writes scratch archives under `.build/`, and writes into
`repository/` only for versions that have no archive yet. Discard generated changes
before committing: `git checkout -- repository releases`.

## Repository layout and ownership

| Path | Contents | Changed by |
| --- | --- | --- |
| `charts/<chart>/` | Chart sources, including vendored dependency archives | Pull requests |
| `addons/registry-dashboards/<chart>/` | Per-registry dashboard chart sources | Pull requests |
| `environments/dev/` | Public dev overlays, endpoint inventory, Farmer Jenkins pin | Pull requests |
| `examples/dev/` | Public configuration checklists; no private values | Pull requests |
| `scripts/` | Validation, release and environment tooling, with tests | Pull requests |
| `docs/` | Guides and environment records ([index](docs/README.md)) | Pull requests |
| `releases/resource-baselines-current.json` | Resource names, selectors and Secret references installed releases depend on | Pull requests, deliberately |
| `releases/<version>.yaml`, other `releases/*.json` | Historical release-train manifests and environment evidence | Pull requests (historical) |
| `repository/` | **Published Helm repository read by Rancher:** archives, `index.yaml`, `SHA256SUMS` | Release workflow only |
| `releases/artifacts.json`, `releases/current.yaml`, `CHANGELOG.md` | Archive seals, latest versions, release notes | Release workflow only |

The `protected-paths` check enforces the last two rows: a pull request touching them
fails, and on `main` any commit touching them must come from the release bot.
Recommended settings for repository admins: a ruleset on `main` that requires a pull
request and the `protected-paths` and `validate` checks, with GitHub Actions as the
only bypass actor so the release commit can still be pushed.

## Further documentation

[docs/README.md](docs/README.md) indexes every guide: Rancher operations, URL and
domain migration, service onboarding, Consent and Aggregation, eSignet, the APISIX
gateway, Grievance and A2C, logging and the registry refactor. Security reports:
[SECURITY.md](SECURITY.md). Licensing: [LICENSE](LICENSE) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
