{{- /*
  Hook stamps: an upgrade re-runs one of our setup hooks only when its inputs changed (G2R-591).

  A hook template keeps its whole content in a define named "oan.hookFile.<name>" and renders it through
  "oan.hook.file". The plain resources of the file (script ConfigMaps, ServiceAccounts, RBAC) always render, so
  nothing is pruned and recreated. Its hook documents (any document with a helm.sh/hook annotation) render only
  when the hook is due:

    - the sha256 of the file's rendered content differs from the hook's stamp in the ConfigMap
      <release>-hook-stamps (read with lookup), or there is no stamp;
    - or hookStamps.forceAll is true, or the hook is listed in hookStamps.force;
    - or hookStamps.enabled is false.

  The content covers the script, the environment, the image and the targets, because they are all rendered into the
  file. A line marked "# oan-hook-volatile" (this revision's number) is left out of the hash. A hook that also
  depends on a Secret's live value puts that value's sha256 into its rendered content (never the value).

  The stamps are written by the last post-install/post-upgrade hook (templates/hook-stamps.yaml), only for the hooks
  that were due in this revision, after every earlier hook succeeded. If a hook fails, --atomic rolls back and the
  stamps stay as they were, so the next upgrade runs it again. Client-side "helm template" has no lookup and renders
  every hook; "helm upgrade --dry-run=server" reads the same ConfigMap as the upgrade and renders the same set.

  After a manual "helm rollback" (which runs no post-upgrade hook), set hookStamps.forceAll for one upgrade.
*/ -}}

{{- /* The hooks under stamps, in the order the writer records them. */ -}}
{{- define "oan.hook.names" -}}
aggregation-staff-client-secret aggregation-staff-grant consent-staff-portal-tile esignet-client-onboarding iam-bene-portal-api iam-login-provider-issuer-sync keycloak-public-client-urls mock-identities
{{- end -}}

{{- /* sha256 of a hook file's rendered content, its volatile lines removed. Argument: (list root name). */ -}}
{{- define "oan.hook.hash" -}}
{{- $root := index . 0 -}}
{{- $content := include (printf "oan.hookFile.%s" (index . 1)) $root -}}
{{- if trim $content -}}
{{- regexReplaceAll "(?m)^.*#\\s*oan-hook-volatile\\s*$\\n?" $content "" | sha256sum -}}
{{- end -}}
{{- end -}}

{{- /* The stored stamps: the live ConfigMap's data, else hookStamps.renderTestStamps (render tests only). */ -}}
{{- define "oan.hook.stored" -}}
{{- $live := lookup "v1" "ConfigMap" .Release.Namespace (printf "%s-hook-stamps" .Release.Name) -}}
{{- if $live -}}
{{- toJson ($live.data | default dict) -}}
{{- else -}}
{{- toJson ((.Values.hookStamps | default dict).renderTestStamps | default dict) -}}
{{- end -}}
{{- end -}}

{{- /* "true" when the hook must run in this revision. Argument: (list root name). */ -}}
{{- define "oan.hook.due" -}}
{{- $root := index . 0 -}}
{{- $name := index . 1 -}}
{{- $s := $root.Values.hookStamps | default dict -}}
{{- $hash := include "oan.hook.hash" (list $root $name) -}}
{{- if $hash -}}
{{- if or (not $s.enabled) $s.forceAll (has $name ($s.force | default list)) -}}
true
{{- else -}}
{{- $stored := include "oan.hook.stored" $root | fromJson -}}
{{- if ne (toString (index $stored $name | default "")) $hash -}}true{{- end -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{- /* Render a hook file: its plain documents always, its hook documents only when due. Argument: (list root name). */ -}}
{{- define "oan.hook.file" -}}
{{- $root := index . 0 -}}
{{- $name := index . 1 -}}
{{- $content := include (printf "oan.hookFile.%s" $name) $root -}}
{{- $due := include "oan.hook.due" (list $root $name) -}}
{{- range $doc := regexSplit "(?m)^---\\s*$" $content -1 -}}
{{- if trim $doc -}}
{{- if or $due (not (regexMatch "(?m)^\\s*\"?helm\\.sh/hook\"?\\s*:" $doc)) }}
---
{{ trim $doc }}
{{- end -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{- /* {name: hash} of the hooks due in this revision, as JSON: what the stamp writer records. */ -}}
{{- define "oan.hook.dueStamps" -}}
{{- $root := . -}}
{{- $stamps := dict -}}
{{- range $name := splitList " " (include "oan.hook.names" $root) -}}
{{- if include "oan.hook.due" (list $root $name) -}}
{{- $_ := set $stamps $name (include "oan.hook.hash" (list $root $name)) -}}
{{- end -}}
{{- end -}}
{{- toJson $stamps -}}
{{- end -}}
