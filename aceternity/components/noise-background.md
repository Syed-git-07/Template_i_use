# noise-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/noise-background/components/ui/noise-background.tsx

[Original source](https://ui.aceternity.com/registry/noise-background.json); SHA-256 `fbedccf1bfdeaca7ddaa024948a791fcd7ff41364b11b6d854c10acdb28a54c8`; 232 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| springX | MotionValue<number> | False | 23 |
| springY | MotionValue<number> | False | 24 |
| gradientColor | string | False | 25 |
| opacity | number | False | 26 |
| multiplier | number | False | 27 |
| children | React.ReactNode | True | 45 |
| className | string | True | 46 |
| containerClassName | string | True | 47 |
| gradientColors | string[] | True | 48 |
| noiseIntensity | number | True | 49 |
| speed | number | True | 50 |
| backdropBlur | boolean | True | 51 |
| animating | boolean | True | 52 |

### Defaults and motion

- Default `noiseIntensity` = `0.2` (line 64).
- Default `speed` = `0.1` (line 65).
- Default `backdropBlur` = `false` (line 66).
- Default `animating` = `true` (line 67).
- `stiffness`: 100 (line 74).
- `damping`: 30 (line 74).
- `stiffness`: 100 (line 75).
- `damping`: 30 (line 75).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
