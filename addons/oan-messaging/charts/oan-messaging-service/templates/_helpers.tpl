{{/* ------------------------------------------------------------------ names */}}
{{- define "oan.name" -}}
{{- $n := default .Chart.Name .Values.nameOverride -}}
{{- if or (gt (len $n) 63) (not (regexMatch "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$" $n)) -}}
{{- fail (printf "nameOverride %q must be a DNS-1123 label of at most 63 characters" $n) -}}
{{- end -}}
{{- $n -}}
{{- end -}}

{{/* Names are never truncated: truncation can erase the component suffix and make two
resources collide. The longest generated name is <fullname>-worker-providers-egress
(24 characters of suffix), Services are DNS labels (63) and CronJob names are limited to
52, so fullname may be at most 39 characters. Longer names fail rendering. */}}
{{- define "oan.maxFullnameLength" -}}39{{- end -}}

{{- define "oan.fullname" -}}
{{- $full := "" -}}
{{- if .Values.fullnameOverride -}}
{{- $full = .Values.fullnameOverride -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- $full = .Release.Name -}}
{{- else -}}
{{- $full = printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}
{{- $max := int (include "oan.maxFullnameLength" .) -}}
{{- if gt (len $full) $max -}}
{{- fail (printf "resource name prefix %q is %d characters; at most %d are allowed so that component suffixes stay unique (set a shorter fullnameOverride)" $full (len $full) $max) -}}
{{- end -}}
{{- if not (regexMatch "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$" $full) -}}
{{- fail (printf "resource name prefix %q must be a DNS-1123 label (lower-case letters, digits, '-')" $full) -}}
{{- end -}}
{{- $full -}}
{{- end -}}

{{/* "oan.componentName" (dict "root" $ "component" "api") -> <fullname>-api */}}
{{- define "oan.componentName" -}}
{{- printf "%s-%s" (include "oan.fullname" .root) .component -}}
{{- end -}}

{{- define "oan.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
{{- default (include "oan.fullname" .) .Values.serviceAccount.name -}}
{{- else -}}
{{- default "default" .Values.serviceAccount.name -}}
{{- end -}}
{{- end -}}

{{/* ----------------------------------------------------------------- labels */}}
{{- define "oan.selectorLabels" -}}
app.kubernetes.io/name: {{ include "oan.name" .root }}
app.kubernetes.io/instance: {{ .root.Release.Name }}
app.kubernetes.io/component: {{ .component }}
{{- end -}}

{{- define "oan.labels" -}}
helm.sh/chart: {{ printf "%s-%s" .root.Chart.Name .root.Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{ include "oan.selectorLabels" . }}
app.kubernetes.io/version: {{ .root.Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .root.Release.Service }}
app.kubernetes.io/part-of: oan-messaging
{{- with .root.Values.commonLabels }}
{{ toYaml . }}
{{- end }}
{{- end -}}

{{/* ------------------------------------------------------------------ image */}}
{{- define "oan.image" -}}
{{- $repo := required "image.repository is required" .Values.image.repository -}}
{{- if .Values.image.digest -}}
{{- if not (regexMatch "^sha256:[a-f0-9]{64}$" .Values.image.digest) -}}
{{- fail "image.digest must look like sha256:<64 hex>" -}}
{{- end -}}
{{- printf "%s@%s" $repo .Values.image.digest -}}
{{- else -}}
{{- printf "%s:%s" $repo (required "image.tag or image.digest is required" .Values.image.tag) -}}
{{- end -}}
{{- end -}}

{{/* --------------------------------------------------------------- security */}}
{{- define "oan.podSecurityContext" -}}
runAsNonRoot: true
runAsUser: {{ .Values.podSecurity.runAsUser }}
runAsGroup: {{ .Values.podSecurity.runAsGroup }}
seccompProfile:
  type: RuntimeDefault
{{- end -}}

{{/* Pods with a private key need fsGroup so the init container (same uid) can read the
Secret volume (root-owned, group = fsGroup, 0440). The main container never mounts that
Secret; it reads 0600 copies owned by its own uid from a memory emptyDir. */}}
{{- define "oan.podSecurityContextWithKeys" -}}
{{ include "oan.podSecurityContext" . }}
fsGroup: {{ .Values.podSecurity.runAsGroup }}
fsGroupChangePolicy: OnRootMismatch
{{- end -}}

{{- define "oan.containerSecurityContext" -}}
allowPrivilegeEscalation: false
readOnlyRootFilesystem: true
runAsNonRoot: true
privileged: false
capabilities:
  drop: [ALL]
seccompProfile:
  type: RuntimeDefault
{{- end -}}

{{/* ---------------------------------------------------------------- guards */}}
{{- define "oan.requireCommand" -}}
{{- if not .cmd -}}
{{- fail (printf "%s.command is required when %s.enabled=true: use values-pilot.yaml, which sets python -m oan_messaging.runtime %s (see docs/deployment/helm.md)" .name .name .name) -}}
{{- end -}}
{{- end -}}

{{/* ------------------------------------------------------------------- env */}}
{{/* Storage settings (oan_messaging.storage.config.StorageSettings). "pool" = {size, maxOverflow}. */}}
{{- define "oan.storageEnv" -}}
{{- $v := .root.Values -}}
- name: OAN_MSG_DATABASE_URL
  valueFrom:
    secretKeyRef:
      name: {{ required "database.existingSecret is required" $v.database.existingSecret }}
      key: {{ required "database.urlKey is required" $v.database.urlKey }}
- name: OAN_MSG_CONTENT_KEYS
  valueFrom:
    secretKeyRef:
      name: {{ required "secrets.core.existingSecret is required" $v.secrets.core.existingSecret }}
      key: {{ $v.secrets.core.contentKeysKey }}
- name: OAN_MSG_FINGERPRINT_KEYS
  valueFrom:
    secretKeyRef:
      name: {{ $v.secrets.core.existingSecret }}
      key: {{ $v.secrets.core.fingerprintKeysKey }}
- name: OAN_MSG_CREDENTIAL_PEPPER
  valueFrom:
    secretKeyRef:
      name: {{ $v.secrets.core.existingSecret }}
      key: {{ $v.secrets.core.credentialPepperKey }}
- name: OAN_MSG_DB_POOL_SIZE
  value: {{ .pool.size | quote }}
- name: OAN_MSG_DB_MAX_OVERFLOW
  value: {{ .pool.maxOverflow | quote }}
- name: PYTHONDONTWRITEBYTECODE
  value: "1"
- name: PYTHONUNBUFFERED
  value: "1"
{{- end -}}

{{- define "oan.envFromConfig" -}}
- configMapRef:
    name: {{ include "oan.fullname" . }}-config
{{- end -}}

{{/* Init container that publishes a validated 0600 snapshot of ONE Secret generation
(files/tls_snapshot.py, embedded verbatim and tested by ci/regression). The Secret is
mounted ONLY into this container; the main container reads <dest>/current/<file>.
args: root, ca (bool) */}}
{{- define "oan.tlsSnapshotInit" -}}
- name: snapshot-tls
  image: {{ include "oan.image" .root }}
  imagePullPolicy: {{ .root.Values.image.pullPolicy }}
  command:
    - python
    - -I
    - -c
    - |
{{ .root.Files.Get "files/tls_snapshot.py" | indent 6 }}
    - --source
    - /secrets/tls-source
    - --dest
    - /run/oan-msg/tls
    - --cert
    - tls.crt
    - --key
    - tls.key
    {{- if .ca }}
    - --ca
    - ca.crt
    {{- end }}
  securityContext:
    {{- include "oan.containerSecurityContext" .root | nindent 4 }}
  resources:
    requests: {cpu: 10m, memory: 32Mi}
    limits: {cpu: 100m, memory: 64Mi}
  volumeMounts:
    - name: tls-source
      mountPath: /secrets/tls-source
      readOnly: true
    - name: tls-snapshot
      mountPath: /run/oan-msg/tls
{{- end -}}

{{/* ---------------------------------------------------------- connection budget */}}
{{/* Integer check: YAML numbers arrive as float64, --set numbers as int64.
args: v, name, min */}}
{{- define "oan.requireInt" -}}
{{- $ok := or (kindIs "int" .v) (kindIs "int64" .v) (and (kindIs "float64" .v) (eq (float64 .v) (floor .v))) -}}
{{- if not $ok -}}
{{- fail (printf "%s must be an integer" .name) -}}
{{- end -}}
{{- if lt (int64 .v) (int64 .min) -}}
{{- fail (printf "%s must be >= %d (got %v)" .name (int64 .min) .v) -}}
{{- end -}}
{{- end -}}

{{/* Validates every input of the connection estimates. SQLAlchemy treats pool_size=0 as
"no limit" and max_overflow=-1 as "unlimited overflow", so both are refused here. */}}
{{- define "oan.validateConnectionInputs" -}}
{{- $v := .Values -}}
{{- range $c := list "api" "worker" "workerTelegram" "receipts" "cleanup" -}}
{{- $cv := index $v $c -}}
{{- include "oan.requireInt" (dict "v" $cv.pool.size "name" (printf "%s.pool.size" $c) "min" 1) -}}
{{- include "oan.requireInt" (dict "v" $cv.pool.maxOverflow "name" (printf "%s.pool.maxOverflow" $c) "min" 0) -}}
{{- if ne $c "cleanup" -}}
{{- include "oan.requireInt" (dict "v" $cv.replicas "name" (printf "%s.replicas" $c) "min" 0) -}}
{{- include "oan.requireInt" (dict "v" $cv.rollout.maxSurge "name" (printf "%s.rollout.maxSurge" $c) "min" 0) -}}
{{- end -}}
{{- end -}}
{{- include "oan.requireInt" (dict "v" $v.worker.coordinationConnections "name" "worker.coordinationConnections" "min" 1) -}}
{{- include "oan.requireInt" (dict "v" $v.workerTelegram.coordinationConnections "name" "workerTelegram.coordinationConnections" "min" 1) -}}
{{- include "oan.requireInt" (dict "v" $v.database.connectionBudget "name" "database.connectionBudget" "min" 0) -}}
{{- end -}}

{{/* Per-pod connection limit from configuration: pool.size + pool.maxOverflow (+ the
worker rate limiter's coordination connections). args: root, component */}}
{{- define "oan.perPod" -}}
{{- $cv := index .root.Values .component -}}
{{- $n := add $cv.pool.size $cv.pool.maxOverflow -}}
{{- if has .component (list "worker" "workerTelegram") -}}{{- $n = add $n $cv.coordinationConnections -}}{{- end -}}
{{- $n -}}
{{- end -}}

{{/* Steady state: every enabled pod at its configured limit. The migration hook is not
running. Cleanup: one CronJob pod (concurrencyPolicy Forbid) or one Deployment pod
(Recreate). */}}
{{- define "oan.connectionSteady" -}}
{{- $v := .Values -}}
{{- $t := 0 -}}
{{- range $c := list "api" "worker" "workerTelegram" "receipts" -}}
{{- $cv := index $v $c -}}
{{- if $cv.enabled -}}
{{- $t = add $t (mul $cv.replicas (include "oan.perPod" (dict "root" $ "component" $c))) -}}
{{- end -}}
{{- end -}}
{{- if $v.cleanup.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "cleanup")) -}}{{- end -}}
{{- if $v.statusCheck.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "statusCheck")) -}}{{- end -}}
{{- if $v.statsRefresh.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "statsRefresh")) -}}{{- end -}}
{{- $t -}}
{{- end -}}

{{/* Upgrade/rollout estimate. Per Deployment the controller keeps at most
replicas + maxSurge non-terminating pods, but terminating pods are not counted, so up to
`replicas` old pods may still hold connections until they exit (bounded by their
terminationGracePeriodSeconds): (2 x replicas + maxSurge) pods. All Deployments may roll
at once. The pre-upgrade migration hook adds 1 connection while the previous release's
workloads are still running. Cleanup stays at one pod (Forbid / Recreate). This is an
estimate from configured limits; nothing at runtime enforces it. */}}
{{- define "oan.connectionRollout" -}}
{{- $v := .Values -}}
{{- $t := 0 -}}
{{- range $c := list "api" "worker" "workerTelegram" "receipts" -}}
{{- $cv := index $v $c -}}
{{- if $cv.enabled -}}
{{- $pods := add (mul 2 $cv.replicas) $cv.rollout.maxSurge -}}
{{- $t = add $t (mul $pods (include "oan.perPod" (dict "root" $ "component" $c))) -}}
{{- end -}}
{{- end -}}
{{- if $v.cleanup.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "cleanup")) -}}{{- end -}}
{{- if $v.statusCheck.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "statusCheck")) -}}{{- end -}}
{{- if $v.statsRefresh.enabled -}}{{- $t = add $t (include "oan.perPod" (dict "root" . "component" "statsRefresh")) -}}{{- end -}}
{{- if $v.migration.enabled -}}{{- $t = add $t 1 -}}{{- end -}}
{{- $t -}}
{{- end -}}

{{/* Pod spec shared by the cleanup CronJob and Deployment modes. Deployment mode runs
the long-lived loop, so --forever is added to the command when it is missing. */}}
{{- define "oan.cleanupPodSpec" -}}
serviceAccountName: {{ include "oan.serviceAccountName" . }}
automountServiceAccountToken: false
enableServiceLinks: false
terminationGracePeriodSeconds: {{ .Values.cleanup.terminationGracePeriodSeconds }}
securityContext:
  {{- include "oan.podSecurityContext" . | nindent 2 }}
{{- with .Values.imagePullSecrets }}
imagePullSecrets:
  {{- toYaml . | nindent 2 }}
{{- end }}
containers:
  - name: cleanup
    image: {{ include "oan.image" . }}
    imagePullPolicy: {{ .Values.image.pullPolicy }}
    {{- with .Values.image.workingDir }}
    workingDir: {{ . }}
    {{- end }}
    {{- $cmd := .Values.cleanup.command }}
    {{- if and (eq .Values.cleanup.mode "deployment") (not (has "--forever" $cmd)) }}
    {{- $cmd = append $cmd "--forever" }}
    {{- end }}
    command:
      {{- toYaml $cmd | nindent 6 }}
    envFrom:
      {{- include "oan.envFromConfig" . | nindent 6 }}
    env:
      {{- include "oan.storageEnv" (dict "root" . "pool" .Values.cleanup.pool) | nindent 6 }}
      {{- with .Values.cleanup.extraEnv }}
      {{- toYaml . | nindent 6 }}
      {{- end }}
    resources:
      {{- toYaml .Values.cleanup.resources | nindent 6 }}
    securityContext:
      {{- include "oan.containerSecurityContext" . | nindent 6 }}
    volumeMounts:
      - name: tmp
        mountPath: /tmp
volumes:
  - name: tmp
    emptyDir: {sizeLimit: 64Mi}
{{- with .Values.nodeSelector }}
nodeSelector:
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- with .Values.tolerations }}
tolerations:
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- end -}}
