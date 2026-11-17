# pagination

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/pagination.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/pagination.tsx); SHA-256 `dcd773ba6f3fca544d528649fd835451c3657967b5a790385d2bd952d520af7d`; 272 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| count | number | False | 63 |
| page | number | True | 64 |
| defaultPage | number | True | 65 |
| siblings | number | True | 66 |
| boundaries | number | True | 67 |
| onPageChange | (page: number) => void | True | 68 |
| count | number | False | 124 |
| page | number | True | 125 |
| defaultPage | number | True | 126 |
| siblings | number | True | 127 |
| boundaries | number | True | 128 |
| onPageChange | (page: number) => void | True | 129 |
| label | string | True | 130 |
| className | string | True | 131 |
| flip | boolean | True | 134 |

### Defaults and motion

- Default `defaultPage` = `1` (line 74).
- Default `siblings` = `1` (line 75).
- Default `boundaries` = `1` (line 76).
- Default `flip` = `false` (line 134).
- Default `label` = `"Pagination"` (line 163).
- Default `className` = `""` (line 164).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `duration`: 0.18 (line 9).
- `ease`: computed; inspect expression (line 9).
- `duration`: 0 (line 10).

### Input, style and lifecycle

Events: onClick (line 197); onClick (line 233); onClick (line 260).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The slot count is identical at every page — the near-start, middle and near-end windows all resolve to the same number of cells, so moving from page 4 to page 5 can never change the row's width or shift the arrows under the cursor.
- The active marker is one always-mounted thumb translated between slots, the dropdown's answer rather than a shared-layout animation: it cannot fly in from a stale position, and slots need no measurement because their width is arithmetic.
- When the window slides, only the cells whose number changed remount, and the new number rolls in from the direction the window travelled; unchanged cells do not flicker.
- The arrows at their limits stay in the accessibility tree with aria-disabled and refuse the click in the handler, keeping our colours instead of the UA's disabled grey.
- Page changes are announced once through a status region after the page has held for half a second, so paging through quickly is one sentence, not a stutter of interruptions.
- Under prefers-reduced-motion the thumb and the numbers arrive instantly; nothing is hidden, only the travel is dropped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| count | number | not specified | Total number of pages. The slot geometry is derived from its digit count, so the row is sized for its widest page from the first paint. |
| page | number | not specified | Controlled current page. Supplying it makes the parent the source of truth. |
| defaultPage | number | 1 | Uncontrolled starting page, clamped into range. |
| siblings | number | 1 | Pages shown on each side of the current page once the window is sliding. |
| boundaries | number | 1 | Pages pinned at each end of the row no matter where the window is. |
| onPageChange | (page: number) => void | not specified | Fires with the next page on every move, controlled or not. |
| label | string | "Pagination" | Accessible name for the nav landmark. |
| className | string | "" | Appended last to the nav element, so a caller's spacing wins. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
