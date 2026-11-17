"""Observe recordings in their public pages; captures remain local and excluded from Git."""
import asyncio,json,sys
from pathlib import Path
from datetime import datetime,timezone
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def main(site,priority=False):
    catalogue=ROOT/site/'catalogue';items=json.loads((catalogue/'index.json').read_text(encoding='utf8'))['items']
    items=[r for r in items if r.get('status')=='indexed' and ('/posts/' in r['path'] if site=='viewport' else '/shots/' in r['path'] or '/motion/' in r['path'])]
    if priority:items=[r for r in items if any(x in r.get('name','').lower() for x in ['skeuomorphic contact','compressing images','shredder'])]
    output=ROOT/'.local'/f'{site}-observations';output.mkdir(parents=True,exist_ok=True)
    dest=catalogue/('priority-media.json' if priority else 'media-browser.json')
    prior=json.loads(dest.read_text(encoding='utf8'))['items'] if dest.exists() else []
    rows=[r for r in prior if r['status'] in ['video-sampled','image-observed'] and r.get('capture_version')==2];done={r['url'] for r in rows}
    queue=asyncio.Queue()
    for r in items:
        if r['url'] not in done:queue.put_nowait(r)
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        async def worker():
            context=await browser.new_context(viewport={'width':1440,'height':1000});page=await context.new_page()
            while not queue.empty():
                entry=await queue.get();row={k:entry[k] for k in ['url','path','name']};row['frames']=[]
                try:
                    media=next((m['url'] for m in entry.get('media',[]) if m['kind'] in ['video','source'] and '.mp4' in m['url']),None)
                    await page.goto(media or row['url'],wait_until='domcontentloaded',timeout=35000)
                    row['observation_surface']='Original public media in browser video player' if media else 'Original reference page'
                    await page.wait_for_timeout(500)
                    video=page.locator('video:visible').first
                    if await video.count():
                        await video.scroll_into_view_if_needed()
                        await video.evaluate('(v)=>{v.muted=true;v.preload="auto";v.autoplay=false;v.pause();}')
                        await page.wait_for_function('()=>[...document.querySelectorAll("video")].some(v=>v.offsetWidth>0&&Number.isFinite(v.duration)&&v.duration>0)',timeout=25000)
                        row.update(await video.evaluate('(v)=>({duration:v.duration,width:v.videoWidth,height:v.videoHeight,source:v.currentSrc})'))
                        # Some hosts expose a zero-length seekable range despite buffering the clip.
                        # An ephemeral browser Blob of the same public media supports frame seeking.
                        # No media file is saved or published.
                        if await video.evaluate('(v)=>!v.seekable.length||v.seekable.end(v.seekable.length-1)<v.duration*.99'):
                            await video.evaluate('''async v=>{const u=v.currentSrc.split('#')[0];v.pause();const r=await fetch(u,{signal:AbortSignal.timeout(45000)});if(!r.ok)throw Error(r.status);const blob=await r.blob();v.src=URL.createObjectURL(blob);await new Promise((ok,no)=>{v.onloadedmetadata=ok;v.onerror=no;v.load()});}''')
                        await page.wait_for_timeout(250)
                        fractions=[0,.15,.3,.45,.6,.75,.9,.98] if priority else [.5]
                        await video.evaluate('(v)=>v.pause()')
                        for n,fraction in enumerate(fractions):
                            when=max(.01,min(row['duration']-.05,row['duration']*fraction))
                            await video.evaluate('(v,t)=>{v.pause();v.currentTime=t}',when)
                            await page.wait_for_timeout(400)
                            try:
                                await page.wait_for_function('()=>[...document.querySelectorAll("video")].some(v=>v.offsetWidth>0&&!v.seeking&&v.readyState>=2)',timeout=10000)
                            except Exception:
                                # Some clips decode sequentially but stall on a mid-clip seek.
                                await video.evaluate('(v)=>{v.currentTime=0;v.loop=false;v.play()}')
                                await page.wait_for_function('(t)=>{const v=document.querySelector("video");return v&&v.currentTime>=t}',arg=when,timeout=min(60000,int(when*1000+12000)))
                                await video.evaluate('(v)=>v.pause()')
                                row['seek_fallback']='Sequential playback used after mid-clip seek stalled'
                            slug=row['path'].rstrip('/').split('/')[-1];filename=f'{slug}-{n}.jpg'
                            await video.screenshot(path=str(output/filename),type='jpeg',quality=75,timeout=12000)
                            actual=await video.evaluate('(v)=>v.currentTime')
                            assert abs(actual-when)<.2,(actual,when)
                            row['frames'].append({'time':when,'actual_time':actual,'file':filename})
                        row['status']='video-sampled'
                    else:
                        img=page.locator('main img:visible,article img:visible').first
                        if not await img.count():img=page.locator('img:visible').first
                        await img.wait_for(timeout=12000)
                        row['image']=await img.get_attribute('src');row['status']='image-observed'
                    row['capture_version']=2
                    row['font_limit']='Fonts visible inside a recording are not identified by DOM styles.'
                except Exception as e:row.update(status='needs-review',error=repr(e)[:500])
                row['limit']='Recording samples only. No original application gesture, exact easing/physics, font-file identity or backend behavior certified.'
                rows.append(row);queue.task_done()
                temporary=dest.with_suffix('.json.tmp')
                temporary.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':sorted(rows,key=lambda r:r['url'])},ensure_ascii=False,indent=2),encoding='utf8')
                temporary.replace(dest)
                if priority or len(rows)%25==0:print(site,'media',len(rows),row['status'],flush=True)
            await context.close()
        workers=4 if site=='60fps' else 2
        await asyncio.gather(*(worker() for _ in range(workers)));await browser.close()
    print(site,'media DONE',len(rows),'needs-review',sum(r['status']=='needs-review' for r in rows),flush=True)
if __name__=='__main__':asyncio.run(main(sys.argv[1],'--priority' in sys.argv))
