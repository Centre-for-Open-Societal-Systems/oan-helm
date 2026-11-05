#!/usr/bin/env bash
# Derive the version of the current commit for a registry repository.
#
# openg2p-derive-version.sh is OpenG2P's versioning policy, copied unchanged from
# OpenG2P/openg2p-packaging (ci/version/derive-version.sh, MPL-2.0). OpenG2P's release
# line is a branch named N.N; OAN calls that branch staging, so staging is versioned
# as the line in RELEASE_LINE (default 1.0). Every other ref follows the policy as it is.
#
#   develop      0.0.0-develop.<n>
#   staging      <line>.<next>-rc.<n>
#   tag N.N.N    N.N.N
#   anything     0.0.0-<slug>.<n>, chart not published
set -euo pipefail
here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ref_name="${REF_NAME:-${GITHUB_REF_NAME:-}}"
ref_type="${REF_TYPE:-${GITHUB_REF_TYPE:-branch}}"
if [ "$ref_type" = branch ] && [ "$ref_name" = staging ]; then
  ref_name="${RELEASE_LINE:-1.0}"
fi
REF_NAME="$ref_name" REF_TYPE="$ref_type" exec bash "$here/openg2p-derive-version.sh"
