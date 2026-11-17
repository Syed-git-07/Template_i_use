# background-cubes-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-cubes-grid/components/ui/background-cubes-grid.tsx

[Original source](https://ui.aceternity.com/registry/background-cubes-grid.json); SHA-256 `10cc2b45bc58114af608ac48877a80b9bee201516a4c69b7373763b2165f5bc4`; 938 lines.

Imports: `react`, `three`, `three/examples/jsm/postprocessing/EffectComposer.js`, `three/examples/jsm/postprocessing/RenderPass.js`, `three/examples/jsm/postprocessing/ShaderPass.js`, `three/examples/jsm/postprocessing/OutputPass.js`, `three/examples/jsm/geometries/RoundedBoxGeometry.js`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "isometric" | True | 23 |
| className | string | True | 24 |
| cellSize | number | True | 26 |
| gap | number | True | 28 |
| topColor | string | True | 30 |
| leftColor | string | True | 32 |
| rightColor | string | True | 34 |
| amplitude | number | True | 36 |
| speed | number | True | 38 |
| damping | number | True | 40 |
| idleRipples | boolean | True | 42 |
| idleDelay | number | True | 44 |
| glowColor | string | True | 46 |
| glow | number | True | 48 |
| x | number | False | 245 |
| z | number | False | 245 |
| x | number | False | 246 |
| z | number | False | 246 |
| variant | "perspective" | False | 480 |
| className | string | True | 481 |
| gridSize | number | True | 483 |
| gap | number | True | 485 |
| baseColor | string | True | 487 |
| waveColor | string | True | 489 |
| backgroundColor | string | True | 491 |
| glow | number | True | 493 |
| amplitude | number | True | 495 |
| tilt | number | True | 497 |
| idleRipples | boolean | True | 499 |
| x | number | False | 595 |
| z | number | False | 595 |
| age | number | False | 595 |
| distDelta | number | False | 595 |
| x | number | False | 667 |
| z | number | False | 667 |

### Defaults and motion

- Default `cellSize` = `150` (line 400).
- Default `gap` = `0.025` (line 401).
- Default `topColor` = `"#fafaf9"` (line 402).
- Default `leftColor` = `"#e7e5e4"` (line 403).
- Default `rightColor` = `"#d6d3d1"` (line 404).
- Default `amplitude` = `0.7` (line 405).
- Default `speed` = `7` (line 406).
- Default `damping` = `0.08` (line 407).
- Default `idleRipples` = `true` (line 408).
- Default `idleDelay` = `1.5` (line 409).
- Default `glowColor` = `"#a8a29e"` (line 410).
- Default `glow` = `0.5` (line 411).
- Default `gridSize` = `44` (line 882).
- Default `gap` = `0.08` (line 883).
- Default `baseColor` = `"#2a2a30"` (line 884).
- Default `waveColor` = `"#ff6a2b"` (line 885).
- Default `backgroundColor` = `"#0b0b0d"` (line 886).
- Default `glow` = `0.9` (line 887).
- Default `amplitude` = `0.5` (line 888).
- Default `tilt` = `0.7` (line 889).
- Default `idleRipples` = `true` (line 890).

### Input, style and lifecycle

Events: pointermove (line 385); pointermove (line 818).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
