# drawer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/drawer.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/drawer.tsx); SHA-256 `5edc07e72e4610ead30abc9b14fefaedf8019deba1bcdeba41e2673fc29dccf3`; 395 lines.

Imports: `react`, `react-dom`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inert | boolean | True | 24 |
| offset | { x: number; y: number } | False | 27 |
| x | number | False | 27 |
| y | number | False | 27 |
| velocity | { x: number; y: number } | False | 28 |
| x | number | False | 28 |
| y | number | False | 28 |
| open | boolean | True | 34 |
| defaultOpen | boolean | True | 35 |
| onOpenChange | (open: boolean) => void | True | 36 |
| side | DrawerSide | True | 37 |
| width | number | True | 38 |
| dismissRatio | number | True | 39 |
| modal | boolean | True | 40 |
| stop | () => void | False | 65 |
| open | boolean | False | 274 |
| onOpenChange | (open: boolean) => void | False | 275 |
| title | string | False | 276 |
| children | React.ReactNode | False | 277 |
| description | string | True | 278 |
| footer | React.ReactNode | True | 279 |
| side | DrawerSide | True | 280 |
| width | number | True | 281 |
| container | "viewport" \| "parent" | True | 282 |
| closeLabel | string | True | 283 |
| dismissOnScrimClick | boolean | True | 284 |
| className | string | True | 285 |

### Defaults and motion

- Default `defaultOpen` = `false` (line 45).
- Default `side` = `"right"` (line 47).
- Default `width` = `320` (line 48).
- Default `dismissRatio` = `0.38` (line 49).
- Default `modal` = `true` (line 50).
- Default `side` = `"right"` (line 295).
- Default `width` = `320` (line 296).
- Default `container` = `"viewport"` (line 297).
- Default `closeLabel` = `"Close panel"` (line 298).
- Default `dismissOnScrimClick` = `true` (line 299).
- Default `className` = `""` (line 300).
- `stiffness`: 150 (line 16).
- `damping`: 27 (line 17).
- `mass`: 1 (line 18).
- `duration`: 0 (line 88).
- `dragMomentum`: false (line 222).
- `dragElastic`: computed; inspect expression (line 224).

### Input, style and lifecycle

Events: onClick (line 333); onPointerDown (line 347); onPointerDown (line 367); onClick (line 368).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Closing translates the panel, it does not unmount it, so the scroll offset inside and the state of every control it holds are still there on reopen; a drawer that unmounts hands back a list scrolled to the top and a form wiped clean.
- Focus is captured when the panel opens and returned to the exact element that opened it, so closing never drops the caret on the body and restart tabbing from the head of the document.
- While open, Tab wraps inside the panel and the rest of the document is marked inert, so nothing behind the scrim can be tabbed into or read out of order.
- Locking the page scroll pads the document by the scrollbar width it just removed, so the content behind the drawer does not jump sideways as the panel arrives.
- The dismiss drag reports its position in six discrete steps rather than a float, and releasing resumes the spring from wherever the panel currently sits, so an interrupted dismiss settles instead of snapping.
- Under prefers-reduced-motion the panel is placed at its final position without the travel, still visible, still focused, never left half open.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| open | boolean | not specified | Controlled visibility. The panel stays mounted either way; this only moves it. |
| onOpenChange | (open: boolean) => void | not specified | Fired by the close button, the scrim, Escape, and a completed dismiss drag. |
| title | string | not specified | Labels the dialog. Read once when focus enters, not on every state change. |
| children | React.ReactNode | not specified | Panel body. Scrolls inside a capped region; its scroll offset survives closing. |
| description | string \| undefined | not specified | Optional second line in the header. Truncates rather than wrapping, so the header height is fixed. |
| footer | React.ReactNode \| undefined | not specified | Pinned below the scroll region. Never scrolls away from the primary action. |
| side | "left" \| "right" | "right" | Which edge the panel is anchored to. Sets the dismiss direction and which corners are rounded. |
| width | number | 320 | Panel width in pixels, clamped to calc(100% - 40px) so the scrim stays reachable on narrow screens. |
| container | "viewport" \| "parent" | "viewport" | "parent" scopes the drawer to the nearest positioned ancestor and skips scroll lock; that ancestor must be relative and overflow-hidden. |
| closeLabel | string | "Close panel" | Accessible name for the icon-only close button. |
| dismissOnScrimClick | boolean | true | Set false when the panel holds unsaved input and a stray click would discard it. |
| className | string | "" | Appended last to the panel, so surface and border classes can be overridden. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
