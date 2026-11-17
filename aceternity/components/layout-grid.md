# layout-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/layout-grid/components/ui/layout-grid.tsx

[Original source](https://ui.aceternity.com/registry/layout-grid.json); SHA-256 `e354ed1870c324a9a665db35809b92cf3306f744c507722f5e67d8ab330448c2`; 113 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | number | False | 7 |
| content | JSX.Element \| React.ReactNode \| string | False | 8 |
| className | string | False | 9 |
| thumbnail | string | False | 10 |
| cards | Card[] | False | 13 |
| card | Card | False | 61 |
| selected | Card \| null | False | 76 |

### Defaults and motion

- `duration`: 0.3 (line 103).
- `ease`: "easeInOut" (line 104).

### Input, style and lifecycle

Events: onClick (line 32); onClick (line 50).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
