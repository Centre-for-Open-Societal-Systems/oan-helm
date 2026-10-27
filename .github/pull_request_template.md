## What changes

<!-- Which charts or files, and what behaviour changes for an installed release. -->

## Upgrade impact

<!-- New required values, migrations, renamed resources, Secret changes, or "none". -->

## Checklist

- [ ] Only chart sources, overlays, scripts or docs changed; no `repository/`, `releases/artifacts.json`, `releases/current.yaml` or `CHANGELOG.md`
- [ ] Chart versions left for the release workflow (or a specific version set on purpose)
- [ ] Images pinned by digest; dependency changes include `Chart.lock` and the vendored archive
- [ ] No secrets, private values or kubeconfigs
- [ ] `python scripts/validate.py --package` and the unit tests pass locally
- [ ] Resource-name, selector or Secret-reference changes are intentional, with `releases/resource-baselines-current.json` updated
