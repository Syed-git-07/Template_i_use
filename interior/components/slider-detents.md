# slider-detents

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/slider-detents.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/slider-detents.tsx); SHA-256 `511da120af711ea229a128a7d2ac64a5637bb60d3139e4b4bae6c3cde170b39f`; 397 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | number | False | 29 |
| label | string | True | 29 |
| value | number | False | 34 |
| onValueChange | (value: number) => void | False | 35 |
| min | number | True | 36 |
| max | number | True | 37 |
| step | number | True | 38 |
| detents | readonly (number \| SliderDetent)[] | True | 39 |
| pull | number | True | 40 |
| thumbSize | number | True | 41 |
| disabled | boolean | True | 42 |
| haptic | boolean | True | 43 |
| format | (value: number) => string | True | 44 |
| label | string | True | 45 |
| labelledBy | string | True | 46 |
| value | number | False | 225 |
| onValueChange | (value: number) => void | False | 226 |
| min | number | True | 227 |
| max | number | True | 228 |
| step | number | True | 229 |
| detents | readonly (number \| SliderDetent)[] | True | 230 |
| pull | number | True | 231 |
| label | string | True | 232 |
| format | (value: number) => string | True | 233 |
| disabled | boolean | True | 234 |
| haptic | boolean | True | 235 |
| className | string | True | 236 |

### Defaults and motion

- Default `min` = `0` (line 52).
- Default `max` = `100` (line 53).
- Default `step` = `1` (line 54).
- Default `disabled` = `false` (line 58).
- Default `haptic` = `true` (line 59).
- Default `min` = `0` (line 242).
- Default `max` = `100` (line 243).
- Default `step` = `1` (line 244).
- Default `label` = `"Value"` (line 247).
- Default `disabled` = `false` (line 249).
- Default `haptic` = `true` (line 250).
- Default `className` = `""` (line 251).
- `stiffness`: 520 (line 11).
- `damping`: 34 (line 11).
- `mass`: 0.45 (line 11).
- `stiffness`: 700 (line 13).
- `damping`: 46 (line 13).
- `mass`: 0.5 (line 13).
- `stiffness`: 260 (line 16).
- `damping`: 34 (line 17).
- `mass`: 0.8 (line 18).
- `duration`: 0 (line 20).

### Input, style and lifecycle

Events: blur (line 148).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- A continuous slider cannot be landed on the one value that matters, so within the pull radius the pointer hands the value to the detent and the thumb springs ahead of the finger to show it happened.
- A sticky detent that also swallows the keyboard would make 0.95 unreachable, so arrow keys move by exactly one step and ignore capture entirely; Shift with an arrow, PageUp and PageDown jump detent to detent.
- The readout never reflows: the widest reachable string — every formatted bound and every detent label — is measured into the same grid cell up front, so the number holds still while the label beside it crossfades in.
- The gesture reports discrete values, so React re-renders once per step instead of once per frame; the thumb, the fill and the tick marks are one spring writing transforms, and the fill is a clipped translate rather than an animated width.
- Position is expressed as a percentage translate inside a thumb-inset track, so there is no measurement pass, no zero-width first paint and no jump on hydration.
- Screen readers get one aria-valuetext per committed step — the formatted value plus the detent name when it is parked on one — and the visible readout is aria-hidden so the value is never announced twice.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | number | not specified | Controlled value. Always one of the step grid or a detent, never a raw pointer float. |
| onValueChange | (value: number) => void | not specified | Fires only when the resolved value actually changes, so dragging across one step emits once. |
| min | number | 0 | Lower bound. Reported as aria-valuemin. |
| max | number | 100 | Upper bound. Reported as aria-valuemax. |
| step | number | 1 | The free grid between detents. Arrow keys move by exactly this, ignoring capture. |
| detents | readonly (number \| SliderDetent)[] | [] | The values worth stopping on. A bare number draws a mark; { value, label } also names it in the readout and in aria-valuetext. |
| pull | number | (max - min) * 0.045 | Capture radius in value units. Inside it the pointer hands the value to the detent. |
| label | string | "Value" | Visible label, wired to the slider with aria-labelledby via useId. |
| format | (value: number) => string | String | Formats the readout and the spoken value. Also sizes the readout cell up front. |
| disabled | boolean | false | Sets aria-disabled and refuses pointer and key input without removing the control from the page. |
| haptic | boolean | true | Fires navigator.vibrate on detent capture where supported, once per crossing. |
| className | string | "" | Appended last on the wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
