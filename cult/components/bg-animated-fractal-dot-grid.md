# bg-animated-fractal-dot-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/bg-animated-fractal-dot-grid.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/bg-animated-fractal-dot-grid.tsx); SHA-256 `0e5da98d0098687363196cc3aeffa302a22949fbcd2e53657e9523d3ddecc9c4`; 388 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| dotSize | number | True | 8 |
| dotSpacing | number | True | 10 |
| dotOpacity | number | True | 12 |
| waveIntensity | number | True | 14 |
| waveRadius | number | True | 16 |
| dotColor | string | True | 18 |
| glowColor | string | True | 20 |
| enableNoise | boolean | True | 22 |
| noiseOpacity | number | True | 24 |
| enableMouseGlow | boolean | True | 26 |
| initialPerformance | "low" \| "medium" \| "high" | True | 28 |
| opacity | number | False | 47 |
| dotSize | number | False | 121 |
| dotSpacing | number | False | 122 |
| dotOpacity | number | False | 123 |
| waveIntensity | number | False | 124 |
| waveRadius | number | False | 125 |
| dotColor | string | False | 126 |
| glowColor | string | False | 127 |
| performance | "low" \| "medium" \| "high" | False | 128 |
| mousePos | { x: number; y: number } | False | 129 |
| x | number | False | 129 |
| y | number | False | 129 |
| glowColor | string | False | 273 |
| mousePos | { x: number; y: number } | False | 274 |
| x | number | False | 274 |
| y | number | False | 274 |

### Defaults and motion

- Default `dotSize` = `4` (line 308).
- Default `dotSpacing` = `20` (line 309).
- Default `dotOpacity` = `0.3` (line 310).
- Default `waveIntensity` = `30` (line 311).
- Default `waveRadius` = `200` (line 312).
- Default `dotColor` = `"rgba(100, 100, 255, 1)"` (line 313).
- Default `glowColor` = `"rgba(100, 100, 255, 1)"` (line 314).
- Default `enableNoise` = `true` (line 315).
- Default `noiseOpacity` = `0.03` (line 316).
- Default `enableMouseGlow` = `true` (line 317).
- Default `initialPerformance` = `"medium"` (line 318).
- `duration`: 1.5 (line 364).
- `ease`: "easeOut" (line 364).

### Input, style and lifecycle

Events: resize (line 70); resize (line 239); mousemove (line 340).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
