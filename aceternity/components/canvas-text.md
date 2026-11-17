# canvas-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/canvas-text/components/ui/canvas-text.tsx

[Original source](https://ui.aceternity.com/registry/canvas-text.json); SHA-256 `cd60ebbddf3b08596c692f34eb5a7db35f65dd84bb1e7cdceebe1a40e693f6f1`; 216 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 6 |
| className | string | True | 7 |
| backgroundClassName | string | True | 8 |
| colors | string[] | True | 9 |
| animationDuration | number | True | 10 |
| lineWidth | number | True | 11 |
| lineGap | number | True | 12 |
| curveIntensity | number | True | 13 |
| overlay | boolean | True | 14 |

### Defaults and motion

- Default `className` = `""` (line 30).
- Default `backgroundClassName` = `"bg-white dark:bg-neutral-950"` (line 31).
- Default `animationDuration` = `5` (line 33).
- Default `lineWidth` = `1.5` (line 34).
- Default `lineGap` = `10` (line 35).
- Default `curveIntensity` = `60` (line 36).
- Default `overlay` = `false` (line 37).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 82.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
