"""Read-only authorization-page regression for the development reverse proxy.

Uses synthetic OAuth state/nonce and submits no credentials. Raw response and
temporary login cookies stay under ignored .build. Requires Postman CLI.
"""
import json
from pathlib import Path
import re
import subprocess
import urllib.parse

ROOT=Path(__file__).resolve().parents[1]


def main():
    query=urllib.parse.urlencode({
        'response_type':'code','client_id':'staff-portal',
        'redirect_uri':'https://staff-iam.development.oanstaging.com/auth/callback',
        'scope':'openid profile email','state':'regression-'+'s'*2048,'nonce':'n'*1024,
    })
    url='https://keycloak.development.oanstaging.com/realms/staff/protocol/openid-connect/auth?'+query
    work=ROOT/'.build/keycloak-login-regression';work.mkdir(parents=True,exist_ok=True)
    result=subprocess.run(['postman','request',url,'--script-post-request','@'+str(ROOT/'postman/check-keycloak-login.js'),
                           '--timeout','15000','--output',str(work/'response.json')],capture_output=True,text=True,encoding='utf-8',timeout=45)
    (work/'postman.log').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    matched=re.search(r'(\d+) passed',result.stdout)
    passed=int(matched[1]) if matched else 0
    report={'postmanExitCode':result.returncode,'assertionsPassed':passed,'assertionsTotal':5,
            'credentialSubmission':False,'syntheticStateCharacters':2059,'syntheticNonceCharacters':1024}
    print(json.dumps(report))
    if result.returncode or passed!=5:raise SystemExit('Keycloak login regression failed; inspect ignored .build/keycloak-login-regression')


if __name__=='__main__':main()
