{{- define "ecrsecret.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end -}}

{{- define "ecrsecret.registry" -}}
{{- $r := required "registry is required" .Values.registry -}}
{{- if not (contains ".dkr.ecr." $r) -}}{{- fail (printf "registry %q is not an ECR registry host" $r) -}}{{- end -}}
{{- $r -}}
{{- end -}}

{{- define "ecrsecret.jobSpec" -}}
{{- $v := .root.Values -}}
{{- $registry := include "ecrsecret.registry" .root -}}
backoffLimit: 2
activeDeadlineSeconds: 300
template:
  metadata:
    labels:
      app.kubernetes.io/name: {{ .root.Chart.Name }}
      app.kubernetes.io/instance: {{ .root.Release.Name }}
  spec:
    serviceAccountName: {{ .serviceAccount }}
    restartPolicy: Never
    initContainers:
      - name: get-token
        image: {{ $v.awsCliImage }}
        command: ["/bin/sh", "-c", "aws ecr get-login-password --region {{ index (splitList "." $registry) 3 }} > /token/ecr"]
        volumeMounts:
          - {name: token, mountPath: /token}
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
            echo "refreshed {{ .root.Release.Namespace }}/{{ $v.name }}"
        volumeMounts:
          - {name: token, mountPath: /token, readOnly: true}
    volumes:
      - name: token
        emptyDir: {medium: Memory}
{{- end -}}
