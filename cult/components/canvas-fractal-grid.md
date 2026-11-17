# canvas-fractal-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/canvas-fractal-grid.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/canvas-fractal-grid.tsx); SHA-256 `725b7f68f5c7a54d0af3bd3ba146c9c915a84b82d8860c7881974afca05e21a6`; 1376 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| color | string | False | 7 |
| position | number | False | 8 |
| stops | GradientStop[] | False | 12 |
| centerX | number | False | 13 |
| centerY | number | False | 14 |
| dotSize | number | True | 19 |
| dotSpacing | number | True | 21 |
| dotOpacity | number | True | 23 |
| gradientAnimationDuration | number | True | 25 |
| mouseTrackingStiffness | number | True | 27 |
| mouseTrackingDamping | number | True | 29 |
| waveIntensity | number | True | 31 |
| waveRadius | number | True | 33 |
| gradients | GradientType[] | True | 35 |
| dotColor | string | True | 37 |
| glowColor | string | True | 39 |
| enableNoise | boolean | True | 41 |
| noiseOpacity | number | True | 43 |
| enableMouseGlow | boolean | True | 45 |
| initialPerformance | "low" \| "medium" \| "high" | True | 47 |
| enableGradient | boolean | True | 49 |
| opacity | number | False | 68 |
| gradients | GradientType[] | False | 149 |
| animationDuration | number | False | 150 |
| dotSize | number | False | 179 |
| dotSpacing | number | False | 180 |
| dotOpacity | number | False | 181 |
| waveIntensity | number | False | 182 |
| waveRadius | number | False | 183 |
| dotColor | string | False | 184 |
| glowColor | string | False | 185 |
| performance | "low" \| "medium" \| "high" | False | 186 |
| mousePos | { x: number; y: number } | False | 187 |
| x | number | False | 187 |
| y | number | False | 187 |
| glowColor | string | False | 333 |
| mousePos | { x: number; y: number } | False | 334 |
| x | number | False | 334 |
| y | number | False | 334 |

### Defaults and motion

- Default `dotSize` = `4` (line 401).
- Default `dotSpacing` = `20` (line 402).
- Default `dotOpacity` = `0.3` (line 403).
- Default `gradientAnimationDuration` = `20` (line 404).
- Default `waveIntensity` = `30` (line 405).
- Default `waveRadius` = `200` (line 406).
- Default `dotColor` = `"rgba(100, 100, 255, 1)"` (line 408).
- Default `glowColor` = `"rgba(100, 100, 255, 1)"` (line 409).
- Default `enableNoise` = `true` (line 410).
- Default `noiseOpacity` = `0.03` (line 411).
- Default `enableMouseGlow` = `true` (line 412).
- Default `initialPerformance` = `"medium"` (line 413).
- Default `enableGradient` = `false` (line 414).
- `duration`: computed; inspect expression (line 163).
- `ease`: "linear" (line 166).
- `duration`: 1.5 (line 462).
- `ease`: "easeOut" (line 462).

### Input, style and lifecycle

Events: resize (line 96); resize (line 299); mousemove (line 438).

Typography/style anchors: 162, 523, 886, 1177.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
