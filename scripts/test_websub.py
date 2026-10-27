"""Render the infrastructure contract without Kubernetes credentials."""
import os
from pathlib import Path
import subprocess
import tempfile
import shutil
import unittest
import yaml

ROOT=Path(__file__).resolve().parents[1]
CHART=ROOT/'charts/openg2p-commons-services'
HELM=os.environ.get('HELM','helm')

def render(enabled):
    # Isolate the unchanged WebSub resources. Commons' real promotion gate must
    # stay closed while its independent Master Data upgrade is rehearsed.
    with tempfile.TemporaryDirectory() as tmp:
        fixture=Path(tmp)
        (fixture/'templates').mkdir()
        (fixture/'charts').mkdir()
        for name in ('_helpers.tpl','_coss.tpl','websub-topics.yaml'):
            shutil.copyfile(CHART/'templates'/name,fixture/'templates'/name)
        shutil.copyfile(CHART/'charts/websub-1.3.2.tgz',fixture/'charts/websub-1.3.2.tgz')
        (fixture/'Chart.yaml').write_text('apiVersion: v2\nname: websub-contract\nversion: 1.0.0\ndependencies:\n- name: websub\n  version: 1.3.2\n  condition: websub.enabled\n')
        shutil.copyfile(CHART/'values.yaml',fixture/'values.yaml')
        args=[HELM,'template','commons-services',str(fixture),'-n','commons']
        if enabled:
            args+=['-f',str(ROOT/'environments/dev/values/commons-services.yaml')]
        result=subprocess.run(args,capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise AssertionError(result.stderr)
    return [d for d in yaml.safe_load_all(result.stdout) if d]

class WebsubContract(unittest.TestCase):
    def test_defaults_do_not_enable_websub(self):
        self.assertFalse(any('websub' in d['metadata']['name'] for d in render(False)))

    def test_dev_reuses_broker_without_public_routes(self):
        docs=render(True)
        hub=[d for d in docs if 'websub' in d['metadata']['name']]
        self.assertEqual({d['metadata']['name'] for d in hub if d['kind']=='Deployment'},
                         {'commons-services-websub','commons-services-websub-consolidator'})
        self.assertFalse(any(d['kind'] in ['VirtualService','Gateway','Ingress','StatefulSet'] for d in hub))
        for d in hub:
            if d['kind']=='Deployment':
                self.assertEqual(d['spec']['replicas'],1)
                self.assertIn('commons-kafka',str(d))
                init=d['spec']['template']['spec']['initContainers']
                self.assertEqual(init[0]['name'],'wait-for-websub-topics')
                self.assertIn('--describe --topic',init[0]['args'][0])
                self.assertNotIn('--create',init[0]['args'][0])
        jobs=[d for d in hub if d['kind']=='Job']
        self.assertEqual(len(jobs),1)
        command=jobs[0]['spec']['template']['spec']['containers'][0]['args'][0]
        for name in ['registered-websub-topics','consolidated-websub-topics',
                     'registered-websub-subscribers','consolidated-websub-subscribers']:
            self.assertIn('topic="'+name+'"',command)
        self.assertEqual(command.count('--create --if-not-exists'),4)
        self.assertEqual(command.count('--add-config retention.ms=-1,retention.bytes=-1'),4)
        self.assertNotIn('--delete',command)

    def test_renderer_keeps_only_reviewed_provisioning_job(self):
        docs=[{'apiVersion':'batch/v1','kind':'Job','metadata':{'name':name,'namespace':ns,
              'labels':{'oan.org/purpose':'websub-topic-provisioning'}},'spec':{}}
              for name,ns in [('commons-services-websub-topics-22','commons'),
                              ('commons-services-websub-topics-22','staging'),
                              ('bootstrap','commons')]]
        result=subprocess.run([__import__('sys').executable,str(ROOT/'scripts/dev-domain-post-renderer.py'),
            '--skip-initialization-jobs'],input=yaml.safe_dump_all(docs),capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        kept=list(yaml.safe_load_all(result.stdout))
        self.assertEqual(len(kept),1)
        self.assertEqual(kept[0]['metadata']['namespace'],'commons')

if __name__=='__main__':unittest.main()
