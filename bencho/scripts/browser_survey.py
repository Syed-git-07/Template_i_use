"""Observe public block panels without login or extracting restricted code.

Requires playwright with Chromium installed. Run after catalogue.py.
These are browser observations, not exhaustive interaction verification.
"""
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]

async def main():
    items = json.loads((ROOT / 'catalogue/index.json').read_text(encoding='utf-8'))['items']
    blocks = [x for x in items if x['kind'] == 'block']
    queue = asyncio.Queue()
    for block in blocks:
        queue.put_nowait(block)
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        async def worker():
            page = await browser.new_page(viewport={'width': 1440, 'height': 1000})
            while not queue.empty():
                block = await queue.get()
                row = {'slug': block['slug'], 'name': block['name'], 'url': block['url']}
                try:
                    await page.goto(block['url'], wait_until='domcontentloaded', timeout=30000)
                    dialog = page.locator('.dtl-shell')
                    await dialog.wait_for(timeout=15000)
                    await page.wait_for_timeout(450)
                    row.update(await dialog.evaluate('''el => ({
                      title: el.querySelector('.dtl-title')?.textContent,
                      preview: el.querySelector('.pro-still') ? 'restricted-static-preview' : 'live-component-rendered',
                      controls: [...el.querySelectorAll('.dtl-ctl')].map(e=>({
                        label:e.querySelector('.dtl-ctl-label')?.textContent,
                        options:[...e.querySelectorAll('button')].map(b=>({label:b.textContent,selected:b.getAttribute('aria-pressed')})),
                        inputs:[...e.querySelectorAll('input')].map(i=>({type:i.type,value:i.value,min:i.min,max:i.max,step:i.step})),
                        sliders:[...e.querySelectorAll('[role=slider]')].map(i=>({value:i.getAttribute('aria-valuenow'),min:i.getAttribute('aria-valuemin'),max:i.getAttribute('aria-valuemax')}))
                      })),
                      componentControls:[...el.querySelectorAll('.dtl-scale button,.dtl-scale input,.dtl-scale [role=slider]')].map(e=>({tag:e.tagName,role:e.getAttribute('role'),label:e.getAttribute('aria-label')||e.textContent,type:e.getAttribute('type')})),
                      canvasCount:el.querySelectorAll('.dtl-scale canvas').length,
                      evidence:'Panel opened at desktop viewport; controls enumerated. No claim of all states tested.'
                    })'''))
                    row['upstream_source'] = (ROOT / 'upstream-free/blocks' / block['slug']).is_dir()
                except Exception as exc:
                    row['error'] = str(exc)[:300]
                results.append(row)
                queue.task_done()
                if len(results) % 20 == 0:
                    print(f'Browser checked {len(results)}/{len(blocks)} blocks', flush=True)
            await page.close()
        await asyncio.gather(worker(), worker(), worker())
        await browser.close()
    results.sort(key=lambda x:x['name'].lower())
    (ROOT / 'catalogue/browser-blocks.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'viewport':[1440,1000],'items':results},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:sum(r.get('preview')==k for r in results) for k in ['restricted-static-preview','live-component-rendered']}),flush=True)
    print('Errors',sum('error' in r for r in results),flush=True)

if __name__ == '__main__':
    asyncio.run(main())
