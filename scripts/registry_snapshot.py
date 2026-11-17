"""Cache the official public registry locally; publish only paths, dependencies and hashes."""
import concurrent.futures,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
import requests
ROOT=Path(__file__).resolve().parents[1];base='https://ui.aceternity.com/registry/'
local=ROOT/'.local/upstream/aceternity';local.mkdir(parents=True,exist_ok=True)
out=ROOT/'aceternity/catalogue';out.mkdir(parents=True,exist_ok=True)
r=requests.get(base+'registry.json',timeout=30);r.raise_for_status();catalogue=r.json()
(local/'registry.json').write_text(r.text,encoding='utf8')
def inspect(item):
    name=item['name'];url=base+name+'.json';row={'name':name,'url':url,'type':item.get('type'),'status':'needs-review'}
    try:
        response=requests.get(url,timeout=35);row['http_status']=response.status_code
        if response.status_code!=200:
            if response.status_code in [401,403]:row['status']='restricted-source'
            return row
        data=response.json();row['dependencies']=data.get('dependencies',[]);row['registry_dependencies']=data.get('registryDependencies',[]);row['files']=[]
        for f in data.get('files',[]):
            content=f.get('content');relative=f.get('path','')
            if not content:continue
            # A registry path is data, not authorization to write outside its own cache.
            target=(local/'components'/name/relative).resolve()
            if not target.is_relative_to((local/'components'/name).resolve()):raise ValueError('Unsafe registry path')
            target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content,encoding='utf8',newline='')
            row['files'].append({'path':target.relative_to(local).as_posix(),'sha256':hashlib.sha256(content.encode()).hexdigest(),'lines':len(content.splitlines())})
        row['status']='source-cached' if row['files'] else 'metadata-only'
    except Exception as e:row['error']=repr(e)[:300]
    return row
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for row in pool.map(inspect,catalogue['items']):
        rows.append(row)
        if len(rows)%25==0:print('Aceternity registry',len(rows),flush=True)
(out/'registry-source.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'source':base+'registry.json','license_boundary':'Local reference only; do not redistribute the item collection. Public endpoint access does not override licensing.','items':rows},indent=2),encoding='utf8')
print('Aceternity registry DONE',len(rows),'unresolved',sum(r['status']=='needs-review' for r in rows),flush=True)
