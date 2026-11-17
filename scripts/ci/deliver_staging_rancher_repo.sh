#!/usr/bin/env bash
# Register the OAN staging Helm repository in Rancher on staging (ClusterRepo oan-staging,
# environments/staging/rancher/oan-staging-clusterrepo.yaml) from this checkout of main. Run by
# ci/jenkins/staging-commons.Jenkinsfile. kubectl apply is idempotent; a server-side dry run comes first.
# Needs KUBECONFIG (the Commons deployer, with environments/staging/rbac/commons-deployer-rancher-repo-rbac.yaml).
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
repo="$root/environments/staging/rancher/oan-staging-clusterrepo.yaml"

kubectl apply -f "$repo" --dry-run=server > /dev/null
kubectl apply -f "$repo"
url=$(kubectl get clusterrepo oan-staging -o jsonpath='{.spec.url}')
echo "Rancher repository oan-staging: $url"
