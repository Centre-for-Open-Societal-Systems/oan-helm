# Changelog

Chart releases, newest first. Each entry is written by `scripts/release.py`
when a merge to `main` changes a chart: the chart gets its next version, its
archive is added to `repository/`, and the commits that touched it are listed
here. Releases up to `1.0.0-dev.16` were published as one release train; their
notes are under `releases/<version>.yaml`.

<!-- Releases are inserted below this line by scripts/release.py. -->

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- chore: remove the Master Data snapshot and Crop lookup reference (a7c0f1d)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- fix(commons): vendor the published Master Data develop.118 dependency (2008980)
- Change repository and version for master-data dependency (e5e405f)
