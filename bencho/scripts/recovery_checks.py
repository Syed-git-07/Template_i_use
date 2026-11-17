"""Additional real pointer and rejected-input demo checks."""
import json
from pathlib import Path
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];results=[]
with sync_playwright() as p:
    browser=p.chromium.launch();page=browser.new_page(viewport={'width':1440,'height':1000});page.set_default_timeout(7000)
    for slug in ['one-time-code','slide-confirm']:
        row={'slug':slug,'assertions':[]}
        try:
            page.goto('https://bencho.dev/blocks/'+slug);stage=page.locator('.dtl-scale');stage.wait_for();page.wait_for_timeout(900)
            if slug=='one-time-code':
                field=stage.locator('input');field.fill('1x2');assert field.input_value()=='12'
                row['assertions'].append('Non-digit input is removed')
                page.get_by_text('Reject',exact=True).click();field.fill('1234');page.wait_for_timeout(500)
                assert stage.locator('.otp').get_attribute('data-phase')=='no'
                page.wait_for_timeout(1300);assert field.input_value()==''
                assert stage.locator('.otp').get_attribute('data-phase')=='type'
                row['assertions'].append('Rejected code enters rejection then clears and restores typing')
                page.emulate_media(reduced_motion='reduce');page.get_by_text('Accept',exact=True).click()
                field.fill('1234');page.wait_for_timeout(500);assert stage.locator('.otp').get_attribute('data-phase')=='ok'
                row['assertions'].append('Accept completes with reduced-motion preference')
                page.emulate_media(reduced_motion='no-preference')
            else:
                control=stage.locator('.sld-grip');box=control.bounding_box();x=box['x']+box['width']/2;y=box['y']+box['height']/2
                page.mouse.move(x,y);page.mouse.down();page.mouse.move(x+25,y,steps=12);page.wait_for_timeout(250);page.mouse.up();page.wait_for_timeout(800)
                assert control.get_attribute('aria-label')=='Slide to confirm'
                after=control.bounding_box();assert abs(after['x']-box['x'])<3
                row['assertions'].append('Short slow drag returns handle to origin without confirming')
                track=stage.locator('.sld-track').bounding_box()
                page.mouse.move(x,y);page.mouse.down();page.mouse.move(track['x']+track['width']+40,y,steps=24);page.mouse.up();page.wait_for_timeout(650)
                assert control.get_attribute('aria-label')=='Confirmed'
                row['assertions'].append('Full pointer drag reaches confirmed demo state')
            row['status']='passed'
        except Exception as e:row.update(status='needs-review',error=repr(e)[:1200])
        results.append(row);print(slug,row['status'],row.get('error',''),flush=True)
    browser.close()
(root/'catalogue/recovery-checks.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Public desktop demos; synthetic code and no real transactions.','items':results},indent=2),encoding='utf8')
