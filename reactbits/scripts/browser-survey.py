"""Public UI observations. No code export, account session, or recording permission."""
import asyncio,json,sys
from pathlib import Path
from datetime import datetime,timezone
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def main():
    output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
    entries=[x for x in json.loads((ROOT/'catalogue/index.json').read_text(encoding='utf8'))['items'] if x['kind']=='component']
    prior=[]
    if '--retry' in sys.argv and (ROOT/'catalogue/browser.json').exists():
        prior=json.loads((ROOT/'catalogue/browser.json').read_text(encoding='utf8'))['items'];done={r['slug'] for r in prior if r['status']=='panel-observed'};entries=[r for r in entries if r['slug'] not in done]
    results=[r for r in prior if r['status']=='panel-observed'];queue=asyncio.Queue()
    for row in entries:queue.put_nowait(row)
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        async def worker():
            context=await browser.new_context(viewport={'width':1440,'height':1050})
            page=await context.new_page();page.set_default_timeout(12000)
            while not queue.empty():
                entry=await queue.get();row={k:entry[k] for k in ['name','category','slug','url']};errors=[]
                handler=lambda e:errors.append(str(e)[:180]);page.on('pageerror',handler)
                try:
                    await page.goto(entry['url'],wait_until='domcontentloaded',timeout=30000)
                    close=page.get_by_role('button',name='Close announcement',exact=True)
                    try:await close.wait_for(timeout=1300);await close.click()
                    except Exception:pass
                    panel=page.locator('.preview-panel');await panel.wait_for(timeout=22000)
                    await page.wait_for_timeout(600)
                    row.update(await panel.evaluate('''el=>({
                      knobs:[...el.querySelectorAll('input,[role=slider],[role=switch],[role=combobox]')].map(e=>({tag:e.tagName,type:e.type,role:e.getAttribute('role'),label:e.getAttribute('aria-label')||e.name||e.id,value:e.value,min:e.min||e.getAttribute('aria-valuemin'),max:e.max||e.getAttribute('aria-valuemax'),current:e.getAttribute('aria-valuenow'),checked:e.getAttribute('aria-checked'),disabled:e.disabled})),
                      api:[...el.querySelectorAll('tbody tr')].map(r=>[...r.querySelectorAll('td')].slice(0,3).map(c=>c.innerText)),
                      previewControls:[...el.querySelectorAll('.demo-container button,.demo-container input,.demo-container [role=button],.demo-container [role=slider]')].map(e=>({tag:e.tagName,role:e.getAttribute('role'),label:e.getAttribute('aria-label')||e.textContent?.slice(0,60),type:e.type,disabled:e.disabled})),
                      canvasCount:el.querySelectorAll('.demo-container canvas').length,
                      svgCount:el.querySelectorAll('.demo-container svg').length,
                      previewCount:el.querySelectorAll('.demo-container').length
                    })'''))
                    demo=panel.locator('.demo-container').first
                    if await demo.count():
                        await demo.scroll_into_view_if_needed();await page.wait_for_timeout(350)
                        box=await demo.bounding_box();row['desktop_size']=box
                        if box and box['height']<1800:
                            await demo.screenshot(path=str(output/f'{entry["slug"]}.jpg'),type='jpeg',quality=65,timeout=10000)
                            row['local_screenshot']=f'{entry["slug"]}.jpg'
                        if box:
                            await page.mouse.move(box['x']+box['width']*.3,box['y']+min(box['height']*.5,400),steps=8)
                            await page.mouse.move(box['x']+box['width']*.7,box['y']+min(box['height']*.5,400),steps=8)
                            row['pointer_sweep']='attempted inside preview; outcome not semantically asserted'
                    row['status']='panel-observed'
                except Exception as e:row['status']='needs-review';row['error']=str(e)[:350]
                row['page_errors']=errors[:4];row['limit']='Desktop panel/controls and a screenshot/pointer sample only. Not exhaustive state, touch, keyboard, WebGL or real-service verification.'
                page.remove_listener('pageerror',handler);results.append(row);queue.task_done()
                if len(results)%20==0:print(f'React Bits browser records {len(results)}',flush=True)
                # Checkpoint so a long survey can be resumed without losing evidence.
                (ROOT/'catalogue/browser.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':sorted(results,key=lambda r:(r['category'],r['name']))},ensure_ascii=False,indent=2),encoding='utf8')
            await context.close()
        await asyncio.gather(worker(),worker())
        await browser.close()
    print('Review-needed',sum(r['status']!='panel-observed' for r in results),'page-error records',sum(bool(r['page_errors']) for r in results),flush=True)
if __name__=='__main__':asyncio.run(main())
