# hold-to-confirm

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/hold-to-confirm.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/hold-to-confirm.tsx); SHA-256 `f6f4472954fef985f16a11b9aaec4be59a71b203fd71c2fe4842d637c6ac147a`; 355 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| onConfirm | () => void | False | 18 |
| onAbort | () => void | True | 19 |
| duration | number | True | 20 |
| steps | number | True | 21 |
| releaseRate | number | True | 22 |
| moveTolerance | number | True | 23 |
| haptic | boolean | True | 24 |
| disabled | boolean | True | 25 |
| x | number | False | 46 |
| y | number | False | 46 |
| x | number | False | 69 |
| y | number | False | 69 |
| onConfirm | () => void | False | 196 |
| children | React.ReactNode | False | 197 |
| onAbort | () => void | True | 198 |
| confirmLabel | string | True | 199 |
| duration | number | True | 200 |
| resetAfter | number | True | 201 |
| steps | number | True | 202 |
| releaseRate | number | True | 203 |
| disabled | boolean | True | 204 |
| className | string | True | 205 |
| committed | boolean | False | 317 |
| confirmLabel | string | False | 318 |
| children | React.ReactNode | False | 319 |

### Defaults and motion

- Default `duration` = `1800` (line 31).
- Default `steps` = `20` (line 32).
- Default `releaseRate` = `2.5` (line 33).
- Default `moveTolerance` = `10` (line 34).
- Default `haptic` = `true` (line 35).
- Default `disabled` = `false` (line 36).
- Default `confirmLabel` = `"Confirmed"` (line 212).
- Default `duration` = `1800` (line 213).
- Default `resetAfter` = `1600` (line 214).
- Default `steps` = `20` (line 215).
- Default `releaseRate` = `2.5` (line 216).
- Default `disabled` = `false` (line 217).
- Default `className` = `""` (line 218).
- `stiffness`: 260 (line 12).
- `damping`: 34 (line 12).
- `mass`: 0.8 (line 12).
- `duration`: 0.12 (line 254).
- `ease`: "linear" (line 254).
- `duration`: computed; inspect expression (line 262).
- `ease`: "linear" (line 263).
- `duration`: computed; inspect expression (line 269).
- `ease`: computed; inspect expression (line 270).

### Input, style and lifecycle

Events: blur (line 134); visibilitychange (line 135).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- A click cannot confirm: the click event is prevented at every stage, so a mis-aimed pointer, a double-click on the row underneath, or a stray Enter on a focused button destroys nothing.
- Releasing early does not snap the progress to zero, it drains at a bounded rate, and pressing again resumes from whatever is left rather than restarting the count.
- The label does not change while you hold. A block sweeps across the button and the same text inverts inside it, so the only thing moving is the progress itself, and the button never changes width. Layout never reflows when the state changes.
- Progress arrives as twenty discrete steps rather than a float, so a 1.2 second hold costs twenty renders instead of eighty, and no React state is written per animation frame.
- Losing the window, hiding the tab, dragging past the move tolerance, or blurring the button all release the hold, so a hold can never survive in the background and fire when nobody is watching.
- Screen readers get a static hint naming the required hold time and one polite announcement at commit, never a stream of progress updates, and prefers-reduced-motion removes the springs while leaving the hold itself intact, because the delay is the guard rail and not decoration.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| onConfirm | () => void | not specified | Fires once, only when the hold reaches full duration. A click never reaches it. |
| children | React.ReactNode | not specified | The resting label. It stays the button's accessible name in every state. |
| onAbort | () => void | undefined | Fires the moment a hold is released early, including a stray click. Useful for measuring how often people almost destroyed something. |
| confirmLabel | string | "Confirmed" | Shown after commit and announced once through a polite live region. |
| duration | number | 1800 | Milliseconds of continuous hold required. Also the number spoken in the screen reader hint. |
| resetAfter | number | 1600 | Milliseconds the confirmed state is held before the button returns to rest. Set to 0 to keep it confirmed and reset it yourself. |
| steps | number | 20 | Render budget for the hold. Progress is sampled this many times, and the sweep runs as one continuous animation independent of them. |
| releaseRate | number | 2.5 | How many times faster progress drains than it fills when you let go. Re-pressing mid-drain resumes from what is left. |
| disabled | boolean | false | Marked with aria-disabled rather than the disabled attribute, so focus is never dropped to the body mid-hold. |
| className | string | "" | Appended last, so the button's surface, radius and width are overridable from outside. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
