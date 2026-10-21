"""Run the saved, live Postman staff regression without publishing run events.

The private workspace launcher refreshes three test tokens and ensures marked
fixtures first. This runner accepts that environment, writes private raw reports
and a sanitized report, and exits nonzero for failures or missing executions.
"""
import argparse
import datetime
import json
from pathlib import Path
import re
import subprocess
import uuid

ROOT=Path(__file__).resolve().parents[1]
COLLECTION=ROOT/'postman/COSS-Automated-Staff.postman_collection.json'


def collection():
    fixture=json.loads((ROOT/'postman/staff-e2e-fixtures.json').read_text())
    expected=[]
    for row in fixture['records']:
        expected.append({**row,'recordId':str(uuid.uuid5(uuid.NAMESPACE_URL,'https://oanstaging.com/tests/'+row['functionalId']))})
    items=[]
    def add(name,method,path,status=200,body=None,script='',pre='',auth='staff_access_token',origin='{{agg_url}}'):
        request={'method':method,'url':origin+path,'header':[],'auth':{'type':'noauth'}}
        if auth:
            request['auth']={'type':'bearer','bearer':[{'key':'token','value':'{{'+auth+'}}','type':'string'}]}
        if body is not None:
            request['header']=[{'key':'Content-Type','value':'application/json'}]
            request['body']={'mode':'raw','raw':body if isinstance(body,str) else json.dumps(body)}
        statuses=status if isinstance(status,list) else [status]
        test="pm.test('HTTP status', () => pm.expect("+json.dumps(statuses)+").to.include(pm.response.code));\n"+script
        events=[{'listen':'test','script':{'type':'text/javascript','exec':test.splitlines()}}]
        if pre:events.insert(0,{'listen':'prerequest','script':{'type':'text/javascript','exec':pre.splitlines()}})
        items.append({'name':name,'request':request,'event':events})
    initialize="""['tab_queue','first_tab','observed_roots'].forEach(k=>pm.collectionVariables.unset(k));
pm.collectionVariables.set('tabs_expected',0);pm.collectionVariables.set('tabs_checked',0);
['staff_access_token','peer_access_token','no_role_access_token'].forEach(k=>{if(!pm.environment.get(k))throw new Error('Run the automated launcher to provision fresh test tokens');});"""
    add('01 Aggregation health','GET','/ping',auth=None,pre=initialize)
    add('02 Public catalog','GET','/aggregation/v1/registries',auth=None,script="""const j=pm.response.json();
pm.test('Exactly the configured registry set',()=>pm.expect(j.registries.map(r=>r.registryCode).sort()).to.eql(['CROPSOWN_REGISTRY','FARMER_REGISTRY','LIVESTOCK_REGISTRY']));
pm.test('No internal service URLs in public catalog',()=>pm.expect(pm.response.text()).not.to.include('svc.cluster.local'));""")
    add('03 Consent UI','GET','/',auth=None,origin='https://consent-manager.development.oanstaging.com',script="pm.test('HTML UI',()=>pm.expect(pm.response.headers.get('Content-Type')).to.include('text/html'));")
    add('04 Consent partner health','GET','/api/consent-manager-partner/ping',auth=None,origin='https://consent-manager-partner.development.oanstaging.com')
    add('05 Consent rejects anonymous administration','GET','/consent/v1/partners',[401,403],auth=None,origin='https://consent-manager.development.oanstaging.com')
    add('06 Aggregation viewer has no Consent administration','GET','/consent/v1/partners',403,origin='https://consent-manager.development.oanstaging.com')
    search='/aggregation/v1/staff/registry/search';tab='/aggregation/v1/staff/registry/tab'
    body={'foundationalId':'{{foundational_id}}','purpose':'synthetic_e2e_validation'}
    add('07 Missing staff token','POST',search,401,body,auth=None)
    add('08 Invalid staff token','POST',search,401,body,auth='invalid_access_token')
    add('09 Valid token without viewer role','POST',search,403,body,auth='no_role_access_token')
    add('10 Missing foundational ID','POST',search,400,{})
    add('11 Unknown registry','POST',search,400,body|{'registryFilter':['OAN_E2E_UNKNOWN']})
    absent_test="""const j=pm.response.json();
pm.test('All registries answered with proven absence',()=>{pm.expect(j.registries).to.have.lengthOf(3);j.registries.forEach(r=>{pm.expect(r.status).to.equal('not_found');pm.expect(r.complete).to.equal(true);pm.expect(r.records).to.eql([]);pm.expect(r.error).to.be.oneOf([null,undefined]);});});"""
    add('12 Absent synthetic subject','POST',search,200,body|{'foundationalId':fixture['absentFoundationalId']},script=absent_test)
    add('13 Substring cannot identify a subject','POST',search,200,body|{'foundationalId':fixture['substringFoundationalId']},script=absent_test)
    add('14 Exact synthetic subject across registries','POST',search,200,body,script="""const j=pm.response.json(); const expected=JSON.parse(pm.collectionVariables.get('expected_records'));
pm.test('Search contract and subject',()=>{pm.expect(j.schemaVersion).to.equal('1');pm.expect(j.foundationalId).to.equal(pm.environment.get('foundational_id'));pm.expect(j.searchId).to.be.a('string').and.not.empty;pm.expect(Date.parse(j.expiresAt)).to.be.above(Date.now());});
pm.test('Exact fixture IDs, complete results, no registry errors',()=>{
 pm.expect(j.registries).to.have.lengthOf(3);
 j.registries.forEach(r=>{const wanted=expected.filter(e=>e.registryCode===r.registryCode);pm.expect(r.status,r.registryCode).to.equal('found');pm.expect(r.complete).to.equal(true);pm.expect(r.error).to.be.oneOf([null,undefined]);pm.expect(r.records.map(x=>x.recordId).sort()).to.eql(wanted.map(x=>x.recordId).sort());r.records.forEach(x=>{const e=wanted.find(e=>e.recordId===x.recordId);pm.expect(x.summary.functionalId).to.equal(e.functionalId);pm.expect([x.summary.foundationalId,x.summary.linkFoundationalId]).to.include(pm.environment.get('foundational_id'));pm.expect(x.tabs.length).to.be.above(0);});});
});
const queue=[];(j.registries||[]).forEach(r=>(r.records||[]).forEach(record=>(record.tabs||[]).forEach(t=>{
 pm.test('Tab request stays on the intended record',()=>{pm.expect(t.request.method).to.equal('POST');pm.expect(t.request.url).to.equal('/aggregation/v1/staff/registry/tab');pm.expect(t.request.body.recordId).to.equal(record.recordId);pm.expect(t.request.body.registryCode).to.equal(r.registryCode);});queue.push(t.request.body);
})));
pm.collectionVariables.set('tab_queue',JSON.stringify(queue));pm.collectionVariables.set('tabs_expected',queue.length);
if(queue.length)pm.collectionVariables.set('first_tab',JSON.stringify(queue[0]));""")
    tab_pre="""const queue=JSON.parse(pm.collectionVariables.get('tab_queue')||'[]');
if(!queue.length)throw new Error('No fixture tabs were returned; refusing a vacuous pass');
pm.variables.set('current_tab',JSON.stringify(queue.shift()));pm.collectionVariables.set('tab_queue',JSON.stringify(queue));"""
    add('15 Open every returned tab','POST',tab,200,'{{current_tab}}',pre=tab_pre,script="""const j=pm.response.json();const sent=JSON.parse(pm.variables.get('current_tab'));
const expected=JSON.parse(pm.collectionVariables.get('expected_records'));const roots=JSON.parse(pm.collectionVariables.get('observed_roots')||'[]');
pm.test('Tab identity and schema match its search request',()=>{pm.expect(j.schemaVersion).to.equal('1');['registryCode','recordId','registerId','tabId','searchId'].forEach(k=>pm.expect(j[k],k).to.equal(sent[k]));pm.expect(j.sections).to.be.an('array');});
pm.test('Sections, fixture values and pagination',()=>{j.sections.forEach(s=>{pm.expect(s.fields).to.be.an('array');pm.expect(s.records).to.be.an('array');if(s.isList){pm.expect(s.pagination.page).to.equal(1);pm.expect(s.pagination.totalItems).to.be.at.least(s.records.length);}s.records.forEach(row=>{pm.expect(row.created_by).to.equal('oan-aggregation-e2e');pm.expect(expected.map(e=>e.recordId)).to.include(row.internal_record_id);if(row.internal_record_id===sent.recordId){const e=expected.find(e=>e.recordId===sent.recordId);pm.expect(row.functional_record_id).to.equal(e.functionalId);Object.entries(e.fields).forEach(([key,value])=>{pm.expect(row,key).to.have.property(key);pm.expect(row[key],key).to.equal(value);});if(!roots.includes(sent.recordId))roots.push(sent.recordId);}});});});
pm.collectionVariables.set('observed_roots',JSON.stringify(roots));pm.collectionVariables.set('tabs_checked',Number(pm.collectionVariables.get('tabs_checked'))+1);
const left=JSON.parse(pm.collectionVariables.get('tab_queue')||'[]');
if(left.length)pm.execution.setNextRequest(pm.info.requestName);
else {pm.test('Every offered tab executed and every root fixture returned',()=>{pm.expect(Number(pm.collectionVariables.get('tabs_checked'))).to.equal(Number(pm.collectionVariables.get('tabs_expected')));pm.expect(roots.sort()).to.eql(expected.map(e=>e.recordId).sort());});}""")
    first="const b=JSON.parse(pm.collectionVariables.get('first_tab')||'null');if(!b)throw new Error('Positive search must return a tab first');\n"
    add('16 Missing token on tab','POST',tab,401,'{{negative_tab}}',auth=None,pre=first+"pm.variables.set('negative_tab',JSON.stringify(b));")
    add('17 Other viewer cannot reuse a ticket','POST',tab,404,'{{negative_tab}}',auth='peer_access_token',pre=first+"pm.variables.set('negative_tab',JSON.stringify(b));")
    add('18 Tampered ticket rejected','POST',tab,404,'{{negative_tab}}',pre=first+"b.searchId += 'tampered';pm.variables.set('negative_tab',JSON.stringify(b));")
    add('19 Different record rejected','POST',tab,400,'{{negative_tab}}',pre=first+"b.recordId='00000000-0000-0000-0000-000000000000';pm.variables.set('negative_tab',JSON.stringify(b));")
    add('20 Unknown tab rejected','POST',tab,400,'{{negative_tab}}',pre=first+"b.tabId='OAN_E2E_UNKNOWN';pm.variables.set('negative_tab',JSON.stringify(b));")
    return {'info':{'name':'COSS automated new-dev staff regression','schema':'https://schema.getpostman.com/json/collection/v2.1.0/collection.json','description':'Run through the authorized local launcher: fixture setup and fresh test service tokens are automatic. Tests live staff access and registry data, Consent routing and access denial. Full partner OTP flow remains blocked pending SMS and partner setup.'},'item':items,'variable':[{'key':'expected_records','value':json.dumps(expected)},{'key':'foundational_id','value':fixture['foundationalId']},{'key':'agg_url','value':fixture['aggregationUrl']},{'key':'invalid_access_token','value':'invalid-regression-token'}]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generate-only',action='store_true')
    parser.add_argument('--environment',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'.build/staff-e2e')
    args=parser.parse_args()
    if args.generate_only:
        COLLECTION.write_text(json.dumps(collection(),indent=2)+'\n',encoding='utf-8')
        return
    if not args.environment:parser.error('--environment is required')
    args.output.mkdir(parents=True,exist_ok=True)
    result=subprocess.run(['postman','collection','run',str(COLLECTION),'-e',str(args.environment),
        '--no-report-events','--disable-unicode','--timeout','180000','--timeout-request','20000'],capture_output=True,text=True,encoding='utf-8',timeout=200)
    (args.output/'private-cli.log').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    stats={name:{'executed':int(executed),'failed':int(failed)} for name,executed,failed in
        re.findall(r'\|\s*(iterations|requests|test-scripts|prerequest-scripts|assertions)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',result.stdout)}
    names=re.findall(r'^Root (.+)$',result.stdout,re.MULTILINE)
    required={item['name'] for item in collection()['item']}
    seen={name.strip() for name in names}
    complete=required<=seen and len(stats)==5 and stats['assertions']['executed']>=40
    tests_passed=complete and all(value['failed']==0 for value in stats.values())
    report={'finishedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'target':'https://aggregation.development.oanstaging.com','live':True,
        'postmanExitCode':result.returncode,'passed':tests_passed and result.returncode==0,
        'cloudRunEventsEnabled':False,'stats':stats,
        'uniqueScenariosExecuted':len(seen),'requiredScenarios':len(required),
        'tabsOpened':sum(name.strip()=='15 Open every returned tab' for name in names),
        'identity':'Dedicated service accounts, not admin or nina.patel',
        'consentPartnerOtp':{'status':'blocked','prerequisites':['Partner realm/client and claims','Reviewed Consent and internal registry bindings plus PM signing key','SMS delivery; OTP remains disabled']},
        'rawReportsPrivate':True}
    (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    raise SystemExit(0 if report['passed'] else 1)


if __name__=='__main__':main()
