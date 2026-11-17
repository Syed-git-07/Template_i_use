# Coverage and evidence

Snapshot: 17 November 2026. This research serves all projects.

**The public component inventory and four-variant scalar-default audit are complete for this snapshot. Every possible microinteraction, device and production integration is not exhaustively certified.**

| Area | Evidence | Limit |
| --- | --- | --- |
| Public catalogue | 237 unique URLs reconciled against the public index and sitemap; 217 components and 20 supporting/tool pages | Future additions require refresh |
| Categories | 33 text animations, 38 animations, 48 components, 34 micro interactions, 64 backgrounds | Backgrounds catalogued, not selected for portfolio |
| Source | 219 components, 876 variant references, 2,788 hashed source/script files locally | EvilEye and FlyingButton are source-only/unlisted; implementation is not redistributed here |
| API audit | 219 prop tables; 4,243 comparable defaults across all four variants; zero reported errors | Ten descriptive defaults excluded; no proof of full semantic equivalence or render correctness |
| Component browser survey | All 217 panels observed; zero recorded page errors or unresolved loads | Desktop controls and screenshot/pointer samples only; no exhaustive branch coverage or GPU correctness claim |
| Direct interaction checks | Seven component scenarios passed, with 16 explicit assertions | Selected public demos, desktop keyboard/pointer, synthetic data; no real services |
| Tools | Five public creative-tool pages included with browser control observations | No complete preset traversal, exports, camera/microphone or sound comparison |
| Build | Official source prop audit executed | Full upstream application build and production integration were not performed |

## Evidence files

- [Public index](catalogue/index.json): headings, canonical URLs and categories.
- [Source index](catalogue/source-index.json): factual APIs, dependencies, pinned variants, motion/event anchors and structural signals.
- [Source audit](catalogue/source-audit.json): exact comparison counts and errors.
- [Source hashes](catalogue/local-source-sha256.json): reproducible local source metadata.
- [Browser records](catalogue/browser.json): observed knobs, API rows, preview controls, canvas counts and capture references.
- [Gesture assertions](catalogue/gesture-checks.json): actual exercised states and recovery.
- [Tool observations](catalogue/tools-browser.json): current public control labels and limits.
- [Per-item ledger](catalogue/review-ledger.json): catalogue-to-source/browser mapping and remaining checks.

Direct checks cover Code Slots numeric filtering, Backspace, accept/read-only and reject/clear; Hold Button short release, Escape cancellation, completed hold and reset; Folder keyboard open, pointer drag and Escape close; Elastic Slider keyboard bounds; Flip Card click/keyboard reversal; Swipe Row keyboard reveal/close and full swipe; Card Nav click/Escape.

The announcement overlay initially blocked Code Slots and Hold Button tests. After inspecting the obstruction, the test closes the delayed announcement and the affected scenarios pass. The Code Slots outcome picker uses visible menu text rather than a native option role. These were browser-test issues, not evidence of a component defect. Element screenshots from the broad survey can include transient overlays or incomplete animation; inspect any capture before using it as a visual specification.

## Remaining fidelity work at integration time

Read computed motion expressions and CSS around the linked lines for the chosen component. Exercise all relevant touch/pen/mouse/keyboard, focus, interrupted gesture, async failure, repeated action, reduced-motion, resize and visibility cases in the target application. Test screen-reader semantics, performance and GPU fallback where relevant. Source pattern matches and screenshots cannot certify these.

No paid Pro internals, authenticated account flows, real authentication, payments, deletion, stored file edits or actual audio recording were verified. The complete original local source plus pinned links preserve access to implementation details without inventing observations or republishing restricted library code.
