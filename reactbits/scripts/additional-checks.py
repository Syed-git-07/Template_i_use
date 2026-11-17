"""Additional mobile-emulation and reduced-motion checks in public demos."""
import json
from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright,expect
root=Path(__file__).resolve().parents[1];rows=[]
with sync_playwright() as p:
    browser=p.chromium.launch();context=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,reduced_motion='reduce')
    page=context.new_page();page.set_default_timeout(15000)
    for slug,category in [('option-wheel','components'),('voice-pill','micro'),('stepper','components'),('hold-button','micro')]:
        row={'slug':slug,'url':f'https://reactbits.dev/{category}/{slug}','environment':'390x844 mobile/touch emulation with reduced motion; not physical-device certification','assertions':[]}
        try:
            page.goto(row['url'],wait_until='domcontentloaded',timeout=45000)
            try:page.get_by_role('button',name='Close announcement',exact=True).click(timeout=6000)
            except Exception:pass
            demo=page.locator('.demo-container').first;demo.wait_for();demo.scroll_into_view_if_needed();page.wait_for_timeout(1000)
            if slug=='option-wheel':
                wheel=demo.get_by_role('listbox',name='Option wheel');wheel.focus();before=wheel.locator('[aria-selected=true]').inner_text()
                page.keyboard.press('ArrowDown');page.wait_for_timeout(500);assert wheel.locator('[aria-selected=true]').inner_text()!=before
                page.keyboard.press('ArrowUp');page.wait_for_timeout(500);assert wheel.locator('[aria-selected=true]').inner_text()==before
                row['assertions'].append('Arrow keys advance and reverse selection under reduced motion')
            elif slug=='voice-pill':
                control=demo.locator('.voice-pill');control.tap();expect(control).to_have_attribute('data-state','listening')
                control.focus();page.keyboard.press('Escape');expect(control).to_have_attribute('data-state','idle')
                row['assertions'].append('Touch tap starts simulated listening; Escape restores idle without microphone access')
                box=control.bounding_box();x=box['x']+box['width']/2;y=box['y']+box['height']/2
                cdp=context.new_cdp_session(page);cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]});page.wait_for_timeout(400)
                for d in [10,30,50,75,90]:cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x-d,'y':y}]})
                cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});expect(control).to_have_attribute('data-state','idle')
                row['assertions'].append('Touch drag left beyond cancel distance returns idle')
            elif slug=='stepper':
                pane=demo.locator('.stepper__pane:not(.stepper__pane--leaving)');before=pane.inner_text()
                demo.get_by_role('button',name='Continue',exact=True).tap();page.wait_for_timeout(500);assert pane.inner_text()!=before
                demo.get_by_role('button',name='Back',exact=True).tap();page.wait_for_timeout(500);assert pane.inner_text()==before
                row['assertions'].append('Touch Continue and Back change and restore displayed step')
            else:
                control=demo.locator('.hold-button').first;control.tap();page.wait_for_timeout(300);expect(control).to_have_attribute('data-phase','idle')
                box=control.bounding_box();cdp=context.new_cdp_session(page)
                cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':box['x']+box['width']/2,'y':box['y']+box['height']/2}]})
                page.wait_for_timeout(2200);expect(control).to_have_attribute('data-phase','done');cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
                row['assertions'].append('Brief touch does not complete; sustained touch reaches done under reduced motion')
            row['status']='passed'
        except Exception as e:row.update(status='needs-review',error=repr(e)[:1000])
        rows.append(row);print(slug,row['status'],row.get('error','')[:160],flush=True)
        (root/'catalogue/additional-checks.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'items':rows},indent=2),encoding='utf8')
    browser.close()
