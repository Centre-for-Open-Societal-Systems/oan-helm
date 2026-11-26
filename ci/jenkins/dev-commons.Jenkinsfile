// Commons on New Dev follows main, the counterpart of ci/jenkins/staging-commons.Jenkinsfile. Every build of main runs
// scripts/ci/deliver_dev_commons.sh, which compares what New Dev runs (ConfigMap commons-services-delivery: pinned chart
// environments/dev/commons-services.chart, sha256 of environments/dev/values/commons-services.yaml and of the secret
// values) with this commit and delivers only when they differ (helm upgrade --reset-values --atomic), then
// scripts/ci/deliver_dev_odk_bootstrap.sh (addons/odk-bootstrap, record odk-bootstrap-delivery) and
// scripts/ci/deliver_dev_oan_messaging.sh (addons/oan-messaging, record oan-messaging-delivery; its image tags are moved by the
// oan-messaging-service and oan-messaging-ui jobs through pull requests). A failed delivery is
// therefore retried by the next build of main. No parameters, no click; pull requests never deliver.
//
// New Dev's Commons base release (commons) and oan-dashboards are not delivered here: they have no New Dev values in
// git, and their saved values (passwords) cannot be rebuilt from git.
//
// Jenkins: multibranch job oan-helm-dev-commons on Centre-for-Open-Societal-Systems/oan-helm, branch main only,
// defined in ci/jenkins/jobs/oan-helm-dev-commons.xml and created or updated by ci/jenkins/apply-job.sh. Credentials:
// dev-commons-deployer-kubeconfig (environments/dev/rbac/commons-deployer-rbac.yaml) and dev-commons-secret-values (a
// secret file with the values not kept in git; see docs/release/environments.md).
pipeline {
    agent { label 'oan-ci-deploy' }
    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '30'))
        timeout(time: 60, unit: 'MINUTES')
    }
    stages {
        // Nothing is delivered unless every GitHub check of this commit passed (scripts/ci/require_green_checks.sh).
        stage('Checks green') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([usernamePassword(credentialsId: 'oan-helm-fork-token', usernameVariable: 'GH_USER', passwordVariable: 'GH_TOKEN')]) {
                    sh 'bash scripts/ci/require_green_checks.sh Centre-for-Open-Societal-Systems/oan-helm HEAD'
                }
            }
        }
        stage('Deliver Commons services') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([
                    file(credentialsId: 'dev-commons-deployer-kubeconfig', variable: 'KUBECONFIG'),
                    file(credentialsId: 'dev-commons-secret-values', variable: 'COMMONS_SECRET_VALUES')
                ]) {
                    sh 'bash scripts/ci/deliver_dev_commons.sh "$COMMONS_SECRET_VALUES"'
                }
            }
        }
        // ODK Central runs in Commons services, so its bootstrap comes after them.
        stage('Deliver ODK bootstrap') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'dev-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_dev_odk_bootstrap.sh'
                }
            }
        }
        // OAN Messaging uses Commons Keycloak, IAM and PostgreSQL, so it comes last.
        stage('Deliver OAN Messaging') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'dev-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_dev_oan_messaging.sh'
                }
            }
        }
    }
    post {
        failure {
            script {
                // Mail the DevOps list and the commit author, as the registry pipelines do; a controller without SMTP
                // must not hide the failure.
                try {
                    def author = ''
                    try { author = sh(script: "git log -1 --pretty=format:'%ae'", returnStdout: true).trim() } catch (ignored) { author = '' }
                    def recipients = ['simretyibeltal@gmail.com', 'pavanns.ns@gmail.com']
                    if (author && !author.contains('noreply')) { recipients = [author] + recipients }
                    mail(
                        to: recipients.unique().join(', '),
                        subject: "Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: "Commons delivery to New Dev failed.\n\nJob:     ${env.JOB_NAME}\nBranch:  ${env.BRANCH_NAME}\nBuild:   #${env.BUILD_NUMBER}\nURL:     ${env.BUILD_URL}\nConsole: ${env.BUILD_URL}console\n\nJenkins"
                    )
                } catch (err) {
                    echo "notification not sent: ${err.message}"
                }
            }
        }
    }
}
