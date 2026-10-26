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
            shutil.copyfile(source/'templates/reporting-views.yaml',fixture/'templates/reporting-views.yaml')
            (fixture/'Chart.yaml').write_text('apiVersion: v2\nname: reporting-contract\nversion: 0.1.0\n')
            values = yaml.safe_load((source/'values.yaml').read_text(encoding='utf-8'))
            values['registry']['dbSeed']['image'] = {'repository':'example.invalid/oan-seed','tag':'verified-source'}
            (fixture/'values.yaml').write_text(yaml.safe_dump(values))
            result = subprocess.run([os.environ.get('HELM','helm'),'template','owned',str(fixture)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            job = yaml.safe_load(result.stdout)
            self.assertEqual(job['metadata']['annotations']['helm.sh/hook'],'post-install,post-upgrade')
            container = job['spec']['template']['spec']['containers'][0]
            self.assertEqual(container['image'],'example.invalid/oan-seed:verified-source')
            self.assertIn('sync_geo_levels.py',container['command'][-1])
            self.assertIn('ON_ERROR_STOP=1',container['command'][-1])
            env = {item['name']:item for item in container['env']}
            self.assertNotIn('value',env['MDS_CLIENT_SECRET'])
            self.assertNotIn('value',env['PGPASSWORD'])
            self.assertNotEqual(env['MDS_CLIENT_SECRET']['valueFrom']['secretKeyRef'],env['PGPASSWORD']['valueFrom']['secretKeyRef'])
            self.assertFalse(any(name.startswith('MD_PG') for name in env))
            self.assertTrue((source/'templates/refactor-promotion-gate.yaml').exists())


if __name__ == '__main__': unittest.main()
