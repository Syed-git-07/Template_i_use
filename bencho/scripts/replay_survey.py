"""Sample each free block's own public guided replay.

Screenshots stay in a caller-provided local folder, not in this reference repo.
This samples demonstrations; it does not test every user gesture/state.
"""
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]

async def main():
    output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
    blocks=[x for x in json.loads((ROOT/'catalogue/browser-blocks.json').read_text(encoding='utf-8'))['items'] if x.get('preview')=='live-component-rendered']
    queue=asyncio.Queue()
    for x in blocks:queue.put_nowait(x)
    results=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        async def worker():
            page=await browser.new_page(viewport={'width':1440,'height':1000})
            while not queue.empty():
                block=await queue.get()
                row={'slug':block['slug'],'url':block['url'],'frames':[],'method':'Bencho Show me how replay, sampled at approximately 0, 1.5 and 4 seconds. Not exhaustive.'}
                try:
                    await page.goto(block['url'],wait_until='domcontentloaded')
                    stage=page.locator('.dtl-stage');await stage.wait_for();await page.wait_for_timeout(600)
                    await page.locator('.dtl-shell').get_by_role('button',name='Show me how',exact=True).click()
                    previous=0
                    for i,ms in enumerate([0,1500,4000]):
                        await page.wait_for_timeout(ms-previous);previous=ms
                        file=output/f'{block["slug"]}-{i}.jpg'
                        await stage.screenshot(path=str(file),type='jpeg',quality=70)
                        row['frames'].append({'approx_ms':ms,'local_file':file.name,'text':(await page.locator('.dtl-scale').inner_text())[:800]})
                    row['status']='replay-sampled'
                except Exception as exc:row['status']='error';row['error']=str(exc)[:300]
                results.append(row);queue.task_done()
                if len(results)%10==0:print(f'Replay sampled {len(results)}/{len(blocks)}',flush=True)
            await page.close()
        await asyncio.gather(worker(),worker())
        await browser.close()
    results.sort(key=lambda x:x['slug'])
    (ROOT/'catalogue/free-replays.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':results},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Replay errors',sum(x['status']=='error' for x in results),flush=True)

if __name__=='__main__':asyncio.run(main())
