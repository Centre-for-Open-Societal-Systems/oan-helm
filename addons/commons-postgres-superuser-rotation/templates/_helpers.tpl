{{- define "rotation.name" -}}{{ .Release.Name }}{{- end -}}
{{- define "rotation.pending" -}}{{ .Release.Name }}-pending{{- end -}}
{{- define "rotation.record" -}}{{ .Release.Name }}-record{{- end -}}
{{- define "rotation.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end -}}
