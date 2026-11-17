# background-ripple-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-ripple-effect/components/ui/background-ripple-effect.tsx

[Original source](https://ui.aceternity.com/registry/background-ripple-effect.json); SHA-256 `bdb7622e70515843fcb52ec0574fccc19c513c35d60f730968ba8361b2a6d9b2`; 134 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| rows | number | True | 10 |
| cols | number | True | 11 |
| cellSize | number | True | 12 |
| row | number | False | 15 |
| col | number | False | 16 |
| className | string | True | 53 |
| rows | number | False | 54 |
| cols | number | False | 55 |
| cellSize | number | False | 56 |
| borderColor | string | False | 57 |
| fillColor | string | False | 58 |
| clickedCell | { row: number; col: number } \| null | False | 59 |
| row | number | False | 59 |
| col | number | False | 59 |
| onCellClick | (row: number, col: number) => void | True | 60 |
| interactive | boolean | True | 61 |
| ["--delay"] | string | True | 65 |
| ["--duration"] | string | True | 66 |

### Defaults and motion

- Default `rows` = `8` (line 6).
- Default `cols` = `27` (line 7).
- Default `cellSize` = `56` (line 8).
- Default `rows` = `7` (line 71).
- Default `cols` = `30` (line 72).
- Default `cellSize` = `56` (line 73).
- Default `borderColor` = `"#3f3f46"` (line 74).
- Default `fillColor` = `"rgba(14,165,233,0.3)"` (line 75).
- Default `clickedCell` = `null` (line 76).
- Default `interactive` = `true` (line 78).

### Input, style and lifecycle

Events: onCellClick (line 41); onClick (line 125).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
