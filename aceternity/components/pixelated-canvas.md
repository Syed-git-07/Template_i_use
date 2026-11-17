# pixelated-canvas

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/pixelated-canvas/components/ui/pixelated-canvas.tsx

[Original source](https://ui.aceternity.com/registry/pixelated-canvas.json); SHA-256 `3fb1d9ae52acfc02a126ec78e05d3aab75bf9d738287a6b634e657eebf5551d1`; 562 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | False | 5 |
| width | number | True | 6 |
| height | number | True | 7 |
| cellSize | number | True | 9 |
| dotScale | number | True | 11 |
| shape | "circle" \| "square" | True | 13 |
| backgroundColor | string | True | 15 |
| grayscale | boolean | True | 17 |
| className | string | True | 18 |
| responsive | boolean | True | 20 |
| dropoutStrength | number | True | 22 |
| interactive | boolean | True | 24 |
| distortionStrength | number | True | 26 |
| distortionRadius | number | True | 28 |
| distortionMode | "repel" \| "attract" \| "swirl" | True | 30 |
| followSpeed | number | True | 32 |
| sampleAverage | boolean | True | 34 |
| tintColor | string | True | 36 |
| tintStrength | number | True | 38 |
| maxFps | number | True | 40 |
| objectFit | "cover" \| "contain" \| "fill" \| "none" | True | 42 |
| jitterStrength | number | True | 44 |
| jitterSpeed | number | True | 46 |
| fadeOnLeave | boolean | True | 48 |
| fadeSpeed | number | True | 50 |
| x | number | False | 83 |
| y | number | False | 84 |
| r | number | False | 85 |
| g | number | False | 86 |
| b | number | False | 87 |
| a | number | False | 88 |
| drop | boolean | False | 89 |
| seed | number | False | 90 |
| width | number | False | 94 |
| height | number | False | 95 |
| dot | number | False | 96 |
| x | number | False | 98 |
| y | number | False | 98 |
| x | number | False | 102 |
| y | number | False | 102 |
| x | number | False | 214 |
| y | number | False | 215 |
| r | number | False | 216 |
| g | number | False | 217 |
| b | number | False | 218 |
| a | number | False | 219 |
| drop | boolean | False | 220 |
| seed | number | False | 221 |

### Defaults and motion

- Default `width` = `400` (line 55).
- Default `height` = `500` (line 56).
- Default `cellSize` = `3` (line 57).
- Default `dotScale` = `0.9` (line 58).
- Default `shape` = `"square"` (line 59).
- Default `backgroundColor` = `"#000000"` (line 60).
- Default `grayscale` = `false` (line 61).
- Default `responsive` = `false` (line 63).
- Default `dropoutStrength` = `0.4` (line 64).
- Default `interactive` = `true` (line 65).
- Default `distortionStrength` = `3` (line 66).
- Default `distortionRadius` = `80` (line 67).
- Default `distortionMode` = `"swirl"` (line 68).
- Default `followSpeed` = `0.2` (line 69).
- Default `sampleAverage` = `true` (line 70).
- Default `tintColor` = `"#FFFFFF"` (line 71).
- Default `tintStrength` = `0.2` (line 72).
- Default `maxFps` = `60` (line 73).
- Default `objectFit` = `"cover"` (line 74).
- Default `jitterStrength` = `4` (line 75).
- Default `jitterSpeed` = `4` (line 76).
- Default `fadeOnLeave` = `true` (line 77).
- Default `fadeSpeed` = `0.1` (line 78).

### Input, style and lifecycle

Events: pointermove (line 386); pointerenter (line 387); pointerleave (line 388); resize (line 514).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
