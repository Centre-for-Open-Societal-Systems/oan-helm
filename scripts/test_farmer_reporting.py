"""Reporting hook rendering keeps registry DB and MDS credentials separate."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml
ROOT = Path(__file__).resolve().parents[1]


class FarmerReporting(unittest.TestCase):
    def test_reporting_hook_uses_native_seed_and_secret_scoped_mds_api(self):
        source = ROOT/'charts/openg2p-farmer-registry'
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory)
            (fixture/'templates').mkdir()
            for name in ('reporting-views.yaml','analytics-jobs.yaml','_mds-api-env.tpl'):
                shutil.copyfile(source/'templates'/name,fixture/'templates'/name)
            (fixture/'Chart.yaml').write_text('apiVersion: v2\nname: reporting-contract\nversion: 0.1.0\n')
            values = yaml.safe_load((source/'values.yaml').read_text(encoding='utf-8'))
            values['analytics']['bulkSample']['enabled'] = False
            values['analytics']['dashboards']['enabled'] = False
            values['registry']['dbSeed']['image'] = {'repository':'example.invalid/oan-seed','tag':'verified-source'}
            (fixture/'values.yaml').write_text(yaml.safe_dump(values))
            result = subprocess.run([os.environ.get('HELM','helm'),'template','owned',str(fixture)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            documents = [document for document in yaml.safe_load_all(result.stdout) if document]
            self.assertEqual(len(documents),1,'Reporting creation must have one owning hook across all analytics templates')
            job = documents[0]
            self.assertEqual(job['metadata']['annotations']['helm.sh/hook'],'post-install,post-upgrade')
            container = job['spec']['template']['spec']['containers'][0]
            self.assertEqual(container['image'],'example.invalid/oan-seed:verified-source')
            self.assertIn('sync_geo_levels.py',container['command'][-1])
            self.assertIn('ON_ERROR_STOP=1',container['command'][-1])
            env = {item['name']:item for item in container['env']}
            self.assertNotIn('value',env['MDS_CLIENT_SECRET'])
            self.assertEqual(env['MDS_CLIENT_ID']['value'],'owned-staff-portal')
            self.assertEqual(env['MDS_CLIENT_SECRET']['valueFrom']['secretKeyRef'],{'name':'owned-staff-portal','key':'client_secret'})
            self.assertNotIn('value',env['PGPASSWORD'])
            self.assertNotEqual(env['MDS_CLIENT_SECRET']['valueFrom']['secretKeyRef'],env['PGPASSWORD']['valueFrom']['secretKeyRef'])
            self.assertFalse(any(name.startswith('MD_PG') for name in env))


if __name__ == '__main__': unittest.main()
