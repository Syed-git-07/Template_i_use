"""Retry the short badges recording using ordinary playback, without seeking."""
import json
from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];file=root/'viewport/catalogue/media-browser.json';data=json.loads(file.read_text(encoding='utf8'));row=next(r for r in data['items'] if '/256-' in r['url']);url='https://viewportui.com/_astro/x.com_1799093609012289903.post.DDAPXXSD.mp4'
with sync_playwright() as p:
    browser=p.chromium.launch();page=browser.new_page(viewport={'width':1440,'height':1000})
    page.goto(url,wait_until='domcontentloaded');video=page.locator('video')
    result=video.evaluate('''async v=>{v.muted=true;v.loop=false;v.controls=false;v.pause();v.load();await new Promise((ok,no)=>{v.onloadeddata=ok;v.onerror=no});const t=v.duration/2;await v.play();await new Promise((ok,no)=>{const end=setTimeout(()=>no(Error('playback timeout')),10000);function check(){if(v.currentTime>=t){v.pause();clearTimeout(end);ok()}else requestAnimationFrame(check)}check()});return {duration:v.duration,time:t,actual_time:v.currentTime,width:v.videoWidth,height:v.videoHeight}}''')
    name='256-shiny-badges-explorations-playback.jpg';video.screenshot(path=str(root/'.local/viewport-observations'/name),type='jpeg',quality=75)
    assert abs(result['time']-result['actual_time'])<.2
    row.update(status='video-sampled',capture_version=2,duration=result['duration'],width=result['width'],height=result['height'],source=url,seek_fallback='Fresh sequential playback, no seeking',frames=[{'time':result['time'],'actual_time':result['actual_time'],'file':name}])
    row.pop('error',None);browser.close()
data['checked_at_utc']=datetime.now(timezone.utc).isoformat();file.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8');print(row['name'],row['status'],row['frames'])
