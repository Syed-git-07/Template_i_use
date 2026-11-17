"""Integrity and publication checks for the shared research update."""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sites=['viewport','60fps','shadcn','interior','motion-primitives','aceternity','cult'];report=[]
for site in sites:
    root=ROOT/site;cat=root/'catalogue';index=json.loads((cat/'index.json').read_text(encoding='utf8'));urls={r['url'] for r in index['items']}
    assert len(urls)==len(index['items']),(site,'duplicate pages')
    assert all(r['status']=='indexed' for r in index['items']),(site,'metadata failure')
    sourcefile=cat/'source-index.json';hashes=0
    if sourcefile.exists():
        source=json.loads(sourcefile.read_text(encoding='utf8'));local=ROOT/source['local_snapshot']
        for r in source['items']:
            assert hashlib.sha256((local/r['file']).read_bytes()).hexdigest()==r['sha256'],(site,r['file'])
            hashes+=1
        if source.get('commit'):assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=local,text=True).strip()==source['commit']
    for file in cat.glob('*.json'):json.loads(file.read_text(encoding='utf8'))
    for name in ['browser.json','media-browser.json','gesture-checks.json']:
        file=cat/name
        if file.exists():
            rows=json.loads(file.read_text(encoding='utf8'))['items'];assert len({r['url'] for r in rows})==len(rows),(site,name,'duplicate evidence')
            assert all(r['url'] in urls for r in rows),(site,name,'unknown page')
            if name=='media-browser.json':
                expected={r['url'] for r in index['items'] if ('/posts/' in r['path'] if site=='viewport' else '/shots/' in r['path'] or '/motion/' in r['path'])}
                assert {r['url'] for r in rows}==expected,(site,'incomplete media inventory')
                for row in rows:
                    for f in row.get('frames',[]):
                        assert abs(f['time']-f['actual_time'])<.2,(site,row['url'],'frame time')
                        assert (ROOT/'.local'/f'{site}-observations'/f['file']).exists(),(site,row['url'],'missing capture')
    snippetfile=cat/'snippet-source.json'
    if snippetfile.exists():
        for r in json.loads(snippetfile.read_text(encoding='utf8'))['items']:
            for block in r['blocks']:
                assert hashlib.sha256((ROOT/'.local/upstream/60fps-snippets'/block['local_file']).read_bytes()).hexdigest()==block['sha256']
    report.append({'site':site,'indexed_pages':len(urls),'verified_source_hashes':hashes})
broken=[]
for site in sites:
    for file in (ROOT/site).rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf8')):
            if target.startswith(('http:','https:','#','mailto:')):continue
            if not (file.parent/target.split('#')[0]).exists():broken.append((str(file.relative_to(ROOT)),target))
assert not broken,broken[:20]
staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
assert not any(p.startswith('.local/') for p in staged),'Local cache staged'
assert not any(re.search(r'\.(mp4|webm|png|jpe?g|wav|mp3|woff2?)$',p,re.I) for p in staged),'Unexpected published media'
assert not any(re.search(r'\.(tsx|jsx|css)$',p) and any(p.startswith(s+'/') for s in sites) for p in staged),'Unexpected implementation publication'
print(json.dumps({'sites':report,'broken_links':broken,'staged_files':len(staged),'result':'passed'},indent=2))
(ROOT/'research-validation.json').write_text(json.dumps({'sites':report,'broken_local_links':0,'result':'passed','scope':'Hashes, catalogue/evidence consistency, local links and staged publication boundaries. Not exhaustive behavior certification.'},indent=2),encoding='utf8')
