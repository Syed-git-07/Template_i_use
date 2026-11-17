# press-depth

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/press-depth.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/press-depth.tsx); SHA-256 `c541742a65bed30f9ae6e085edcd87fa1baf73ff49770fd7fea527f3c999f49e`; 210 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| disabled | boolean | True | 9 |
| onPressStart | () => void | True | 10 |
| onPressEnd | () => void | True | 11 |
| x | number | False | 14 |
| y | number | False | 14 |
| pressed | boolean | False | 17 |
| origin | PressOrigin \| null | False | 18 |
| ref | (node: HTMLElement \| null) => void | False | 19 |
| bind | {     onPointerDown: (event: React.PointerEvent) => void;     onKeyDown: (event: React.KeyboardEvent) => void;     onKeyUp: (event: React.KeyboardEvent) => void;     onBlur: () => void;   } | False | 20 |
| onPointerDown | (event: React.PointerEvent) => void | False | 21 |
| onKeyDown | (event: React.KeyboardEvent) => void | False | 22 |
| onKeyUp | (event: React.KeyboardEvent) => void | False | 23 |
| onBlur | () => void | False | 24 |
| children | React.ReactNode | False | 141 |
| depth | number | True | 142 |
| tilt | number | True | 143 |
| disabled | boolean | True | 144 |
| type | "button" \| "submit" \| "reset" | True | 145 |
| onClick | React.MouseEventHandler<HTMLButtonElement> | True | 146 |
| className | string | True | 147 |
| "aria-label" | string | True | 148 |

### Defaults and motion

- Default `disabled` = `false` (line 31).
- Default `depth` = `4` (line 153).
- Default `tilt` = `7` (line 154).
- Default `disabled` = `false` (line 155).
- Default `type` = `"button"` (line 156).
- Default `className` = `""` (line 158).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `duration`: 0 (line 194).
- `duration`: 0 (line 202).

### Input, style and lifecycle

Events: pointermove (line 89); pointerup (line 90); pointercancel (line 91); blur (line 92); visibilitychange (line 93); onClick (line 173).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The key reserves its travel as bottom padding before the first press, so depressing it moves a transform and never the layout around it.
- Press state is tracked on the window rather than the element, so a pointer that leaves the key mid-hold lifts it, and a pointer that comes back presses it again — the visual state and the browser's own click suppression agree.
- A press that is interrupted by a scroll, a tab switch, a window blur, or a disabled prop arriving mid-hold releases instead of sticking down forever.
- Activation stays with the browser: Enter and Space fire a real click on a real button, so no synthetic handler double-fires and no keyboard path is invented.
- Auto-repeat is ignored, so holding Enter presses once instead of hammering the key sixty times a second.
- Under prefers-reduced-motion the key still lands at full depth, instantly — the confirmation survives, only the spring is dropped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| children | React.ReactNode | not specified | Label content for the key face. |
| depth | number | 2 | Travel in pixels. The wrapper reserves this space as bottom padding before the first press, so the key never changes footprint. |
| disabled | boolean | false | Blocks the gesture and releases any press already in flight. |
| type | "button" \| "submit" \| "reset" | "button" | Forwarded to the underlying button so the key works inside a form. |
| onClick | React.MouseEventHandler<HTMLButtonElement> | not specified | Native click. Activation is left to the browser, so Enter, Space, and release-outside behave exactly as they do on a plain button. |
| className | string | "" | Appended last to the key face, so surface, padding, and type are overridable. |
| aria-label | string | not specified | Accessible name for icon-only keys. |
| usePressDepth(options) | (options?: UsePressDepthOptions) => UsePressDepthResult | not specified | Returns { pressed, ref, bind } for drawing your own surface. Options are disabled, onPressStart, onPressEnd. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
