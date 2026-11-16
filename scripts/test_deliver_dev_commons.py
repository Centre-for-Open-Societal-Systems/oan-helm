"""Commons New Dev delivery: the pinned chart is sealed, the job runs services then ODK bootstrap with its own deployer,
and the scripts never reuse saved values."""
import hashlib
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts/ci'))
import commons_values_guard as guard

PIPELINE = ROOT / 'ci/jenkins/dev-commons.Jenkinsfile'


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


class DeliverDevCommons(unittest.TestCase):
    def test_pinned_chart_is_in_the_repository_and_sealed(self):
        version = read('environments/dev/commons-services.chart').strip()
        archive = f'openg2p-commons-services-{version}.tgz'
        sums = dict(line.split('  ', 1)[::-1] for line in read('repository/SHA256SUMS').splitlines() if '  ' in line)
        self.assertIn(archive, sums)
        self.assertEqual(hashlib.sha256((ROOT / 'repository' / archive).read_bytes()).hexdigest(), sums[archive])

    def test_services_delivery_uses_the_dev_files_and_never_reuses_saved_values(self):
        script = read('scripts/ci/deliver_dev_commons.sh')
        for path in ('environments/dev/values/commons-services.yaml', 'environments/dev/commons-services.chart',
                     'environments/dev/commons-services.retired-keys'):
            self.assertIn(path, script)
        self.assertNotIn('environments/staging', script)
        self.assertIn('--reset-values', script)
        self.assertNotIn('--reuse-values', script)
        self.assertIn('commons_values_guard.py', script)
        self.assertIn('record=commons-services-delivery', script)
        self.assertLess(script.index('--atomic --wait'), script.index('kubectl create configmap'))

    def test_retired_keys_drop_only_the_hand_set_seed_image(self):
        retired = guard.retired_keys(ROOT / 'environments/dev/commons-services.retired-keys')
        self.assertEqual(retired, ['master-data.geoSeed.image'])
        saved = {'master-data': {'geoSeed': {'image': {'tag': 'old'}, 'enabled': True}}, 'keymanager': {'p': 'x'}}
        given = {'master-data': {'geoSeed': {'enabled': True}}}
        self.assertEqual(guard.missing(saved, given, retired), ['keymanager.p'])

    def test_odk_bootstrap_delivery_follows_services(self):
        script = read('scripts/ci/deliver_dev_odk_bootstrap.sh')
        self.assertIn('record=odk-bootstrap-delivery', script)
        self.assertIn('addons/odk-bootstrap', script)
        self.assertIn('environments/dev/values/odk-bootstrap.yaml', script)
        self.assertIn('--reset-values', script)
        self.assertLess(script.index('--atomic --wait'), script.index('kubectl create configmap'))
        self.assertIn('kubectl logs "job/$release"', script)
        pipeline = PIPELINE.read_text(encoding='utf-8')
        self.assertLess(pipeline.index("sh 'bash scripts/ci/deliver_dev_commons.sh"),
                        pipeline.index("sh 'bash scripts/ci/deliver_dev_odk_bootstrap.sh'"))

    def test_job_builds_main_only_with_the_dev_deployer(self):
        body = PIPELINE.read_text(encoding='utf-8').split('pipeline {', 1)[1]
        self.assertNotIn('parameters', body)
        self.assertNotIn('changeset', body)
        self.assertNotIn('staging', body)
        self.assertEqual(body.count("credentialsId: 'dev-commons-deployer-kubeconfig'"), 2)
        self.assertEqual(body.count("allOf { branch 'main'; not { changeRequest() } }"), 3)  # the gate and two deliveries
        job = read('ci/jenkins/jobs/oan-helm-dev-commons.xml')
        self.assertIn('<scriptPath>ci/jenkins/dev-commons.Jenkinsfile</scriptPath>', job)
        self.assertIn('<includes>main</includes>', job)
        self.assertNotIn('staging-commons', job)

    def test_dev_deployer_rbac_matches_staging_and_stays_in_commons(self):
        def body(path):
            return '\n'.join(line for line in read(path).splitlines() if not line.startswith('#'))
        dev = body('environments/dev/rbac/commons-deployer-rbac.yaml')
        self.assertEqual(dev, body('environments/staging/rbac/commons-deployer-rbac.yaml'))
        self.assertNotIn('ClusterRole', dev)
        self.assertEqual(set(re.findall(r'namespace: (\S+)', dev)), {'commons'})
        # odk-bootstrap owns only kinds the Role already covers.
        owned = set(re.findall(r'^kind: (\S+)', read('addons/odk-bootstrap/templates/job.yaml'), re.M))
        self.assertEqual(owned, {'ServiceAccount', 'Role', 'RoleBinding', 'ConfigMap', 'Job'})


if __name__ == '__main__':
    unittest.main()
