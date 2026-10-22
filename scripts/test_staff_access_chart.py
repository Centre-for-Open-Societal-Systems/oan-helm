"""Validate the opt-in staff hook without any cluster access."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ITEMS=[{'registry':r,'template':(ROOT/f'charts/openg2p-{r}-registry/templates/staff-access-job.yaml').read_text()} for r in ['farmer','livestock','cropsown']]
SHELLS=[]
import json,pathlib,subprocess,tempfile,yaml
checks=0
with tempfile.TemporaryDirectory(prefix='staff-hook-validation-') as directory:
 root=pathlib.Path(directory);(root/'templates').mkdir()
 (root/'Chart.yaml').write_text('apiVersion: v2\nname: staff-hook-test\nversion: 0.0.1\n')
 for item in ITEMS:
  (root/'templates/staff-access-job.yaml').write_text(item['template'])
  values={'openg2p-registry':{'dbSeed':{'image':{'repository':'example.invalid/seed','tag':'fixture'}}},'staffAccess':{'enabled':False,'existingSecret':'fixture-secret','twoStages':item['registry']=='farmer','policyKeys':['registry.intake_form.'+item['registry']]}}
  def render():
   (root/'values.yaml').write_text(yaml.safe_dump(values))
   return subprocess.run(['helm','template','fixture',str(root)],text=True,capture_output=True)
  r=render();assert r.returncode==0 and not r.stdout.strip();checks+=1
  values['staffAccess']['enabled']=True;r=render();assert r.returncode==0,r.stderr
  job=list(yaml.safe_load_all(r.stdout))[0];container=job['spec']['template']['spec']['containers'][0]
  assert container['command']==['python3','/seed/staff_access.py']
  assert container['envFrom'][0]['secretRef']['name']=='fixture-secret'
  assert job['spec']['template']['spec']['automountServiceAccountToken'] is False
  assert dict((x['name'],x['value']) for x in container['env'])['STAFF_SEED_REGISTRY']==item['registry'];checks+=1
  values['staffAccess']['existingSecret']='';assert render().returncode!=0;checks+=1
  values['staffAccess']['existingSecret']='fixture-secret';values['staffAccess']['policyKeys']=[];assert render().returncode!=0;checks+=1
 for shell in SHELLS:
  r=subprocess.run(['sh','-n'],input=shell,text=True,capture_output=True);assert r.returncode==0,r.stderr;checks+=1
print(json.dumps({'helmAndShellChecks':checks,'result':'passed','deploymentPerformed':False}))
