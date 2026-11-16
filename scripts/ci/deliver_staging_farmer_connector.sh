#!/usr/bin/env bash
# Install or upgrade the Farmer connector on staging with Helm, from a checkout of this repository.
# Credentials go first because the database setup job and the workloads read their Secrets.
# Rollback: helm rollback farmer-registry-connector -n farmer, see docs/rollback.md.
#
# Further arguments go to the connector upgrade, after the staging values: the Farmer staging pipeline passes the
# images of the promoted build (--values <override>), so the image pinned in farmer-connector.yaml is only the fallback.
set -euo pipefail
cd "$(dirname "$0")/../.."
values=environments/staging/values

helm upgrade --install farmer-connector-credentials addons/farmer-connector-credentials --namespace farmer \
  --values "$values/farmer-connector-credentials.yaml" --reset-values --atomic --wait --timeout 3m
helm upgrade --install farmer-registry-connector addons/farmer-connector --namespace farmer \
  --values "$values/farmer-connector.yaml" "$@" --reset-values --atomic --wait --timeout 10m
