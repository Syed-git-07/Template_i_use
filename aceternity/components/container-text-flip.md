# container-text-flip

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/container-text-flip/components/ui/container-text-flip.tsx

[Original source](https://ui.aceternity.com/registry/container-text-flip.json); SHA-256 `593026cdbc3ae45b0ac3e7a31525b33311e5bb10057538e24209f7cd1e460bad`; 105 lines.

Imports: `react`, `motion/react`, `@/utils/cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| words | string[] | True | 10 |
| interval | number | True | 12 |
| className | string | True | 14 |
| textClassName | string | True | 16 |
| animationDuration | number | True | 18 |

### Defaults and motion

- Default `interval` = `3000` (line 23).
- Default `animationDuration` = `700` (line 26).
- `duration`: computed; inspect expression (line 61).
- `duration`: computed; inspect expression (line 74).
- `ease`: "easeInOut" (line 75).
- `delay`: computed; inspect expression (line 94).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
