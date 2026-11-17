"""Selected reversible gestures in public documentation demos, with explicit assertions."""
import json,sys,re
from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright,expect
ROOT=Path(__file__).resolve().parents[1]
cases=[('interior','hold-to-confirm','https://www.interior.dev/docs/hold-to-confirm'),('interior','tag-input','https://www.interior.dev/docs/tag-input'),('interior','modal','https://www.interior.dev/docs/modal'),('shadcn','dialog','https://ui.shadcn.com/docs/components/base/dialog'),('shadcn','dropdown-menu','https://ui.shadcn.com/docs/components/base/dropdown-menu'),('shadcn','alert-dialog','https://ui.shadcn.com/docs/components/base/alert-dialog'),('motion-primitives','accordion','https://motion-primitives.com/docs/accordion')]
cases += [('cult','popover-form','https://www.cult-ui.com/docs/components/popover-form'),('aceternity','3d-card-effect','https://ui.aceternity.com/components/3d-card-effect')]
with sync_playwright() as p:
    browser=p.chromium.launch();page=browser.new_page(viewport={'width':1440,'height':1000});page.set_default_timeout(15000)
    for site,slug,url in cases:
        if len(sys.argv)>1 and slug not in sys.argv[1:]:continue
        row={'slug':slug,'url':url,'assertions':[]}
        try:
            page.goto(url,wait_until='domcontentloaded',timeout=45000);page.locator('h1').first.wait_for();page.wait_for_timeout(2200)
            if site=='interior':
                demo=page.locator('body')
                if slug=='hold-to-confirm':
                    button=demo.get_by_role('button',name=re.compile('Hold to delete workspace')).first;status=button.get_by_role('status')
                    button.click(delay=150);page.wait_for_timeout(700);assert status.inner_text()==''
                    row['assertions'].append('Short press does not confirm')
                    button.focus();page.keyboard.down('Space');page.wait_for_timeout(400);page.keyboard.press('Escape');page.keyboard.up('Space');page.wait_for_timeout(500)
                    assert status.inner_text()=='';row['assertions'].append('Escape cancels incomplete keyboard hold')
                    box=button.bounding_box();page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);page.mouse.down();page.wait_for_timeout(2000)
                    assert 'deleted' in status.inner_text().lower();page.mouse.up();row['assertions'].append('Full hold announces demo completion')
                    page.wait_for_timeout(1800);assert status.inner_text()=='';row['assertions'].append('Completion resets')
                elif slug=='tag-input':
                    field=page.get_by_placeholder('Add a topic',exact=True);field.fill('reference-check');page.keyboard.press('Enter')
                    remove=demo.get_by_role('button',name='Remove reference-check',exact=True);assert remove.count()==1
                    row['assertions'].append('Enter adds the typed tag')
                    field.focus();page.keyboard.press('Backspace');assert remove.count()==1
                    page.keyboard.press('Backspace');page.wait_for_timeout(400);assert remove.count()==0
                    row['assertions'].append('First empty Backspace selects; second removes the tag')
                else:
                    trigger=demo.get_by_role('button',name='Delete project',exact=True);trigger.click()
                    dialog=page.get_by_role('dialog');dialog.wait_for();assert dialog.is_visible()
                    page.keyboard.press('Escape');page.wait_for_timeout(500);assert not dialog.is_visible()
                    assert trigger.evaluate('(e)=>document.activeElement===e')
                    row['assertions'].append('Modal opens, Escape closes, focus returns to trigger; deletion not invoked')
            elif site=='shadcn':
                slot={'dialog':'dialog-trigger','dropdown-menu':'dropdown-menu-trigger','alert-dialog':'alert-dialog-trigger'}[slug]
                trigger=page.get_by_role('button',name='Open Dialog',exact=True).first if slug=='dialog' else page.get_by_role('button',name='Show Dialog',exact=True).first if slug=='alert-dialog' else page.locator(f'main [data-slot="{slot}"]').first
                trigger.click();role='menu' if slug=='dropdown-menu' else 'alertdialog' if slug=='alert-dialog' else 'dialog'
                overlay=page.get_by_role(role).last;overlay.wait_for();assert overlay.is_visible()
                if slug=='alert-dialog':overlay.get_by_role('button',name='Cancel',exact=True).click()
                else:page.keyboard.press('Escape')
                page.wait_for_timeout(500);assert not overlay.is_visible()
                assert trigger.evaluate('(e)=>document.activeElement===e')
                row['assertions'].append('Demo overlay opens and cancels/closes with focus restored')
            elif site=='cult':
                trigger=page.get_by_role('button',name='Feedback',exact=True).first;trigger.click()
                field=page.locator('textarea:visible').first;field.fill('Reference interaction check')
                assert field.input_value()=='Reference interaction check'
                page.get_by_role('button',name='Close',exact=True).first.click();page.wait_for_timeout(700)
                assert not field.is_visible()
                row['assertions'].append('Feedback form expands, accepts text and closes; no submission sent')
            elif site=='aceternity':
                outer=page.locator('div[style*="perspective"]').first;card=outer.locator(':scope > div').first;card.scroll_into_view_if_needed()
                box=card.bounding_box();page.mouse.move(box['x']+15,box['y']+15,steps=12);page.wait_for_timeout(500)
                transform=card.evaluate('(e)=>e.style.transform')
                assert 'rotate' in transform and transform!='rotateY(0deg) rotateX(0deg)'
                page.mouse.move(10,10,steps=12);page.wait_for_timeout(500)
                assert card.evaluate('(e)=>e.style.transform')=='rotateY(0deg) rotateX(0deg)'
                row['assertions'].append('Pointer position tilts the card; leaving restores zero rotation')
                row['observed_tilt']=transform
            else:
                trigger=page.get_by_role('button',name='Getting Started',exact=True).first
                before=trigger.get_attribute('aria-expanded');trigger.click();page.wait_for_timeout(350)
                expect(trigger).not_to_have_attribute('aria-expanded',before)
                trigger.focus();page.keyboard.press('Enter');page.wait_for_timeout(350)
                expect(trigger).to_have_attribute('aria-expanded',before)
                row['assertions'].append('Accordion click changes expansion; Enter reverses it')
            row['status']='passed'
        except Exception as e:
            row.update(status='needs-review',error=repr(e)[:1300]);dest=ROOT/'.local/interaction-errors';dest.mkdir(parents=True,exist_ok=True)
            try:page.screenshot(path=str(dest/f'{site}-{slug}.png'),timeout=5000)
            except Exception:pass
        path=ROOT/site/'catalogue/gesture-checks.json';old=json.loads(path.read_text(encoding='utf8'))['items'] if path.exists() else []
        old=[x for x in old if x['slug']!=slug]+[row]
        path.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Selected desktop public-demo actions; no real data deletion, submission or production guarantee.','items':old},indent=2),encoding='utf8')
        print(site,slug,row['status'],row.get('error','')[:180],flush=True)
    browser.close()
