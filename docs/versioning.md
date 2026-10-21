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

- A maintainer chooses and records the next version in the PR before packaging.
  A merge, calendar date or cluster upgrade does not assign it automatically.
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

This repository currently publishes the five charts together under one release
version, enforced by `scripts/validate.py` and `releases/current.yaml`. Keep that
release train consistent until per-chart versioning is explicitly introduced.
Publishing together does not require upgrading every installed release.

## Publication and promotion

1. Record the version, changes, compatibility impact, prerequisites and any
   migrations in `releases/<version>.yaml`; update all five `Chart.yaml` versions,
   `releases/current.yaml` and the preserved resource baseline for this release.
2. Verify image availability/digests and locked dependencies. Run strict lint,
   representative renders, namespace/ownership/Secret checks, regression checks
   and exact package/installability validation. Rehearse material migrations.
3. Package once, retain source seals/checksums and add entries to the cumulative
   relative-URL index. Existing archives remain unchanged. CI validates the PR;
   publication to the fork is preview, and upstream merge publishes to main.
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
