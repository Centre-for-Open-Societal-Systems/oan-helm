#!/usr/bin/env bash
# Deliver the odk-bootstrap release (namespace commons) to New Dev from this checkout of main.
# Run by ci/jenkins/dev-commons.Jenkinsfile after Commons services, which run ODK Central: its hook Job makes sure each
# registry's Central project has the test-submission app user on its published forms and keeps the token in a Secret
# (addons/odk-bootstrap, values environments/dev/values/odk-bootstrap.yaml).
#
# What New Dev runs is recorded in ConfigMap odk-bootstrap-delivery (sha256 of the chart directory and of the values).
# If it matches this commit nothing is done, so a failed delivery is retried by the next build of main.
# helm upgrade --install --reset-values --atomic --wait: a failed upgrade is rolled back by Helm.
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 15m (the Job itself stops after 900 s).
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
release=odk-bootstrap namespace=commons record=odk-bootstrap-delivery
chart="$root/addons/odk-bootstrap"
values="$root/environments/dev/values/odk-bootstrap.yaml"

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
if ! helm upgrade --install "$release" "$chart" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-15m}"; then
  # The hook Job is kept until the next delivery (hook-delete-policy before-hook-creation), so its log is still here.
  # The bootstrap script prints registry, project and app-user states and error messages; never a password or token.
  echo "odk-bootstrap failed; log of job/$release:"
  kubectl logs "job/$release" -n "$namespace" --all-containers --tail=50 || true
  exit 1
fi

kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)" --dry-run=client -o yaml \
  | kubectl apply -f -
echo "delivered $release: $wanted"
