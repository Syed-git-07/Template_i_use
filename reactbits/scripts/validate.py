"""Validate coverage, cross-links and local source hashes; generate an evidence ledger."""
import hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def read(name):return json.loads((root/'catalogue'/name).read_text(encoding='utf8'))
index=read('index.json')['items'];sources=read('source-index.json');items=sources['items']
browser={x['slug']:x for x in read('browser.json')['items']}
gestures={x['slug']:x for x in read('gesture-checks.json')['items']}
tools={x['slug']:x for x in read('tools-browser.json')['items']}
public=[x for x in index if x['kind']=='component']
assert len(index)==237 and len(public)==217 and len(items)==219
assert len({x['url'] for x in index})==237
assert {x['url'] for x in public}=={x['url'] for x in items if x['publicly_listed']}
assert len(browser)==217 and all(x['status']=='panel-observed' and not x['page_errors'] for x in browser.values())
assert all(len(x['variants'])==4 for x in items)
audit=read('source-audit.json');assert audit['comparedDefaults']==4243 and not audit['errors']
assert len(gestures)==7 and all(x['status']=='passed' for x in gestures.values())
assert len(tools)==5 and all(x['status']=='page-observed' for x in tools.values())
local=root.parent/'.local/react-bits'/sources['commit']
hashes=read('local-source-sha256.json')
assert len(hashes)==2788
for name,digest in hashes.items():assert hashlib.sha256((local/name).read_bytes()).hexdigest()==digest,name
by_url={r['url']:r for r in items if r['url']}
ledger=[]
for row in index:
    source=by_url.get(row['url']);observation=browser.get(row['slug']) if row['kind']=='component' else tools.get(row['slug']);gesture=gestures.get(row['slug'])
    ledger.append({'name':row['name'],'url':row['url'],'kind':row['kind'],
       'source_guide':f'components/{source["name"]}.md' if source else None,
       'source_variants':len(source['variants']) if source else 0,
       'browser_status':observation['status'] if observation else 'HTTP heading indexed only',
       'browser_errors':observation.get('page_errors',[]) if observation else [],
       'gesture_assertions':gesture['assertions'] if gesture else [],
       'remaining':'Project-specific interaction, accessibility, touch, interruption, reduced-motion and integration verification; computed formulas require original source.' if source else 'Full tool/preset/export or supporting-page workflow not verified.'})
for row in items:
    if not row['publicly_listed']:ledger.append({'name':row['name'],'kind':'unlisted-source','url':None,'source_guide':f'components/{row["name"]}.md','source_variants':4,'remaining':'Not in current public component catalogue; no public preview assertion.'})
(root/'catalogue/review-ledger.json').write_text(json.dumps({'scope':'Dated inventory and evidence levels, not exhaustive interaction certification.','items':ledger},indent=2),encoding='utf8')
bad=[]
for file in list(root.rglob('*.md'))+[root.parent/'README.md',root.parent/'REUSE-PROMPT.md']:
    for link in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf8')):
        if not link.startswith(('http:','https:','#')) and not (file.parent/link.split('#')[0]).exists():bad.append((str(file),link))
assert not bad,bad
print(json.dumps({'public_components':len(public),'source_components':len(items),'variants':sum(len(x['variants']) for x in items),'verified_local_hashes':len(hashes),'browser_panels':len(browser),'gesture_scenarios':len(gestures),'gesture_assertions':sum(len(x['assertions']) for x in gestures.values()),'tools':len(tools),'tool_page_error_records':sum(bool(x['page_errors']) for x in tools.values()),'ledger_rows':len(ledger),'broken_local_links':len(bad)},indent=2))
