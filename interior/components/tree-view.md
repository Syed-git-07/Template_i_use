# tree-view

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/tree-view.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/tree-view.tsx); SHA-256 `91026b1b0c42c2067bb48144de8d7e47142c1149b94fb2399b4c53d58bbe1b31`; 372 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 19 |
| label | string | False | 20 |
| meta | string | True | 22 |
| children | TreeNode[] | True | 23 |
| node | TreeNode | False | 27 |
| level | number | False | 28 |
| parentId | string \| null | False | 29 |
| posinset | number | False | 30 |
| setsize | number | False | 31 |
| branch | boolean | False | 32 |
| open | boolean | False | 33 |
| nodes | TreeNode[] | False | 62 |
| expanded | string[] | True | 63 |
| defaultExpanded | string[] | True | 64 |
| onExpandedChange | (expanded: string[]) => void | True | 65 |
| selected | string \| null | True | 66 |
| defaultSelected | string \| null | True | 67 |
| onSelectedChange | (selected: string) => void | True | 68 |
| open | boolean | False | 214 |
| nodes | TreeNode[] | False | 239 |
| label | string | False | 240 |
| expanded | string[] | True | 241 |
| defaultExpanded | string[] | True | 242 |
| onExpandedChange | (expanded: string[]) => void | True | 243 |
| selected | string \| null | True | 244 |
| defaultSelected | string \| null | True | 245 |
| onSelectedChange | (selected: string) => void | True | 246 |
| className | string | True | 247 |

### Defaults and motion

- Default `defaultSelected` = `null` (line 77).
- Default `className` = `""` (line 259).
- `stiffness`: 700 (line 10).
- `damping`: 46 (line 10).
- `mass`: 0.5 (line 10).
- `duration`: 0.28 (line 12).
- `ease`: computed; inspect expression (line 12).
- `duration`: 0.18 (line 13).
- `ease`: computed; inspect expression (line 13).
- `duration`: 0.2 (line 14).
- `ease`: computed; inspect expression (line 14).
- `duration`: 0.14 (line 15).
- `ease`: computed; inspect expression (line 15).
- `duration`: 0 (line 16).

### Input, style and lifecycle

Events: onFocus (line 293); onKeyDown (line 294); onClick (line 295).

Typography/style anchors: 334, 338.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The keyboard model is the full APG tree pattern, not a subset: arrows walk and fold, Home and End jump, Enter and Space choose, and typing a letter moves to the next visible name that starts with it.
- One tab stop for the whole tree. If the focused row is folded away by an ancestor, the stop falls back to the selection or the first row without stealing the browser's focus from wherever it actually is.
- A closed branch is not rendered and hidden — it is not rendered at all, so assistive technology is never handed rows the eye cannot reach.
- Disclosure runs height and opacity on separate clocks with opacity finishing first, so rows are fully formed before the reflow that reveals them has finished.
- aria-level, aria-setsize and aria-posinset are written from the data on every row, so a screen reader hears 'level 2, item 3 of 5' rather than a flat list.
- Every row reserves the caret's slot whether or not it has one, so labels in one list share one left edge instead of ragging on folder boundaries.
- Under prefers-reduced-motion branches open and close in place; the information arrives, the travel is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| nodes | TreeNode[] | not specified | The tree, root list first. Each node is { id, label, meta?, children? }; id must be stable because it keys expansion, selection and the roving focus. |
| label | string | not specified | Accessible name for the tree. |
| expanded | string[] | not specified | Controlled set of open branch ids. |
| defaultExpanded | string[] | [] | Uncontrolled starting open set. |
| onExpandedChange | (expanded: string[]) => void | not specified | Fires with the next open set on every toggle. |
| selected | string \| null | not specified | Controlled selected id. |
| defaultSelected | string \| null | null | Uncontrolled starting selection. |
| onSelectedChange | (selected: string) => void | not specified | Fires when a row is chosen by click, Enter or Space. |
| className | string | "" | Appended last to the card, so a caller's width and surface win. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
