"""Selected anonymous public demo gestures; never invokes a real application service."""
import json, sys
from pathlib import Path
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page(viewport={'width':1440,'height':1050})
    page.set_default_timeout(7000)
    cases=['code-slots','hold-button','folder','elastic-slider','flip-card','swipe-row','card-nav']
    for slug in (sys.argv[1:] or cases):
        category='components' if slug in ['folder','elastic-slider','card-nav'] else 'micro'
        row={'slug':slug,'url':f'https://reactbits.dev/{category}/{slug}','assertions':[]}
        try:
            page.goto(row['url'],wait_until='domcontentloaded')
            close=page.get_by_role('button',name='Close announcement',exact=True)
            try: close.wait_for(timeout=6000);close.click();page.locator('.announcement-modal-backdrop').wait_for(state='hidden',timeout=5000)
            except Exception:pass
            demo=page.locator('.demo-container').first
            demo.wait_for(timeout=25000);demo.scroll_into_view_if_needed();page.wait_for_timeout(700)
            if slug=='code-slots':
                field=demo.get_by_role('textbox',name='One-time code');field.focus()
                page.keyboard.type('12a3');page.wait_for_timeout(200)
                assert demo.locator('[data-filled]').count()==3
                row['assertions'].append('Non-numeric typed character ignored; 3 numeric slots filled')
                page.keyboard.press('Backspace');assert demo.locator('[data-filled]').count()==2
                row['assertions'].append('Backspace removes one digit')
                page.keyboard.type('3456');page.wait_for_timeout(650)
                assert demo.locator('.code-slots__row').get_attribute('data-status')=='success'
                assert field.get_attribute('readonly') is not None
                row['assertions'].append('Six digits produce demo success and lock input')
                page.wait_for_timeout(1900)
                page.get_by_role('button',name='Outcome',exact=True).click()
                page.get_by_text('Reject',exact=True).click()
                field.focus();page.keyboard.type('123456');page.wait_for_timeout(500)
                assert demo.locator('.code-slots__row').get_attribute('data-status')=='error'
                page.wait_for_timeout(1300)
                assert demo.locator('[data-filled]').count()==0
                row['assertions'].append('Reject outcome enters error and drains all digits')
            elif slug=='hold-button':
                control=demo.locator('.hold-button').first
                control.click(delay=150);page.wait_for_timeout(300)
                assert control.get_attribute('data-phase')=='idle'
                row['assertions'].append('Short press returns idle without completing')
                control.focus();page.keyboard.down('Space');page.wait_for_timeout(350)
                page.keyboard.press('Escape');page.keyboard.up('Space')
                assert control.get_attribute('data-phase')=='idle'
                row['assertions'].append('Escape cancels a keyboard hold')
                box=control.bounding_box();page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2)
                page.mouse.down();page.wait_for_timeout(2200)
                assert control.get_attribute('data-phase')=='done';page.mouse.up()
                row['assertions'].append('Full pointer hold reaches done')
                page.wait_for_timeout(1400);assert control.get_attribute('data-phase')=='idle'
                row['assertions'].append('Completion resets to idle')
            elif slug=='folder':
                control=demo.locator('.folder-stage').first
                control.focus();page.keyboard.press('Enter');page.wait_for_timeout(700)
                assert control.get_attribute('aria-expanded')=='true'
                row['assertions'].append('Enter opens folder')
                item=demo.locator('[data-folder-item]').last
                before=item.get_attribute('style');box=item.bounding_box()
                page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);page.mouse.down()
                page.mouse.move(box['x']+box['width']/2+90,box['y']+box['height']/2-70,steps=15)
                page.wait_for_timeout(150);after=item.get_attribute('style');page.mouse.up()
                assert before!=after
                row['assertions'].append('Real pointer drag changes paper transform; persistence not asserted')
                page.keyboard.press('Escape');page.wait_for_timeout(500)
                assert control.get_attribute('aria-expanded')=='false'
                row['assertions'].append('Escape closes folder')
            elif slug=='elastic-slider':
                control=demo.get_by_role('slider').first;control.focus()
                page.keyboard.press('End');assert float(control.get_attribute('aria-valuenow'))==float(control.get_attribute('aria-valuemax'))
                page.keyboard.press('ArrowRight');assert float(control.get_attribute('aria-valuenow'))==float(control.get_attribute('aria-valuemax'))
                page.keyboard.press('Home');assert float(control.get_attribute('aria-valuenow'))==float(control.get_attribute('aria-valuemin'))
                row['assertions'].append('Keyboard End/Home reach bounds; extra Right remains clamped at maximum')
            elif slug=='flip-card':
                control=demo.locator('.flip-card').first;before=control.get_attribute('aria-pressed')
                control.click();page.wait_for_timeout(650);assert control.get_attribute('aria-pressed')!=before
                control.focus();page.keyboard.press('Enter');page.wait_for_timeout(650)
                assert control.get_attribute('aria-pressed')==before
                row['assertions'].append('Click flips and Enter reverses face')
            elif slug=='swipe-row':
                control=demo.locator('.swipe-row').first;toggle=control.locator('.swipe-row__toggle')
                toggle.focus();page.keyboard.press('ArrowLeft');page.wait_for_timeout(500)
                assert toggle.get_attribute('aria-expanded')=='true'
                page.keyboard.press('Escape');page.wait_for_timeout(500)
                assert toggle.get_attribute('aria-expanded')=='false'
                row['assertions'].append('Keyboard ArrowLeft reveals actions; Escape closes')
                box=control.bounding_box();x=box['x']+box['width']*.85;y=box['y']+box['height']/2
                page.mouse.move(x,y);page.mouse.down();page.mouse.move(box['x']+10,y,steps=24);page.mouse.up();page.wait_for_timeout(300)
                row['after_full_swipe']=control.get_attribute('data-phase') if control.count() else 'removed'
                assert row['after_full_swipe'] in ['folding','gone','removed','collapsing','collapsed']
                row['assertions'].append('Full swipe commits and removes/collapses demo row; no real deletion')
            elif slug=='card-nav':
                control=demo.locator('button[aria-expanded]').first
                control.click();page.wait_for_timeout(700);assert control.get_attribute('aria-expanded')=='true'
                page.keyboard.press('Escape');page.wait_for_timeout(500);assert control.get_attribute('aria-expanded')=='false'
                row['assertions'].append('Menu click opens and Escape closes cards')
            row['status']='passed'
        except Exception as e:
            row['status']='needs-review';row['error']=str(e)[:2200]
            target=ROOT.parent/'.local'/'reactbits-observations';target.mkdir(parents=True,exist_ok=True)
            page.screenshot(path=str(target/f'error-{slug}.png'))
        results.append(row);print(slug,row['status'],row.get('error',''),flush=True)
        destination=ROOT/'catalogue/gesture-checks.json'
        previous=json.loads(destination.read_text(encoding='utf8'))['items'] if destination.exists() else []
        combined=[r for r in previous if r['slug'] not in {x['slug'] for x in results}]+results
        destination.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Selected desktop public-demo states. No real authentication, deletion, file storage or payments.','items':combined},indent=2),encoding='utf8')
    browser.close()
