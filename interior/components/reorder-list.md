# reorder-list

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/reorder-list.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/reorder-list.tsx); SHA-256 `56e1a353f6f05819ce08f651e3cbc2410c93ab8b281d638c38397462a9582f1e`; 251 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | readonly T[] | False | 17 |
| getId | (item: T) => string | False | 18 |
| getLabel | (item: T) => string | False | 19 |
| onReorder | (next: T[]) => void | False | 20 |
| onCommit | (next: T[]) => void | True | 21 |
| disabled | boolean | True | 22 |
| children | (item: T) => React.ReactNode | False | 156 |
| label | string | False | 157 |
| className | string | True | 158 |

### Defaults and motion

- Default `disabled` = `false` (line 31).
- Default `className` = `""` (line 175).
- Default `disabled` = `false` (line 178).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `duration`: 0 (line 7).

### Input, style and lifecycle

Events: onReorder (line 188); onKeyDown (line 206); onDragStart (line 207); onDragEnd (line 208); onBlur (line 209).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- There is no ghost. The thing you are dragging is the row itself, lifted off the surface, and the gap the siblings open is the drop target — a floating copy would be one statement too many.
- Siblings close and open the gap with a layout spring; the dragged row never animates its height and the list never reflows more than the two rows trading places.
- The keyboard is a second complete implementation: Space grabs, arrows carry the row a slot at a time, Space drops, Escape restores the order from before the grab — pointer drags get the same Escape.
- A grabbed row wears the accent, because the system is responding to you right now; a merely hovered row only lifts.
- One announcement per move — 'position 2 of 5' — never a stream, and blurring a grabbed row cancels instead of leaving it stranded.
- onReorder keeps the preview live while onCommit fires once at the drop, so persistence code runs when the person decides, not while they are deciding.
- Under prefers-reduced-motion the rows trade places instantly; the order still changes, only the travel is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | readonly T[] | not specified | The list, in its current order. The component never owns the data. |
| getId | (item: T) => string | not specified | Stable identity for each row. Keys, focus and announcements all hang off it. |
| getLabel | (item: T) => string | not specified | What the screen reader calls the row while it moves. |
| onReorder | (next: T[]) => void | not specified | Fires live as the order changes, once per crossing, so the gap can follow the drag. |
| onCommit | (next: T[]) => void | not specified | Fires once when the drag drops or a keyboard move lands. The one to persist from. |
| children | (item: T) => ReactNode | not specified | The row's content. The grip, lift and focus are already handled around it. |
| label | string | not specified | Accessible name of the list. |
| disabled | boolean | false | Freezes the order and takes the rows out of the tab order. |
| className | string | "" | Appended to the outer wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
