"""Retain 60fps public snippets locally and publish factual parameter/source references."""
import hashlib,json,re
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1];site=ROOT/'60fps';local=ROOT/'.local/upstream/60fps-snippets';local.mkdir(parents=True,exist_ok=True)
rows=[]
for row in json.loads((site/'catalogue/index.json').read_text(encoding='utf8'))['items']:
    if not row['path'].startswith('/snippets/'):continue
    cache=ROOT/'.local/html/60fps'/(hashlib.sha256(row['url'].encode()).hexdigest()+'.html')
    soup=BeautifulSoup(cache.read_text(encoding='utf8'),'html.parser');blocks=list(dict.fromkeys(p.get_text() for p in soup.select('pre')));slug=row['path'].split('/')[-1]
    record={'name':row['name'],'url':row['url'],'blocks':[]}
    for n,text in enumerate(blocks):
        ext='swift' if 'import SwiftUI' in text else 'txt';name=f'{slug}-{n}.{ext}';(local/name).write_text(text,encoding='utf8',newline='')
        lines=text.splitlines();facts={'local_file':name,'sha256':hashlib.sha256(text.encode()).hexdigest(),'lines':len(lines),'language':ext,'parameters':[],'events':[],'signals':{}}
        for i,line in enumerate(lines):
            for key,value in re.findall(r'\b(duration|delay|response|dampingFraction|blendDuration|bounce|stiffness|damping|mass|minimumDistance|minimumDuration)\s*:\s*(-?[0-9]+(?:\.[0-9]+)?)',line):facts['parameters'].append({'name':key,'value':float(value),'line':i+1})
            for event in re.findall(r'\b(onTapGesture|onLongPressGesture|onChanged|onEnded|onChange|onAppear|onDisappear|DragGesture|MagnifyGesture|RotationGesture)\b',line):facts['events'].append({'name':event,'line':i+1})
        for key,pattern in {'reduced_motion':'accessibilityReduceMotion','async':'Task|async|await','haptic':'UIImpactFeedbackGenerator|sensoryFeedback','shared_geometry':'matchedGeometryEffect','spring':'spring|interpolatingSpring'}.items():facts['signals'][key]=bool(re.search(pattern,text))
        record['blocks'].append(facts)
    rows.append(record)
(site/'catalogue/snippet-source.json').write_text(json.dumps({'note':'Code remains in ignored local cache; no blanket redistribution license established. Parameters are literal source facts, not runtime measurements. Duplicate responsive code blocks deduplicated per page.','items':rows},indent=2),encoding='utf8')
dest=site/'snippets';dest.mkdir(exist_ok=True)
for r in rows:
    lines=[f'# {r["name"]}','',f'[Original snippet]({r["url"]})','','The code is retained in the ignored local source cache. Read the original terms before use or redistribution. SwiftUI behavior is not automatically equivalent to a React implementation.','']
    for b in r['blocks']:
        lines += [f'## {b["local_file"]}','',f'{b["language"]}; {b["lines"]} lines; SHA-256 `{b["sha256"]}`.','']
        lines += [f'- `{x["name"]}` = {x["value"]}, line {x["line"]}.' for x in b['parameters']]
        lines += ['','Input/lifecycle locations: '+', '.join(f'{x["name"]}:{x["line"]}' for x in b['events'])+'.','', 'Signals: '+', '.join(k for k,v in b['signals'].items() if v)+'.','']
    (dest/(r['url'].split('/')[-1]+'.md')).write_text('\n'.join(lines),encoding='utf8')
print(len(rows),'snippet pages;',sum(len(r['blocks']) for r in rows),'deduplicated local code blocks')
