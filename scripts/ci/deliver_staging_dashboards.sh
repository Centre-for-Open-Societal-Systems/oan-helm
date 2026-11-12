#!/usr/bin/env bash
# Install or upgrade the staging dashboards with Helm, from a checkout of this repository. The dashboard API of each
# registry comes with its registry chart; these are the dashboard UIs and the shared oan-dashboards. Each release keeps
# its own ECR pull secret and Keycloak client. --atomic restores the previous revision when an upgrade fails (a failed first
# install is removed). Manual rollback: helm rollback <release> -n <namespace>, see docs/rollback.md.
#
#   deliver_staging_dashboards.sh [farmer] [cropsown] [livestock] [oan-dashboards]     (no argument: all four)
#
# Who runs it, each with a kubeconfig that has rights in that namespace only:
#   oan-dashboards (commons)  ci/jenkins/staging-commons.Jenkinsfile, ServiceAccount commons/commons-deployer
#   farmer / cropsown / livestock dashboard UI   each registry's staging pipeline, after its promotion
set -euo pipefail
cd "$(dirname "$0")/../.."
values=environments/staging/values

deliver() {
  helm upgrade --install "$1" "$3" --namespace "$2" --values "$4" --reset-values --atomic --wait --timeout 10m
}

[ "$#" -gt 0 ] || set -- farmer cropsown livestock oan-dashboards
for name in "$@"; do
  case "$name" in
    farmer) deliver farmer-registry-dashboard farmer repository/farmer-registry-dashboard-0.1.2.tgz "$values/farmer-dashboard.yaml" ;;
    cropsown) deliver cropsown-registry-dashboard crop repository/cropsown-registry-dashboard-0.1.2.tgz "$values/cropsown-dashboard.yaml" ;;
    livestock) deliver livestock-registry-dashboard live repository/livestock-registry-dashboard-0.1.2.tgz "$values/livestock-dashboard.yaml" ;;
    oan-dashboards) deliver oan-dashboards commons addons/oan-dashboards "$values/oan-dashboards.yaml" ;;
    *) echo "unknown dashboard $name (farmer, cropsown, livestock, oan-dashboards)" >&2; exit 2 ;;
  esac
done
