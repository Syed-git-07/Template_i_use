"""Observe documentation demos and controls without triggering external actions."""
import asyncio,json,sys
from pathlib import Path
from datetime import datetime,timezone
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def main(site):
    folder=ROOT/site/'catalogue';index=json.loads((folder/'index.json').read_text(encoding='utf8'))['items']
    if site=='shadcn':items=[r for r in index if '/docs/components/' in r['path']]
    elif site in ['interior','motion-primitives']:items=[r for r in index if r['path'].startswith('/docs/')]
    elif site=='cult':items=[r for r in index if '/docs/components/' in r['path']]
    else:items=[r for r in index if any(r['path'].startswith('/'+k+'/') for k in ['components','blocks','interactions','pages','templates'])]
    dest=folder/'browser.json';prior=json.loads(dest.read_text(encoding='utf8'))['items'] if dest.exists() else []
    if '--issues' in sys.argv:
        issues=[r for r in prior if r['status']!='page-observed' or r.get('page_errors')]
        (folder/'browser-initial-issues.json').write_text(json.dumps({'items':issues,'note':'Previous observations retained before a targeted retry; not a claim of a component defect.'},indent=2),encoding='utf8')
    rows=[r for r in prior if r['status']=='page-observed' and not ('--issues' in sys.argv and r.get('page_errors'))];done={r['url'] for r in rows};q=asyncio.Queue()
    for r in items:
        if r['url'] not in done:q.put_nowait(r)
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        async def worker():
            context=await browser.new_context(viewport={'width':1440,'height':1000});page=await context.new_page()
            while not q.empty():
                entry=await q.get();row={k:entry[k] for k in ['url','path','name']};errors=[]
                listener=lambda e:errors.append(str(e)[:200]);page.on('pageerror',listener)
                try:
                    response=await page.goto(row['url'],wait_until='domcontentloaded',timeout=35000)
                    row['http_status']=response.status if response else None
                    if response and response.status>=400:raise RuntimeError('HTTP '+str(response.status))
                    await page.wait_for_timeout(900)
                    await page.locator('h1').first.wait_for(timeout=15000)
                    row.update(await page.evaluate('''()=>{const main=document.querySelector('main')||document.body;const h=document.querySelector('h1');return {heading:h?.textContent,typography:{heading: h?{font:getComputedStyle(h).fontFamily,size:getComputedStyle(h).fontSize,weight:getComputedStyle(h).fontWeight,spacing:getComputedStyle(h).letterSpacing}:null,body:getComputedStyle(main).fontFamily},controls:[...main.querySelectorAll('button,input,textarea,select,[role=tab],[role=slider]')].map(e=>({tag:e.tagName,role:e.getAttribute('role'),type:e.type,label:e.getAttribute('aria-label')||e.innerText?.slice(0,60),disabled:e.disabled,expanded:e.getAttribute('aria-expanded')})),iframes:[...main.querySelectorAll('iframe')].map(e=>e.src),canvasCount:main.querySelectorAll('canvas').length,previewCount:main.querySelectorAll('[data-slot=preview],[data-slot=component-preview],[data-preview],.preview').length,restrictionLabels:[...main.querySelectorAll('button,a')].map(e=>e.innerText).filter(s=>/unlock|get all.access|sign in|buy now|purchase/i.test(s))}}'''))
                    row['status']='page-observed'
                except Exception as e:row.update(status='needs-review',error=repr(e)[:500])
                row['page_errors']=errors[:5];row['limit']='Rendered desktop documentation and control inventory. Host typography is not necessarily component typography. No blanket clicking, account action or complete state certification.'
                page.remove_listener('pageerror',listener);rows.append(row);q.task_done()
                dest.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':sorted(rows,key=lambda r:r['url'])},ensure_ascii=False,indent=2),encoding='utf8')
                if len(rows)%25==0:print(site,'browser',len(rows),'/',len(items),flush=True)
            await context.close()
        await asyncio.gather(worker(),worker());await browser.close()
    print(site,'browser DONE',len(rows),'errors',sum(r['status']!='page-observed' for r in rows),flush=True)
if __name__=='__main__':
    for site in sys.argv[1:]:
        if not site.startswith('--'):asyncio.run(main(site))
