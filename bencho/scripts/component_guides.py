"""Navigation guides for the licensed, immutable Bencho source snapshot."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
destination=root/'components';destination.mkdir(exist_ok=True)
for row in json.loads((root/'catalogue/source-index.json').read_text(encoding='utf8'))['items']:
    lines=[f'# {row["name"]}','',f'Public reference: https://bencho.dev/blocks/{row["slug"]}','',
      f'[Original API and usage guide](../upstream-free/blocks/{row["slug"]}/README.md). The upstream files remain unchanged and retain their MIT notices.','',
      '## Implementation and formation','']
    for f in row['files']:lines.append(f'- [{Path(f["path"]).name}](../{f["path"]}): {f["lines"]} lines; SHA-256 `{f["sha256"]}`.')
    lines+=['','## Motion and transition locations','', 'These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.','']
    for m in row['motion_locations']:lines.append(f'- [{Path(m["file"]).name}:{m["line"]}](../{m["file"]}#L{m["line"]}): `{m["text"].replace("`", chr(39))}`')
    lines+=['','## Verification','', '[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.','']
    (destination/(row['slug']+'.md')).write_text('\n'.join(lines),encoding='utf8')
print('Generated',len(list(destination.glob('*.md'))),'Bencho component guides')
