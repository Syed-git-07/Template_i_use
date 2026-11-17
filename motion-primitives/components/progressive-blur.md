# progressive-blur

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/progressive-blur.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/progressive-blur.tsx); SHA-256 `c2a9cea444556165a28ae5fa0ff680c96264fe38779c9713ffafae73c61d9083`; 64 lines.

Imports: `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| direction | keyof typeof GRADIENT_ANGLES | True | 13 |
| blurLayers | number | True | 14 |
| className | string | True | 15 |
| blurIntensity | number | True | 16 |

### Defaults and motion

- Default `direction` = `"bottom"` (line 20).
- Default `blurLayers` = `8` (line 21).
- Default `blurIntensity` = `0.25` (line 23).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
