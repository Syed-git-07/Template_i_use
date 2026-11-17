# copy-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/copy-button.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/copy-button.tsx); SHA-256 `909f649e6c364000a4c2cfa0a602b049d02e5be004632b30847e554cef6cac13`; 253 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| timeout | number | True | 15 |
| onCopy | (value: string) => void | True | 16 |
| onError | (reason: unknown) => void | True | 17 |
| value | string | False | 119 |
| label | string | True | 120 |
| copiedLabel | string | True | 121 |
| errorLabel | string | True | 122 |
| timeout | number | True | 123 |
| onCopy | (value: string) => void | True | 124 |
| onError | (reason: unknown) => void | True | 125 |
| disabled | boolean | True | 126 |
| className | string | True | 127 |

### Defaults and motion

- Default `timeout` = `2000` (line 51).
- Default `label` = `"Copy"` (line 132).
- Default `copiedLabel` = `"Copied"` (line 133).
- Default `errorLabel` = `"Failed"` (line 134).
- Default `timeout` = `2000` (line 135).
- Default `disabled` = `false` (line 138).
- Default `className` = `""` (line 139).
- `stiffness`: 520 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.45 (line 7).
- `stiffness`: 260 (line 8).
- `damping`: 34 (line 8).
- `mass`: 0.8 (line 8).
- `duration`: 0.26 (line 9).
- `ease`: computed; inspect expression (line 9).
- `duration`: 0 (line 10).

### Input, style and lifecycle

Events: onClick (line 158).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, async, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The three labels — rest, success, failure — occupy one grid cell, so the button is sized to its widest reachable state before the first click and neighbours never shift when the tick arrives.
- A second click while the tick is showing restarts the two-second revert instead of stacking a second timer, and every timer is cleared on unmount, so a button removed mid-countdown cannot set state on a dead component.
- The write is attempted through the async clipboard API and falls back to a detached textarea selection, restoring the user's prior selection range afterwards; when both refuse, the button says so rather than showing a tick it did not earn.
- The accessible name is fixed to the resting label and the outcome is announced once through a polite live region, so a screen reader hears "Copied" a single time instead of a renamed control.
- prefers-reduced-motion collapses the crossfade and the tick draw to zero duration: the state still changes, only the trip is skipped, and nothing is hidden.
- Only opacity, scale, transform and stroke length are animated, and no state is written from an animation callback, so a rapid double click interrupts the spring from its current position instead of restarting it.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | string | not specified | The text written to the clipboard. An empty string is a no-op: the button never reports a success it did not perform. |
| label | string | "Copy" | Resting label, and the button's fixed accessible name, so the name never changes under the user mid-interaction. |
| copiedLabel | string | "Copied" | Success label. It shares a grid cell with the other two labels, so its width is reserved before the first click. |
| errorLabel | string | "Failed" | Shown when both the async clipboard and the selection fallback refuse. Failure is stated, not swallowed. |
| timeout | number | 2000 | Milliseconds the tick is held before reverting to rest. Each new copy restarts the clock rather than stacking timers. |
| onCopy | (value: string) => void | not specified | Fires only after the write actually resolves, with the exact string that reached the clipboard. |
| onError | (reason: unknown) => void | not specified | Fires with the rejection when every write path fails, including a denied permission in an insecure context. |
| disabled | boolean | false | Blocks the write and the press transform; the reserved width is unchanged so nothing around it moves. |
| className | string | "" | Appended last, so callers can override any surface class on the button. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
