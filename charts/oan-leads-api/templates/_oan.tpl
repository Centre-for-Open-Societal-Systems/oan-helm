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

{{- define "oan-leads-api.pullSecrets" -}}
{{- $pullSecrets := .Values.imagePullSecrets | default list -}}
{{- if .Values.ecrPullSecret.enabled -}}
{{- $pullSecrets = prepend $pullSecrets (dict "name" .Values.ecrPullSecret.name) -}}
{{- end -}}
{{- with $pullSecrets }}
imagePullSecrets:
  {{- toYaml . | nindent 2 }}
{{- end -}}
{{- end -}}

{{- define "oan-leads-api.ecrRefresher" -}}
{{- printf "%s-ecr-refresh" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* ECR registry host (<account>.dkr.ecr.<region>.amazonaws.com): ecrPullSecret.registry, else the host of image.repository. */}}
{{- define "oan-leads-api.ecrRegistry" -}}
{{- $registry := .Values.ecrPullSecret.registry | default (first (splitList "/" (toString .Values.image.repository))) -}}
{{- if not (contains ".dkr.ecr." $registry) -}}
{{- fail (printf "ecrPullSecret: %q is not an ECR registry host; set ecrPullSecret.registry or disable ecrPullSecret" $registry) -}}
{{- end -}}
{{- $registry -}}
{{- end -}}

{{/* Job spec that fetches an ECR token and writes the pull secret. Takes dict root, serviceAccount. */}}
{{- define "oan-leads-api.ecrJobSpec" -}}
{{- $v := .root.Values.ecrPullSecret -}}
{{- $registry := include "oan-leads-api.ecrRegistry" .root -}}
backoffLimit: 2
activeDeadlineSeconds: 300
template:
  metadata:
    labels:
      app.kubernetes.io/name: oan-leads-api-ecr-refresh
      app.kubernetes.io/instance: {{ .root.Release.Name }}
  spec:
    serviceAccountName: {{ .serviceAccount }}
    restartPolicy: Never
    initContainers:
      - name: get-token
        image: {{ $v.awsCliImage }}
        command: ["/bin/sh", "-c", "aws ecr get-login-password --region {{ index (splitList "." $registry) 3 }} > /token/ecr"]
        volumeMounts:
          - name: token
            mountPath: /token
    containers:
      - name: write-secret
        image: {{ $v.kubectlImage }}
        command:
          - /bin/sh
          - -c
          - |
            set -eu
            kubectl create secret docker-registry {{ $v.name }} \
              --namespace {{ .root.Release.Namespace }} \
              --docker-server={{ $registry }} \
              --docker-username=AWS \
              --docker-password="$(cat /token/ecr)" \
              --dry-run=client -o yaml | kubectl apply -f -
        volumeMounts:
          - name: token
            mountPath: /token
            readOnly: true
    volumes:
      - name: token
        emptyDir:
          medium: Memory
{{- end -}}
