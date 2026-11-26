#!/usr/bin/env bash
# Deliver the oan-messaging release (namespace commons) to New Dev from this checkout of main.
# Run by ci/jenkins/dev-commons.Jenkinsfile after the Commons services (Keycloak, IAM, PostgreSQL are theirs): the
# release brings the messaging service, its database on the shared PostgreSQL, the staff console, the Keycloak
# client, role and staff-portal tile (addons/oan-messaging, values environments/dev/values/oan-messaging.yaml).
# The image tags in those values are moved by the Jenkins jobs oan-messaging-service and oan-messaging-ui, which open
# a pull request here after each develop build (scripts/ci/pin_image_in_oan_helm.py in those repositories).
#
# What New Dev runs is recorded in ConfigMap oan-messaging-delivery (sha256 of the chart directory and of the values).
# If it matches this commit nothing is done, so a failed delivery is retried by the next build of main.
# helm upgrade --install --reset-values --atomic --wait: a failed upgrade is rolled back by Helm. Saved values are never reused.
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 20m (the hooks stop after 15 min each at most).
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
release=oan-messaging namespace=commons record=oan-messaging-delivery
chart="$root/addons/oan-messaging"
values="$root/environments/dev/values/oan-messaging.yaml"

chart_sha=$(cd "$chart" && find . -type f | LC_ALL=C sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
values_sha=$(sha256sum "$values" | cut -d' ' -f1)
wanted="chart=$chart_sha values=$values_sha"
running=$(kubectl get configmap "$record" -n "$namespace" -o jsonpath='{.data.delivered}' 2>/dev/null || true)
if [ "$running" = "$wanted" ]; then
  echo "New Dev already runs $release with these values; nothing to deliver"
  exit 0
fi
echo "delivering $release (New Dev runs: ${running:-no record})"

flags=(-n "$namespace" --reset-values -f "$values")
helm upgrade --install "$release" "$chart" "${flags[@]}" --dry-run=server > /dev/null
if ! helm upgrade --install "$release" "$chart" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-20m}"; then
  # Hook Jobs are kept until the next delivery (before-hook-creation), so their logs are still here. The scripts print
  # states and error messages; never a password, key or token.
  for job in init-secrets db-init migration grants callers; do
    echo "log of job/$release-$job:"
    kubectl logs "job/$release-$job" -n "$namespace" --all-containers --tail=30 || true
  done
  exit 1
fi

kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)" --dry-run=client -o yaml \
  | kubectl apply -f -
echo "delivered $release: $wanted"
