# reading-progress

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/reading-progress.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/reading-progress.tsx); SHA-256 `1dd8ece7e3a556fc477182b7d552ce5ea26295d41d6e24b3364b2e0087a7a2d7`; 227 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| current | HTMLElement \| null | False | 12 |
| target | ScrollRef | True | 15 |
| scroller | ScrollRef | True | 16 |
| steps | number | True | 17 |
| words | number | True | 18 |
| wordsPerMinute | number | True | 19 |
| step | number | False | 23 |
| steps | number | False | 24 |
| progress | number | False | 25 |
| percent | number | False | 26 |
| minutesLeft | number | False | 27 |
| totalMinutes | number | False | 28 |
| complete | boolean | False | 29 |
| label | string | True | 122 |
| doneLabel | string | True | 123 |
| className | string | True | 124 |

### Defaults and motion

- Default `steps` = `24` (line 40).
- Default `words` = `0` (line 41).
- Default `wordsPerMinute` = `220` (line 42).
- Default `steps` = `24` (line 130).
- Default `words` = `0` (line 131).
- Default `wordsPerMinute` = `220` (line 132).
- Default `label` = `"Reading progress"` (line 133).
- Default `doneLabel` = `"End"` (line 134).
- Default `className` = `""` (line 135).
- `stiffness`: 210 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.9 (line 6).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0.3 (line 9).
- `ease`: computed; inspect expression (line 9).
- `delay`: 0.08 (line 9).
- `duration`: 0 (line 10).

### Input, style and lifecycle

Events: scroll (line 83); resize (line 84).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, cleanup, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Scroll is measured inside a single coalesced requestAnimationFrame and committed only when the quantized step changes, so a fast flick through a long article costs at most twenty-four renders instead of one per frame — the quantization is a render budget, not a look; the fill itself moves on a spring, on a transform.
- The track is a recessed well and the fill is the accent, because a progress fill is the system answering your scroll right now — and the radii nest, four outside, two inside, with the two pixels of padding between them.
- The estimate and the end state occupy the same grid cell, sized up front by an invisible copy of the longest string it can ever hold, so the number never shifts the header as it counts down from two digits to one.
- Progress is derived from the article's own box, not the document's, so a tall footer or a sticky sidebar cannot report the reader as finished while paragraphs remain.
- A container shorter than its viewport reports complete rather than dividing by zero, and content that grows after mount is caught by a ResizeObserver instead of freezing the track at a stale height.
- Screen readers get a progressbar with a real name and a value, and nothing else. A second live region narrating the same number is a running commentary, not an aid.
- Under prefers-reduced-motion the springs are removed and the readout is not; scroll and resize listeners, the pending frame and the observer are all torn down on unmount.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| target | { readonly current: HTMLElement \| null } | not specified | The article element. Progress runs from its top edge to its last visible line, so headers and footers outside it never count as reading. |
| scroller | { readonly current: HTMLElement \| null } | window | The scroll container, when the article lives in a pane rather than the document. Omit for window scrolling. |
| steps | number | 24 | How finely the scroll is quantized, and therefore the maximum number of renders a full scroll can cost. The fill still reads as continuous — the spring smooths between steps. |
| words | number | 0 | Word count of the article. Above zero the readout is minutes remaining. At zero there is no readout at all — the track is the percentage. |
| wordsPerMinute | number | 220 | Reading rate used for the estimate. |
| label | string | "Reading progress" | Accessible name of the progressbar, also used in the completion announcement. |
| doneLabel | string | "End" | Replaces the estimate once the last cell lights. |
| className | string | "" | Appended last, so callers can override height, gap and color. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
