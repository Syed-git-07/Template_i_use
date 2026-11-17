# like-burst

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/like-burst.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/like-burst.tsx); SHA-256 `ec8118bf86546614bfce0acaa424df537a30ab87ff66af483465844524f290e3`; 328 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| toggle | () => void | False | 41 |
| initialLiked | boolean | True | 45 |
| initialCount | number | True | 46 |
| onCommit | LikeCommit | True | 47 |
| onError | (error: unknown) => void | True | 48 |
| settle | number | True | 49 |
| liked | boolean | False | 53 |
| count | number | False | 54 |
| base | number | False | 55 |
| pending | boolean | False | 56 |
| burst | number | False | 57 |
| settled | { liked: boolean; count: number } | False | 58 |
| liked | boolean | False | 58 |
| count | number | False | 58 |
| toggle | () => void | False | 59 |
| initialLiked | boolean | True | 179 |
| initialCount | number | True | 180 |
| onCommit | LikeCommit | True | 181 |
| onError | (error: unknown) => void | True | 182 |
| onToggle | (liked: boolean) => void | True | 183 |
| settle | number | True | 184 |
| label | string | True | 185 |
| activeLabel | string | True | 186 |
| format | (value: number) => string | True | 187 |
| disabled | boolean | True | 188 |
| className | string | True | 189 |
| ref | React.Ref<LikeBurstHandle> | True | 205 |

### Defaults and motion

- Default `initialLiked` = `false` (line 63).
- Default `initialCount` = `0` (line 64).
- Default `settle` = `400` (line 67).
- Default `initialLiked` = `false` (line 193).
- Default `initialCount` = `0` (line 194).
- Default `settle` = `400` (line 198).
- Default `label` = `"Like"` (line 199).
- Default `activeLabel` = `"Liked"` (line 200).
- Default `disabled` = `false` (line 202).
- Default `className` = `""` (line 203).
- `stiffness`: 520 (line 13).
- `damping`: 34 (line 13).
- `mass`: 0.45 (line 13).
- `stiffness`: 260 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.8 (line 14).
- `duration`: 0 (line 15).
- `delay`: computed; inspect expression (line 28).
- `duration`: 0.44 (line 275).
- `delay`: computed; inspect expression (line 275).
- `ease`: computed; inspect expression (line 275).

### Input, style and lifecycle

Events: onClick (line 225).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, async, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Nine taps produce one request. Intent is debounced by settle, and a burst that returns to the confirmed state sends nothing at all, so a double tap is not a write followed by an undo write.
- Responses that arrive out of order cannot win. Every flush increments a sequence number and aborts the previous controller, so a slow unlike landing after a fast like is discarded rather than applied.
- A rejected commit rolls the count and the fill back to the last confirmed value, not to zero and not to a guess, so the number on screen is never a lie the user has to reload to discover.
- The button never changes width. Both labels share one grid cell, and the count cell reserves the wider of base and base + 1 up front, so a like at 999 does not shove the row.
- Screen readers get the settled value once from a polite status region; the optimistic count and the burst are aria-hidden, so a fast tapper does not queue nine announcements.
- Under prefers-reduced-motion the sparks are not rendered and the fill switches with no transition. The state still arrives, only the trip is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| initialLiked | boolean | false | Server truth at mount. Read once; the hook owns the value afterwards so a re-render never yanks the count back mid-gesture. |
| initialCount | number | 0 | Server truth at mount. Both reachable counts, base and base + 1, are measured up front to reserve width. |
| onCommit | (liked: boolean, signal: AbortSignal) => Promise<unknown> | undefined | Called once per settled intent, never once per tap. Reject to trigger rollback; the signal aborts when a newer intent supersedes this one. |
| onError | (error: unknown) => void | undefined | Fires after the UI has already rolled back to the last confirmed state, so the handler only has to explain, not repair. |
| onToggle | (liked: boolean) => void | undefined | Fires on every tap with the intended state. Use for analytics; do not use for writes. |
| settle | number | 400 | Milliseconds of quiet before intent is committed. A burst of taps inside this window collapses into at most one request. |
| label | string | "Like" | The button's accessible name in both states; pressed state is carried by aria-pressed, not by the name. |
| activeLabel | string | "Liked" | Visible label when liked. Shares a grid cell with label, so the button width is the wider of the two at all times. |
| format | (value: number) => string | Intl.NumberFormat("en-US") | Formats the count. Must be pure and locale-fixed; it runs during render on both server and client. |
| disabled | boolean | false | Blocks new intent. In-flight commits still settle and still reconcile. |
| className | string | "" | Appended last on the wrapper so callers win on every conflicting utility. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
