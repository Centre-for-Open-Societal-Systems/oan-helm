{{- define "oan-loki.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
{{- end -}}

{{- define "oan-loki.url" -}}
{{- if .Values.grafanaDatasource.url -}}
{{ .Values.grafanaDatasource.url }}
{{- else -}}
{{ printf "http://%s-gateway.%s.svc.cluster.local" (.Values.loki.fullnameOverride | default "loki") .Release.Namespace }}
{{- end -}}
{{- end -}}
