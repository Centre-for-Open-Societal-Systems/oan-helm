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

{{/* Every ECR registry the pull secret covers, space-separated: the API registry, ecrPullSecret.extraRegistries and, with telephony enabled, telephony.registry. */}}
{{- define "oan-leads-api.ecrRegistries" -}}
{{- $registries := list (include "oan-leads-api.ecrRegistry" .) -}}
{{- $extra := .Values.ecrPullSecret.extraRegistries | default list -}}
{{- if and .Values.telephony.enabled .Values.telephony.registry -}}
{{- $extra = append $extra .Values.telephony.registry -}}
{{- end -}}
{{- range $extra -}}
{{- if not (contains ".dkr.ecr." .) -}}
{{- fail (printf "ecrPullSecret: %q is not an ECR registry host (<account>.dkr.ecr.<region>.amazonaws.com)" .) -}}
{{- end -}}
{{- $registries = append $registries (trimSuffix "/" .) -}}
{{- end -}}
{{- $registries | uniq | join " " -}}
{{- end -}}

{{/* Job spec that fetches an ECR token per registry and writes one pull secret covering all of them. Takes dict root, serviceAccount. */}}
{{- define "oan-leads-api.ecrJobSpec" -}}
{{- $v := .root.Values.ecrPullSecret -}}
{{- $registries := splitList " " (include "oan-leads-api.ecrRegistries" .root) -}}
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
        command:
          - /bin/sh
          - -c
          - |
            set -eu
            {{- range $registries }}
            aws ecr get-login-password --region {{ index (splitList "." .) 3 }} > /token/{{ . }}
            {{- end }}
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
            auths=""
            for registry in {{ join " " $registries }}; do
              token="$(cat "/token/$registry")"
              auth="$(printf 'AWS:%s' "$token" | base64 | tr -d '\n')"
              auths="${auths:+$auths,}\"$registry\":{\"username\":\"AWS\",\"password\":\"$token\",\"auth\":\"$auth\"}"
            done
            printf '{"auths":{%s}}' "$auths" > /tmp/config.json
            kubectl create secret generic {{ $v.name }} \
              --namespace {{ .root.Release.Namespace }} \
              --type=kubernetes.io/dockerconfigjson \
              --from-file=.dockerconfigjson=/tmp/config.json \
              --dry-run=client -o yaml | kubectl apply -f -
            rm -f /tmp/config.json
        volumeMounts:
          - name: token
            mountPath: /token
            readOnly: true
    volumes:
      - name: token
        emptyDir:
          medium: Memory
{{- end -}}
