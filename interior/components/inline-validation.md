# inline-validation

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/inline-validation.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/inline-validation.tsx); SHA-256 `7cfd26aa5cc2aef85f96fc3320de6b7575319bac86a40656c0d6b4bee5ab603b`; 293 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 16 |
| validate | Validator | False | 17 |
| debounce | number | True | 18 |
| status | ValidationStatus | False | 22 |
| error | string \| null | False | 23 |
| message | string | False | 24 |
| touched | boolean | False | 25 |
| commit | () => void | False | 26 |
| reset | () => void | False | 27 |
| fieldProps | {     onBlur: () => void;     "aria-invalid": boolean;   } | False | 28 |
| onBlur | () => void | False | 29 |
| "aria-invalid" | boolean | False | 30 |
| status | ValidationStatus | False | 35 |
| error | string \| null | False | 36 |
| message | string | False | 37 |
| label | string | False | 116 |
| value | string | False | 117 |
| onChange | (value: string) => void | False | 118 |
| validate | Validator | False | 119 |
| hint | string | True | 120 |
| id | string | True | 121 |
| name | string | True | 122 |
| type | "text" \| "email" \| "password" \| "tel" \| "url" \| "search" | True | 123 |
| placeholder | string | True | 124 |
| autoComplete | string | True | 125 |
| inputMode | React.ComponentProps<"input">["inputMode"] | True | 126 |
| debounce | number | True | 127 |
| reserveLines | number | True | 128 |
| disabled | boolean | True | 129 |
| required | boolean | True | 130 |
| className | string | True | 131 |

### Defaults and motion

- Default `debounce` = `400` (line 45).
- Default `type` = `"text"` (line 142).
- Default `debounce` = `400` (line 146).
- Default `reserveLines` = `1` (line 147).
- Default `disabled` = `false` (line 148).
- Default `required` = `false` (line 149).
- Default `className` = `""` (line 150).
- `stiffness`: 260 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.8 (line 6).
- `duration`: 0 (line 7).

### Input, style and lifecycle

Events: onChange (line 202).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The message slot is measured and reserved before anything is wrong, so an error arriving never pushes the next field, the footer or the submit button down the page.
- Validation waits for the first blur; a field you have not finished with is never told it is wrong halfway through the first word.
- After that first blur a value that becomes correct clears the message immediately, while a value that is still wrong waits out the debounce, so the text under the input cannot flicker once per keystroke.
- Hint and error occupy the same grid cell and only opacity and three pixels of travel move between them, so swapping one for the other cannot change the row's width or height.
- A long message clamps inside its reserved lines rather than animating to an unbounded height, so no validator can make the form taller than it declared it would be.
- The announcement lives in one polite region carrying only the settled message, so a screen reader hears the error once instead of on every keypress, and under prefers-reduced-motion the message and the status glyph arrive at full opacity with no travel.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| label | string | not specified | Visible label, wired to the input with htmlFor. |
| value | string | not specified | Controlled value. The field owns no text of its own. |
| onChange | (value: string) => void | not specified | Receives the raw input value on every keystroke. |
| validate | (value: string) => string \| null | not specified | Pure check. Return the message to show, or null when the value is acceptable. |
| hint | string | undefined | Resting help text. Shares one grid cell with the error and crossfades out when the error takes over. |
| debounce | number | 400 | Milliseconds a still-wrong value waits before the message updates. Clearing is never debounced. |
| reserveLines | number | 1 | Lines of message space reserved up front. Longer messages clamp instead of growing the field. |
| type | "text" \| "email" \| "password" \| "tel" \| "url" \| "search" | "text" | Native input type. |
| required | boolean | false | Sets required and aria-required. The message still comes from validate. |
| disabled | boolean | false | Disables the input and dims the whole field. |
| id | string | undefined | Overrides the generated input id. Hint and error ids are always derived from useId, so they are stable across server and client. |
| className | string | "" | Appended last to the field wrapper. |
| useInlineValidation | (opts: { value: string; validate: Validator; debounce?: number }) => UseInlineValidationReturn | not specified | The behaviour without the chrome: status, error, message, touched, commit, reset and fieldProps for your own markup. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
