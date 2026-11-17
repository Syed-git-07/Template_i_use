# load-more

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/load-more.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/load-more.tsx); SHA-256 `63123fd91950853760551973a813f00ff3f23e5c24f0157fc819dffbd8a17150`; 350 lines.

Imports: `react`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| onLoad | () => unknown | False | 14 |
| hasMore | boolean | True | 15 |
| auto | boolean | True | 16 |
| rootRef | RefObject<Element \| null> | True | 17 |
| rootMargin | string | True | 18 |
| maxAutoLoads | number | True | 19 |
| onError | (error: unknown) => void | True | 20 |
| status | LoadMoreStatus | False | 24 |
| paused | boolean | False | 25 |
| sentinelRef | RefObject<HTMLDivElement \| null> | False | 26 |
| load | () => void | False | 27 |
| spinning | boolean | False | 201 |
| onLoad | () => unknown | False | 245 |
| hasMore | boolean | True | 246 |
| auto | boolean | True | 247 |
| rootRef | RefObject<Element \| null> | True | 248 |
| rootMargin | string | True | 249 |
| maxAutoLoads | number | True | 250 |
| labels | Partial<LoadMoreLabels> | True | 251 |
| onError | (error: unknown) => void | True | 252 |
| className | string | True | 253 |

### Defaults and motion

- Default `hasMore` = `true` (line 32).
- Default `auto` = `true` (line 33).
- Default `rootMargin` = `"600px 0px"` (line 35).
- Default `maxAutoLoads` = `3` (line 36).
- Default `hasMore` = `true` (line 258).
- Default `auto` = `true` (line 259).
- Default `rootMargin` = `"600px 0px"` (line 261).
- Default `maxAutoLoads` = `3` (line 262).
- Default `className` = `""` (line 265).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0 (line 8).
- `duration`: 0.7 (line 9).
- `ease`: "linear" (line 9).
- `threshold`: 0 (line 145).

### Input, style and lifecycle

Events: onClick (line 304).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, async, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The sentinel fires once per page: a request already in flight, an exhausted feed, or a second intersection callback in the same frame is dropped by a ref, so one scroll never buys two copies of page four.
- A page shorter than the viewport leaves the sentinel on screen, and the naive version answers by draining the entire dataset in three frames; consecutive automatic loads are capped at maxAutoLoads and the counter resets only when the sentinel actually leaves the viewport.
- A rejected request never auto-retries. Automatic loading is blocked until a person presses the button, because a sentinel sitting on a failing endpoint is a denial-of-service attack on your own API.
- Scroll position is not an input method, so the footer is a real button in every state and reachable by keyboard and assistive tech even when auto is on; it is marked aria-disabled rather than disabled, so a focused button is never yanked out of the tab order mid-page.
- The four states share one grid cell, so the footer is the width of its longest label from first paint and the list below it never jumps when loading turns into caught up. The live region speaks once, at the end and on failure, not on every frame of the meter.
- Responses that land after unmount, or after a newer request was issued, write nothing. Under prefers-reduced-motion the meter is not paced at all and the labels swap instantly, which is the only part that was ever decorative.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| onLoad | () => unknown | not specified | Fetches the next page. Resolving `false` means that was the last one and the sentinel stops observing; rejecting puts the footer into its retry state. |
| hasMore | boolean | true | Cursor-driven alternative to resolving `false`. Either one ends the feed; setting it back to true reopens the sentinel. |
| auto | boolean | true | False observes nothing and leaves a plain button. The button exists in both modes. |
| rootRef | React.RefObject<Element \| null> | undefined | The scroll container. Required when the list scrolls inside an element rather than the document, because rootMargin is measured against the root and nothing else. |
| rootMargin | string | "600px 0px" | How far ahead of the footer the page is requested. This is the whole component: 600px of runway is roughly one flick of the thumb. |
| maxAutoLoads | number | 3 | Consecutive automatic loads allowed while the sentinel stays on screen. The count resets the moment the sentinel scrolls out of view. |
| steps | number | 8 | Cells in the progress meter drawn along the bottom lip of the button. |
| expected | number | 900 | Milliseconds the meter is paced against. It is an estimate, not a promise: the meter parks on its last cell until the request actually settles. |
| labels | Partial<Record<LoadMoreStatus, string>> | undefined | Overrides for the idle, loading, error and end copy. The button sizes to the longest one, so all four are measured up front. |
| onError | (error: unknown) => void | undefined | Receives the rejection so it can reach your logger. The component keeps the message to itself. |
| className | string | "" | Appended last to the footer wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
