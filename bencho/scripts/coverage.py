"""Build an honest, per-item evidence ledger from the saved observations."""
from pathlib import Path
from collections import Counter
import json

ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/'catalogue'/name).read_text(encoding='utf-8'))
items=read('index.json')['items']
blocks={x['slug']:x for x in read('browser-blocks.json')['items']}
replays={x['slug']:x for x in read('free-replays.json')['items']}
finds={x['slug']:x for x in read('finds-browser.json')['items']}
gestures={x['slug']:x for x in read('gesture-checks.json')['items']}
recovery={x['slug']:x for x in read('recovery-checks.json')['items']}
ledger=[]
for item in items:
    row={'kind':item['kind'],'slug':item['slug'],'name':item['name'],'url':item['url'],'public_metadata_checked':item['page_verified'],'complete_motion_verification':False}
    if item['kind']=='block':
        b=blocks.get(item['slug'],{});r=replays.get(item['slug'],{});g=gestures.get(item['slug'],{})
        row.update(panel=b.get('preview','not checked'),source_archived=b.get('upstream_source',False),replay=r.get('status','not applicable'),direct_check=g.get('status','not checked'))
        if item['slug'] in recovery:row['recovery_check']=recovery[item['slug']]
        guide=ROOT/'components'/(item['slug']+'.md')
        if guide.exists():row['component_guide']='components/'+guide.name
        row['remaining']='Exact live/source motion restricted by Pro access' if b.get('preview')=='restricted-static-preview' else 'Exhaustive state/input/device review and real application integration remain project-specific work'
    elif item['kind']=='find':
        f=finds.get(item['slug'],{});row.update(media=f.get('status','not checked'),frames=len(f.get('frames',[])))
        row['remaining']='Full sequence, trigger, reverse, interruption and source parameters not established by sampled frames'
        if f.get('error'):row['access_issue']=f['error']
    elif item['kind']=='sound':row['remaining']='Auditory comparison not performed; exact free synthesizer source is archived separately'
    else:row['remaining']='Supporting page metadata indexed; no claim to account/billing workflow verification'
    ledger.append(row)
(ROOT/'catalogue/review-ledger.json').write_text(json.dumps({'note':'No item is labelled exhaustive-motion-verified. Indexed, sampled and source-backed evidence are separate.','items':ledger},ensure_ascii=False,indent=2),encoding='utf-8')
counts=Counter(x['kind'] for x in items)
fc=Counter(x['status'] for x in finds.values())
rc=Counter(x['status'] for x in replays.values())
gc=Counter(x['status'] for x in gestures.values())
lines=['# Coverage and remaining work','','Snapshot: 17 November 2026. Shared reference research for all projects.','',
       '**The public inventory is complete against the three indexes and sitemap. Every microinteraction is not certified as exhaustively reviewed.**','',
       '| Area | Evidence | Limitation |','| --- | --- | --- |',
       f'| Public inventory | {len(items)} unique URLs, all public headings checked | Dated catalogue, not future additions |',
       '| Blocks | 168 panels opened: 47 live, 121 static Pro previews | Restricted stills cannot establish motion |',
       '| Free source | 47 components, 24 synthesised sounds, 170 unchanged upstream files | MIT source snapshot, not production integration |',
       f'| Free demonstrations | {rc.get("replay-sampled",0)} guided replays sampled; Label input exercised directly | Sampling around 0, 1.5 and 4 seconds misses intermediate/longer states |',
       f'| Direct interactions | {gc.get("passed",0)} selected checks passed | Desktop browser, synthetic demo inputs only |',
       '| Additional recovery checks | OTP rejection/clear and reduced-motion accept; slide short-release/full-confirm passed | Public demos, not real authentication or transactions |',
       f'| Finds | {fc.get("video-frames-sampled",0)} videos sampled; {fc.get("static-image-sampled",0)} static images sampled; {fc.get("error",0)} unresolved media checks | Mostly one midpoint frame; seven named priorities have four frames. Not full playback or original-source verification |',
       '| Sounds | 145 public entries indexed; 24 free sound implementations archived | No listening comparison or paid WAV/source extraction |',
       '| Supporting pages | 13 public pages indexed; Docs, Licence, MCP, pricing and Bench inspected in browser | No account creation, purchase, billing or signed-in workflow tested |',
       '| Build | Upstream TypeScript and production build passed | Large full-playground chunks; some sample image paths are absent |','',
       '## Evidence files','',
       '- [Per-item ledger](catalogue/review-ledger.json): all 587 entries, with explicit remaining work.',
       '- [Block controls](catalogue/browser-blocks.json), [free replay observations](catalogue/free-replays.json), [direct gesture checks](catalogue/gesture-checks.json).',
       '- [Finds browser observations](catalogue/finds-browser.json): access method, duration and sampled positions where available.',
       '- [Source formulas/events index](catalogue/source-index.json), [file hashes](catalogue/upstream-sha256.json).','',
       '- [47 free-component guides](components/) and [additional recovery checks](catalogue/recovery-checks.json).','',
       'Screenshots are local observation aids, not redistributed assets. Some early captures caught the panel-opening transition; the media pass was repeated with an explicit settle interval. Do not use a capture without visually checking it. Small contact-sheet inspection is a broad visual pass, not a precision timing measurement.','',
       '## What is still needed for exact fidelity','',
       '1. For the free component selected by a project, start with the archived source and record chosen props. Then verify all relevant pointer/keyboard/touch and interruption states in that project.',
       '2. For Pro blocks, keep the attributed static reference and available control labels. The user has no Pro subscription; source and live behavior remain unavailable through this access. Do not publish Pro blocks as a library even if access later changes.',
       '3. For Finds, review the full recording around the relevant transitions and, where publicly available, the creator\'s source. A video does not disclose hidden interaction rules or precise spring constants.',
       '4. For sound fidelity, listen on the intended device and compare levels, attack/decay and repeated playback; keep sound optional.',
       '5. Resolve the spoken “tool stack” and “slash/slide bar” references at implementation time; candidate links are retained in INTERACTIONS.','',
       'The [browser-side handoff prompt](BROWSER-HANDOFF.md) is available for references that behave differently in the user\'s browser. It does not ask for an upgrade, credentials or restricted-source exports.','',
       '## Media checks needing follow-up','']
errors=[x for x in finds.values() if x['status']=='error']
if errors:
    for x in errors:lines.append(f'- [{x["name"]}]({x["url"]}): browser media check failed; see the exact observation in finds-browser.json. The public metadata entry remains retained.')
else:lines.append('No unresolved media-loading checks in the latest saved pass. This does not mean every motion state was inspected.')
lines.extend(['','## Resume without repeating completed work','',
              'Use the ledger and canonical URLs. Skip re-indexing unless checking for new entries. Focus the next batch on full state sequences for chosen references, recording trigger, before/after, reverse path, cancellation, timing evidence, props, input method, reduced-motion behavior and unresolved questions. Keep new project-specific choices separate from this shared library.',''])
(ROOT/'COVERAGE.md').write_text('\n'.join(lines),encoding='utf-8')
print(dict(fc));print(f'Wrote {len(ledger)} evidence rows')
