"""Read-only live routing and authentication checks; submits no credentials/data.

Requires Postman CLI. Detailed responses remain in ignored .build; no tokens,
partner registrations, grants or registry searches are created by these probes.
"""
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PROBES=[
    ('aggregation-health','GET','https://aggregation.development.oanstaging.com/ping',[200],None),
    ('aggregation-catalog','GET','https://aggregation.development.oanstaging.com/aggregation/v1/registries',[200],None),
    ('staff-search-no-token','POST','https://aggregation.development.oanstaging.com/aggregation/v1/staff/registry/search',[401],None),
    ('staff-search-invalid-token','POST','https://aggregation.development.oanstaging.com/aggregation/v1/staff/registry/search',[401],'Bearer invalid-regression-token'),
    ('staff-tab-no-token','POST','https://aggregation.development.oanstaging.com/aggregation/v1/staff/registry/tab',[401],None),
    ('consent-staff-no-token','GET','https://consent-manager.development.oanstaging.com/consent/v1/partners',[401,403],None),
    ('consent-partner-health','GET','https://consent-manager-partner.development.oanstaging.com/api/consent-manager-partner/ping',[200],None),
    ('consent-ui','GET','https://consent-manager.development.oanstaging.com/',[200],None),
    ('legacy-consent-ui','GET','https://consent-manager-development.oanstaging.com/',[200],None),
    ('legacy-consent-partner-health','GET','https://consent-manager-partner-development.oanstaging.com/api/consent-manager-partner/ping',[200],None),
]


def main():
    work=ROOT/'.build/consent-aggregation-live';work.mkdir(parents=True,exist_ok=True)
    report={'profile':'live read-only health/routing and missing/invalid-token rejection; no credential submission','probes':[]}
    for name,method,url,statuses,authorization in PROBES:
        assertions="pm.test('Expected HTTP status', () => pm.expect("+json.dumps(statuses)+").to.include(pm.response.code));\n"
        if name=='aggregation-catalog':
            assertions+="pm.test('Three configured registries', () => pm.expect(pm.response.json().registries).to.have.lengthOf(3));\n"
            assertions+="pm.test('Internal service addresses are hidden', () => pm.expect(pm.response.text()).not.to.include('svc.cluster.local'));\n"
        script=work/(name+'.js');script.write_text(assertions,encoding='utf-8')
        args=['postman','request',method,url,'--script-post-request','@'+str(script),'--timeout','20000','--output',str(work/(name+'.json'))]
        if method=='POST':args+=['--header','Content-Type: application/json','--body','{}']
        if authorization:args+=['--header','Authorization: '+authorization]
        result=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=35)
        (work/(name+'.log')).write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
        match=re.search(r'(\d+) passed',result.stdout);passed=int(match[1]) if match else 0
        expected=3 if name=='aggregation-catalog' else 1
        # The CLI exits 1 on an HTTP 4xx even when its status assertions pass.
        expected_rejection=all(status>=400 for status in statuses)
        execution_ok=result.returncode==0 or (expected_rejection and result.returncode==1)
        report['probes'].append({'name':name,'expectedStatuses':statuses,'expectedHttpRejection':expected_rejection,'postmanExitCode':result.returncode,'assertionsPassed':passed,'assertionsTotal':expected,'passed':execution_ok and passed==expected})
    report['passed']=all(p['passed'] for p in report['probes'])
    report['assertionsPassed']=sum(p['assertionsPassed'] for p in report['probes'])
    report['assertionsTotal']=sum(p['assertionsTotal'] for p in report['probes'])
    (work/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
