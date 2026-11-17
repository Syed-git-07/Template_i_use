# loading-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/loading-button.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/loading-button.tsx); SHA-256 `204ea287294cb28de76c0a7fce5c83b5de9d798b9d8994439c075c662da5a22c`; 284 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| action | () => unknown | False | 13 |
| resetAfter | number | True | 14 |
| onError | (error: unknown) => void | True | 15 |
| still | boolean | False | 99 |
| onAction | () => unknown | False | 169 |
| children | string | False | 170 |
| pendingLabel | string | True | 171 |
| successLabel | string | True | 172 |
| errorLabel | string | True | 173 |
| resetAfter | number | True | 174 |
| disabled | boolean | True | 175 |
| onError | (error: unknown) => void | True | 176 |
| className | string | True | 177 |

### Defaults and motion

- Default `resetAfter` = `1400` (line 20).
- Default `successLabel` = `"Done"` (line 184).
- Default `errorLabel` = `"Try again"` (line 185).
- Default `resetAfter` = `1400` (line 186).
- Default `disabled` = `false` (line 187).
- Default `className` = `""` (line 189).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0 (line 8).
- `duration`: 0.85 (line 110).
- `ease`: "linear" (line 110).

### Input, style and lifecycle

Events: onClick (line 248).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, async, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- All four labels are rendered into a single grid cell, so the widest one reserves the button's width before the first click; "Publish" becoming "Publishing…" cannot grow the button or shove the controls beside it.
- The button is never given the native disabled attribute while a request is in flight — it carries aria-busy and aria-disabled instead — so a keyboard user's focus is not dropped onto the body the moment they press Enter.
- A second click during flight is ignored, and every run carries an id, so a slow first response can never overwrite the result of the run that replaced it.
- Pending is indeterminate, because the button does not know how long the request will take. A meter filling against a guessed duration claims progress it cannot know, so the wait is shown as a wait.
- The rAF loop and the reset timer are cancelled on unmount and every settlement checks an alive flag, so a promise resolving after navigation sets no state.
- Under prefers-reduced-motion the meter's rAF never starts and the state lands instantly; the label still changes and a polite status region announces success or failure exactly once, not on every tick.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| onAction | () => unknown | not specified | Runs on click. Sync throws and rejected promises both settle the button into its error state; anything else settles it into success. |
| children | string | — | The idle label. A string rather than a node because it also becomes the button's accessible name. |
| pendingLabel | string | children | Label while the action is in flight. Defaults to the idle label so the button can stay silent and let the meter speak. |
| successLabel | string | "Done" | Label after the action resolves, shown with a check mark. |
| errorLabel | string | "Try again" | Label after the action rejects, shown with an alert mark. Make it the next action, not the diagnosis. |
| resetAfter | number | 1400 | Milliseconds the settled state is held before returning to idle. |
| disabled | boolean | false | Genuinely unavailable, as opposed to busy. Only this sets the native disabled attribute. |
| onError | (error: unknown) => void | not specified | Receives the rejection value. The button reports the state; reporting the error is the caller's job. |
| className | string | "" | Appended last, so callers can override the surface, radius or type scale. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
