"""Refresh public reference metadata, not paid source or third-party media.

Run: python bencho/scripts/catalogue.py
Requires requests and beautifulsoup4. Never uses a signed-in session.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import json
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://bencho.dev'

def get(url):
    response = requests.get(url, timeout=35)
    response.raise_for_status()
    return response

def detail(item):
    try:
        response = get(item['url'])
        soup = BeautifulSoup(response.text, 'html.parser')
        heading = soup.find('h1')
        item['http_status'] = response.status_code
        item['page_heading'] = heading.get_text(' ', strip=True) if heading else None
        item['page_verified'] = bool(heading and 'not found' not in heading.text.lower())
        # One short attributed excerpt per detail page; no bulk page/source copies.
        paragraph = heading.find_next('p') if heading else None
        item['source_summary'] = paragraph.get_text(' ', strip=True) if paragraph else ''
        item['source_summary'] = ' '.join(item['source_summary'].split()[:20])
        item['external_credits'] = [
            {'label': a.get_text(' ', strip=True), 'url': a['href']}
            for a in soup.select('a[href^="https://"]')
            if not a['href'].startswith(BASE)
        ]
        if item['kind'] == 'find':
            tag_node = paragraph.find_next_sibling('p') if paragraph else None
            # Credit paragraph precedes the tag paragraph on public Finds detail pages.
            if tag_node and tag_node.find('a'):
                tag_node = tag_node.find_next_sibling('p')
            item['tags'] = [x.strip() for x in tag_node.get_text(' ', strip=True).split(',')] if tag_node else []
        item['evidence'] = 'public page metadata; live behavior not yet reviewed'
    except Exception as exc:
        item['page_verified'] = False
        item['error'] = str(exc)
    return item

def main():
    ROOT.joinpath('catalogue').mkdir(exist_ok=True)
    items = []
    for path, kind, prefix in [('/', 'block', '/blocks/'), ('/finds', 'find', '/finds/'), ('/sounds', 'sound', '/sounds/')]:
        soup = BeautifulSoup(get(BASE + path).text, 'html.parser')
        for anchor in soup.select('a[href]'):
            href = anchor['href']
            if not href.startswith(prefix):
                continue
            label = anchor.get_text(' ', strip=True)
            name, _, suffix = label.partition(' — ')
            item = {'kind': kind, 'slug': href.split('/')[-1], 'name': name, 'url': BASE + href}
            item['creator' if kind == 'find' else 'category'] = suffix
            items.append(item)
    items = list({x['url']: x for x in items}.values())
    sitemap = ET.fromstring(get(BASE + '/sitemap.xml').text)
    urls = [e.text for e in sitemap.findall('.//{*}loc')]
    known = {x['url'] for x in items}
    for url in urls:
        if url not in known:
            path = url.removeprefix(BASE)
            kind = next((k for p, k in [('/blocks/', 'block'), ('/finds/', 'find'), ('/sounds/', 'sound')] if path.startswith(p)), 'page')
            items.append({'kind': kind, 'slug': path.strip('/') or 'home', 'name': path.strip('/') or 'Home', 'url': url})
    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(detail, item) for item in items]
        for future in as_completed(futures):
            results.append(future.result())
            if len(results) % 50 == 0:
                print(f'Checked {len(results)}/{len(items)} public pages', flush=True)
    results.sort(key=lambda x: (x['kind'], x['name'].lower()))
    payload = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'source': BASE,
               'scope': 'All entries linked from public Blocks, Finds, Sounds indexes plus sitemap pages',
               'sitemap_urls': len(urls), 'counts': {k: sum(x['kind'] == k for x in results) for k in ['block','find','sound','page']},
               'items': results}
    ROOT.joinpath('catalogue/index.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    for kind in ['block', 'find', 'sound', 'page']:
        lines = [f'# Bencho {kind} catalogue', '', f'Source: {BASE}. Metadata checked {payload["checked_at_utc"]}.', '',
                 'Indexing is not a claim of motion, keyboard, touch, or source verification. See the review ledger.', '',
                 '| Reference | Category / creator | Page checked |', '| --- | --- | --- |']
        for item in results:
            if item['kind'] == kind:
                lines.append(f'| [{item["name"]}]({item["url"]}) | {item.get("category", item.get("creator", ""))} | {"Yes" if item.get("page_verified") else "No"} |')
        ROOT.joinpath(f'catalogue/{kind}s.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(payload['counts']), flush=True)
    print('Failures:', sum(not x.get('page_verified') for x in results), flush=True)

if __name__ == '__main__':
    main()
