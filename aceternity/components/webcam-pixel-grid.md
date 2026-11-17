# webcam-pixel-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/webcam-pixel-grid/components/ui/webcam-pixel-grid.tsx

[Original source](https://ui.aceternity.com/registry/webcam-pixel-grid.json); SHA-256 `a1702ec46e566f8c32cbbf030a3df2599411e08a7fd251668668f2a2a777e5f1`; 536 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gridCols | number | True | 7 |
| gridRows | number | True | 9 |
| maxElevation | number | True | 11 |
| motionSensitivity | number | True | 13 |
| elevationSmoothing | number | True | 15 |
| colorMode | "webcam" \| "monochrome" | True | 17 |
| monochromeColor | string | True | 19 |
| backgroundColor | string | True | 21 |
| mirror | boolean | True | 23 |
| gapRatio | number | True | 25 |
| invertColors | boolean | True | 27 |
| darken | number | True | 29 |
| borderColor | string | True | 31 |
| borderOpacity | number | True | 33 |
| className | string | True | 35 |
| onWebcamError | (error: Error) => void | True | 37 |
| onWebcamReady | () => void | True | 39 |
| r | number | False | 43 |
| g | number | False | 44 |
| b | number | False | 45 |
| motion | number | False | 46 |
| targetElevation | number | False | 47 |
| currentElevation | number | False | 48 |

### Defaults and motion

- Default `gridCols` = `64` (line 52).
- Default `gridRows` = `48` (line 53).
- Default `maxElevation` = `15` (line 54).
- Default `motionSensitivity` = `0.4` (line 55).
- Default `elevationSmoothing` = `0.1` (line 56).
- Default `colorMode` = `"webcam"` (line 57).
- Default `monochromeColor` = `"#00ff88"` (line 58).
- Default `backgroundColor` = `"#0a0a0a"` (line 59).
- Default `mirror` = `true` (line 60).
- Default `gapRatio` = `0.1` (line 61).
- Default `invertColors` = `false` (line 62).
- Default `darken` = `0` (line 63).
- Default `borderColor` = `"#ffffff"` (line 64).
- Default `borderOpacity` = `0.08` (line 65).

### Input, style and lifecycle

Events: onClick (line 434); onClick (line 478); onClick (line 504).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
