# wavy-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/wavy-background/components/ui/wavy-background.tsx

[Original source](https://ui.aceternity.com/registry/wavy-background.json); SHA-256 `76b9dcfa2143c9d80c3e0c9d7f09c1dd5e3319be9e941d9192b28e0b78b2ea26`; 133 lines.

Imports: `@/lib/utils`, `react`, `simplex-noise`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | any | True | 18 |
| className | string | True | 19 |
| containerClassName | string | True | 20 |
| colors | string[] | True | 21 |
| waveWidth | number | True | 22 |
| backgroundFill | string | True | 23 |
| blur | number | True | 24 |
| speed | "slow" \| "fast" | True | 25 |
| waveOpacity | number | True | 26 |

### Defaults and motion

- Default `blur` = `10` (line 13).
- Default `speed` = `"fast"` (line 14).
- Default `waveOpacity` = `0.5` (line 15).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
