#!/usr/bin/env bash
# Install or upgrade the staging dashboards with Helm, from a checkout of this repository. The dashboard API of each
# registry comes with its registry chart; these are the dashboard UIs and the shared oan-dashboards. Each release keeps
# its own ECR pull secret and Keycloak client. --atomic restores the previous revision when an upgrade fails (a failed first
# install is removed). Manual rollback: helm rollback <release> -n <namespace>, see docs/rollback.md.
set -euo pipefail
cd "$(dirname "$0")/../.."
values=environments/staging/values

deliver() {
  helm upgrade --install "$1" "$3" --namespace "$2" --values "$4" --reset-values --atomic --wait --timeout 10m
}

deliver farmer-registry-dashboard farmer repository/farmer-registry-dashboard-0.1.2.tgz "$values/farmer-dashboard.yaml"
deliver cropsown-registry-dashboard crop repository/cropsown-registry-dashboard-0.1.2.tgz "$values/cropsown-dashboard.yaml"
deliver livestock-registry-dashboard live repository/livestock-registry-dashboard-0.1.2.tgz "$values/livestock-dashboard.yaml"
deliver oan-dashboards commons addons/oan-dashboards "$values/oan-dashboards.yaml"
