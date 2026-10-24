"""Isolated template contracts; candidate promotion gates remain unconditional."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HELM = os.environ.get('HELM', 'helm')


class RefactorContracts(unittest.TestCase):
    def test_master_data_snapshot_is_exact_and_pinned(self):
        folder = ROOT/'upstream-snapshots/master-data-location'
        source = json.loads((folder/'SOURCE.json').read_text(encoding='utf-8'))
        for name, digest in source['sourceFilesSha256'].items():
            self.assertEqual(hashlib.sha256((folder/'openg2p-master-data'/name).read_bytes()).hexdigest(),digest,name)
        values = yaml.safe_load((ROOT/'charts/openg2p-commons-services/values.yaml').read_text(encoding='utf-8'))['master-data']
        self.assertFalse(values['geoSeed']['enabled'])
        self.assertFalse(values['geoSeed']['load']['samples'])
        self.assertFalse(values['geoSeed']['autoPublish'])
        self.assertEqual(len(source['images']),3)

    def render(self, chart, *args):
        return subprocess.run([HELM,'template','test',str(chart),*args],capture_output=True,text=True,encoding='utf-8')

    def test_dashboard_auth_digest_and_pull_settings(self):
        for domain in ('cropsown','livestock'):
            with self.subTest(domain=domain), tempfile.TemporaryDirectory() as tmp:
                source = ROOT/f'charts/openg2p-{domain}-registry'
                fixture = Path(tmp)
                (fixture/'templates').mkdir()
                # Render only the reporting API template, without registry workloads.
                # The real chart gate is neither edited nor bypassed for deployment.
                for name in ('_coss.tpl','_reporting.tpl','dashboard-api.yaml'):
                    shutil.copyfile(source/'templates'/name,fixture/'templates'/name)
                (fixture/'Chart.yaml').write_text('apiVersion: v2\nname: auth-contract\nversion: 1.0.0+test\n')
                values = yaml.safe_load((source/'values.yaml').read_text(encoding='utf-8'))
                values['dashboardApi'].update({'enabled':True,'image':{'repository':'example.invalid/api','digest':'sha256:'+'a'*64},
                    'imagePullSecrets':[{'name':'preserved-pull'}],'envFrom':[{'secretRef':{'name':'preserved-env'}}]})
                values['dashboardApi']['auth']['issuer']='https://iam.verification.invalid/realms/staff'
                (fixture/'values.yaml').write_text(yaml.safe_dump(values))
                result = self.render(fixture)
                self.assertEqual(result.returncode,0,result.stderr)
                deployment = next(doc for doc in yaml.safe_load_all(result.stdout) if doc['kind']=='Deployment')
                pod = deployment['spec']['template']['spec']
                container = pod['containers'][0]
                env = {item['name']:item for item in container['env']}
                self.assertEqual(env['AUTH_ENABLED']['value'],'true')
                self.assertEqual(env['AUTH_ROLE']['value'],'charts:read')
                self.assertEqual(container['image'],'example.invalid/api@sha256:'+'a'*64)
                self.assertEqual(pod['imagePullSecrets'],[{'name':'preserved-pull'}])
                self.assertEqual(container['envFrom'],[{'secretRef':{'name':'preserved-env'}}])
                self.assertIn('secretKeyRef',env['PGPASSWORD']['valueFrom'])
                for settings, message in [(['--set','dashboardApi.auth.enabled=false'],'require dashboardApi.auth.enabled=true'),
                    (['--set','dashboardApi.auth.issuer=','--set','dashboardApi.auth.iamUrl='],'issuer or dashboardApi.auth.iamUrl is required'),
                    (['--set','dashboardApi.env.AUTH_ENABLED=false'],'reserved authentication settings')]:
                    rejected = self.render(fixture,*settings)
                    self.assertNotEqual(rejected.returncode,0)
                    self.assertIn(message,rejected.stderr)


if __name__=='__main__': unittest.main()
