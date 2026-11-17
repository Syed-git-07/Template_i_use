"""Readable per-component guides from pinned source facts; no implementation bodies."""
import json,re,sys
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
def esc(s):return str(s).replace('|','\\|').replace('\r','').replace('\n',' ')
for site in sys.argv[1:]:
    root=ROOT/site;data=json.loads((root/'catalogue/source-index.json').read_text(encoding='utf8'));groups=defaultdict(list)
    contracts={r['slug']:r for r in json.loads((root/'catalogue/contracts.json').read_text(encoding='utf8'))['items']} if site=='interior' else {}
    for r in data['items']:
        f=r['file']
        selected=(site=='shadcn' and re.search(r'registry/(bases/(base|radix|aria)|new-york-v4)/ui/[^/]+\.tsx$',f)) or (site=='cult' and '/registry/default/ui/' in f and f.endswith('.tsx')) or (site=='interior' and f.startswith('components/interior/') and f.endswith('.tsx')) or (site=='motion-primitives' and f.startswith('components/core/') and f.endswith('.tsx')) or (site=='aceternity' and f.endswith(('.tsx','.jsx','.ts','.js')))
        if selected:groups[Path(f).stem].append(r)
    dest=root/'components';dest.mkdir(exist_ok=True)
    catalogue=[]
    for slug,variants in sorted(groups.items()):
        lines=[f'# {slug}','','Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.','',f'Pinned revision: `{data["commit"] or "dated public registry; file hashes recorded"}`.','']
        for row in variants:
            link=row['url'] or 'https://ui.aceternity.com/registry/'+row['file'].split('/')[1]+'.json'
            lines += [f'## {row["file"]}','',f'[Original source]({link}); SHA-256 `{row["sha256"]}`; {row["lines"]} lines.','', 'Imports: '+', '.join(f'`{x}`' for x in row['imports']), '','### API structure','','| Name | Type | Optional | Source line |','| --- | --- | --- | --- |']
            for prop in row['props']:lines.append(f'| {esc(prop["name"])} | {esc(prop.get("type","inferred"))} | {prop["optional"]} | {prop["line"]} |')
            if not row['props']:lines+=['','Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.']
            lines+=['','### Defaults and motion','']
            for prop in row['defaults']:lines.append(f'- Default `{prop["name"]}` = `{json.dumps(prop["value"],ensure_ascii=False)}` (line {prop["line"]}).')
            for m in row['motion']:lines.append(f'- `{m["parameter"]}`: {"computed; inspect expression" if m.get("computed") else json.dumps(m.get("value"))} (line {m["line"]}).')
            lines+=['','### Input, style and lifecycle','', 'Events: '+('; '.join(f'{e["name"]} (line {e["line"]})' for e in row['events']) or 'none directly declared in this file')+'.', '', 'Typography/style anchors: '+(', '.join(str(x['line']) for x in row['styles']) or 'none matched; utility classes or shared theme may own these')+'.','', 'Source signals: '+(', '.join(k for k,v in row['signals'].items() if v) or 'none matched')+'.','']
        if slug in contracts:
            contract=contracts[slug]
            lines+=['## Original author behavior contract','','The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.','']
            lines += ['- '+n for n in contract.get('notes',[])]
            lines += ['','| Prop | Type | Documented default | Original note |','| --- | --- | --- | --- |']
            for p in contract.get('props',[]):lines.append(f'| {esc(p["name"])} | {esc(p["type"])} | {esc(p.get("default","not specified"))} | {esc(p.get("note",""))} |')
            lines.append('')
        lines+=['## Reuse and verification','','Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.','']
        (dest/(slug+'.md')).write_text('\n'.join(line.rstrip() for line in lines),encoding='utf8')
        catalogue.append({'slug':slug,'guide':'components/'+slug+'.md','variants':[r['file'] for r in variants]})
    (root/'catalogue/component-guides.json').write_text(json.dumps({'items':catalogue},indent=2),encoding='utf8')
    print(site,len(catalogue),'component guides')
