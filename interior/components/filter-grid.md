# filter-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/filter-grid.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/filter-grid.tsx); SHA-256 `ee43cd5745df2367ddb9a2dab55f2ce94536a9b362d03d6762aa8e6d396b14c2`; 329 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 21 |
| label | string | False | 22 |
| match | (item: T) => boolean | False | 23 |
| items | readonly T[] | False | 27 |
| filters | readonly FilterDefinition<T>[] | False | 28 |
| value | string | True | 29 |
| defaultValue | string | True | 30 |
| onValueChange | (id: string) => void | True | 31 |
| active | string | False | 35 |
| activeLabel | string | False | 36 |
| select | (id: string) => void | False | 37 |
| visible | T[] | False | 38 |
| counts | Record<string, number> | False | 39 |
| total | number | False | 40 |
| items | readonly T[] | False | 95 |
| filters | readonly FilterDefinition<T>[] | False | 96 |
| getKey | (item: T) => string | False | 97 |
| renderItem | (item: T) => ReactNode | False | 98 |
| label | string | False | 99 |
| value | string | True | 100 |
| defaultValue | string | True | 101 |
| onValueChange | (id: string) => void | True | 102 |
| columns | number | True | 103 |
| rowHeight | number | True | 104 |
| maxRows | number | True | 105 |
| gap | number | True | 106 |
| emptyLabel | string | True | 107 |
| className | string | True | 108 |

### Defaults and motion

- Default `columns` = `3` (line 120).
- Default `rowHeight` = `72` (line 121).
- Default `maxRows` = `4` (line 122).
- Default `gap` = `8` (line 123).
- Default `emptyLabel` = `"Nothing matches this filter"` (line 124).
- Default `className` = `""` (line 125).
- `stiffness`: 520 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.45 (line 14).
- `stiffness`: 260 (line 15).
- `damping`: 34 (line 15).
- `mass`: 0.8 (line 15).
- `duration`: 0.14 (line 17).
- `ease`: computed; inspect expression (line 17).
- `duration`: 0 (line 18).
- `duration`: 0.2 (line 196).
- `ease`: computed; inspect expression (line 196).
- `duration`: 0.2 (line 313).
- `ease`: computed; inspect expression (line 313).

### Input, style and lifecycle

Events: onClick (line 221); onKeyDown (line 222); onExitComplete (line 290).

Typography/style anchors: 297, 312.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The grid reserves the height of the whole unfiltered set before the first paint, so narrowing forty cards to three never drags the content below it up the page; past maxRows the box scrolls rather than growing.
- An item that survives a filter change is never unmounted and remounted — it keeps its element and travels to its new slot on transform, while the items that lost are pulled out of flow by popLayout, so the grid rearranges instead of blinking white between two states.
- Counts are computed per filter over the full set, not the visible one, so a chip's width is the same in every reachable state and the chip row cannot reflow when the selection moves.
- Filters clicked in fast succession interrupt: each card's spring resumes from where it currently sits, and no card replays a trip it had already half finished.
- If focus was inside a card that the new filter removed, it lands on the grid container once the exit settles, never on the document body.
- The count is announced once per settled filter change through a polite region rather than per item, and under prefers-reduced-motion the cards are simply in their new slots — the empty state and the counts still arrive.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | readonly T[] | not specified | The full unfiltered set. Its length fixes the reserved height, so it must not depend on the active filter. |
| filters | readonly FilterDefinition<T>[] | not specified | Each entry is { id, label, match }. Include an "all" entry whose match returns true; the first entry is the fallback when value is unknown. |
| getKey | (item: T) => string | not specified | Stable identity per item. A key that changes between filters turns a move into an unmount and remount. |
| renderItem | (item: T) => ReactNode | not specified | Cell contents only. The component owns the card chrome, the radius and the fixed row height. |
| label | string | not specified | Accessible name for the filter radiogroup. |
| value | string \| undefined | not specified | Active filter id for controlled use. Omit to let the component hold the selection. |
| defaultValue | string \| undefined | filters[0].id | Initial filter id when uncontrolled. |
| onValueChange | ((id: string) => void) \| undefined | not specified | Fires only when the active id actually changes, never on a re-click of the current filter. |
| columns | number | 3 | Fixed column count. A number, not a breakpoint, because the reserved height is derived from it during render. |
| rowHeight | number | 72 | Row height in px. Fixed so the grid's height is known before the first paint and identical on server and client. |
| maxRows | number | 4 | Height cap in rows. Beyond it the grid scrolls internally instead of growing. |
| gap | number | 8 | Gap in px between cells, counted into the reserved height. |
| emptyLabel | string | "Nothing matches this filter" | Shown centred in the reserved space when a filter matches nothing. |
| className | string | "" | Appended last on the outer wrapper. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
