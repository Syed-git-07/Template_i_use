# image-generation-loader

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/image-generation-loader/components/ui/image-generation-loader.tsx

[Original source](https://ui.aceternity.com/registry/image-generation-loader.json); SHA-256 `4b22af88a23992c561cb6bce732b7fd9be46e021c9be29d2185c64a7adc0f715`; 574 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 23 |
| cellSize | number | True | 24 |
| gap | number | True | 25 |
| bandHeight | number | True | 26 |
| duration | number | True | 27 |
| effect | ImageGenerationLoaderEffect | True | 28 |
| waveAmplitude | number | True | 29 |
| scaleAmplitude | number | True | 30 |
| colors | ImageGenerationLoaderColors | True | 31 |
| text | string | True | 32 |
| textLetterSpacing | number | True | 33 |
| textWordSpacing | number | True | 34 |
| overlayOpacity | number | True | 35 |
| overlayExitDuration | number | True | 36 |
| easing | ImageGenerationLoaderEasing | True | 37 |
| column | number | False | 41 |
| row | number | False | 42 |
| opacity | number | False | 43 |
| phase | number | False | 44 |
| scaleSeed | number | False | 45 |
| isText | boolean | False | 46 |

### Defaults and motion

- Default `cellSize` = `5` (line 175).
- Default `gap` = `2` (line 176).
- Default `bandHeight` = `48` (line 177).
- Default `duration` = `4000` (line 178).
- Default `effect` = `"shimmer"` (line 179).
- Default `waveAmplitude` = `12` (line 180).
- Default `scaleAmplitude` = `0.75` (line 181).
- Default `overlayOpacity` = `0.3` (line 186).
- Default `overlayExitDuration` = `700` (line 187).
- Default `easing` = `"ease-in-out"` (line 188).

### Input, style and lifecycle

Events: change (line 522).

Typography/style anchors: 240.

Source signals: reduced_motion, cleanup, resize, visibility, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
