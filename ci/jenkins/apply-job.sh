#!/usr/bin/env bash
# Create or update a Jenkins job from its definition in ci/jenkins/jobs/<name>.xml, so jobs come from git and are never
# put together in the UI.
#
#   JENKINS_URL=https://jenkins.oanstaging.com JENKINS_USER=... JENKINS_TOKEN=... ci/jenkins/apply-job.sh <name> [credential-id ...]
#
# Each credential id given must already exist in the Jenkins system store; the script checks ids only (never values)
# and stops before touching the job if one is missing, so the first build cannot fail on a missing credential.
# Creating the job triggers its first branch scan, which builds main. Updating an existing job replaces its config.
set -euo pipefail
name=${1:?usage: apply-job.sh <job name> [required credential id ...]}
shift
: "${JENKINS_URL:?}" "${JENKINS_USER:?}" "${JENKINS_TOKEN:?}"
config="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/jobs/$name.xml"
test -s "$config" || { echo "no job definition $config" >&2; exit 1; }
auth=(-u "$JENKINS_USER:$JENKINS_TOKEN")
api() { curl -sS --fail-with-body "${auth[@]}" "$@"; }

ids=$(api "$JENKINS_URL/credentials/store/system/domain/_/api/json?tree=credentials%5Bid%5D")
for id in "$@"; do
  grep -q "\"id\":\"$id\"" <<< "$ids" || { echo "Jenkins credential $id is missing; create it first (see the job's Jenkinsfile header)" >&2; exit 1; }
  echo "credential $id: present"
done

crumb=$(api "$JENKINS_URL/crumbIssuer/api/json" | python3 -c 'import json,sys; c=json.load(sys.stdin); print(c["crumbRequestField"]+":"+c["crumb"])')
code=$(curl -sS -o /dev/null -w '%{http_code}' "${auth[@]}" "$JENKINS_URL/job/$name/config.xml")
if [ "$code" = 200 ]; then
  api -X POST -H "$crumb" -H 'Content-Type: application/xml' --data-binary @"$config" "$JENKINS_URL/job/$name/config.xml" > /dev/null
  echo "updated job $name from $config"
else
  api -X POST -H "$crumb" -H 'Content-Type: application/xml' --data-binary @"$config" "$JENKINS_URL/createItem?name=$name" > /dev/null
  echo "created job $name from $config"
fi
