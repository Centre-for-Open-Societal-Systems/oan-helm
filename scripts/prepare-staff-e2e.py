"""New-dev-only fixture and least-privilege test identity preparation.

Executed on the authorized RKE2 host by a private transport wrapper. A caller
injects FIXTURE and TRANSFER_PUBLIC_KEY before this file. Only encrypted,
short-lived test tokens leave the host. Existing human accounts are untouched.
"""
import base64
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request
import uuid

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

os.umask(0o077)
os.environ['KUBECONFIG']='/etc/rancher/rke2/rke2.yaml'
K='/var/lib/rancher/rke2/bin/kubectl'
ROLE='AGGREGATION_STAFF_VIEWER'
CLIENTS={'staff_access_token':True,'peer_access_token':True,'no_role_access_token':False}


def run(args, data=None):
    result=subprocess.run(args,input=data,capture_output=True,timeout=30)
    if result.returncode:raise RuntimeError('Protected preparation command failed; output withheld')
    return result.stdout.decode()


def resource(kind,name):
    return json.loads(run([K,'get',kind,name,'-n','commons','-o','json']))


def sql(database,query):
    return run([K,'exec','-i','-n','commons','commons-postgresql-0','--','sh','-c',
        'export PGPASSWORD="$POSTGRES_POSTGRES_PASSWORD"; exec "$@"','e2e',
        'psql','-X','-q','-At','-v','ON_ERROR_STOP=1','-h','127.0.0.1',
        '-U','postgres','-d',database],query.encode())


def literal(value):
    return "'"+str(value).replace("'","''")+"'"


def main():
    assert FIXTURE['profile']=='oan-new-dev-staff-e2e-v1'
    assert FIXTURE['issuer']=='https://keycloak.development.oanstaging.com/realms/staff'
    routes=json.loads(run([K,'get','virtualservices.networking.istio.io','-n','commons','-o','json']))['items']
    assert any('aggregation.development.oanstaging.com' in item['spec'].get('hosts',[]) for item in routes), 'Wrong cluster profile'
    values=json.loads(run(['helm','get','values','commons','-n','commons','--all','-o','json']))
    base='http://'+resource('service','commons-keycloak')['spec']['clusterIP']
    password=base64.b64decode(resource('secret','commons-keycloak')['data']['admin-password']).decode()
    def token(form):
        with urllib.request.urlopen(urllib.request.Request(base+'/realms/'+form.pop('_realm','staff')+'/protocol/openid-connect/token',data=urllib.parse.urlencode(form).encode()),timeout=20) as response:
            return json.load(response)['access_token']
    admin=token({'_realm':'master','grant_type':'password','client_id':'admin-cli','username':values['keycloak']['auth']['adminUser'],'password':password})
    def api(path,method='GET',body=None):
        request=urllib.request.Request(base+'/admin/realms/staff'+path,method=method,data=None if body is None else json.dumps(body).encode(),headers={'Authorization':'Bearer '+admin,'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=20) as response:
            data=response.read()
            return json.loads(data) if data else None
    role=api('/roles/'+ROLE)
    tokens={};identity_audit=[]
    for variable,viewer in CLIENTS.items():
        client_id={'staff_access_token':'oan-aggregation-e2e','peer_access_token':'oan-aggregation-e2e-peer','no_role_access_token':'oan-aggregation-e2e-denied'}[variable]
        matches=api('/clients?'+urllib.parse.urlencode({'clientId':client_id}))
        settings={'clientId':client_id,'name':'OAN automated staff test '+('viewer' if viewer else 'denial'),'description':'Dedicated development test identity; no human impersonation or registry client grants.','enabled':True,'protocol':'openid-connect','publicClient':False,'serviceAccountsEnabled':True,'standardFlowEnabled':False,'implicitFlowEnabled':False,'directAccessGrantsEnabled':False,'fullScopeAllowed':False}
        created=not matches
        if created:
            api('/clients','POST',settings)
            matches=api('/clients?'+urllib.parse.urlencode({'clientId':client_id}))
        assert len(matches)==1
        client=matches[0]
        for key in ['enabled','publicClient','serviceAccountsEnabled','standardFlowEnabled','implicitFlowEnabled','directAccessGrantsEnabled','fullScopeAllowed']:
            assert client.get(key)==settings[key], 'Existing test identity has unexpected settings'
        account=api('/clients/'+client['id']+'/service-account-user')
        paths=['/users/'+account['id']+'/role-mappings/realm','/clients/'+client['id']+'/scope-mappings/realm']
        for path in paths:
            mapped=api(path)
            if viewer and not any(item['id']==role['id'] for item in mapped):
                api(path,'POST',[{'id':role['id'],'name':role['name']}])
        effective=api(paths[0]+'/composite')
        assert any(item['id']==role['id'] for item in effective)==viewer
        mappings=api('/users/'+account['id']+'/role-mappings')
        assert not mappings.get('clientMappings'), 'Dedicated test account has unexpected client roles'
        secret=api('/clients/'+client['id']+'/client-secret')['value']
        issued=token({'grant_type':'client_credentials','client_id':client_id,'client_secret':secret})
        claims=json.loads(base64.urlsafe_b64decode(issued.split('.')[1]+'==='))
        assert claims['iss']==FIXTURE['issuer'] and claims['azp']==client_id
        assert (ROLE in claims.get('realm_access',{}).get('roles',[]))==viewer
        tokens[variable]=issued
        identity_audit.append({'clientId':client_id,'created':created,'viewer':viewer,'humanAccount':False,'passwordGrantEnabled':False,'expiresAt':claims['exp']})
    rows=[]
    for definition in FIXTURE['records']:
        definition=dict(definition)
        definition['recordId']=str(uuid.uuid5(uuid.NAMESPACE_URL,'https://oanstaging.com/tests/'+definition['functionalId']))
        row={'internal_record_id':definition['recordId'],'functional_record_id':definition['functionalId'],
             'record_name':'OAN AUTOMATED TEST '+definition['functionalId'],
             'created_by':FIXTURE['marker'],'last_approved_by':FIXTURE['marker'],
             'created_at':'2026-10-19 00:00:00','last_approved_at':'2026-10-19 00:00:00',
             'record_status':'ACTIVE','search_text':FIXTURE['foundationalId']+' '+definition['functionalId']+' '+FIXTURE['marker'],**definition['fields']}
        definition['expectedFields']=row
        rows.append(definition)
    fixture_audit=[]
    # Preflight every target and collision before any fixture insertion.
    for row in rows:
        table=row['table'];database=row['database']
        assert database in ['farmer_registry','cropsown_registry','livestock_registry']
        assert table in ['g2p_register_farmers','g2p_register_crop_sowns','g2p_register_livestocks']
        columns=json.loads(sql(database,"SELECT json_agg(column_name) FROM information_schema.columns WHERE table_schema='public' AND table_name="+literal(table)))
        assert set(row['expectedFields'])<=set(columns),'Fixture differs from deployed schema'
        collisions=json.loads(sql(database,"SELECT coalesce(json_agg(to_jsonb(t)), '[]'::json) FROM "+table+" t WHERE internal_record_id="+literal(row['recordId'])+" OR functional_record_id="+literal(row['functionalId'])+" OR (search_text LIKE '%OAN-E2E-UIN-0001%' AND created_by<>"+literal(FIXTURE['marker'])+")"))
        for existing in collisions:
            assert existing['internal_record_id']==row['recordId'] and existing['created_by']==FIXTURE['marker'],'Fixture collides with an unrelated row'
            for key,value in row['expectedFields'].items():
                if key in ['created_at','last_approved_at']:continue
                assert existing.get(key)==value,'Existing fixture drifted; refusing to overwrite'
        row['alreadyPresent']=bool(collisions)
    for database in sorted({row['database'] for row in rows}):
        statements=['BEGIN;','SET LOCAL lock_timeout = \'5s\';','SET LOCAL statement_timeout = \'15s\';']
        for row in rows:
            if row['database']!=database:continue
            document=json.dumps(row['expectedFields'])
            statements.append('INSERT INTO '+row['table']+' SELECT * FROM json_populate_record(NULL::'+row['table']+','+literal(document)+') ON CONFLICT (internal_record_id) DO NOTHING;')
        statements.append('COMMIT;')
        sql(database,'\n'.join(statements))
    for row in rows:
        stored=json.loads(sql(row['database'],'SELECT to_jsonb(t) FROM '+row['table']+' t WHERE internal_record_id='+literal(row['recordId'])))
        assert stored['created_by']==FIXTURE['marker'] and stored['functional_record_id']==row['functionalId']
        for key,value in row['expectedFields'].items():
            if key not in ['created_at','last_approved_at']:assert stored.get(key)==value
        fixture_audit.append({'database':row['database'],'table':row['table'],'recordId':row['recordId'],'functionalId':row['functionalId'],'inserted':not row['alreadyPresent'],'sha256':hashlib.sha256(json.dumps(stored,sort_keys=True).encode()).hexdigest()})
    deployed=[]
    for name in ['commons-services-aggregation-api','commons-services-cm-api','commons-services-cm-partner-api']:
        workload=resource('deployment',name)
        deployed.append({'name':name,'images':[container['image'] for container in workload['spec']['template']['spec']['containers']],
                         'replicas':workload['spec'].get('replicas',1),'readyReplicas':workload.get('status',{}).get('readyReplicas',0)})
    report={'preparedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'identities':identity_audit,'fixtures':fixture_audit,'deployedWorkloads':deployed,'existingRowsUpdated':False,'otpEnabled':False,'humanAccountsModified':False}
    audit=Path('/var/lib/oan-aggregation-development/e2e');audit.mkdir(mode=0o700,parents=True,exist_ok=True)
    (audit/'last-preparation.json').write_text(json.dumps(report,indent=2)+'\n')
    plaintext=json.dumps({'tokens':tokens,'fixture':FIXTURE|{'records':rows},'preparation':report}).encode()
    aes=AESGCM.generate_key(bit_length=256);nonce=os.urandom(12)
    public=serialization.load_pem_public_key(TRANSFER_PUBLIC_KEY.encode())
    encrypted_key=public.encrypt(aes,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    print(json.dumps({'encryptedTransfer':{'key':base64.b64encode(encrypted_key).decode(),'nonce':base64.b64encode(nonce).decode(),'data':base64.b64encode(AESGCM(aes).encrypt(nonce,plaintext,None)).decode()}}))


if __name__=='__main__':
    main()
