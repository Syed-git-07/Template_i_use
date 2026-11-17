"""Sample public Finds in the browser; retain attribution, not media copies.

Local screenshots are observation aids only and are not published to the repo.
A sampled frame is not a full playback or exact-motion review.
"""
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
PRIORITY={'altinsmaili-button-anatomy','abtste11a-trip-cards','imharshin-genie-menu','koppkev-liquid-menus','raminnasibov-download-progress','raul-tool-folders','adi-tool-grid'}

async def main():
    output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
    items=[x for x in json.loads((ROOT/'catalogue/index.json').read_text(encoding='utf8'))['items'] if x['kind']=='find']
    previous=[]
    if '--retry' in sys.argv and (ROOT/'catalogue/finds-browser.json').exists():
        previous=json.loads((ROOT/'catalogue/finds-browser.json').read_text(encoding='utf8'))['items']
        done={x['slug'] for x in previous if x['status']!='error'}
        items=[x for x in items if x['slug'] not in done]
    queue=asyncio.Queue()
    for item in items:queue.put_nowait(item)
    results=[x for x in previous if x['status']!='error']
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        async def worker():
            page=await browser.new_page(viewport={'width':1200,'height':800})
            page.set_default_timeout(10000)
            while not queue.empty():
                item=await queue.get();row={'slug':item['slug'],'name':item['name'],'url':item['url'],'frames':[]}
                try:
                    await page.goto(item['url'],wait_until='domcontentloaded',timeout=30000)
                    video=page.locator('.fnd-dtl-vid')
                    try:await video.wait_for(timeout=2500)
                    except Exception:
                        # Some published deep links do not hydrate their detail panel.
                        # Open the same public entry through its gallery link instead.
                        await page.goto('https://bencho.dev/finds',wait_until='domcontentloaded')
                        frame=page.locator(f'.fnd-tile[data-id="{item["slug"]}"] .fnd-frame')
                        await frame.scroll_into_view_if_needed()
                        video=frame.locator('video,img').first
                        await video.wait_for()
                        row['navigation']='public gallery media; direct detail did not open'
                    # Let the detail opening transition finish before capture.
                    # Media readyState alone does not mean the panel is opaque.
                    await page.wait_for_timeout(1000)
                    if await video.evaluate('(e)=>e.tagName')=='IMG':
                        await page.wait_for_function('(e)=>e.complete&&e.naturalWidth>0',arg=await video.element_handle())
                        file=output/f'{item["slug"]}-0.jpg'
                        await video.screenshot(path=str(file),type='jpeg',quality=65)
                        row['frames']=[{'local_file':file.name}]
                        row['status']='static-image-sampled'
                        row['limit']='Original entry is a static image; no motion can be verified.'
                        results.append(row);queue.task_done();continue
                    await page.wait_for_function('(v)=>v.readyState>=2 && Number.isFinite(v.duration)',arg=await video.element_handle(),timeout=15000)
                    row['duration_seconds']=await video.evaluate('(v)=>{v.pause();return v.duration}')
                    row['original_link']=item.get('external_credits',[])
                    times=[0.05,0.35,0.65,0.95] if item['slug'] in PRIORITY else [0.5]
                    for i,fraction in enumerate(times):
                        second=row['duration_seconds']*fraction
                        await video.evaluate('(v,t)=>{v.currentTime=t}',second)
                        await page.wait_for_function('(v)=>!v.seeking',arg=await video.element_handle())
                        await page.wait_for_timeout(100)
                        file=output/f'{item["slug"]}-{i}.jpg'
                        await video.screenshot(path=str(file),type='jpeg',quality=65)
                        row['frames'].append({'seconds':round(second,3),'local_file':file.name})
                    row['status']='video-frames-sampled'
                    row['limit']='Selected frames only. Trigger, reverse path, touch, easing and all intermediate states are not verified by frame sampling.'
                except Exception as exc:row['status']='error';row['error']=str(exc)[:350]
                results.append(row);queue.task_done()
                if len(results)%20==0:print(f'Finds records {len(results)}',flush=True)
            await page.close()
        await asyncio.gather(worker(),worker())
        await browser.close()
    results.sort(key=lambda x:x['name'].lower())
    (ROOT/'catalogue/finds-browser.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':results},ensure_ascii=False,indent=2),encoding='utf8')
    print('Finds errors',sum(x['status']=='error' for x in results),flush=True)

if __name__=='__main__':asyncio.run(main())
