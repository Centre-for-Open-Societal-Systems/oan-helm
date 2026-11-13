#!/usr/bin/env bash
# Deliver the Commons Postgres superuser rotation (release commons-postgres-superuser-rotation, namespace commons) to
# staging from this checkout of main. Run by ci/jenkins/staging-commons.Jenkinsfile after the Commons base release and
# before Commons services, so the services delivery already reads the rotated value.
#
# What staging runs is recorded in ConfigMap commons-postgres-superuser-rotation-delivery (sha256 of the chart
# directory and of the staging values). If it matches this commit nothing is done. The chart itself rotates only when
# rotation.id is new (its Job records the done id), so redelivering never rotates twice.
# helm upgrade --install --reset-values --atomic --wait: a failed rotation Job fails the upgrade. The Job resumes a
# half-done rotation with the password it kept in Secret commons-postgres-superuser-rotation-pending.
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 10m.
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
release=commons-postgres-superuser-rotation namespace=commons record=commons-postgres-superuser-rotation-delivery
chart="$root/addons/commons-postgres-superuser-rotation"
values="$root/environments/staging/values/commons-postgres-superuser-rotation.yaml"

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
# The Job's log is the proof (old password refused, new accepted, copies written); it holds no secret.
kubectl logs -n "$namespace" "job/$release" --all-containers --prefix 2>/dev/null || true

kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)" --dry-run=client -o yaml \
  | kubectl apply -f -
echo "delivered $release: $wanted"
