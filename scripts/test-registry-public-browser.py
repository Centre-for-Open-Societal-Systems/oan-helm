"""Check legacy navigation reaches canonical registry URLs and the shared staff login.

Uses a fresh anonymous browser context. No credentials, form submission or data
changes. Requires Playwright and Chromium; raw browser state is never exported.
"""
import argparse
import datetime
import json
from pathlib import Path
from urllib.parse import parse_qs,urlsplit

from playwright.sync_api import sync_playwright


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--browser-executable')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    reports=[]
    with sync_playwright() as p:
        settings={'headless':True}
        if args.browser_executable:settings['executable_path']=args.browser_executable
        browser=p.chromium.launch(**settings)
        for registry in ['crop','livestock']:
            context=browser.new_context()
            page=context.new_page()
            errors=[];navigations=[]
            def response_seen(response):
                if response.status>=400:
                    parsed=urlsplit(response.url)
                    errors.append({'host':parsed.netloc,'path':parsed.path,'status':response.status})
            def request_seen(request):
                if request.is_navigation_request():
                    parsed=urlsplit(request.url)
                    navigations.append({'host':parsed.netloc,'path':parsed.path})
            page.on('response',response_seen);page.on('request',request_seen)
            canonical=registry+'-registry.development.oanstaging.com'
            try:
                page.goto('https://'+registry+'-registry-development.oanstaging.com/',wait_until='networkidle',timeout=45000)
                page.locator('#username').wait_for(timeout=15000)
                parsed=urlsplit(page.url);query=parse_qs(parsed.query)
                expected={'host':canonical,'path':'/api/me','status':401}
                # Anonymous /api/me returning 401 initiates the normal login.
                # Keycloak returns to shared IAM, which restores the registry URL.
                passed=(any(n['host']==canonical for n in navigations)
                    and parsed.netloc=='keycloak.development.oanstaging.com'
                    and parsed.path=='/realms/staff/protocol/openid-connect/auth'
                    and page.locator('#password').is_visible()
                    and query.get('client_id')==['staff-portal']
                    and query.get('redirect_uri')==['https://staff-iam.development.oanstaging.com/auth/callback']
                    and all(error==expected for error in errors))
                reports.append({'registry':registry,'passed':passed,'navigations':navigations,
                    'loginHost':parsed.netloc,'loginClient':query.get('client_id'),
                    'loginRedirect':query.get('redirect_uri'),'httpErrors':errors})
            except Exception:
                reports.append({'registry':registry,'passed':False,'reason':'Browser routing or login form check failed'})
            finally:context.close()
        browser.close()
    report={'checkedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'live':True,
        'passed':all(r['passed'] for r in reports),'registries':reports,
        'authenticatedSessionTested':False,'credentialsRequired':False}
    (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    raise SystemExit(0 if report['passed'] else 1)


if __name__=='__main__':main()
