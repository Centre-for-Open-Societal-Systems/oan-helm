#!/usr/bin/env bash
# Promote the develop chart of this source tree to staging, deploy it, and publish it. Run by a registry staging pipeline
# in a full checkout of the staging branch. Nothing is built here.
#
#   deliver_staging.sh <chart> <release> <namespace> <overlay file in environments/staging/values/> [helm flags]
#
# Further arguments go to helm upgrade, after the overlay: a registry's own value layers or its post-renderer.
#
# 1. promote_chart.py adds the rc tag to the images New Dev ran and packages the rc chart. It fails if develop never
#    built this source tree.
# 2. helm upgrade --install with --reset-values and the staging overlay only, so saved values cannot override the images
#    of the chart. Hooks run as on New Dev.
# 3. If the upgrade fails on a release that had a deployed revision, Helm is rolled back to it. A rollback restores the
#    chart and values only; it cannot undo a database change made by a hook. Nothing is published after a failure.
# 4. publish_chart.py adds the same archive to repository/staging/ of oan-helm.
#
# Needs KUBECONFIG, AWS credentials for ECR and GH_TOKEN. HELM_TIMEOUT defaults to 30m.
set -euo pipefail
chart=$1 release=$2 namespace=$3 overlay=$4
shift 4
here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
values="$here/../../environments/staging/values/$overlay"
test -f "$values" || { echo "no staging values $overlay in oan-helm" >&2; exit 1; }

python3 "$here/promote_chart.py" --chart "$chart" --release "$release" --namespace "$namespace" \
  --overlay "environments/staging/values/$overlay" --output built-chart
archive=$(ls built-chart/*.tgz)
echo "promoted $(basename "$archive")"

# A first install has no history, and helm history fails.
previous=$(helm history "$release" -n "$namespace" -o json 2>/dev/null | python3 -c '
import json, sys
try:
    deployed = [r["revision"] for r in json.load(sys.stdin) if r["status"] in ("deployed", "superseded")]
except ValueError:
    deployed = []
print(deployed[-1] if deployed else "")' || true)

if ! helm upgrade --install "$release" "$archive" -n "$namespace" --create-namespace --reset-values -f "$values" "$@" \
    --wait --timeout "${HELM_TIMEOUT:-30m}"; then
  echo "the upgrade of $release failed" >&2
  kubectl get pods -n "$namespace" || true
  if [ -n "$previous" ]; then
    echo "rolling back to revision $previous" >&2
    helm rollback "$release" "$previous" -n "$namespace" --wait --timeout 15m || echo "the rollback failed too" >&2
  fi
  exit 1
fi

# A rerun of the same source promotes the same rc version, and a published version is never replaced (exit 4).
status=0
python3 "$here/publish_chart.py" "$archive" || status=$?
case $status in
  0|4) ;;
  *) exit "$status" ;;
esac
