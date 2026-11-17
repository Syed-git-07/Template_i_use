"""Index public reference sites. Cache HTML privately; publish facts and source links only."""
import concurrent.futures,hashlib,json,re,sys,time
from pathlib import Path
from urllib.parse import urljoin,urlparse
from datetime import datetime,timezone
import requests
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
SITES={'viewport':'https://viewportui.com','60fps':'https://60fps.design','shadcn':'https://ui.shadcn.com','interior':'https://www.interior.dev','motion-primitives':'https://motion-primitives.com','aceternity':'https://ui.aceternity.com','cult':'https://www.cult-ui.com'}
def fetch(url):
    for attempt in range(3):
        try:
            r=requests.get(url,timeout=35);r.encoding='utf8'
            if r.status_code==429 or r.status_code>=500:
                time.sleep(2+attempt*2);continue
            return r
        except requests.RequestException:
            if attempt==2:raise
            time.sleep(1)
    return r
def main(site):
    base=SITES[site];out=ROOT/site/'catalogue';out.mkdir(parents=True,exist_ok=True)
    cache=ROOT/'.local/html'/site;cache.mkdir(parents=True,exist_ok=True)
    sm=fetch(base+'/sitemap.xml');urls=sorted(set(re.findall(r'<loc>(.*?)</loc>',sm.text)))
    if not urls:
        response=fetch(base+'/docs');soup=BeautifulSoup(response.text,'html.parser')
        urls=sorted({urljoin(base,a['href']).split('#')[0] for a in soup.select('a[href]') if urljoin(base,a['href']).startswith(base) and urlparse(urljoin(base,a['href'])).path.startswith('/docs')})
    # Preserve complete discovery, including category and supporting pages.
    (out/'discovery.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'sitemap_status':sm.status_code,'urls':urls},indent=2),encoding='utf8')
    if site=='viewport':selected=[u for u in urls if '/posts/' in u]+[base+'/about']
    elif site=='60fps':selected=[u for u in urls if not any(x in u for x in ['/category/','/tags/','/tag/'])]
    else:selected=urls
    destination=out/'index.json'
    prior=json.loads(destination.read_text(encoding='utf8'))['items'] if destination.exists() else []
    good={r['url']:r for r in prior if r.get('status')=='indexed'}
    queue=[u for u in selected if u not in good];rows=list(good.values())
    def inspect(url):
        row={'url':url,'path':urlparse(url).path,'status':'needs-review'}
        try:
            key=hashlib.sha256(url.encode()).hexdigest()+'.html';saved=cache/key
            if saved.exists():html=saved.read_text(encoding='utf8');status=200
            else:
                r=fetch(url);html=r.text;status=r.status_code
                if status==200:saved.write_text(html,encoding='utf8')
            row['http_status']=status
            if status!=200:return row
            s=BeautifulSoup(html,'html.parser');main=s.select_one('main,article') or s
            h=s.find('h1');title=s.find('title');row['name']=h.get_text(' ',strip=True) if h else (title.get_text(' ',strip=True) if title else urlparse(url).path)
            row['headings']=[x.get_text(' ',strip=True) for x in main.select('h2,h3')]
            row['source_links']=sorted({urljoin(url,a['href']) for a in s.select('a[href]') if any(v in a['href'] for v in ['github.com/','codepen.io/','codesandbox.io/','stackblitz.com/','x.com/','twitter.com/'])})
            row['media']=[{'kind':x.name,'url':urljoin(url,x.get('src') or x.get('data-src') or ''),'poster':urljoin(url,x['poster']) if x.get('poster') else None,'label':x.get('aria-label')} for x in s.select('video,video source,iframe') if x.get('src') or x.get('data-src')]
            row['categories']=[{'name':a.get_text(' ',strip=True),'url':urljoin(url,a['href'])} for a in s.select('a[href]') if re.search(r'/(kind|font|style|industry)/',a['href'])]
            row['api_tables']=[]
            for table in main.select('table'):
                cells=[[c.get_text(' ',strip=True) for c in tr.select('th,td')] for tr in table.select('tr')]
                if not cells:continue
                keep=[i for i,h in enumerate(cells[0]) if h.strip().lower() in ['prop','property','name','type','default','default value','component','dependencies','required']]
                if keep:row['api_tables'].append([[r[i] if i<len(r) else '' for i in keep] for r in cells])
            row['code_blocks']=len(main.select('pre'))
            row['documentation_links']=sorted({urljoin(url,a['href']).split('#')[0] for a in main.select('a[href]') if '/docs/' in a['href']})
            text=main.get_text(' ',strip=True)
            row['access_signals']=[word for word in ['Get All-Access','Unlock','Sign in','Premium','Pro','Purchase'] if word in text]
            row['status']='indexed';row['html_sha256']=hashlib.sha256(html.encode()).hexdigest()
            row['limit']='Public page structure only. Navigation may contribute headings/tables. Media and code not republished; behavior not established by HTML.'
        except Exception as e:row['error']=repr(e)[:350]
        return row
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for row in pool.map(inspect,queue):
            rows.append(row)
            if len(rows)%25==0:
                print(site,len(rows),'/',len(selected),flush=True)
                destination.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'site':base,'discovered':len(urls),'selected':len(selected),'items':sorted(rows,key=lambda r:r['url'])},ensure_ascii=False,indent=2),encoding='utf8')
    destination.write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'site':base,'discovered':len(urls),'selected':len(selected),'items':sorted(rows,key=lambda r:r['url'])},ensure_ascii=False,indent=2),encoding='utf8')
    print(site,'DONE',len(rows),'errors',sum(r['status']!='indexed' for r in rows),flush=True)
if __name__=='__main__':
    for site in sys.argv[1:]:main(site)
