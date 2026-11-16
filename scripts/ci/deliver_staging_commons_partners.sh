#!/usr/bin/env bash
# Deliver the commons-partners release (namespace commons) to staging from this checkout of main.
# Run by ci/jenkins/staging-commons.Jenkinsfile after Commons services: its hook Job makes sure the partners the registries
# rely on (PARTNER_STAFF_PORTAL, the sender of staff file imports) exist and are active in Partner Management.
#
# What staging runs is recorded in ConfigMap commons-partners-delivery (sha256 of the chart directory and of the staging
# values). If it matches this commit nothing is done, so a failed delivery is retried by the next build of main.
# helm upgrade --install --reset-values --atomic --wait: a failed upgrade is rolled back by Helm.
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 10m.
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
release=commons-partners namespace=commons record=commons-partners-delivery
chart="$root/addons/commons-partners"
values="$root/environments/staging/values/commons-partners.yaml"

chart_sha=$(cd "$chart" && find . -type f | LC_ALL=C sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
values_sha=$(sha256sum "$values" | cut -d' ' -f1)
wanted="chart=$chart_sha values=$values_sha"
running=$(kubectl get configmap "$record" -n "$namespace" -o jsonpath='{.data.delivered}' 2>/dev/null || true)
if [ "$running" = "$wanted" ]; then
  echo "staging already runs $release with these values; nothing to deliver"
  exit 0
fi
echo "delivering $release (staging runs: ${running:-no record})"

flags=(-n "$namespace" --reset-values -f "$values")
helm upgrade --install "$release" "$chart" "${flags[@]}" --dry-run=server > /dev/null
helm upgrade --install "$release" "$chart" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-10m}"

kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)" --dry-run=client -o yaml \
  | kubectl apply -f -
echo "delivered $release: $wanted"
