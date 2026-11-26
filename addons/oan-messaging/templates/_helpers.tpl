{{- define "oanmsg.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimAll "-_." | quote }}
{{- end -}}

{{/* The service chart's fullname (its Services are <fullname>-api and <fullname>-receipts). */}}
{{- define "oanmsg.svc" -}}
{{- index .Values "oan-messaging-service" "fullnameOverride" | default "oan-messaging" -}}
{{- end -}}

{{- define "oanmsg.serviceImage" -}}
{{- $i := index .Values "oan-messaging-service" "image" -}}
{{- printf "%s:%s" $i.repository $i.tag -}}
{{- end -}}

{{- define "oanmsg.uiImage" -}}
{{- printf "%s:%s" (required "ui.image.repository is required" .Values.ui.image.repository) (required "ui.image.tag is required" .Values.ui.image.tag) -}}
{{- end -}}

{{- define "oanmsg.pullSecrets" -}}
{{- with .Values.imagePullSecrets }}
imagePullSecrets:
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- end -}}

{{- define "oanmsg.uiHost" -}}
{{- .Values.ui.host | default (printf "messaging.%s" (trimPrefix "." .Values.cookieDomain)) -}}
{{- end -}}

{{- define "oanmsg.apiHost" -}}
{{- .Values.api.host | default (printf "oan-messaging.%s" (trimPrefix "." .Values.cookieDomain)) -}}
{{- end -}}

{{- define "oanmsg.clientSecretName" -}}
{{- printf "%s-ui-client" .Release.Name -}}
{{- end -}}

{{/* Hook annotations: dict "weight" "phase" "delete" */}}
{{- define "oanmsg.hook" -}}
helm.sh/hook: {{ .phase }}
helm.sh/hook-weight: {{ .weight | quote }}
helm.sh/hook-delete-policy: {{ .delete | default "before-hook-creation" }}
{{- end -}}

{{/* Settings every service-image hook needs to open the database and the keys. */}}
{{- define "oanmsg.runtimeEnv" -}}
- name: OAN_MSG_DATABASE_URL
  valueFrom: {secretKeyRef: {name: oan-messaging-database, key: runtime-url}}
- name: OAN_MSG_CONTENT_KEYS
  valueFrom: {secretKeyRef: {name: oan-messaging-core, key: content-keys}}
- name: OAN_MSG_FINGERPRINT_KEYS
  valueFrom: {secretKeyRef: {name: oan-messaging-core, key: fingerprint-keys}}
- name: OAN_MSG_CREDENTIAL_PEPPER
  valueFrom: {secretKeyRef: {name: oan-messaging-core, key: credential-pepper}}
- name: OAN_MSG_CONTENT_KEY_CURRENT
  value: v1
- name: OAN_MSG_FINGERPRINT_KEY_CURRENT
  value: k1
{{- end -}}

{{- define "oanmsg.hookSecurity" -}}
runAsNonRoot: true
runAsUser: 10001
runAsGroup: 10001
{{- end -}}
