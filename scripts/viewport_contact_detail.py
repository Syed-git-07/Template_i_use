"""Dense observation of the requested contact-form recording, not a form submission."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];out=root/'.local/viewport-observations';out.mkdir(parents=True,exist_ok=True)
entry=next(x for x in json.loads((root/'viewport/catalogue/index.json').read_text(encoding='utf8'))['items'] if '/598-' in x['url'])
url=entry['media'][0]['url'].split('#')[0];rows=[]
with sync_playwright() as p:
    b=p.chromium.launch();page=b.new_page(viewport={'width':1440,'height':1000});page.goto(url,wait_until='domcontentloaded')
    video=page.locator('video');video.wait_for()
    video.evaluate('''async v=>{v.pause();v.muted=true;v.autoplay=false;const r=await fetch(v.currentSrc);const blob=await r.blob();v.src=URL.createObjectURL(blob);await new Promise((ok,no)=>{v.onloadedmetadata=ok;v.onerror=no;v.load()});v.controls=false}''')
    for t in [11,11.5,12,12.25,12.5,12.75,13,13.25,13.5,14,14.5]:
        video.evaluate('(v,t)=>{v.pause();v.currentTime=t}',t);page.wait_for_timeout(400)
        actual=video.evaluate('(v)=>v.currentTime');assert abs(actual-t)<.15
        file=f'contact-send-{t}.jpg';video.screenshot(path=str(out/file),type='jpeg',quality=80)
        rows.append({'requested_time':t,'actual_time':actual,'local_file':file})
    b.close()
(root/'viewport/catalogue/contact-sequence.json').write_text(json.dumps({'url':entry['url'],'media':url,'frames':rows,'limit':'Public recording timeline; no exact physics/source or live email delivery tested.'},indent=2),encoding='utf8')
print('Contact sequence',len(rows),'frames verified')
