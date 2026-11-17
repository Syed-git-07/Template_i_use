# new-items-pill

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/new-items-pill.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/new-items-pill.tsx); SHA-256 `ad608bdc4067d61d32de1c1328954478dcf52b516f1f9d378e844fa946181b63`; 225 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| itemCount | number | False | 23 |
| anchor | NewItemsAnchor | True | 24 |
| threshold | number | True | 25 |
| scrollProps | {     ref: React.RefObject<T \| null>;     tabIndex: number;     style: React.CSSProperties;   } | False | 29 |
| ref | React.RefObject<T \| null> | False | 30 |
| tabIndex | number | False | 31 |
| style | React.CSSProperties | False | 32 |
| unread | number | False | 34 |
| pinned | boolean | False | 35 |
| jump | () => number | False | 37 |
| count | number | False | 123 |
| onJump | () => void | False | 124 |
| anchor | NewItemsAnchor | True | 125 |
| label | (count: number) => string | True | 126 |
| max | number | True | 127 |
| className | string | True | 128 |

### Defaults and motion

- Default `anchor` = `"top"` (line 42).
- Default `threshold` = `24` (line 43).
- Default `anchor` = `"top"` (line 136).
- Default `max` = `99` (line 138).
- Default `className` = `""` (line 139).
- `stiffness`: 540 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.5 (line 14).
- `duration`: 0 (line 15).
- `duration`: 0.16 (line 178).
- `ease`: computed; inspect expression (line 178).
- `duration`: 0.16 (line 184).
- `ease`: computed; inspect expression (line 184).

### Input, style and lifecycle

Events: scroll (line 72); onClick (line 167).

Typography/style anchors: 173, 178.

Source signals: reduced_motion, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Prepending to a scrolled list normally shoves the line you were reading down the screen; the hook records the distance from the reading position to the end of the list and restores it in the same frame the new items commit, and sets overflow-anchor: none so the browser's own anchoring cannot correct it a second time.
- The pill is absolutely positioned over the scroller, so neither its arrival nor a count crossing from one digit to three ever reflows a single row underneath it. It arrives from the edge the items arrived from and leaves the same way.
- Jumping returns how many had piled up, so the rows you were called back for can be marked once you get there. Being told there are nine new posts and then dropped at the top with no idea which nine is half an answer.
- Focus is the brand blue border and the surface lifting, never a ring. A halo on top of a border and a shadow is the third signal nobody asked for.
- Scroll offset is read into a ref on a passive listener; React re-renders only when the pinned boolean flips or the buffered count changes, never once per scroll event.
- Scrolling back to the edge yourself clears the count without a click, so the pill never sits over content you have already reached.
- Screen readers get one settled count 700ms after the last arrival instead of one announcement per item, and the visible text is hidden from them so the button is named once rather than twice.
- Under prefers-reduced-motion the pill still appears and still states the count, only crossing in on opacity, and the jump becomes an instant scroll; either way focus lands on the scroll container before the pill unmounts, so it is never dropped to the body.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| count | number | not specified | Unread arrivals to advertise. The pill is absent at 0 and enters when it crosses 1. Feed it `unread` from useNewItems. |
| onJump | () => void | not specified | Fired on click or Enter/Space. Pass `jump` from useNewItems, which scrolls to the anchored edge, clears the count and moves focus to the scroll container. It returns how many had piled up, so the caller can mark what just arrived. |
| anchor | "top" \| "bottom" | "top" | Which edge new items arrive at. Sets where the pill sits, which way its arrow points, and the direction it enters from. |
| label | (count: number) => string | n => `${n} new item(s)` | Builds the visible text and the accessible name from the count. Pluralise here; nothing downstream guesses at grammar. |
| max | number | 99 | Counts above this render as "99+" so the pill cannot grow without bound on a busy stream. |
| className | string | "" | Appended last to the absolutely positioned wrapper, so callers can move the pill or change its inset without editing the file. |
| itemCount | number | not specified | useNewItems option. The current length of the rendered list. Every increase is treated as an arrival; decreases are ignored. |
| useNewItems.anchor | "top" \| "bottom" | "top" |  "top" compensates the scroll offset when items are prepended; "bottom" follows the tail only while the reader is already at it. |
| threshold | number | 24 | useNewItems option. Pixels from the anchored edge still counted as being at the edge, so a one-pixel drift does not start buffering. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
