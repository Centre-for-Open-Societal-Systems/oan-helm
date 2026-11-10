#!/usr/bin/env bash
# Deliver the Commons base release (commons, chart openg2p-commons-base) to staging from this checkout of main.
# Run by ci/jenkins/staging-commons.Jenkinsfile on every build of main, before Commons services.
#
#   deliver_staging_commons_base.sh
#
# 1. The chart is the OpenG2P archive named by environments/staging/commons-base.chart ("<version> <sha256>"),
#    downloaded from the OpenG2P Helm repository and checked against that sha256. OpenG2P can republish a version, so
#    the hash, not the version, decides what is delivered.
# 2. Values: the release keeps its saved values (a full copy of the chart defaults with the staging passwords), and
#    environments/staging/values/commons-base.yaml is applied over them with --reuse-values. The saved values cannot be
#    rebuilt from git, so --reset-values is never used here.
# 3. --reuse-values does not pick up the defaults of a new chart version, so this delivers only the version the
#    release already runs. A chart version change is a reviewed manual upgrade; after it, the pin is moved to match.
# 4. What staging runs is recorded in ConfigMap commons-base-delivery (pin, archive sha256, sha256 of the overlay,
#    commit). If the cluster already runs exactly this, nothing is done; otherwise it is delivered, so a failed or
#    skipped delivery is caught up by the next build of main.
# 5. A server-side dry run, then helm upgrade --reuse-values --atomic --wait: a failed upgrade is rolled back by Helm.
#    The record is written only after a successful upgrade.
#
# Needs KUBECONFIG, helm, kubectl and curl. HELM_TIMEOUT defaults to 30m.
set -euo pipefail
release=commons namespace=commons record=commons-base-delivery chart=openg2p-commons-base
repository=${OPENG2P_HELM_REPOSITORY:-https://openg2p.github.io/openg2p-helm}
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
values="$root/environments/staging/values/commons-base.yaml"
read -r version sha < "$root/environments/staging/commons-base.chart" || true  # a missing final newline must not stop the script; the check below decides
[[ "$version" && "$sha" =~ ^[0-9a-f]{64}$ ]] || { echo "environments/staging/commons-base.chart must be '<version> <sha256>'" >&2; exit 1; }

values_sha=$(sha256sum "$values" | cut -d' ' -f1)
wanted="chart=$version archive=$sha values=$values_sha"
running=$(kubectl get configmap "$record" -n "$namespace" -o jsonpath='{.data.delivered}' 2>/dev/null || true)
if [ "$running" = "$wanted" ]; then
  echo "staging already runs $release $chart-$version with these values; nothing to deliver"
  exit 0
fi

installed=$(helm list -n "$namespace" --filter "^$release\$" -o json | python3 -c 'import json,sys; r=json.load(sys.stdin); print(r[0]["chart"] if r else "")')
if [ "$installed" != "$chart-$version" ]; then
  echo "release $release runs '${installed:-nothing}', the pin is $chart-$version: --reuse-values cannot change the chart" \
       "version safely. Upgrade by hand (reviewed), then move environments/staging/commons-base.chart." >&2
  exit 1
fi
echo "delivering $release $chart-$version (staging runs: ${running:-no record})"

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
archive="$work/$chart-$version.tgz"
curl -fsSL --retry 3 -o "$archive" "$repository/$chart-$version.tgz"
echo "$sha  $archive" | sha256sum -c --quiet - \
  || { echo "$chart-$version.tgz from $repository does not match the pinned sha256" >&2; exit 1; }

flags=(-n "$namespace" --reuse-values -f "$values")
helm upgrade "$release" "$archive" "${flags[@]}" --dry-run=server > /dev/null
helm upgrade "$release" "$archive" "${flags[@]}" --atomic --wait --timeout "${HELM_TIMEOUT:-30m}"

commit=$(git -C "$root" rev-parse HEAD 2>/dev/null || echo unknown)
kubectl create configmap "$record" -n "$namespace" --from-literal=delivered="$wanted" \
  --from-literal=commit="$commit" --dry-run=client -o yaml | kubectl apply -f -
echo "delivered $release $chart-$version to staging ($commit)"
