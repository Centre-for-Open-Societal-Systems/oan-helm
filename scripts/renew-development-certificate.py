"""Renew dev wildcard TLS through Jenkins; AWS credentials exist only for this run.

Requires AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY, SSH_KEY and SSH_KNOWN_HOSTS
bindings on the existing VPN Jenkins agent. Never prints credential values.
"""
import json
import os
import subprocess
import base64

REMOTE = r'''
import sys,json,os,subprocess,shutil,re
from pathlib import Path
os.umask(0o077)
credentials=json.load(sys.stdin)
home=Path('/var/lib/oan-development-acme');home.mkdir(mode=0o700,parents=True,exist_ok=True)
ca=Path('/opt/acme.sh/ca')
if ca.is_dir() and not (home/'ca').exists():shutil.copytree(ca,home/'ca')
env=dict(os.environ,**credentials)
log=home/'renewal.log'
try:
    args=['/opt/acme.sh/acme.sh','--home','/opt/acme.sh','--config-home',str(home),'--server','letsencrypt']
    cert=home/'development.oanstaging.com_ecc'/'fullchain.cer'
    action=['--renew','-d','development.oanstaging.com','--ecc'] if cert.exists() else ['--issue','--dns','dns_aws','-d','development.oanstaging.com','-d','*.development.oanstaging.com','--keylength','ec-256']
    with log.open('ab') as out:
        result=subprocess.run(args+action,env=env,stdout=out,stderr=out,timeout=600)
    if result.returncode not in [0,2]:raise RuntimeError('ACME operation failed; inspect private renewal.log')
    # The DNS plugin persists credential fields by default. Strip them after
    # every run; Jenkins supplies the binding afresh on the next scheduled run.
    target=Path('/etc/openg2p/certs/development-wildcard.oanstaging.com');target.mkdir(mode=0o700,parents=True,exist_ok=True)
    install=args+['--install-cert','-d','development.oanstaging.com','--ecc','--key-file',str(target/'privkey.pem'),'--fullchain-file',str(target/'fullchain.pem'),'--reloadcmd','nginx -t && systemctl reload nginx']
    with log.open('ab') as out:subprocess.run(install,env=env,stdout=out,stderr=out,check=True,timeout=60)
    metadata=subprocess.run(['openssl','x509','-in',str(target/'fullchain.pem'),'-noout','-dates','-ext','subjectAltName'],capture_output=True,text=True,check=True).stdout
    print(json.dumps({'certificateInstalled':True,'publicMetadata':metadata.strip(),'privateLog':str(log),'renewalOwner':'Jenkins oan-development-wildcard-certificate-renewal'}))
finally:
    for p in [home/'account.conf',*home.glob('**/*.conf')]:
        if p.is_file():
            text=p.read_text();clean=re.sub(r'(?m)^(?:SAVED_)?AWS_(?:ACCESS_KEY_ID|SECRET_ACCESS_KEY|SESSION_TOKEN)=.*\n?','',text)
            if text!=clean:p.write_text(clean)
'''


def main():
    credentials={k:os.environ[k] for k in ['AWS_ACCESS_KEY_ID','AWS_SECRET_ACCESS_KEY']}
    if os.environ.get('AWS_SESSION_TOKEN'):credentials['AWS_SESSION_TOKEN']=os.environ['AWS_SESSION_TOKEN']
    command='sudo -n python3 -c "import base64;exec(base64.b64decode(\''+base64.b64encode(REMOTE.encode()).decode()+'\'))"'
    result=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','StrictHostKeyChecking=yes','-o','UserKnownHostsFile='+os.environ['SSH_KNOWN_HOSTS'],'-i',os.environ['SSH_KEY'],'ubuntu@13.201.58.55',command],input=json.dumps(credentials),capture_output=True,text=True,timeout=750)
    for line in result.stdout.splitlines():
        if line.startswith('{'):print(line)
    if result.returncode:raise RuntimeError('Certificate operation failed; inspect the protected server log. SSH/ACME raw output withheld.')


if __name__=='__main__':main()
