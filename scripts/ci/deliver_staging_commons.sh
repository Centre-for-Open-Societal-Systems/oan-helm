#!/usr/bin/env bash
# Deliver Commons services to staging from this checkout of main. Run by ci/jenkins/staging-commons.Jenkinsfile after a
# merge that changes the staging Commons values or the pinned chart; nothing is built here.
#
#   deliver_staging_commons.sh <secret values file>
#
# 1. The chart is the archive in repository/ named by environments/staging/commons-services.chart, checked against
#    repository/SHA256SUMS.
# 2. Values are environments/staging/values/commons-services.yaml plus the secret values file (a Jenkins secret file
#    with the keys that are not kept in git: the keymanager keystore password and the Enketo secrets).
# 3. Guard: every key of the release's saved values must be in those two files, so --reset-values drops nothing.
#    Only key names are printed.
# 4. A server-side dry run, then helm upgrade --reset-values --atomic --wait: a failed upgrade is rolled back by Helm.
#    A rollback restores the chart and values only; it cannot undo a database change made by a hook.
#
# Needs KUBECONFIG. HELM_TIMEOUT defaults to 30m.
set -euo pipefail
secrets=${1:?usage: deliver_staging_commons.sh <secret values file>}
release=commons-services namespace=commons
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
values="$root/environments/staging/values/commons-services.yaml"
version=$(tr -d '[:space:]' < "$root/environments/staging/commons-services.chart")
name="openg2p-commons-services-$version.tgz"
archive="repository/$name"
test -s "$secrets" || { echo "the secret values file is empty or missing" >&2; exit 1; }
(cd "$root/repository" && grep -E "^[0-9a-f]{64}  $name\$" SHA256SUMS | sha256sum -c --quiet -) \
  || { echo "$archive is missing or does not match repository/SHA256SUMS" >&2; exit 1; }

saved=$(mktemp)
trap 'rm -f "$saved"' EXIT
helm get values "$release" -n "$namespace" -o json > "$saved"
python3 "$root/scripts/ci/commons_values_guard.py" "$saved" "$values" "$secrets"

flags=(-n "$namespace" --reset-values -f "$values" -f "$secrets")
helm upgrade "$release" "$root/$archive" "${flags[@]}" --dry-run=server > /dev/null
helm upgrade "$release" "$root/$archive" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-30m}"
echo "delivered $release $version to staging"
