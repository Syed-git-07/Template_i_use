# otp-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/otp-input.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/otp-input.tsx); SHA-256 `63c469181b3e322c48d5b673b7d41ce66d089582d764e0986e17604466b7dc56`; 482 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| length | number | True | 29 |
| mode | OtpMode | True | 30 |
| defaultValue | string | True | 31 |
| disabled | boolean | True | 32 |
| onChange | (value: string) => void | True | 33 |
| onComplete | (value: string) => void | True | 34 |
| ref | (el: HTMLInputElement \| null) => void | False | 38 |
| value | string | False | 39 |
| disabled | boolean | False | 40 |
| type | "text" | False | 41 |
| inputMode | "numeric" \| "text" | False | 42 |
| autoComplete | string | False | 43 |
| autoCorrect | "off" | False | 44 |
| autoCapitalize | "off" | False | 45 |
| spellCheck | false | False | 46 |
| onChange | (e: ChangeEvent<HTMLInputElement>) => void | False | 47 |
| onKeyDown | (e: KeyboardEvent<HTMLInputElement>) => void | False | 48 |
| onPaste | (e: ClipboardEvent<HTMLInputElement>) => void | False | 49 |
| onFocus | (e: FocusEvent<HTMLInputElement>) => void | False | 50 |
| onBlur | (e: FocusEvent<HTMLInputElement>) => void | False | 51 |
| chars | string[] | False | 55 |
| value | string | False | 56 |
| length | number | False | 57 |
| complete | boolean | False | 58 |
| focusedIndex | number | False | 59 |
| getCellProps | (index: number) => OtpCellProps | False | 60 |
| focusAt | (index: number) => void | False | 61 |
| clear | () => void | False | 62 |
| clear | () => void | False | 279 |
| focus | () => void | False | 280 |
| length | number | True | 284 |
| mode | OtpMode | True | 285 |
| defaultValue | string | True | 286 |
| onChange | (value: string) => void | True | 287 |
| onComplete | (value: string) => void | True | 288 |
| status | OtpStatus | True | 289 |
| errorMessage | string | True | 290 |
| successMessage | string | True | 291 |
| hint | string | True | 292 |
| label | string | True | 293 |
| groupEvery | number | True | 294 |
| disabled | boolean | True | 295 |
| autoFocus | boolean | True | 296 |
| focusOnError | boolean | True | 297 |
| className | string | True | 298 |
| ref | React.Ref<OtpInputHandle> | True | 299 |

### Defaults and motion

- Default `length` = `6` (line 66).
- Default `mode` = `"numeric"` (line 67).
- Default `defaultValue` = `""` (line 68).
- Default `disabled` = `false` (line 69).
- Default `length` = `6` (line 303).
- Default `mode` = `"numeric"` (line 304).
- Default `defaultValue` = `""` (line 305).
- Default `status` = `"idle"` (line 308).
- Default `errorMessage` = `""` (line 309).
- Default `successMessage` = `""` (line 310).
- Default `hint` = `""` (line 311).
- Default `label` = `"Verification code"` (line 312).
- Default `groupEvery` = `3` (line 313).
- Default `disabled` = `false` (line 314).
- Default `autoFocus` = `false` (line 315).
- Default `focusOnError` = `true` (line 316).
- Default `className` = `""` (line 317).
- `stiffness`: 260 (line 17).
- `damping`: 34 (line 17).
- `mass`: 0.8 (line 17).
- `duration`: 0 (line 357).
- `duration`: 0.22 (line 357).
- `ease`: computed; inspect expression (line 357).
- `duration`: 0 (line 358).
- `duration`: 0.32 (line 378).
- `ease`: computed; inspect expression (line 378).
- `duration`: 0 (line 442).
- `duration`: 1.06 (line 444).
- `ease`: "linear" (line 447).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- A pasted code fills every cell from one event: paste is intercepted, filtered to the allowed alphabet, and distributed from cell zero whenever the clipboard holds a full-length code, so pasting into the wrong cell is not a failure state.
- Autofilled codes arrive as a single multi-character input event and are distributed the same way, because only the first cell claims autocomplete one-time-code and no cell sets maxLength.
- Rejection never destroys work: the characters stay where they are, focus returns to the first cell with its content selected, and the shake plays once on the false to true edge instead of on every render while the error is up.
- The cell array is the source of truth, so clearing a digit in the middle leaves a hole instead of sliding the digits after it one place left.
- The hint and the error message share one grid cell and only opacity moves, so a wrapped two-line error cannot push the submit button down the page.
- Screen readers get the message once from a polite live region and each cell announces its own position; under prefers-reduced-motion the shake, the sliding focus mark and the character entrance are skipped while the value, the invalid border and the status line still arrive.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| length | number | 6 | Number of cells. The group reserves its full width on first paint. |
| mode | "numeric" \| "alphanumeric" | "numeric" | Which characters survive typing and pasting. Sets inputMode so phones open the right keyboard. |
| defaultValue | string | "" | Seed characters, filtered by mode and truncated to length. The cells own the value after mount. |
| onChange | (value: string) => void | not specified | Fires on every accepted edit, including a paste that fills several cells at once. |
| onComplete | (value: string) => void | not specified | Fires the moment every cell holds a character, and again on each later edit of a full code. |
| error | boolean | false | Marks every cell aria-invalid and shakes the group once on the false to true edge. The characters are kept. |
| errorMessage | string | "" | Shown in the status line and announced once through a polite live region. |
| hint | string | "" | Occupies the same grid cell as the error message, so the two never move each other. |
| label | string | "Verification code" | Names the group and each cell, as "character 3 of 6". |
| disabled | boolean | false | Disables every cell and drops the focus indicator. |
| autoFocus | boolean | false | Focuses the first cell after mount rather than during render. |
| focusOnError | boolean | true | On rejection, returns focus to the first cell with its character selected so retyping overwrites. |
| className | string | "" | Appended last on the outer wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
