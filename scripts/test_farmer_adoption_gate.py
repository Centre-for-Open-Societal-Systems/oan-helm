"""Unit-test the actual gate with only its Kubernetes lookup supplied by fixture."""
import copy
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
HELM = os.environ.get('HELM', 'helm')
ROLES = {'staffApi':'staff-api','partnerApi':'partner-api','celeryWorker':'celery',
         'celeryBeat':'celery','staffUi':'staff-ui','dbSeed':'db-seed','sanity':'sanity-tests'}


class FarmerAdoptionGate(unittest.TestCase):
    def fixture(self):
        source = 'a' * 40
        images = {role:'example.invalid/' + role + ':' + source[:12] + '@sha256:' + 'b' * 64 for role in set(ROLES.values())}
        receipt = {'state':'NATIVE_READY','clusterUid':'a842b14f-b29f-4e78-b9d2-bfb22a17e53a',
                   'sourceCommit':source,'chartVersion':'1.0.0-dev.16','chartSha256':'c' * 64,
                   'backupVerified':True,'originalBusinessPreserved':True,'lock':'d' * 32,
                   'expiresAt':int(time.time()) + 3600,'images':images}
        values = {'farmerAdoption':{'mode':'preserving-upgrade','sourceCommit':source,'chartSha256':'c' * 64},
                  'registry':{component:{'image':{'repository':images[role].split(':',1)[0],
                                               'tag':images[role].split(':',1)[1]}} for component,role in ROLES.items()},
                  '_fixtureReceipt':{'data':{'receipt.json':json.dumps(receipt)}}}
        return values, receipt

    def render(self, values, upgrade=True, namespace='farmer', release='farmer-registry'):
        source = (ROOT/'charts/openg2p-farmer-registry/templates/refactor-promotion-gate.yaml').read_text()
        lookup = 'lookup "v1" "ConfigMap" "farmer" "registry-preserve-farmer"'
        self.assertEqual(source.count(lookup),1)
        # The whole production guard runs; only its external lookup is isolated.
        source = source.replace(lookup,'.Values._fixtureReceipt',1)
        with tempfile.TemporaryDirectory() as tmp:
            chart = Path(tmp)
            (chart/'templates').mkdir()
            (chart/'Chart.yaml').write_text('apiVersion: v2\nname: gate-fixture\nversion: 1.0.0-dev.16\n')
            (chart/'templates/gate.yaml').write_text(source)
            (chart/'values.yaml').write_text(yaml.safe_dump(values))
            args = [HELM,'template',release,str(chart),'-n',namespace]
            if upgrade: args.append('--is-upgrade')
            return subprocess.run(args,capture_output=True,text=True)

    def test_exact_native_ready_receipt_and_digest_images_pass(self):
        values,_ = self.fixture()
        result = self.render(values)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_wrong_receipt_identity_or_incomplete_preservation_is_blocked(self):
        defects = {'state':'BACKED_UP','clusterUid':'another','sourceCommit':'e'*40,
                   'chartVersion':'1.0.0-dev.14','chartSha256':'f'*64,'backupVerified':False,
                   'originalBusinessPreserved':False,'lock':'','expiresAt':int(time.time())-1}
        for key,value in defects.items():
            with self.subTest(key=key):
                values,receipt = self.fixture()
                receipt[key]=value
                values['_fixtureReceipt']['data']['receipt.json']=json.dumps(receipt)
                result=self.render(values)
                self.assertNotEqual(result.returncode,0)
                self.assertIn('develop-refactor is incomplete:',result.stderr)

    def test_every_image_is_bound_to_its_native_ready_digest(self):
        values,_=self.fixture()
        for component in ROLES:
            with self.subTest(component=component):
                changed=copy.deepcopy(values)
                changed['registry'][component]['image']['tag']='unreviewed@sha256:'+'e'*64
                self.assertNotEqual(self.render(changed).returncode,0)

    def test_install_other_release_namespace_and_value_only_admission_fail(self):
        values,_=self.fixture()
        for options in ({'upgrade':False},{'namespace':'crop'},{'release':'another'}):
            self.assertNotEqual(self.render(values,**options).returncode,0)
        values['_fixtureReceipt']=None
        self.assertNotEqual(self.render(values).returncode,0)
        self.assertNotEqual(self.render({}).returncode,0)

    def test_adoption_cannot_run_legacy_identity_provisioning(self):
        values,_=self.fixture()
        values['staffAccess']={'enabled':True}
        self.assertNotEqual(self.render(values).returncode,0)


if __name__ == '__main__': unittest.main()
