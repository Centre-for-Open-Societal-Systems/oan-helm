set -u
log() { echo "[lease-renewal] $*"; }
token() { # url client_id client_secret -> access token
  curl -sS --fail-with-body -X POST "$1" \
    --data-urlencode grant_type=client_credentials \
    --data-urlencode "client_id=$2" --data-urlencode "client_secret=$3" \
    | sed -n 's/.*"access_token" *: *"\([^"]*\)".*/\1/p'
}
hub_header=""
if [ -n "${HUB_TOKEN_URL:-}" ]; then
  t=$(token "$HUB_TOKEN_URL" "$HUB_CLIENT_ID" "$HUB_CLIENT_SECRET")
  [ -n "$t" ] || { log "hub token request failed"; exit 1; }
  hub_header="Authorization: Bearer $t"
fi
for topic in $TOPICS; do
  code=$(curl -sS -o /tmp/unsub.out -w '%{http_code}' -X POST "$HUB_URL" \
    ${hub_header:+-H "$hub_header"} \
    --data-urlencode hub.mode=unsubscribe --data-urlencode "hub.topic=$topic" \
    --data-urlencode "hub.callback=$CALLBACK_URL" --data-urlencode "hub.secret=$HUB_SECRET")
  case "$code" in
    200|202|204) log "unsubscribe $topic accepted ($code)";;
    *) log "unsubscribe $topic refused ($code): $(head -c 300 /tmp/unsub.out); subscription left unchanged"; exit 1;;
  esac
done
# The hub verifies the unsubscription by calling the callback.
sleep "$VERIFY_WAIT_SECONDS"
t=$(token "$ADMIN_TOKEN_URL" "$ADMIN_CLIENT_ID" "$ADMIN_CLIENT_SECRET")
[ -n "$t" ] || { log "admin token request failed; connector $CONNECTOR_ID is UNSUBSCRIBED"; exit 1; }
n=1
while [ "$n" -le "$SYNC_ATTEMPTS" ]; do
  code=$(curl -sS -o /tmp/sync.out -w '%{http_code}' -X POST \
    -H "Authorization: Bearer $t" \
    "$CONNECTOR_API_URL/connectors/$CONNECTOR_ID/websub/sync-subscriptions")
  if [ "$code" = 200 ] && grep -q '"all_subscribe_ok" *: *true' /tmp/sync.out; then
    log "connector $CONNECTOR_ID resubscribed"; exit 0
  fi
  log "sync attempt $n failed ($code): $(head -c 300 /tmp/sync.out)"
  n=$((n+1)); sleep 10
done
log "connector $CONNECTOR_ID is UNSUBSCRIBED; run sync-subscriptions manually"
exit 1
