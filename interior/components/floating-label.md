# floating-label

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/floating-label.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/floating-label.tsx); SHA-256 `ae6db66c15a14ecf9a9b606d17bbc30c4e576f2f7f332f3c65f9bb40d98f15c4`; 283 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | True | 25 |
| defaultValue | string | True | 26 |
| disabled | boolean | True | 27 |
| ref | React.RefObject<HTMLInputElement \| null> | False | 31 |
| raised | boolean | False | 32 |
| focused | boolean | False | 33 |
| filled | boolean | False | 34 |
| length | number | False | 35 |
| instant | boolean | False | 36 |
| fieldProps | {     onFocus: () => void;     onBlur: () => void;     onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;   } | False | 37 |
| onFocus | () => void | False | 38 |
| onBlur | () => void | False | 39 |
| onChange | (event: React.ChangeEvent<HTMLInputElement>) => void | False | 40 |
| length | number | False | 44 |
| instant | boolean | False | 44 |
| label | string | False | 113 |
| value | string | True | 114 |
| defaultValue | string | True | 115 |
| onChange | (value: string, event: React.ChangeEvent<HTMLInputElement>) => void | True | 116 |
| onFocus | () => void | True | 117 |
| onBlur | () => void | True | 118 |
| hint | string | True | 119 |
| invalid | boolean | True | 120 |
| id | string | True | 121 |
| name | string | True | 122 |
| type | "text" \| "email" \| "password" \| "search" \| "tel" \| "url" | True | 123 |
| autoComplete | string | True | 124 |
| inputMode | React.ComponentProps<"input">["inputMode"] | True | 125 |
| maxLength | number | True | 126 |
| required | boolean | True | 127 |
| disabled | boolean | True | 128 |
| readOnly | boolean | True | 129 |
| inputRef | React.Ref<HTMLInputElement> | True | 130 |
| className | string | True | 131 |

### Defaults and motion

- Default `disabled` = `false` (line 49).
- Default `invalid` = `false` (line 142).
- Default `type` = `"text"` (line 145).
- Default `required` = `false` (line 149).
- Default `disabled` = `false` (line 150).
- Default `readOnly` = `false` (line 151).
- Default `className` = `""` (line 153).
- `duration`: 0 (line 13).
- `stiffness`: 760 (line 15).
- `damping`: 46 (line 15).
- `mass`: 0.5 (line 15).

### Input, style and lifecycle

Events: input (line 81); change (line 82); onFocus (line 205); onBlur (line 209); onChange (line 213).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The label makes room instead of disappearing: the field reserves the raised row and the hint row at mount, so it stands 52px tall in every reachable state and a counter, an error color or a hint arriving on blur cannot push the submit button down the page.
- The label travels on transform only — y and scale, origin pinned to its left edge — so raising it costs no layout and the spring resumes from wherever the label currently is when you refocus a field you were leaving.
- A value the browser restores on back-navigation, or one a password manager writes without a React change event, still raises the label: the field reads its own node on mount and listens for native input and change, so text is never printed underneath the label.
- The mount-time raise is applied with zero duration, so a field that arrives pre-filled from the server presents its label already raised rather than animating on page load.
- Under prefers-reduced-motion the label still occupies the raised slot and the hint still changes; only the trip is skipped, and nothing is hidden.
- Screen readers get the hint once through aria-describedby and never hear the character counter, which is aria-hidden — the native maxLength attribute carries that information instead of sixty live-region updates.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| label | string | not specified | The field's name. It moves into a reserved slot above the text; it is never swapped out for a placeholder. |
| value | string | not specified | Controlled value. Omit for an uncontrolled field and the label still tracks the DOM node. |
| defaultValue | string | not specified | Uncontrolled starting value. Counted on the first render, so a pre-filled field never animates its label on load. |
| onChange | (value: string, event: React.ChangeEvent<HTMLInputElement>) => void | not specified | Receives the value first so `onChange={setEmail}` is the whole handler. |
| hint | string | not specified | Secondary line under the field. Read once by screen readers through aria-describedby, not re-announced per keystroke. |
| invalid | boolean | false | Recolors the border and the label and sets aria-invalid. The message itself stays the caller's job. |
| maxLength | number | not specified | Enables the counter. Its width is reserved at the largest string it can ever show, so digits rolling over never nudge the row. |
| required | boolean | false | Sets the native constraint and marks the label. The asterisk is aria-hidden because the input already announces required. |
| disabled | boolean | false | Dims the field and drops focus state, so a field disabled mid-focus does not keep a lit border. |
| readOnly | boolean | false | Keeps the field focusable and the label raised while refusing edits. |
| type | "text" \| "email" \| "password" \| "search" \| "tel" \| "url" | "text" | Single-line types only; the geometry is built around one 17px line. |
| inputRef | React.Ref<HTMLInputElement> | not specified | Merged with the internal ref, so form libraries can focus or scroll to the field. |
| className | string | "" | Appended last on the wrapper. Width and margins are yours. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
