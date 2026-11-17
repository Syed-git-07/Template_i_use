# popover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/popover.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/popover.tsx); SHA-256 `440a8f42027bbbb53515c8bd4debff236db6a8c1886a7db836dec9050affcf3e`; 377 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| x | number | True | 38 |
| y | number | True | 38 |
| open | boolean | False | 50 |
| side | PopoverSide | True | 51 |
| align | PopoverAlign | True | 52 |
| offset | number | True | 53 |
| padding | number | True | 54 |
| arrowSize | number | True | 55 |
| boundary | React.RefObject<HTMLElement \| null> | True | 56 |
| anchorRef | React.RefObject<A \| null> | False | 60 |
| floatingRef | React.RefObject<HTMLDivElement \| null> | False | 61 |
| panelRef | React.RefObject<HTMLDivElement \| null> | False | 62 |
| contentRef | React.RefObject<HTMLDivElement \| null> | False | 63 |
| arrowRef | React.RefObject<HTMLSpanElement \| null> | False | 64 |
| side | PopoverSide | False | 65 |
| update | () => void | False | 66 |
| trigger | React.ReactNode | False | 219 |
| children | React.ReactNode | False | 220 |
| label | string | False | 221 |
| open | boolean | True | 222 |
| defaultOpen | boolean | True | 223 |
| onOpenChange | (open: boolean) => void | True | 224 |
| side | PopoverSide | True | 225 |
| align | PopoverAlign | True | 226 |
| offset | number | True | 227 |
| padding | number | True | 228 |
| arrowSize | number | True | 229 |
| boundary | React.RefObject<HTMLElement \| null> | True | 230 |
| triggerClassName | string | True | 231 |
| className | string | True | 232 |

### Defaults and motion

- Default `side` = `"bottom"` (line 71).
- Default `align` = `"center"` (line 72).
- Default `offset` = `10` (line 73).
- Default `padding` = `8` (line 74).
- Default `arrowSize` = `9` (line 75).
- Default `defaultOpen` = `false` (line 240).
- Default `side` = `"bottom"` (line 242).
- Default `align` = `"center"` (line 243).
- Default `offset` = `10` (line 244).
- Default `padding` = `8` (line 245).
- Default `arrowSize` = `9` (line 246).
- Default `triggerClassName` = `""` (line 248).
- Default `className` = `""` (line 249).
- `stiffness`: 260 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.8 (line 14).
- `duration`: 0.1 (line 347).
- `duration`: 0.13 (line 351).
- `ease`: computed; inspect expression (line 351).
- `duration`: 0 (line 356).
- `duration`: 0.14 (line 357).
- `ease`: computed; inspect expression (line 357).

### Input, style and lifecycle

Events: scroll (line 204); resize (line 205); pointerdown (line 301); keydown (line 302); onClick (line 317); onBlurCapture (line 328).

Typography/style anchors: 347, 351.

Source signals: reduced_motion, keyboard, focus, cleanup, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Placement is measured, never assumed: the requested side is kept only when the panel actually fits there, and flips to its opposite when the opposite has more room, so a trigger near an edge cannot open a panel that runs off the screen.
- The cross axis is clamped inside the boundary while the arrow is re-solved against the trigger's centre, so a panel that had to slide back into view still points at the control that opened it instead of at nothing.
- transform-origin is written to the arrow's position on every measurement, so the panel scales out of its trigger rather than out of its own middle, and under prefers-reduced-motion it simply arrives in place, still fully rendered.
- Scroll, resize and content changes reposition through one rAF that writes left, top and the arrow offset straight to the DOM nodes; React re-renders only when the resolved side genuinely flips, so tracking a scrolling anchor costs no renders.
- Available room caps the content box, which scrolls inside its own overscroll-contained region, so the panel never animates toward an unbounded height and never grows past the boundary it was given.
- Escape closes and returns focus to the trigger, moving focus out of the panel closes it, an outside pointer closes it, and the trigger carries aria-haspopup, aria-expanded and aria-controls against a labelled dialog.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| trigger | React.ReactNode | not specified | Content of the button that owns the popover. The button is the anchor every measurement is taken from. |
| children | React.ReactNode | not specified | Panel content. It is placed in a scroll box that is capped to the room actually available. |
| label | string | not specified | Accessible name for the dialog. Read once when the panel takes focus. |
| open | boolean | — | Controlled state. Omit it to let the component own its own open state. |
| defaultOpen | boolean | false | Initial state when uncontrolled. |
| onOpenChange | (open: boolean) => void | — | Fires for every close path: trigger, Escape, outside pointer, focus leaving the panel. |
| side | "top" \| "right" \| "bottom" \| "left" | "bottom" | The side asked for. Honoured when it fits, flipped to its opposite when the opposite has more room. |
| align | "start" \| "center" \| "end" | "center" | Cross-axis alignment against the trigger, before collision clamping. |
| offset | number | 10 | Gap in px between trigger and panel, counted as part of the room a side needs. |
| padding | number | 8 | Minimum px kept between the panel and the edge of the collision boundary. |
| arrowSize | number | 9 | Edge length of the arrow square. Its centre sits on the panel border and tracks the trigger. |
| boundary | React.RefObject<HTMLElement \| null> | viewport | Element the panel must stay inside. Intersected with the viewport, so both are respected. |
| triggerClassName | string | "" | Appended last to the trigger button. |
| className | string | "" | Appended last to the panel. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
