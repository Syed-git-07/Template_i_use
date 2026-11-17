# dither-shader

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/dither-shader/components/ui/dither-shader.tsx

[Original source](https://ui.aceternity.com/registry/dither-shader.json); SHA-256 `b3c1064c304d4c6648335febbb12a541f7c81905f1998e72202adb661ffc7503`; 461 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | False | 10 |
| gridSize | number | True | 12 |
| ditherMode | DitheringMode | True | 14 |
| colorMode | ColorMode | True | 16 |
| invert | boolean | True | 18 |
| pixelRatio | number | True | 20 |
| primaryColor | string | True | 22 |
| secondaryColor | string | True | 24 |
| customPalette | string[] | True | 26 |
| brightness | number | True | 28 |
| contrast | number | True | 30 |
| backgroundColor | string | True | 32 |
| objectFit | "cover" \| "contain" \| "fill" \| "none" | True | 34 |
| threshold | number | True | 36 |
| animated | boolean | True | 38 |
| animationSpeed | number | True | 40 |
| className | string | True | 42 |
| width | number | False | 121 |
| height | number | False | 121 |
| width | number | False | 127 |
| height | number | False | 128 |

### Defaults and motion

- Default `gridSize` = `4` (line 98).
- Default `ditherMode` = `"bayer"` (line 99).
- Default `colorMode` = `"original"` (line 100).
- Default `invert` = `false` (line 101).
- Default `pixelRatio` = `1` (line 102).
- Default `primaryColor` = `"#000000"` (line 103).
- Default `secondaryColor` = `"#ffffff"` (line 104).
- Default `brightness` = `0` (line 106).
- Default `contrast` = `1` (line 107).
- Default `backgroundColor` = `"transparent"` (line 108).
- Default `objectFit` = `"cover"` (line 109).
- Default `threshold` = `0.5` (line 110).
- Default `animated` = `false` (line 111).
- Default `animationSpeed` = `0.02` (line 112).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
