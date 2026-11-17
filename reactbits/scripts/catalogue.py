"""Inventory public React Bits pages. Save links/facts, never component code."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlparse
import requests,json,re,xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
BASE='https://reactbits.dev'
def get(url):
    r=requests.get(url,timeout=35);r.raise_for_status();r.encoding='utf-8';return r
def main():
    out=ROOT/'catalogue';out.mkdir(exist_ok=True)
    soup=BeautifulSoup(get(BASE+'/get-started/index').text,'html.parser')
    rows={}
    for a in soup.select('a[href]'):
        path=urlparse(a['href']).path
        if re.match(r'^/(text-animations|animations|components|micro|backgrounds)/[^/]+$',path):
            rows[path]={'kind':'component','category':path.split('/')[1],'slug':path.split('/')[-1],'name':a.get_text(' ',strip=True),'url':BASE+path}
    sitemap=ET.fromstring(get(BASE+'/sitemap.xml').text)
    urls=[e.text for e in sitemap.findall('.//{*}loc')]
    for url in urls:
        path=urlparse(url).path
        if path not in rows:rows[path]={'kind':'tool' if path.startswith('/tools/') else 'page','slug':path.strip('/') or 'home','name':path.strip('/') or 'Home','url':BASE+path}
    def inspect(row):
        try:
            r=get(row['url']);s=BeautifulSoup(r.text,'html.parser');h=s.find('h1')
            row['http_status']=r.status_code;row['heading']=h.get_text(' ',strip=True) if h else None
            row['page_verified']=bool(h and 'not found' not in h.text.lower())
            if row['kind']!='component' and h:row['name']=row['heading']
            p=h.find_next('p') if h else None
            row['source_excerpt']=' '.join(p.get_text(' ',strip=True).split()[:16]) if p else ''
        except Exception as e:row['page_verified']=False;row['error']=str(e)[:250]
        return row
    items=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for f in as_completed([pool.submit(inspect,r) for r in rows.values()]):
            items.append(f.result())
            if len(items)%40==0:print(f'Public pages checked {len(items)}/{len(rows)}',flush=True)
    items.sort(key=lambda x:(x.get('category',x['kind']),x['name'].lower()))
    counts={k:sum(x.get('category')==k for x in items) for k in ['text-animations','animations','components','micro','backgrounds']}
    data={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'source':BASE,'sitemap_urls':len(urls),'counts':counts,'items':items}
    (out/'index.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
    for group in [*counts,'tools-and-pages']:
        selection=[x for x in items if (x.get('category')==group if group in counts else x['kind']!='component')]
        lines=[f'# React Bits: {group}','','Public entry metadata, not complete interaction verification. See COVERAGE.md.','','| Reference | Page checked |','| --- | --- |']
        lines.extend(f'| [{x["name"]}]({x["url"]}) | {x["page_verified"]} |' for x in selection)
        (out/f'{group}.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(counts,'total',len(items),'failed',sum(not x['page_verified'] for x in items),flush=True)
if __name__=='__main__':main()
