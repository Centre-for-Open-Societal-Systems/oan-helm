#!/usr/bin/env bash
# Deliver the Commons ECR pull-secret refresher (release commons-ecr-pull-secret, namespace commons) to staging from this
# checkout of main. Run by ci/jenkins/staging-commons.Jenkinsfile before the other Commons releases, so their pods can
# pull. Recorded in ConfigMap commons-ecr-pull-secret-delivery (sha256 of the chart directory and the staging values);
# nothing is done when it matches. helm upgrade --install --reset-values --atomic --wait --wait-for-jobs.
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 10m.
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
release=commons-ecr-pull-secret namespace=commons record=commons-ecr-pull-secret-delivery
chart="$root/addons/commons-ecr-pull-secret"
values="$root/environments/staging/values/commons-ecr-pull-secret.yaml"

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
helm upgrade --install "$release" "$chart" "${flags[@]}" --atomic --wait --wait-for-jobs --timeout "${HELM_TIMEOUT:-10m}"
kubectl logs -n "$namespace" "job/$release-refresh-init" -c write-secret 2>/dev/null || true

kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)" --dry-run=client -o yaml \
  | kubectl apply -f -
echo "delivered $release: $wanted"
