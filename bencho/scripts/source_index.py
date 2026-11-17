"""Index the unchanged MIT snapshot with line references and integrity hashes."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'upstream-free'
MOTION = re.compile(r'\b(stiffness|damping|mass|duration|delay|ease|bounce|dragElastic|dragMomentum|transition|spring|friction|threshold)\b', re.I)
rows = []
for folder in sorted((SOURCE / 'blocks').iterdir()):
    if not folder.is_dir():
        continue
    readme = (folder / 'README.md').read_text(encoding='utf-8')
    row = {'slug':folder.name,'name':readme.splitlines()[0].removeprefix('# '),
           'props':[line for line in readme.splitlines() if line.startswith('| `')],
           'dependencies':[], 'files':[], 'motion_locations':[], 'event_handlers':[], 'capability_signals':{}}
    for file in sorted(folder.glob('*')):
        if file.suffix not in ['.tsx','.ts','.css']:
            continue
        text = file.read_text(encoding='utf-8')
        relative = file.relative_to(ROOT).as_posix()
        row['files'].append({'path':relative,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'lines':len(text.splitlines())})
        row['dependencies'].extend(re.findall(r'from [\"\']([^\"\']+)[\"\']',text))
        for number,line in enumerate(text.splitlines(),1):
            if MOTION.search(line) and not line.strip().startswith(('*','//')):
                row['motion_locations'].append({'file':relative,'line':number,'text':line.strip()})
            if re.search(r'on(Pointer|Key|Click|Drag|Focus|Blur|Change|Touch|Wheel)',line):
                row['event_handlers'].append({'file':relative,'line':number,'text':line.strip()})
        for name, pattern in {
            'reduced_motion_text':r'prefers-reduced-motion|useReducedMotion',
            'keyboard_handler_text':r'onKeyDown|onKeyUp|keydown',
            'pointer_cancel_text':r'onPointerCancel|pointercancel',
            'frame_loop_text':r'requestAnimationFrame',
            'visibility_text':r'document.hidden|visibilitychange|IntersectionObserver',
            'microphone_api_text':r'getUserMedia|MediaRecorder',
            'network_api_text':r'fetch\(|XMLHttpRequest|axios\.',
        }.items():
            row['capability_signals'][name] = row['capability_signals'].get(name,False) or bool(re.search(pattern,text))
    row['dependencies'] = sorted(set(row['dependencies']))
    rows.append(row)
(ROOT/'catalogue/source-index.json').write_text(json.dumps({'note':'Pattern index only. Presence or absence is not a behavior or security certification. Line references are for the pinned snapshot.','items':rows},ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# Free source index','','47 MIT component folders. Exact settings, formulas, event handlers, and CSS remain in the pinned source. This index does not rewrite or simplify their motion.','','| Component | Props and integration | Motion references | Dependencies |','| --- | --- | --- | --- |']
for row in rows:
    locations=row['motion_locations']
    first=locations[0] if locations else None
    link=f'[{len(locations)} locations](../{first["file"]}#L{first["line"]})' if first else 'See source'
    lines.append(f'| {row["name"]} | [README](../upstream-free/blocks/{row["slug"]}/README.md) | {link} | {", ".join(row["dependencies"])} |')
(ROOT/'catalogue/free-source.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
manifest={p.relative_to(SOURCE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCE.rglob('*') if p.is_file() and not any(part in ['node_modules','dist','.git'] for part in p.relative_to(SOURCE).parts)}
(ROOT/'catalogue/upstream-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(f'Indexed {len(rows)} components and {len(manifest)} upstream files')
