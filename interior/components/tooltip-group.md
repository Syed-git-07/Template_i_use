# tooltip-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/tooltip-group.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/tooltip-group.tsx); SHA-256 `92c6dea9ac216942529ad67992ecef7bd2794ca9b8aa865fbc1cdab052744f16`; 527 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| openDelay | number | False | 32 |
| closeDelay | number | False | 33 |
| skipDelay | number | False | 34 |
| seat | string | False | 40 |
| subscribe | (fn: () => void) => () => void | False | 41 |
| getActive | () => string \| null | False | 42 |
| getWarm | () => boolean | False | 43 |
| getSkipped | () => boolean | False | 44 |
| getTravel | () => number | False | 45 |
| open | (id: string, immediate: boolean, x?: number) => void | False | 46 |
| close | (id: string, immediate: boolean) => void | False | 47 |
| dismiss | (id: string) => void | False | 48 |
| unblock | (id: string) => void | False | 49 |
| reset | () => void | False | 50 |
| dispose | () => void | False | 51 |
| children | React.ReactNode | False | 216 |
| openDelay | number | True | 217 |
| closeDelay | number | True | 218 |
| skipDelay | number | True | 219 |
| onWarmChange | (warm: boolean) => void | True | 220 |
| className | string | True | 221 |
| disabled | boolean | True | 265 |
| openDelay | number | True | 266 |
| closeDelay | number | True | 267 |
| skipDelay | number | True | 268 |
| onPointerEnter | (event: React.PointerEvent<HTMLElement>) => void | False | 272 |
| onPointerLeave | (event: React.PointerEvent<HTMLElement>) => void | False | 273 |
| onPointerDown | (event: React.PointerEvent<HTMLElement>) => void | False | 274 |
| onPointerCancel | (event: React.PointerEvent<HTMLElement>) => void | False | 275 |
| onFocus | (event: React.FocusEvent<HTMLElement>) => void | False | 276 |
| onBlur | (event: React.FocusEvent<HTMLElement>) => void | False | 277 |
| onKeyDown | (event: React.KeyboardEvent<HTMLElement>) => void | False | 278 |
| open | boolean | False | 282 |
| warm | boolean | False | 283 |
| skipped | boolean | False | 284 |
| travel | number | False | 285 |
| tooltipId | string | False | 286 |
| seat | string | False | 288 |
| triggerProps | TooltipTriggerProps | False | 289 |
| "aria-describedby" | string | True | 384 |
| label | React.ReactNode | False | 388 |
| children | TriggerChild | False | 389 |
| side | "top" \| "bottom" | True | 390 |
| className | string | True | 391 |
| contentClassName | string | True | 392 |

### Defaults and motion

- Default `openDelay` = `200` (line 226).
- Default `closeDelay` = `120` (line 227).
- Default `skipDelay` = `400` (line 228).
- Default `className` = `""` (line 230).
- Default `disabled` = `false` (line 301).
- Default `openDelay` = `200` (line 302).
- Default `closeDelay` = `120` (line 303).
- Default `skipDelay` = `400` (line 304).
- Default `side` = `"top"` (line 408).
- Default `disabled` = `false` (line 409).
- Default `className` = `""` (line 413).
- Default `contentClassName` = `""` (line 414).
- `stiffness`: 560 (line 16).
- `damping`: 34 (line 16).
- `mass`: 0.6 (line 16).
- `stiffness`: 900 (line 18).
- `damping`: 48 (line 18).
- `mass`: 0.5 (line 18).
- `stiffness`: 520 (line 20).
- `damping`: 40 (line 20).
- `mass`: 0.75 (line 20).
- `stiffness`: 700 (line 22).
- `damping`: 44 (line 22).
- `mass`: 0.5 (line 22).
- `duration`: 0 (line 482).
- `duration`: 0.12 (line 488).
- `ease`: computed; inspect expression (line 488).
- `duration`: 0 (line 493).
- `duration`: 0 (line 502).
- `duration`: 0 (line 515).

### Input, style and lifecycle

Events: blur (line 206); visibilitychange (line 207).

Typography/style anchors: 482, 488.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The delay is charged once per visit, not once per trigger: after the first tooltip opens, every sibling in the group opens on contact until the pointer has been away for skipDelay, so a toolbar sweep stops feeling like five separate waits.
- Two tooltips can never be on screen at once; the group holds a single active id, so an outgoing close timer and an incoming open cannot overlap into a double reading.
- The tooltip is absolutely positioned against its trigger and mounts outside the flow, so opening one moves nothing — the toolbar keeps its width and the row below keeps its baseline.
- Crossing the gap between two triggers costs nothing: closeDelay holds the old tooltip while the next pointerenter cancels the close, which is what stops the flicker on a 2px seam.
- Focus opens the tooltip only when the browser reports :focus-visible, so clicking a button does not leave a tooltip parked over the thing you just clicked, and Escape dismisses it and blocks that trigger until the pointer actually leaves.
- aria-describedby is attached only while the tooltip is mounted, so a screen reader reads the label once on focus rather than on every pointer pass, and reduced motion keeps the tooltip and drops only the blur and the travel.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| TooltipGroup.children | React.ReactNode | not specified | The triggers that share one delay. Any depth of nesting works; the group is a context, not a layout. |
| TooltipGroup.openDelay | number | 200 | Milliseconds a cold pointer must rest on a trigger before its tooltip opens. |
| TooltipGroup.closeDelay | number | 120 | Grace period after the pointer leaves, so crossing a 2px gap between two triggers does not blink. |
| TooltipGroup.skipDelay | number | 400 | How long the group stays warm after the last tooltip closes. While warm, openDelay is zero. |
| TooltipGroup.onWarmChange | (warm: boolean) => void | not specified | Fires once per transition between cold and warm. Never fires per frame. |
| TooltipGroup.className | string | not specified | When set, the group renders one wrapper div with these classes. When omitted it renders no element at all. |
| Tooltip.label | React.ReactNode | not specified | The tooltip body. Wraps at 220px rather than running off the viewport. |
| Tooltip.children | React.ReactElement | not specified | A single focusable element. Its own handlers are called before the tooltip's, never replaced. |
| Tooltip.side | "top" \| "bottom" | "top" | Which edge the tooltip leaves from. transformOrigin and the 4px entry offset follow it. |
| Tooltip.disabled | boolean | false | Suppresses opening and closes an already-open tooltip on the next commit. |
| Tooltip.openDelay | number | 200 | Used only when the Tooltip sits outside a TooltipGroup, where it keeps a private store. |
| Tooltip.closeDelay | number | 120 | Ungrouped fallback timing, matching the group default. |
| Tooltip.skipDelay | number | 400 | Ungrouped fallback timing, matching the group default. |
| Tooltip.className | string | not specified | Applied to the relative wrapper span, appended last. |
| Tooltip.contentClassName | string | not specified | Applied to the tooltip surface, appended last. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
