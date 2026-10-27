# Chart versioning and release guidelines

Use **`MAJOR.MINOR.PATCH-prerelease.number`**, for example `1.0.1-dev.1`.
`1.0.1.dev1` is not the Semantic Versioning form used by these charts.

The chart version identifies an immutable installation package: templates,
defaults, dependency locks, bundled dependencies and chart-owned documentation.
It is separate from application image tags/digests, the upstream Commons
`appVersion`, source commits and the installed Helm release revision.

## Choosing the next version

| Situation | Example next version | Meaning |
| --- | --- | --- |
| Another development package for the current unreleased 1.0.0 baseline | `1.0.0-dev.6` to `1.0.0-dev.7` | Continue the same development series |
| Baseline ready for release-candidate validation | `1.0.0-rc.1` | Candidate package; still a prerelease |
| Release candidate accepted | `1.0.0` | First stable chart contract |
| Compatible fix after stable 1.0.0 | `1.0.1-dev.1`, then `1.0.1` | Patch: correct behavior without changing the chart contract |
| Compatible feature after stable 1.0.0 | `1.1.0-dev.1`, then `1.1.0` | Minor: add a supported optional workload or setting while retaining existing behavior |
| Incompatible upgrade contract | `2.0.0-dev.1`, then `2.0.0` | Major: for example, remove supported values or require resource/ownership migration |

The `dev` counter resets for a new target version. Use numeric identifiers
without leading zeroes. A prerelease sorts before its corresponding stable
version. Do not use build metadata alone to distinguish packages that Rancher
must select or upgrade independently.

Currently **1.0.0 has not been released as stable**. The portal is part of the
initial baseline, so the current package remains in the `1.0.0-dev.N` series.
If the same optional portal were added after stable `1.0.0`, it would normally
be a `1.1.0-dev.1` feature release, rather than a patch release.

For chart compatibility, review existing value names/defaults, Kubernetes
versions, required Secrets/permissions, dependency behavior, resource names,
selectors, ownership and upgrade/migration steps. An application or dependency
upgrade is not automatically a patch: classify its effect on that contract.

## When a version changes

- Merging a change to a chart's source into `main` gives that chart its next
  version automatically (see [Automatic release](#automatic-release)). To choose
  a different version, such as a minor or `rc` step, set it in the PR's
  `Chart.yaml`; the release packages that version as it is.
- Any change inside a published chart source requires a new chart version and
  archive. A new default image digest is a chart change too. Never replace an
  existing archive/tag, alter its checksum or repoint its index entry.
- Repository-only guides, external examples or test tooling do not by themselves
  require new chart packages. Chart-bundled README changes do, because they alter
  the archive. Private value changes can create a new Helm revision without
  changing the chart version when the existing chart already supports them.
- Rebuilding an application image alone does not require a chart release unless
  the chart's pinned references or deployment contract change. Record each
  component's real source commit and immutable digest separately; they do not
  share a synchronized build number.

Each chart is versioned on its own: changing Farmer releases only Farmer.
Charts up to `1.0.0-dev.16` were published together as one release train, whose
notes remain under `releases/<version>.yaml`. `releases/current.yaml` lists the
latest version of every chart.

## Automatic release

`.github/workflows/release.yaml` runs `scripts/release.py` on every push to
`main` that touches `charts/` or `addons/registry-dashboards/`:

1. Each chart's source fingerprint is compared with the one recorded in
   `releases/artifacts.json` for its current version's archive.
2. A changed chart's version is raised: `1.0.0-dev.16` becomes `1.0.0-dev.17`,
   a stable `1.0.0` becomes `1.0.1`. A version already raised in the PR, with
   no archive yet, is kept.
3. The chart is packaged into `repository/`, added to `index.yaml` (existing
   entries are left untouched) and `SHA256SUMS`, and sealed in `artifacts.json`.
4. `CHANGELOG.md` gets an entry listing the commits that touched the chart since
   its previous archive.
5. The full validation runs, then `github-actions[bot]` commits
   `chore(release): ...` to `main` and pushes a `<chart>-<version>` tag.

Pull requests may not edit `repository/`, `releases/artifacts.json`,
`releases/current.yaml` or `CHANGELOG.md`; the `protected-paths` check enforces
this. PR validation accepts a chart whose source changed without a version bump and
reports it as unreleased: it packages a scratch archive to verify, but does not
publish it. Run `python scripts/release.py --dry-run` to see what a merge would
release. Upstream resource identities, selectors and Secret references are
compared with `releases/resource-baselines-current.json`; update it in the same
PR when a change intentionally alters them.

## Publication and promotion

1. Describe compatibility impact, prerequisites and migrations in the PR, and
   for material changes in the chart's README.
2. Verify image availability/digests and locked dependencies (`helm dependency
   update` and commit `Chart.lock` with the bundled archive). Rehearse material
   migrations.
3. Merge. The release workflow versions, packages, indexes and records the chart;
   existing archives remain unchanged. Refresh the Rancher repository to see it.
4. Before promoting to stable, accept the intended supported chart contract and
   the upgrade/recovery evidence. Clearly identify disabled optional components
   and untested application integrations. A stable chart does not imply every
   optional application workflow is configured in every environment.
5. Upgrade each intended existing release explicitly, using its current name and
   namespace, private configuration, backup and reviewed manifest comparison.
   Rancher repository refresh or a Git merge does not deploy it. Helm revision
   numbers count release operations and are not chart versions.

These are the repository's release conventions, based on
[Helm chart versioning](https://helm.sh/docs/topics/charts/#charts-and-versioning)
and [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).
