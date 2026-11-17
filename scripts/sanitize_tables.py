"""Keep factual API columns; omit copied descriptive/editorial table prose."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for site in ['viewport','60fps','shadcn','interior','motion-primitives','aceternity','cult']:
    file=root/site/'catalogue/index.json';data=json.loads(file.read_text(encoding='utf8'));removed=0
    for row in data['items']:
        result=[]
        for table in row.get('api_tables',[]):
            if not table:continue
            keep=[i for i,h in enumerate(table[0]) if h.strip().lower() in ['prop','property','name','type','default','default value','component','dependencies','required']]
            removed+=len(table[0])-len(keep)
            if keep:result.append([[r[i] if i<len(r) else '' for i in keep] for r in table])
        row['api_tables']=result
    file.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8');print(site,'excluded non-factual columns',removed)
