# swipe-deck

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/swipe-deck.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/swipe-deck.tsx); SHA-256 `62029704f5f5ee2bae0c5dfbf2ca48e86d46da5e5569f9106ef75b8300abf72c`; 522 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| dir | -1 \| 0 \| 1 | False | 20 |
| step | number | False | 20 |
| dir | -1 \| 1 | False | 22 |
| kind | "decide" \| "undo" | False | 22 |
| count | number | False | 29 |
| threshold | number | True | 30 |
| steps | number | True | 31 |
| flick | number | True | 32 |
| onDecide | (index: number, choice: SwipeChoice) => void | True | 33 |
| onUndo | (index: number) => void | True | 34 |
| disabled | boolean | True | 35 |
| depth | number | False | 236 |
| height | number | False | 237 |
| entryX | number | False | 238 |
| active | boolean | False | 239 |
| reduced | boolean | False | 240 |
| label | string | False | 241 |
| leftLabel | string | False | 242 |
| rightLabel | string | False | 243 |
| intent | SwipeIntent | False | 244 |
| steps | number | False | 245 |
| onMove | (dx: number) => void | False | 246 |
| onRelease | (dx: number, vx: number) => void | False | 247 |
| children | React.ReactNode | False | 248 |
| items | readonly T[] | False | 366 |
| itemKey | (item: T) => string | False | 367 |
| itemLabel | (item: T) => string | False | 368 |
| children | (item: T) => React.ReactNode | False | 369 |
| onDecide | (item: T, choice: SwipeChoice) => void | True | 370 |
| onUndo | (item: T) => void | True | 371 |
| label | string | True | 372 |
| leftLabel | string | True | 373 |
| rightLabel | string | True | 374 |
| undoLabel | string | True | 375 |
| emptyLabel | string | True | 376 |
| height | number | True | 377 |
| threshold | number | True | 378 |
| steps | number | True | 379 |
| peek | number | True | 380 |
| className | string | True | 381 |

### Defaults and motion

- Default `threshold` = `92` (line 40).
- Default `steps` = `6` (line 41).
- Default `flick` = `520` (line 42).
- Default `disabled` = `false` (line 45).
- Default `label` = `"Card deck"` (line 391).
- Default `leftLabel` = `"Skip"` (line 392).
- Default `rightLabel` = `"Keep"` (line 393).
- Default `undoLabel` = `"Undo"` (line 394).
- Default `emptyLabel` = `"Deck cleared"` (line 395).
- Default `height` = `180` (line 396).
- Default `threshold` = `92` (line 397).
- Default `steps` = `6` (line 398).
- Default `peek` = `3` (line 399).
- Default `className` = `""` (line 400).
- `stiffness`: 520 (line 13).
- `damping`: 34 (line 13).
- `mass`: 0.45 (line 13).
- `stiffness`: 150 (line 14).
- `damping`: 27 (line 14).
- `mass`: 1 (line 14).
- `stiffness`: 260 (line 15).
- `damping`: 34 (line 15).
- `mass`: 0.8 (line 15).
- `threshold`: computed; inspect expression (line 162).
- `duration`: 0 (line 275).
- `duration`: 0 (line 293).
- `duration`: 0 (line 317).
- `duration`: 0.3 (line 319).
- `ease`: computed; inspect expression (line 319).
- `duration`: 0.1 (line 320).
- `ease`: "linear" (line 320).
- `duration`: 0 (line 329).
- `delay`: 0.1 (line 331).
- `duration`: 0 (line 439).

### Input, style and lifecycle

Events: blur (line 145); visibilitychange (line 146); onDrag (line 341); onDragEnd (line 342); onMove (line 461); onRelease (line 462); onClick (line 473); onClick (line 490); onClick (line 502).

Typography/style anchors: 316.

Source signals: reduced_motion, keyboard, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The deck reserves height + 26 pixels before the first card is drawn, and every card, the fanned stack behind it and the empty state are absolutely positioned inside that one rectangle, so a decision never moves the page underneath it.
- Drag distance is reported as one of six discrete steps per side rather than a float, so a 300-pixel swipe costs six renders instead of one per frame, and the cells state where the commit point is before you cross it rather than after.
- A card that snaps back was never decided: the commit rule lives in useSwipeDeck and asks for either the full threshold or a genuine flick, so a card cannot leave on a twitch.
- Every decision is kept, so Undo restores the card and flies it back in from the side it left; a mis-swipe costs one keystroke, not a lost record.
- The deck is a focusable group where the arrow keys decide and Backspace reverses, and the same three actions exist as real buttons, so the interaction is not reachable by pointer alone.
- Screen readers get one polite announcement per settled card, its label and its position in the queue, never the drag offset; under prefers-reduced-motion the card still leaves and the counter still moves, only the fly-out is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | readonly T[] | not specified | The queue, in order. The deck consumes it from the front; nothing is mutated. |
| itemKey | (item: T) => string | not specified | Stable identity per card. Drives React keys and presence, so it must not change between renders. |
| itemLabel | (item: T) => string | not specified | One-line summary. Labels the card for assistive tech and is what the live region announces once per settled card. |
| children | (item: T) => React.ReactNode | not specified | Render prop for the card face. Receives a box of exactly `height` pixels; leave the top 24px clear so the decision stamp has somewhere to land. |
| onDecide | (item: T, choice: SwipeChoice) => void | undefined | Fired once when a card commits, by drag, flick, arrow key or button. |
| onUndo | (item: T) => void | undefined | Fired when a decision is reversed, with the item that came back. |
| label | string | "Card deck" | Accessible name for the deck group. |
| leftLabel | string | "Skip" | Left decision. Used on the button and on the stamp that fades in as you drag left. |
| rightLabel | string | "Keep" | Right decision, same treatment mirrored. |
| undoLabel | string | "Undo" | Label on the undo control, which is always present and disabled rather than absent. |
| emptyLabel | string | "Deck cleared" | Shown in the reserved box once the queue is spent. |
| height | number | 180 | Card height in pixels. The deck reserves height + 26 so the fanned stack never overflows. |
| threshold | number | 92 | Horizontal pixels a card must travel to commit. Also the denominator for the intent cells. |
| steps | number | 6 | How many cells the approach to the threshold is quantised into, per side. |
| peek | number | 3 | Cards mounted at once. Everything past this is not in the DOM. |
| className | string | "" | Appended last to the outer wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
