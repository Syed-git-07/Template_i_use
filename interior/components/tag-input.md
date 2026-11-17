# tag-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/tag-input.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/tag-input.tsx); SHA-256 `8891f34b76bbc20bd615101872f3f040514bf889eb07434074b8e55d7ac8e08e`; 443 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string[] | True | 20 |
| defaultValue | string[] | True | 21 |
| onChange | (tags: string[]) => void | True | 22 |
| max | number | True | 23 |
| separators | string[] | True | 24 |
| allowDuplicates | boolean | True | 25 |
| validate | (candidate: string, tags: string[]) => boolean | True | 26 |
| reason | TagRejection | False | 29 |
| tag | string | False | 29 |
| visible | boolean | False | 29 |
| reason | TagRejection | False | 109 |
| tag | string | False | 109 |
| label | string | True | 252 |
| placeholder | string | True | 253 |
| hint | string | True | 254 |
| className | string | True | 255 |

### Defaults and motion

- Default `allowDuplicates` = `false` (line 37).
- Default `placeholder` = `"Add a tag"` (line 276).
- Default `hint` = `"Enter adds · Backspace removes"` (line 277).
- Default `className` = `""` (line 278).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `stiffness`: 700 (line 8).
- `damping`: 46 (line 8).
- `mass`: 0.5 (line 8).
- `duration`: 0.18 (line 9).
- `ease`: computed; inspect expression (line 9).
- `duration`: 0 (line 10).

### Input, style and lifecycle

Events: onPointerDown (line 321); onMouseDown (line 355); onClick (line 356).

Typography/style anchors: 340, 341.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Backspace on an empty field highlights the last tag before it removes anything, and a held Backspace is dropped until the key is released, so key repeat cannot chain-delete a list a user only meant to trim by one.
- Enter is ignored while an IME composition is open, so confirming a Japanese or Korean candidate commits the word to the field instead of committing a half-typed tag to the list.
- Pasted text is split on the configured separators plus newlines and tabs, so a copied comma list arrives as six tags rather than one tag six words long.
- A refused duplicate lights the tag that already holds the value instead of only printing an error, and the hint and the error share one grid cell, so nothing below the field moves when a message appears.
- The idle and highlighted labels are two layers in the same grid cell, so arming a tag never re-measures it; removals leave on opacity and x while the remaining tags close the gap with layout position, and the row is capped in height and scrolls rather than growing without bound.
- Assistive technology gets one polite announcement per event — added, selected, removed, each with the running count — not a stream, and every path is reachable from the keyboard: arrow keys walk the tags, Delete removes the armed one, Escape only disarms so a surrounding dialog still closes.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | string[] | not specified | Controlled list of tags. Omit to let the component own its state. |
| defaultValue | string[] | [] | Initial list when the component is uncontrolled. |
| onChange | (tags: string[]) => void | not specified | Fires once per committed change, never per keystroke. |
| max | number | not specified | Hard ceiling. Reaching it shows the limit message and reveals a counter whose width is reserved for the largest value. |
| separators | string[] | [","] | Characters that commit the draft on keypress and split pasted text. Enter always commits; newlines and tabs always split. |
| allowDuplicates | boolean | false | When false, a repeat entry is refused and the tag already holding that value is lit instead. |
| validate | (candidate: string, tags: string[]) => boolean | not specified | Runs on the trimmed, whitespace-collapsed candidate before it is added. |
| label | string | not specified | Rendered as a real label bound to the input. Without it the input falls back to aria-label. |
| placeholder | string | "Add a tag" | Placeholder for the draft field. |
| hint | string | "Enter adds · Backspace removes" | Persistent description, referenced by aria-describedby. Rejection messages cross-fade over it in the same grid cell. |
| className | string | "" | Appended last to the wrapper so callers win. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
