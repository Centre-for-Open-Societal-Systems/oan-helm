"""Check live UI/API routing and temporary legacy compatibility without credentials."""
import argparse
import datetime
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
COLLECTION=ROOT/'postman/COSS-Registry-Public-URLs.postman_collection.json'


def collection():
    items=[]
    def add(name,url,accept,status,script,redirect=True):
        tests="pm.test('Expected HTTP status',()=>pm.response.to.have.status("+str(status)+"));\n"+script
        items.append({'name':name,'protocolProfileBehavior':{'followRedirects':redirect},
            'request':{'method':'GET','url':url,'auth':{'type':'noauth'},'header':[{'key':'Accept','value':accept}]},
            'event':[{'listen':'test','script':{'type':'text/javascript','exec':tests.splitlines()}}]})
    for registry in ['crop','livestock']:
        canonical='https://'+registry+'-registry.development.oanstaging.com'
        legacy='https://'+registry+'-registry-development.oanstaging.com'
        html="pm.test('Registry HTML returned',()=>pm.expect(pm.response.headers.get('Content-Type')).to.include('text/html'));"
        add(registry+' canonical UI',canonical+'/en','text/html',200,html)
        add(registry+' legacy browser redirect',legacy+'/en?routing-check=1','text/html',307,
            "pm.test('Canonical redirect preserves path and query',()=>pm.expect(pm.response.headers.get('Location')).to.equal("+json.dumps(canonical+'/en?routing-check=1')+"));",False)
        add(registry+' legacy non-browser proxy',legacy+'/en','application/json',200,html,False)
        for role in ['staff','partner']:
            for old in [False,True]:
                host=role+'-'+registry+('-development' if old else '.development')+'.oanstaging.com'
                add(registry+' '+role+(' legacy' if old else ' canonical')+' API','https://'+host+'/ping','application/json',200,
                    "pm.test('Registry API answered',()=>pm.expect(pm.response.json()).to.equal('pong'));",False)
    return {'info':{'name':'COSS registry public URL regression','schema':'https://schema.getpostman.com/json/collection/v2.1.0/collection.json',
        'description':'Read-only live routing checks, with no login or fixtures. Detects canonical routes missing despite healthy internal registry APIs. Legacy HTML GET redirects, JSON/API calls keep proxy compatibility.'},'item':items}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generate-only',action='store_true')
    parser.add_argument('--output',type=Path,default=ROOT/'.build/registry-public-urls')
    args=parser.parse_args()
    if args.generate_only:
        COLLECTION.write_text(json.dumps(collection(),indent=2)+'\n',encoding='utf-8',newline='\n')
        return
    args.output.mkdir(parents=True,exist_ok=True)
    result=subprocess.run(['postman','collection','run',str(COLLECTION),'--no-report-events','--disable-unicode',
        '--timeout','120000','--timeout-request','15000'],capture_output=True,text=True,encoding='utf-8',timeout=135)
    (args.output/'cli.log').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    stats={name:{'executed':int(total),'failed':int(failed)} for name,total,failed in
        re.findall(r'\|\s*(requests|assertions)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',result.stdout)}
    passed=result.returncode==0 and len(stats)==2 and stats['requests']['executed']==14 and stats['assertions']['executed']==28 and all(s['failed']==0 for s in stats.values())
    report={'checkedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'live':True,'passed':passed,
        'postmanExitCode':result.returncode,'stats':stats,'credentialsRequired':False,'cloudRunEventsEnabled':False}
    (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    raise SystemExit(0 if passed else 1)


if __name__=='__main__':main()
