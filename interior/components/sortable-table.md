# sortable-table

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/sortable-table.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/sortable-table.tsx); SHA-256 `32f32ac9f0e586cee5dc1a681c87462a833ba51e755faca91b89c7b0947774ec`; 436 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| columnId | string | False | 21 |
| direction | SortDirection | False | 21 |
| id | string | False | 24 |
| header | string | False | 25 |
| width | string | True | 26 |
| align | "start" \| "end" | True | 27 |
| numeric | boolean | True | 28 |
| sortable | boolean | True | 29 |
| value | (row: T) => string \| number \| null \| undefined | True | 30 |
| cell | (row: T) => ReactNode | True | 31 |
| id | string | False | 34 |
| row | T | False | 34 |
| index | number | False | 34 |
| rows | T[] | False | 37 |
| getRowId | (row: T) => string | False | 38 |
| getValue | (row: T, columnId: string) => string \| number \| null \| undefined | False | 39 |
| sort | SortState \| null | True | 40 |
| defaultSort | SortState \| null | True | 41 |
| onSortChange | (next: SortState \| null) => void | True | 42 |
| restoreOriginal | boolean | True | 43 |
| rows | T[] | False | 121 |
| columns | SortableColumn<T>[] | False | 122 |
| getRowId | (row: T) => string | False | 123 |
| label | string | False | 124 |
| rowHeight | number | True | 125 |
| maxHeight | number | True | 126 |
| sort | SortState \| null | True | 127 |
| defaultSort | SortState \| null | True | 128 |
| onSortChange | (next: SortState \| null) => void | True | 129 |
| markable | boolean | True | 130 |
| onMarkChange | (id: string \| null) => void | True | 131 |
| getRowLabel | (row: T) => string | True | 132 |
| className | string | True | 133 |

### Defaults and motion

- Default `defaultSort` = `null` (line 51).
- Default `restoreOriginal` = `true` (line 53).
- Default `rowHeight` = `44` (line 141).
- Default `defaultSort` = `null` (line 144).
- Default `markable` = `false` (line 146).
- Default `className` = `""` (line 149).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 700 (line 8).
- `damping`: 46 (line 8).
- `mass`: 0.5 (line 8).
- `duration`: 0.12 (line 12).
- `ease`: computed; inspect expression (line 12).
- `duration`: 0.25 (line 13).
- `ease`: computed; inspect expression (line 13).
- `duration`: 0 (line 285).
- `duration`: 0 (line 342).
- `delay`: computed; inspect expression (line 343).
- `duration`: 0 (line 371).

### Input, style and lifecycle

Events: onClick (line 262); onClick (line 355).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Sorting a table normally teleports every row and the one you were reading is gone; here each row keeps its element and travels to its new index, so it can be followed rather than found again.
- Rows are placed by transform inside a body whose height is reserved from the row count, so a reorder relayouts nothing and the table never grows, shrinks or shifts the columns under the cursor.
- Sort again mid-flight and the springs resume from where the rows currently are instead of restarting from the order they were leaving.
- DOM order always matches visual order, so a screen reader reads the sorted table, and the result is announced once as a single sentence naming the column, the direction and the row count instead of once per row.
- A third activation of the same header restores the order the rows arrived in, a state most tables make unreachable, and sorting is stable on the original index with empty values held last in both directions.
- Comparison runs through a fixed Intl.Collator and no clock or random source is touched during render, so the server and the client agree on the markup; under prefers-reduced-motion the rows are placed instantly and the announcement still fires.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| rows | T[] | not specified | The data, in its original order. That order is preserved and stays reachable. |
| columns | SortableColumn<T>[] | not specified | Column id, header, optional fixed width, alignment, a value accessor used for sorting and a cell renderer used for display. |
| getRowId | (row: T) => string | not specified | Stable identity per row. This is what lets a row keep its element across a reorder instead of being recycled into a different one. |
| label | string | not specified | Accessible name for the table. |
| rowHeight | number | 44 | Fixed row height in pixels. Rows are positioned by transform against this, so the table's height never changes when the order does. |
| maxHeight | number \| undefined | not specified | Caps the body and scrolls inside it. Without it the body is exactly rows.length * rowHeight. |
| sort | SortState \| null \| undefined | not specified | Controlled sort. Pass null for unsorted; omit the prop entirely to let the table own it. |
| defaultSort | SortState \| null | null | Initial sort when uncontrolled. |
| onSortChange | (next: SortState \| null) => void | not specified | Fires on every header activation, including the third click that returns to the original order. |
| markable | boolean | false | Adds a leading follow toggle so one row can be marked and watched across a reorder. |
| onMarkChange | (id: string \| null) => void | not specified | Reports the marked row id, or null when it is cleared. |
| getRowLabel | (row: T) => string | not specified | Accessible name for a row's follow button. Falls back to the first column's value. |
| className | string | "" | Appended last, so any of the container classes can be overridden. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
