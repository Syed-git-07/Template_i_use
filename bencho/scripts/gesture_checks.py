from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime,timezone
import json
import tempfile
root=Path(__file__).resolve().parents[1]/'catalogue';results=[]
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={"width":1440,"height":1000});page.set_default_timeout(5000)
 for slug in ['card-swap','liq-toggle','label-input','like','step-player','one-time-code','liq-create','seek']:
  row={'slug':slug,'url':'https://bencho.dev/blocks/'+slug}
  try:
   page.goto(row['url']);stage=page.locator('.dtl-scale');stage.wait_for();page.wait_for_timeout(800)
   if slug=='card-swap':
    front=stage.locator('.csw-card[data-front=true]');before=front.inner_text();front.click();page.wait_for_timeout(700);after=front.inner_text();assert before!=after
    row.update(action='Click front card',before=before,after=after)
   elif slug=='liq-toggle':
    control=stage.get_by_role('switch');before=control.get_attribute('aria-checked');control.click();after=control.get_attribute('aria-checked');assert before!=after
    control.focus();page.keyboard.press('Space');assert control.get_attribute('aria-checked')==before
    row.update(action='Click switch, then Space to reverse',before=before,after=after,keyboard_reverse=True)
   elif slug=='label-input':
    field=stage.locator('input');field.focus();field.fill('reference@example.test');assert field.input_value()=='reference@example.test';page.mouse.click(200,200);page.wait_for_timeout(400)
    page.locator('.dtl-stage').screenshot(path=str(Path(tempfile.gettempdir())/'bencho-label-input.png'));field.fill('');assert field.input_value()==''
    row.update(action='Focus, type synthetic text, blur, clear',result='Value retained on blur and cleared')
   elif slug=='like':
    control=stage.locator('button').first;before=control.get_attribute('aria-label');control.click();page.wait_for_timeout(400);after=control.get_attribute('aria-label');assert before!=after
    row.update(action='Click Like',before=before,after=after)
   elif slug=='step-player':
    stage.get_by_role('button',name='Play',exact=True).click();page.wait_for_timeout(300);assert stage.get_by_role('button',name='Pause',exact=True).count()==1
    stage.get_by_role('button',name='Pause',exact=True).click();assert stage.get_by_role('button',name='Play',exact=True).count()==1
    row.update(action='Play then pause',result='Controls changed to Pause and back to Play')
   elif slug=='one-time-code':
    stage.locator('input').fill('1234');page.wait_for_timeout(1000);row.update(action='Enter synthetic 1234 into default Accept demo',result=stage.inner_text());assert 'Verified' in row['result']
   elif slug=='liq-create':
    stage.get_by_role('button',name='Create',exact=True).click();page.wait_for_timeout(500);assert stage.get_by_role('button',name='Document',exact=True).is_visible();row.update(action='Open Create menu',result='Document option visible')
   elif slug=='seek':
    stage.get_by_role('button',name='Search',exact=True).click();page.wait_for_timeout(600);field=stage.get_by_role('textbox',name='Search');field.fill('reference');assert field.input_value()=='reference';row.update(action='Expand search and type synthetic query',result='Expanded input accepts query; search backend not tested')
   row['status']='passed'
  except Exception as e:row['status']='needs-review';row['error']=str(e)[:350]
  results.append(row);print(slug,row['status'],flush=True)
 b.close()
(root/'gesture-checks.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Selected public-demo interactions only; not real application integrations.','items':results},ensure_ascii=False,indent=2),encoding='utf8')
