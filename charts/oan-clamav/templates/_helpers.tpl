{{- define "clamav.labels" -}}
app.kubernetes.io/name: oan-clamav
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{/*
Resource name. A release already named after clamav (the standalone `grievance-clamav`) keeps its
name; embedded as a subchart of another release it becomes <release>-clamav.
*/}}
{{- define "clamav.fullname" -}}
{{- if contains "clamav" .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-clamav" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
