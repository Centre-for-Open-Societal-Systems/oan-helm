"""Normal browser PKCE login using a private synthetic partner account.

Requires Playwright and Chromium. Never uses a real user's session/profile,
never prints credentials or token-bearing URLs, and creates no Consent grants.
"""
import argparse
import datetime
import json
from pathlib import Path
import urllib.parse

from playwright.sync_api import sync_playwright, expect

HOST='https://consent-partner-portal.development.oanstaging.com'
ISSUER='https://keycloak.development.oanstaging.com/realms/partner'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--credentials-file',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--browser-executable')
    args=parser.parse_args()
    credentials=json.loads(args.credentials_file.read_text(encoding='utf-8'))
    assert credentials['username']=='oan-partner-e2e' and credentials['partner_id']=='oan-partner-e2e'
    args.output.mkdir(parents=True,exist_ok=True)
    report={'startedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host':HOST,'syntheticUser':credentials['username'],'partnerId':credentials['partner_id'],'authorizationCodeWithPkce':False,'codeVerifierSent':False,'apiResponses':[],'pages':[],'consoleErrors':0,'passed':False}
    token={}
    with sync_playwright() as playwright:
        settings={'headless':True}
        if args.browser_executable:settings['executable_path']=args.browser_executable
        browser=playwright.chromium.launch(**settings)
        context=browser.new_context(viewport={'width':1440,'height':1000})
        page=context.new_page()
        def request_seen(request):
            parsed=urllib.parse.urlsplit(request.url)
            if request.url.startswith(ISSUER+'/protocol/openid-connect/auth?'):
                query=urllib.parse.parse_qs(parsed.query)
                report['authorizationCodeWithPkce']=(query.get('response_type')==['code'] and query.get('client_id')==['consent-partner-portal'] and query.get('code_challenge_method')==['S256'] and bool(query.get('code_challenge')))
            if request.url==ISSUER+'/protocol/openid-connect/token' and request.method=='POST':
                form=urllib.parse.parse_qs(request.post_data or '')
                report['codeVerifierSent']=bool(form.get('code_verifier')) and form.get('grant_type')==['authorization_code']
            if parsed.netloc==urllib.parse.urlsplit(HOST).netloc and parsed.path=='/consent/v1/partner-portal/me':
                authorization=request.headers.get('authorization','')
                if authorization.startswith('Bearer '):token['access_token']=authorization[7:]
        def response_seen(response):
            parsed=urllib.parse.urlsplit(response.url)
            if parsed.netloc==urllib.parse.urlsplit(HOST).netloc and parsed.path.startswith('/consent/v1/partner-portal/'):
                report['apiResponses'].append({'path':parsed.path,'status':response.status})
        page.on('request',request_seen)
        page.on('response',response_seen)
        page.on('pageerror',lambda _:report.update(consoleErrors=report['consoleErrors']+1))
        try:
            page.goto(HOST,wait_until='domcontentloaded',timeout=30000)
            page.locator('#username').wait_for(timeout=30000)
            page.locator('#username').fill(credentials['username'])
            page.locator('#password').fill(credentials['password'])
            page.locator('#kc-login').click()
            page.wait_for_url(HOST+'/**',timeout=30000)
            expect(page.get_by_role('heading',name='Consent requests',exact=True)).to_be_visible(timeout=30000)
            expect(page.locator('.user-partner')).to_have_text(credentials['partner_id'])
            expect(page.locator('.dev-pill')).to_have_count(0)
            report['pages'].append('/requests')
            for link,heading,path in [('Consents','Consents','/consents'),('What we can ask for','What we can ask for','/access')]:
                page.get_by_role('link',name=link,exact=True).click()
                expect(page.get_by_role('heading',name=heading,exact=True)).to_be_visible(timeout=15000)
                expect(page.locator('.notice-error')).to_have_count(0)
                report['pages'].append(path)
            page.screenshot(path=str(args.output/'portal-signed-in.png'),full_page=True)
            assert report['authorizationCodeWithPkce'] and report['codeVerifierSent']
            required={'/consent/v1/partner-portal/me','/consent/v1/partner-portal/consent-requests','/consent/v1/partner-portal/consents','/consent/v1/partner-portal/bindings'}
            assert required<={entry['path'] for entry in report['apiResponses']}
            assert all(entry['status']==200 for entry in report['apiResponses'])
            assert report['consoleErrors']==0 and token.get('access_token')
            environment={'name':'OAN private partner portal browser session','_postman_variable_scope':'environment','values':[{'key':'portal_url','value':HOST,'enabled':True,'type':'default'},{'key':'partner_access_token','value':token['access_token'],'enabled':True,'type':'secret'},{'key':'expected_partner_id','value':credentials['partner_id'],'enabled':True,'type':'default'},{'key':'expected_username','value':credentials['username'],'enabled':True,'type':'default'}]}
            (args.output/'private-postman-environment.json').write_text(json.dumps(environment,indent=2)+'\n',encoding='utf-8')
            report['passed']=True
        except Exception as error:
            report['errorType']=type(error).__name__
            report['lastPagePath']=urllib.parse.urlsplit(page.url).path
            page.screenshot(path=str(args.output/'portal-failure.png'),full_page=True)
        finally:
            browser.close()
            report['finishedAtUtc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
            (args.output/'browser-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
            print(json.dumps(report))
    return 0 if report['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
