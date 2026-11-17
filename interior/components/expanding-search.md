# expanding-search

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/expanding-search.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/expanding-search.tsx); SHA-256 `b611f91f566307bb15d12466e29a42945bb7d22fb78f1c4fe7d61e6cc90730a3`; 422 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | True | 28 |
| defaultValue | string | True | 29 |
| onChange | (value: string) => void | True | 30 |
| onSearch | (value: string) => void | True | 31 |
| onSubmit | (value: string) => void | True | 32 |
| open | boolean | True | 33 |
| defaultOpen | boolean | True | 34 |
| onOpenChange | (open: boolean) => void | True | 35 |
| debounce | number | True | 36 |
| collapseOnBlur | boolean | True | 37 |
| disabled | boolean | True | 38 |
| open | boolean | False | 42 |
| focused | boolean | False | 43 |
| query | string | False | 44 |
| expand | () => void | False | 45 |
| collapse | (returnFocus?: boolean) => void | False | 46 |
| toggle | () => void | False | 47 |
| clear | () => void | False | 48 |
| inputRef | React.RefObject<HTMLInputElement \| null> | False | 49 |
| triggerRef | React.RefObject<HTMLButtonElement \| null> | False | 50 |
| rootProps | {     onFocus: (event: React.FocusEvent<HTMLElement>) => void;     onBlur: (event: React.FocusEvent<HTMLElement>) => void;   } | False | 51 |
| onFocus | (event: React.FocusEvent<HTMLElement>) => void | False | 52 |
| onBlur | (event: React.FocusEvent<HTMLElement>) => void | False | 53 |
| triggerProps | {     ref: React.RefObject<HTMLButtonElement \| null>;     type: "button";     disabled: boolean;     tabIndex: number;     "aria-expanded": boolean;     onClick: () => void;   } | False | 55 |
| ref | React.RefObject<HTMLButtonElement \| null> | False | 56 |
| type | "button" | False | 57 |
| disabled | boolean | False | 58 |
| tabIndex | number | False | 59 |
| "aria-expanded" | boolean | False | 60 |
| onClick | () => void | False | 61 |
| inputProps | {     ref: React.RefObject<HTMLInputElement \| null>;     value: string;     disabled: boolean;     tabIndex: number;     onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;     onKeyDown: (event: React.KeyboardEvent<HTMLInputElement>) => void;     onFocus: () => void;   } | False | 63 |
| ref | React.RefObject<HTMLInputElement \| null> | False | 64 |
| value | string | False | 65 |
| disabled | boolean | False | 66 |
| tabIndex | number | False | 67 |
| onChange | (event: React.ChangeEvent<HTMLInputElement>) => void | False | 68 |
| onKeyDown | (event: React.KeyboardEvent<HTMLInputElement>) => void | False | 69 |
| onFocus | () => void | False | 70 |
| label | string | True | 239 |
| placeholder | string | True | 240 |
| resultCount | number | True | 241 |
| align | "left" \| "right" | True | 242 |
| className | string | True | 243 |

### Defaults and motion

- Default `defaultValue` = `""` (line 76).
- Default `defaultOpen` = `false` (line 81).
- Default `debounce` = `220` (line 83).
- Default `collapseOnBlur` = `true` (line 84).
- Default `disabled` = `false` (line 85).
- Default `label` = `"Search"` (line 247).
- Default `placeholder` = `"Search"` (line 248).
- Default `align` = `"right"` (line 250).
- Default `className` = `""` (line 251).
- `stiffness`: 380 (line 13).
- `damping`: 38 (line 13).
- `mass`: 0.7 (line 13).
- `stiffness`: 260 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.8 (line 14).
- `stiffness`: 520 (line 15).
- `damping`: 34 (line 15).
- `mass`: 0.45 (line 15).
- `duration`: 0 (line 16).
- `delay`: computed; inspect expression (line 346).

### Input, style and lifecycle

Events: onMouseDown (line 319); onClick (line 368).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The track reserves the expanded width before anything opens, so the row beside the field never reflows; neighbouring actions fade where they stand instead of being shoved sideways.
- Focus moves to the input synchronously inside the click handler rather than on animation-complete, so the iOS keyboard is not suppressed and a screen reader is never left pointing at a trigger that has already gone.
- Blur collapses the field only when it is empty, and a blur caused by switching browser tabs is ignored, so a typed query is never destroyed by clicking somewhere else.
- Escape clears a non-empty query and collapses an empty one, returning focus to the trigger instead of the document body, and the event is consumed so a dialog behind the field does not close along with it.
- Keystrokes are debounced before onSearch fires and Enter flushes the pending call, so the search runs once per intent; the polite live region announces only the settled result count, not one message per character.
- The input holds its expanded width at all times and is clipped by the shell, so the text inside never re-wraps mid-spring, and prefers-reduced-motion drops the transitions to zero without hiding either state.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| label | string | "Search" | Accessible name shared by the collapsed trigger and the input, so both read the same in the a11y tree. |
| placeholder | string | "Search" | Placeholder text; it is clipped by the shell while collapsed rather than being unmounted. |
| resultCount | number | not specified | When supplied, reserves a fixed tabular slot in the field and feeds the debounced live region. Omit it and the slot is never allocated. |
| align | "left" \| "right" | "right" | Which edge of the reserved track the field is anchored to. Right-anchored fields open leftward over the toolbar actions. |
| value | string | not specified | Controlled query. Leave undefined to let the component own it. |
| defaultValue | string | "" | Initial query when uncontrolled. A literal, so remounting resets the field. |
| onChange | (value: string) => void | not specified | Fires on every keystroke. Use it to mirror state, not to run the search. |
| onSearch | (value: string) => void | not specified | Fires once the typing settles, and immediately on Enter. This is the one to hang a query off. |
| onSubmit | (value: string) => void | not specified | Enter. The pending debounce is flushed first so onSearch never arrives after it. |
| debounce | number | 220 | Milliseconds of quiet before onSearch fires. |
| open | boolean | not specified | Controlled expansion. Focus handling still runs; only the state lives outside. |
| defaultOpen | boolean | false | Start expanded, for a page whose primary action is searching. |
| onOpenChange | (open: boolean) => void | not specified | Called once per real transition, never twice for the same expand. |
| collapseOnBlur | boolean | true | Collapse when focus leaves and the query is empty. A non-empty query is never collapsed away. |
| disabled | boolean | false | Blocks expansion and the input, and keeps the trigger out of the tab order's reach. |
| className | string | "" | Appended last to the reserved track, so width and position are overridable from outside. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
