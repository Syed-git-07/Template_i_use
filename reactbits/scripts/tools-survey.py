"""Observe public creative tools without importing media or requesting devices."""
import json
from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];rows=[]
with sync_playwright() as p:
    browser=p.chromium.launch();page=browser.new_page(viewport={'width':1440,'height':1050})
    for slug in ['background-studio','center-stage','shape-magic','texture-lab','sound-lab']:
        row={'slug':slug,'url':'https://reactbits.dev/tools/'+slug};errors=[]
        listener=lambda e:errors.append(str(e)[:200]);page.on('pageerror',listener)
        try:
            page.goto(row['url'],wait_until='domcontentloaded',timeout=45000)
            try:page.get_by_role('button',name='Close announcement',exact=True).click(timeout=5000)
            except Exception:pass
            page.wait_for_timeout(2200)
            row.update(page.evaluate('''()=>({headings:[...document.querySelectorAll('h1,h2')].map(e=>e.textContent.trim()).filter(Boolean),controls:[...document.querySelectorAll('button,input,select,[role=slider]')].map(e=>({tag:e.tagName,role:e.getAttribute('role'),label:e.getAttribute('aria-label')||e.textContent?.trim().slice(0,60),type:e.type,min:e.min||e.getAttribute('aria-valuemin'),max:e.max||e.getAttribute('aria-valuemax')})),canvasCount:document.querySelectorAll('canvas').length})'''))
            row['status']='page-observed'
        except Exception as e:row.update(status='needs-review',error=repr(e)[:400])
        row['page_errors']=errors;row['limit']='Initial public controls only; no exports, uploads, camera, microphone, listening or exhaustive preset traversal.'
        page.remove_listener('pageerror',listener);rows.append(row);print(slug,row['status'],flush=True)
    browser.close()
(root/'catalogue/tools-browser.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':rows},indent=2),encoding='utf8')
