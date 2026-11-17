"""Search all saved reference catalogues by name, category and canonical path."""
import argparse,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('query');parser.add_argument('--limit',type=int,default=30);args=parser.parse_args()
terms=args.query.casefold().split();matches=[]
for file in root.glob('*/catalogue/index.json'):
    data=json.loads(file.read_text(encoding='utf8'))
    for row in data.get('items',[]):
        text=' '.join(str(row.get(k,'')) for k in ['name','slug','path','category','categories','kind']).casefold()
        if all(term in text for term in terms):matches.append({'site':file.parents[1].name,'name':row.get('name'),'url':row.get('url'),'guide':str(file.parents[1]/'README.md')})
for row in matches[:args.limit]:print(json.dumps(row,ensure_ascii=False))
print(f'{len(matches)} matches; showing {min(len(matches),args.limit)}')
