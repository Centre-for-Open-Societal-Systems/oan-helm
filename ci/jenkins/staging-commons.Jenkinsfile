// Commons services on staging follow main: a merge that changes the staging Commons values or the pinned chart version
// delivers them with scripts/ci/deliver_staging_commons.sh (helm upgrade --reset-values --atomic). No parameters, no
// click. Other merges to main build nothing here.
//
// Jenkins: a multibranch job on Centre-for-Open-Societal-Systems/oan-helm, branch main only, script path
// ci/jenkins/staging-commons.Jenkinsfile. Credentials: staging-rke2-kubeconfig (as the registries) and
// staging-commons-secret-values (a secret file with the values not kept in git; see docs/release/environments.md).
pipeline {
    agent { label 'oan-ci-deploy' }
    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '30'))
        timeout(time: 60, unit: 'MINUTES')
    }
    stages {
        stage('Deliver Commons services') {
            when {
                allOf {
                    branch 'main'
                    not { changeRequest() }
                    anyOf {
                        changeset 'environments/staging/values/commons-services.yaml'
                        changeset 'environments/staging/commons-services.chart'
                    }
                }
            }
            steps {
                withCredentials([
                    file(credentialsId: 'staging-rke2-kubeconfig', variable: 'KUBECONFIG'),
                    file(credentialsId: 'staging-commons-secret-values', variable: 'COMMONS_SECRET_VALUES')
                ]) {
                    sh 'bash scripts/ci/deliver_staging_commons.sh "$COMMONS_SECRET_VALUES"'
                }
            }
        }
    }
}
