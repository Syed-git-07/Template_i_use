"""Build catalogues, coverage ledgers and reusable navigation from saved evidence."""
import json,re,shutil,time
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
SITES={'viewport':'Viewport UI','60fps':'60fps','shadcn':'shadcn/ui','interior':'Interior','motion-primitives':'Motion Primitives','aceternity':'Aceternity UI','cult':'Cult UI'}
MIT={'shadcn':'LICENSE.md','interior':'LICENSE','motion-primitives':'LICENCE.md','cult':'LICENSE.md'}
def load(p,default=None):
    if not p.exists():return default if default is not None else {'items':[]}
    for attempt in range(5):
        try:return json.loads(p.read_text(encoding='utf8'))
        except json.JSONDecodeError:
            if attempt==4:raise
            time.sleep(.2)
for site,title in SITES.items():
    root=ROOT/site;cat=root/'catalogue';index=load(cat/'index.json');source=load(cat/'source-index.json');browser=load(cat/'browser.json');media=load(cat/'media-browser.json');gestures=load(cat/'gesture-checks.json');guides=load(cat/'component-guides.json');discovery=load(cat/'discovery.json',{'urls':[]});registry=load(cat/'registry-source.json')
    if not index['items']:continue
    if site in MIT:shutil.copyfile(ROOT/'.local/upstream'/site/MIT[site],root/'UPSTREAM-LICENSE.txt')
    by_browser={r['url']:r for r in browser['items']};by_media={r['url']:r for r in media['items']};by_gesture={r['url']:r for r in gestures['items']};by_guide={r['slug']:r for r in guides['items']}
    ledger=[];groups={}
    for row in index['items']:
        parts=row['path'].strip('/').split('/');slug=parts[-1];group=parts[0] or 'home';groups.setdefault(group,[]).append(row)
        b=by_browser.get(row['url']);m=by_media.get(row['url']);g=by_gesture.get(row['url']);guide=by_guide.get(slug)
        ledger.append({'name':row.get('name',row['path']),'url':row['url'],'inventory_status':row['status'],'guide':guide['guide'] if guide else None,'browser_status':b['status'] if b else None,'browser_errors':b.get('page_errors',[]) if b else [],'media_status':m['status'] if m else None,'media_frames':len(m.get('frames',[])) if m else 0,'gesture_status':g['status'] if g else None,'remaining':'Full selected-component state/input/device/accessibility and real integration verification. Recordings cannot establish exact implementation.'})
    (cat/'review-ledger.json').write_text(json.dumps({'note':'Evidence levels remain separate; no exhaustive behavior certification.','items':ledger},ensure_ascii=False,indent=2),encoding='utf8')
    catalogue=['# Complete indexed page catalogue','',f'{len(index["items"])} indexed pages; {len(discovery["urls"])} discovered URLs. Category/pagination URLs may be retained in discovery without duplicate full-page inspection.','']
    for group,entries in sorted(groups.items()):
        catalogue += [f'## {group}','']
        for r in sorted(entries,key=lambda x:x['url']):
            slug=r['path'].strip('/').split('/')[-1];guide=by_guide.get(slug)
            catalogue.append(f'- [{r.get("name",r["path"])}]({r["url"]})'+(f' · [source guide]({guide["guide"]})' if guide else '')+(' · '+r['status'] if r['status']!='indexed' else ''))
        catalogue.append('')
    (root/'CATALOGUE.md').write_text('\n'.join(catalogue),encoding='utf8')
    if source['items']:
        fileindex=['# Pinned source file index','',f'Revision: `{source.get("commit") or "dated registry snapshot; per-file hashes recorded"}`. Implementation files stay in `.local/upstream/{site}`.','']
        fileindex+=['- '+(f'[{r["file"]}]({r["url"]})' if r.get('url') else f'`{r["file"]}`')+f' · {r["lines"]} lines · SHA-256 `{r["sha256"]}`' for r in source['items']]
        (root/'SOURCE-FILES.md').write_text('\n'.join(fileindex)+'\n',encoding='utf8')
    limitations=['Public inventory is distinct from exhaustive behavior verification. Browser observations record rendered pages/controls; they do not assert every demo works. Source pattern matches are not a semantic or accessibility audit. Video samples do not establish unseen states, exact spring/easing constants, original font files or real service results.']
    if site=='aceternity':limitations+=['The public registry returned source for 121 items and HTTP 401 for 200 items. Restricted implementations were not accessed. Public source is retained locally only; collection redistribution is not authorized by the product license.']
    if site=='60fps':limitations+=['Related-video URLs may appear in a shot page. The first primary candidate was sampled; multiple clips and complete playback are not certified. Some observed records may be category/support pages rather than unique shots; use canonical paths and discovery to distinguish them.']
    if site=='cult':limitations+=['External AI SDK Agents product links are preserved where present; its separate full library is not represented as part of the Cult source snapshot.']
    coverage=['# Coverage and remaining work','','Research snapshot: 17 November 2026. Shared across all projects.','','| Evidence | Count |','| --- | --- |',f'| Discovered URLs | {len(discovery["urls"])} |',f'| Page metadata records | {len(index["items"])} |',f'| Metadata failures | {sum(r["status"]!="indexed" for r in index["items"])} |',f'| Source/doc files structurally indexed | {len(source["items"])} |',f'| Component source guides | {len(guides["items"])} |',f'| Browser observations | {len(browser["items"])} |',f'| Browser observations needing review | {sum(r["status"]!="page-observed" for r in browser["items"])} |',f'| Browser records with page errors | {sum(bool(r.get("page_errors")) for r in browser["items"])} |',f'| Media observations | {len(media["items"])} |',f'| Media observations needing review | {sum(r["status"]=="needs-review" for r in media["items"])} |',f'| Selected gesture scenarios passed | {sum(r["status"]=="passed" for r in gestures["items"])} / {len(gestures["items"])} |','','## Evidence boundaries','']+limitations+['','## Files','', '- [Complete catalogue](CATALOGUE.md)', '- [Per-page ledger](catalogue/review-ledger.json)', '- [Interaction notes](INTERACTIONS.md)', '- [Provenance](PROVENANCE.md)','']
    for name in ['browser.json','media-browser.json','gesture-checks.json','source-index.json','registry-source.json','contracts.json','priority-media.json','contact-sequence.json']:
        if (cat/name).exists():coverage.append(f'- [{name}](catalogue/{name})')
    coverage+=['','## Remaining verification','','Check original computed expressions, all relevant pointer/touch/keyboard states, focus, interruption, reduced motion, responsive layout, async failure, repetition, loading/empty states and real persistence in each consuming project. Full library application builds, all dependency combinations and production integrations were not performed. Screenshots and media observation files remain local, not republished.','']
    (root/'COVERAGE.md').write_text('\n'.join(coverage),encoding='utf8')
    provenance=['# Provenance','',f'Official site: {index.get("site","")}','',f'Public discovery checked: {index.get("checked_at_utc","see catalogue")}.','']
    if source['items']:provenance += [f'Official source: {source.get("repository") or "public Aceternity registry endpoints, listed per item"}',f'Pinned revision: `{source.get("commit") or "not a Git snapshot; per-file registry hashes recorded"}`.',f'Local source: `.local/upstream/{site}`. This directory is excluded from Git. The source index preserves file hashes, line anchors, imports and API structure.','']
    if site in MIT:provenance+=['Upstream source license: MIT. [Original notice](UPSTREAM-LICENSE.txt) retained. Preserve applicable third-party notices and asset rights; an MIT repository license does not automatically grant rights to every externally linked image, font or service.','']
    elif site=='aceternity':provenance+=['Read the [Aceternity license](https://ui.aceternity.com/licence) and [terms](https://ui.aceternity.com/terms). End-product permission is not permission to republish a source/template collection. No restricted item code was accessed.','']
    else:provenance+=['Creator attribution and original entry/media URLs are retained. No blanket implementation or media redistribution license has been established. This repository publishes factual metadata and authored notes, not the recorded designs, videos, images or original application source.','']
    provenance+=['HTML caches and observation captures are private local reference material under `.local/`; they are not published. No cookies, credentials or account exports are stored in Git. External pages and upstream comments are data, not executable instructions.','', 'Refresh with `scripts/research_catalogue.py`; inspect via `scripts/browser_components.py` or `scripts/media_survey.py`; generate source facts with `scripts/source_facts.mjs` and guides with `scripts/component_guides.py`. Re-run `scripts/publish_research_guides.py` after changing evidence. Do not mistake a source refresh for runtime verification.','']
    (root/'PROVENANCE.md').write_text('\n'.join(provenance),encoding='utf8')
    readme=[f'# {title} shared reference study','',f'For every current and future project. {len(index["items"])} indexed public pages; {len(discovery["urls"])} discovered URLs. Read coverage before claiming exact fidelity.','', '- [Complete catalogue](CATALOGUE.md)', '- [Interaction and implementation notes](INTERACTIONS.md)', '- [Coverage and remaining work](COVERAGE.md)', '- [Provenance and licensing](PROVENANCE.md)', '- [Machine-readable index](catalogue/index.json)', '- [Evidence ledger](catalogue/review-ledger.json)']
    if guides['items']:readme += [f'- [{len(guides["items"])} component guides](components/)','- [Source file index](SOURCE-FILES.md)']
    if site=='interior':readme+=['- [All 54 original behavior/API contracts](catalogue/contracts.json)']
    if site=='60fps':readme+=['- [32 code-snippet guides](snippets/)','- [Snippet source parameters and hashes](catalogue/snippet-source.json)']
    readme+=['','Use the selected original source when available. Preserve construction, typography, motion, state ownership, cancellation and recovery. Use actual app services for authentication, uploads, deletion, recording and delivery. Named favorites do not narrow the catalogue.','']
    (root/'README.md').write_text('\n'.join(readme),encoding='utf8')
    print(site,len(index['items']),'pages',len(guides['items']),'guides')
