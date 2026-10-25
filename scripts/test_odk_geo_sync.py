"""Render the optional ODK job alone; deployment promotion gates stay intact."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
HELM = os.environ.get('HELM', 'helm')


class OdkGeoSyncContract(unittest.TestCase):
    def test_three_registries_render_secret_scoped_jobs_and_preserve_default_off(self):
        for domain in ('farmer', 'cropsown', 'livestock'):
            with self.subTest(registry=domain), tempfile.TemporaryDirectory() as directory:
                source = ROOT / f'charts/openg2p-{domain}-registry'
                values = yaml.safe_load((source / 'values.yaml').read_text(encoding='utf-8'))
                self.assertFalse(values['odkGeoSync']['enabled'])
                self.assertFalse(values['odkGeoSync']['runOnInstall'])
                fixture = Path(directory)
                (fixture / 'templates').mkdir()
                for name in ('odk-geo-sync.yaml', '_coss.tpl'):
                    shutil.copyfile(source / 'templates' / name, fixture / 'templates' / name)
                (fixture / 'Chart.yaml').write_text('apiVersion: v2\nname: job-contract\nversion: 0.1.0\n')
                values['odkGeoSync'].update(enabled=True, runOnInstall=True,
                    image={'repository': 'example.invalid/odk-geo-sync', 'tag': 'source-123', 'digest': ''},
                    odk={'url': 'https://central.example.invalid', 'projectId': '5',
                         'credentialsSecret': {'name': 'registry-central', 'emailKey': 'email', 'passwordKey': 'password'}})
                (fixture / 'values.yaml').write_text(yaml.safe_dump(values))
                result = subprocess.run([HELM, 'template', 'owned', str(fixture)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                documents = list(yaml.safe_load_all(result.stdout))
                self.assertEqual({doc['kind'] for doc in documents}, {'CronJob', 'Job'})
                cron = next(doc for doc in documents if doc['kind'] == 'CronJob')
                self.assertEqual(cron['spec']['concurrencyPolicy'], 'Forbid')
                pod = cron['spec']['jobTemplate']['spec']['template']['spec']
                container = pod['containers'][0]
                self.assertTrue(container['securityContext']['readOnlyRootFilesystem'])
                self.assertFalse(container['securityContext']['allowPrivilegeEscalation'])
                env = {item['name']: item for item in container['env']}
                self.assertEqual(env['ODK_CENTRAL_PASSWORD']['valueFrom']['secretKeyRef']['name'], 'registry-central')
                self.assertNotIn('value', env['ODK_CENTRAL_PASSWORD'])
                self.assertEqual(env['ODK_PROJECT_ID']['value'], '5')
                self.assertTrue((source / 'templates' / 'refactor-promotion-gate.yaml').is_file())
