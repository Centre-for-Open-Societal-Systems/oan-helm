#!/usr/bin/env bash
# Deliver Commons services to staging from this checkout of main. Run by ci/jenkins/staging-commons.Jenkinsfile on
# every build of main; nothing is built here.
#
#   deliver_staging_commons.sh <secret values file>
#
# 1. The chart is the archive in repository/ named by environments/staging/commons-services.chart, checked against
#    repository/SHA256SUMS.
# 2. Values are environments/staging/values/commons-services.yaml plus the secret values file (a Jenkins secret file
#    with the keys that are not kept in git: the keymanager keystore password and the Enketo secrets).
# 3. What staging runs is recorded in ConfigMap commons-services-delivery (the pin, the sha256 of the values file and
#    of the secret file, and the commit). If the cluster already runs exactly this, nothing is done; otherwise it is
#    delivered, so a failed or skipped delivery is caught up by the next build of main, whatever that merge changed.
# 4. Guard: every key of the release's saved values must be set by the two files, so --reset-values drops nothing.
#    The merged values are rendered by helm itself; only key names are printed.
# 5. A server-side dry run, then helm upgrade --reset-values --atomic --wait: a failed upgrade is rolled back by Helm.
#    A rollback restores the chart and values only; it cannot undo a database change made by a hook. The record is
#    written only after a successful upgrade.
#
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 30m.
set -euo pipefail
secrets=${1:?usage: deliver_staging_commons.sh <secret values file>}
release=commons-services namespace=commons record=commons-services-delivery
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
values="$root/environments/staging/values/commons-services.yaml"
version=$(tr -d '[:space:]' < "$root/environments/staging/commons-services.chart")
name="openg2p-commons-services-$version.tgz"
archive="repository/$name"
test -s "$secrets" || { echo "the secret values file is empty or missing" >&2; exit 1; }
(cd "$root/repository" && grep -E "^[0-9a-f]{64}  $name\$" SHA256SUMS | sha256sum -c --quiet -) \
  || { echo "$archive is missing or does not match repository/SHA256SUMS" >&2; exit 1; }

values_sha=$(sha256sum "$values" | cut -d' ' -f1)
secrets_sha=$(sha256sum "$secrets" | cut -d' ' -f1)
wanted="chart=$version values=$values_sha secrets=$secrets_sha"
running=$(kubectl get configmap "$record" -n "$namespace" -o jsonpath='{.data.delivered}' 2>/dev/null || true)
if [ "$running" = "$wanted" ]; then
  echo "staging already runs $release $version with these values; nothing to deliver"
  exit 0
fi
echo "delivering $release $version (staging runs: ${running:-no record})"

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/merged/templates"
printf 'apiVersion: v2\nname: merged-values\nversion: 0.0.0\n' > "$work/merged/Chart.yaml"
printf '{{ toJson .Values }}\n' > "$work/merged/templates/values.json"
helm template merged "$work/merged" -f "$values" -f "$secrets" --show-only templates/values.json \
  | grep -v -e '^---' -e '^# Source:' > "$work/given.json"
helm get values "$release" -n "$namespace" -o json > "$work/saved.json"
python3 "$root/scripts/ci/commons_values_guard.py" "$work/saved.json" "$work/given.json"

flags=(-n "$namespace" --reset-values -f "$values" -f "$secrets")
helm upgrade "$release" "$root/$archive" "${flags[@]}" --dry-run=server > /dev/null
helm upgrade "$release" "$root/$archive" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-30m}"

commit=$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)
kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$commit" --dry-run=client -o yaml | kubectl apply -f -
echo "delivered $release $version to staging ($commit)"
