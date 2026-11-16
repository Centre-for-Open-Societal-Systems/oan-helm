{{- define "oan.image" -}}
{{- $repository := required "enabled component requires image.repository" .repository -}}
{{- if .digest -}}
{{- if not (regexMatch "^sha256:[a-f0-9]{64}$" .digest) -}}
{{- fail "image.digest must be sha256 followed by 64 lowercase hex characters" -}}
{{- end -}}
{{- printf "%s@%s" $repository .digest -}}
{{- else -}}
{{- printf "%s:%s" $repository (required "enabled component requires image.tag or image.digest" .tag) -}}
{{- end -}}
{{- end -}}

{{- define "oan-leads-api.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" }}
{{- end -}}

{{/* API pods only; keeps the Redis pods out of the API Service and PDB. */}}
{{- define "oan-leads-api.selectorLabels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/component: api
{{- end -}}

{{- define "oan-leads-api.redisName" -}}
{{- printf "%s-redis" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "oan-leads-api.secretName" -}}
{{- required "secret.name (an existing Secret in the release namespace) is required" .Values.secret.name -}}
{{- end -}}
