# Contributing

Every change to this repository goes through a pull request to `main`. Rancher installs
from `repository/`, which only the release workflow writes, so a reviewed and merged PR
is the only way to publish a chart.

## Rules

1. **Change sources, not release outputs.** Edit `charts/`, `addons/`, `environments/`,
   `examples/`, `scripts/` or `docs/`. Never edit `repository/`,
   `releases/artifacts.json`, `releases/current.yaml` or `CHANGELOG.md`; the
   `protected-paths` check fails any PR that does.
2. **Do not bump chart versions** unless you need a specific step (minor, `rc`,
   stable). After merge, the release workflow gives each changed chart its next
   version, packages it and writes its changelog entry.
3. **No secrets.** No passwords, tokens, kubeconfigs, private values or live Helm value
   exports. Charts reference existing Secrets by name and key.
4. **Pin what you deploy.** Images by digest; dependencies by exact version with
   `Chart.lock` and the vendored archive committed.
5. **Preserve installed releases.** Changing resource names, selectors or Secret
   references breaks upgrades. When a change does so on purpose, update
   `releases/resource-baselines-current.json` and describe the upgrade steps in the PR
   and the chart's README.
6. **Describe the behaviour.** Commit subjects become the chart's changelog lines.
7. **Use LF line endings.** Packaging rejects CRLF in chart sources.

## Workflow

```sh
git switch -c <topic> origin/main
# edit charts/<chart>/...
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/validate.py --package
python scripts/validate_registry_addons.py --package
python scripts/release.py --dry-run          # charts the merge will release
git checkout -- repository releases          # drop files the local validation generated
```

Open the PR and fill in its template. It needs green `protected-paths` and `validate`
checks and a review. After merge, `.github/workflows/release.yaml` publishes the
release; follow the [README](README.md#deploying-with-rancher-or-helm) to deploy it.

## Updating a dependency

```sh
# change the dependency version in charts/<chart>/Chart.yaml
helm dependency update charts/<chart>
git status charts/<chart>/charts
```

Commit `Chart.lock` and the new archive, delete the old archive, and restore any
unrelated archive whose bytes changed on re-download
(`git checkout -- charts/<chart>/charts/<other>.tgz`).

## Release workflow failures

If the release workflow fails after a merge, nothing is published. Fix the cause in a
new PR; the next release picks up every chart that changed since its last published
version. To rerun without a change, use *Run workflow* on
[Release Helm charts](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/actions/workflows/release.yaml).
