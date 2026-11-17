// Commons on staging follows main. Every build of main first runs scripts/ci/deliver_staging_commons_base.sh for the
// base release (commons: pinned OpenG2P chart, --reuse-values with the staging overlay, record commons-base-delivery),
// then scripts/ci/deliver_staging_commons.sh, which
// compares what staging runs (ConfigMap commons-services-delivery: pinned chart, sha256 of the staging values and of
// the secret values) with this commit and delivers only when they differ (helm upgrade --reset-values --atomic). A
// failed delivery is therefore retried by the next build of main. No parameters, no click; pull requests never deliver.
//
// Jenkins: multibranch job oan-helm-staging-commons on Centre-for-Open-Societal-Systems/oan-helm, branch main only,
// defined in ci/jenkins/jobs/oan-helm-staging-commons.xml and created or updated by ci/jenkins/apply-job.sh. Credentials: staging-commons-deployer-kubeconfig (environments/staging/rbac/commons-deployer-rbac.yaml) and
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
        // Nothing is delivered unless every GitHub check of this commit passed (scripts/ci/require_green_checks.sh).
        stage('Checks green') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([usernamePassword(credentialsId: 'oan-helm-fork-token', usernameVariable: 'GH_USER', passwordVariable: 'GH_TOKEN')]) {
                    sh 'bash scripts/ci/require_green_checks.sh Centre-for-Open-Societal-Systems/oan-helm HEAD'
                }
            }
        }
        // The ECR pull secret first: every later release pulls with commons/ecr-pull-secret.
        stage('Deliver Commons ECR pull secret') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_commons_ecr_pull_secret.sh'
                }
            }
        }
        // The base release first: Commons services run on it.
        stage('Deliver Commons base') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_commons_base.sh'
                }
            }
        }
        // Rotates the Commons Postgres superuser password when environments/staging/values/
        // commons-postgres-superuser-rotation.yaml names a new rotation.id; otherwise a no-op.
        stage('Rotate Commons Postgres superuser') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_commons_postgres_superuser_rotation.sh'
                }
            }
        }
        stage('Deliver Commons services') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([
                    file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG'),
                    file(credentialsId: 'staging-commons-secret-values', variable: 'COMMONS_SECRET_VALUES')
                ]) {
                    sh 'bash scripts/ci/deliver_staging_commons.sh "$COMMONS_SECRET_VALUES"'
                }
            }
        }
        // Partners every registry relies on, onboarded in Partner Management (scripts/ci/deliver_staging_commons_partners.sh,
        // record commons-partners-delivery). After Commons services, which run Partner Management and Keycloak.
        stage('Deliver Commons partners') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_commons_partners.sh'
                }
            }
        }
        // The OAN staging Helm repository in Rancher (scripts/ci/deliver_staging_rancher_repo.sh).
        stage('Register OAN Helm repository in Rancher') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_rancher_repo.sh'
                }
            }
        }
        // The shared dashboard no registry owns (scripts/ci/deliver_staging_oan_dashboards.sh, record oan-dashboards-delivery).
        stage('Deliver oan-dashboards') {
            when { allOf { branch 'main'; not { changeRequest() } } }
            steps {
                withCredentials([file(credentialsId: 'staging-commons-deployer-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'bash scripts/ci/deliver_staging_oan_dashboards.sh'
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
                        body: "Commons delivery to staging failed.\n\nJob:     ${env.JOB_NAME}\nBranch:  ${env.BRANCH_NAME}\nBuild:   #${env.BUILD_NUMBER}\nURL:     ${env.BUILD_URL}\nConsole: ${env.BUILD_URL}console\n\nJenkins"
                    )
                } catch (err) {
                    echo "notification not sent: ${err.message}"
                }
            }
        }
    }
}
