# long-press

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/long-press.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/long-press.tsx); SHA-256 `726ce952a7350ed8b479756bbf9f937c1973ed0abba8a1735d830ce345fd8661`; 231 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| onLongPress | () => void | False | 11 |
| duration | number | True | 12 |
| steps | number | True | 13 |
| moveTolerance | number | True | 14 |
| haptic | boolean | True | 15 |
| disabled | boolean | True | 16 |
| onCancel | () => void | True | 17 |
| x | number | False | 39 |
| y | number | False | 39 |
| x | number | False | 67 |
| y | number | False | 67 |
| onLongPress | () => void | False | 164 |
| children | React.ReactNode | False | 165 |
| duration | number | True | 166 |
| steps | number | True | 167 |
| disabled | boolean | True | 168 |
| className | string | True | 169 |

### Defaults and motion

- Default `duration` = `550` (line 24).
- Default `steps` = `12` (line 25).
- Default `moveTolerance` = `8` (line 26).
- Default `haptic` = `true` (line 27).
- Default `disabled` = `false` (line 28).
- Default `duration` = `550` (line 175).
- Default `steps` = `12` (line 176).
- Default `disabled` = `false` (line 177).
- Default `className` = `""` (line 178).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 640 (line 7).
- `damping`: 22 (line 7).
- `mass`: 0.7 (line 7).
- `duration`: 0 (line 8).

### Input, style and lifecycle

Events: blur (line 106); visibilitychange (line 107).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Drifting more than eight pixels cancels the press. On a phone this is the difference between holding a row and scrolling past it, and it is the reason most long-press implementations feel broken on touch.
- The click that follows a completed press is swallowed. Otherwise the element runs its normal tap action immediately after the hold already ran.
- Progress is reported in discrete steps, not as a float, so a 550ms press costs twelve renders instead of thirty-three.
- Losing the window, hiding the tab, a pointercancel from the browser taking over the gesture, or Escape all end the press. A hold that survives you switching apps is not a hold.
- Space and Enter hold too, so the gesture is reachable without a pointer, and the duration is announced through a described-by hint.
- The native touch callout and context menu are suppressed on the target, because on touch platforms they are the default answer to a long press.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| onLongPress | () => void | not specified | Fires once, when the press survives the full duration |
| duration | number | 550 | Milliseconds the press has to survive |
| steps | number | 12 | Cells drawn, and the render budget for the whole gesture |
| moveTolerance | number | 8 | Pixels of drift allowed before it is treated as a scroll (hook only) |
| haptic | boolean | true | Buzz on commit where the platform supports it (hook only) |
| onCancel | () => void | not specified | Fires when a press is abandoned, never after it commits (hook only) |
| disabled | boolean | false | Refuses to start |
| className | string | not specified | Applied to the button |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
