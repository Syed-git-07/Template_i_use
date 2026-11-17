# Coverage and remaining work

Snapshot: 17 November 2026. Shared reference research for all projects.

**The public inventory is complete against the three indexes and sitemap. Every microinteraction is not certified as exhaustively reviewed.**

| Area | Evidence | Limitation |
| --- | --- | --- |
| Public inventory | 587 unique URLs, all public headings checked | Dated catalogue, not future additions |
| Blocks | 168 panels opened: 47 live, 121 static Pro previews | Restricted stills cannot establish motion |
| Free source | 47 components, 24 synthesised sounds, 170 unchanged upstream files | MIT source snapshot, not production integration |
| Free demonstrations | 46 guided replays sampled; Label input exercised directly | Sampling around 0, 1.5 and 4 seconds misses intermediate/longer states |
| Direct interactions | 8 selected checks passed | Desktop browser, synthetic demo inputs only |
| Finds | 260 videos sampled; 1 static images sampled; 0 unresolved media checks | Mostly one midpoint frame; seven named priorities have four frames. Not full playback or original-source verification |
| Sounds | 145 public entries indexed; 24 free sound implementations archived | No listening comparison or paid WAV/source extraction |
| Supporting pages | 13 public pages indexed; Docs, Licence, MCP, pricing and Bench inspected in browser | No account creation, purchase, billing or signed-in workflow tested |
| Build | Upstream TypeScript and production build passed | Large full-playground chunks; some sample image paths are absent |

## Evidence files

- [Per-item ledger](catalogue/review-ledger.json): all 587 entries, with explicit remaining work.
- [Block controls](catalogue/browser-blocks.json), [free replay observations](catalogue/free-replays.json), [direct gesture checks](catalogue/gesture-checks.json).
- [Finds browser observations](catalogue/finds-browser.json): access method, duration and sampled positions where available.
- [Source formulas/events index](catalogue/source-index.json), [file hashes](catalogue/upstream-sha256.json).

Screenshots are local observation aids, not redistributed assets. Some early captures caught the panel-opening transition; the media pass was repeated with an explicit settle interval. Do not use a capture without visually checking it. Small contact-sheet inspection is a broad visual pass, not a precision timing measurement.

## What is still needed for exact fidelity

1. For the free component selected by a project, start with the archived source and record chosen props. Then verify all relevant pointer/keyboard/touch and interruption states in that project.
2. For Pro blocks, keep the attributed static reference and available control labels. The user has no Pro subscription; source and live behavior remain unavailable through this access. Do not publish Pro blocks as a library even if access later changes.
3. For Finds, review the full recording around the relevant transitions and, where publicly available, the creator's source. A video does not disclose hidden interaction rules or precise spring constants.
4. For sound fidelity, listen on the intended device and compare levels, attack/decay and repeated playback; keep sound optional.
5. Resolve the spoken “tool stack” and “slash/slide bar” references at implementation time; candidate links are retained in INTERACTIONS.

The [browser-side handoff prompt](BROWSER-HANDOFF.md) is available for references that behave differently in the user's browser. It does not ask for an upgrade, credentials or restricted-source exports.

## Media checks needing follow-up

No unresolved media-loading checks in the latest saved pass. This does not mean every motion state was inspected.

## Resume without repeating completed work

Use the ledger and canonical URLs. Skip re-indexing unless checking for new entries. Focus the next batch on full state sequences for chosen references, recording trigger, before/after, reverse path, cancellation, timing evidence, props, input method, reduced-motion behavior and unresolved questions. Keep new project-specific choices separate from this shared library.
