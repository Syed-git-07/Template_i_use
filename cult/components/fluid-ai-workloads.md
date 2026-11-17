# fluid-ai-workloads

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/fluid-ai-workloads.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/fluid-ai-workloads.tsx); SHA-256 `9d4b10f4f211a85ff35f8a06348db2096f205d800b8416808568977fdc54ed9c`; 418 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| width | number | True | 9 |
| height | number | True | 10 |
| backgroundColor | string | True | 11 |
| cardFill | string | True | 12 |
| cardStroke | string | True | 13 |
| bubbleFill | string | True | 14 |
| bubbleStroke | string | True | 15 |
| logoColor | string | True | 16 |
| lineColorTop | string | True | 17 |
| lineColorUpperMid | string | True | 18 |
| lineColorLowerMid | string | True | 19 |
| lineColorBottom | string | True | 20 |
| connectorLineColor | string | True | 21 |
| connectorDotFill | string | True | 22 |
| connectorDotStroke | string | True | 23 |
| shadowFilterId | string | False | 31 |
| leftCardClipId | string | False | 32 |
| centerLogoClipId | string | False | 33 |
| shadowFilterId | string | False | 60 |
| leftCardClipId | string | False | 101 |
| cardFill | string | False | 102 |
| cardStroke | string | False | 103 |
| bubbleFill | string | False | 104 |
| bubbleStroke | string | False | 105 |
| dotColor | string | False | 106 |
| cardFill | string | False | 192 |
| cardStroke | string | False | 193 |
| logoColor | string | False | 194 |
| centerLogoClipId | string | False | 195 |
| lineColorBottom | string | False | 226 |
| lineColorTop | string | False | 227 |
| lineColorLowerMid | string | False | 228 |
| lineColorUpperMid | string | False | 229 |
| cardFill | string | False | 263 |
| cardStroke | string | False | 264 |
| connectorDotFill | string | False | 265 |
| connectorDotStroke | string | False | 266 |

### Defaults and motion

- Default `width` = `448` (line 331).
- Default `height` = `195` (line 332).
- Default `backgroundColor` = `"var(--background)"` (line 333).
- Default `cardFill` = `"var(--card)"` (line 334).
- Default `cardStroke` = `"var(--border)"` (line 335).
- Default `bubbleFill` = `"var(--muted)"` (line 336).
- Default `bubbleStroke` = `"var(--border)"` (line 337).
- Default `logoColor` = `"var(--foreground)"` (line 338).
- Default `lineColorTop` = `"#52AEFF"` (line 339).
- Default `lineColorUpperMid` = `"#E5484D"` (line 340).
- Default `lineColorLowerMid` = `"#FFB224"` (line 341).
- Default `lineColorBottom` = `"#45DEC4"` (line 342).
- Default `connectorLineColor` = `"var(--muted-foreground)"` (line 343).
- Default `connectorDotFill` = `"var(--card)"` (line 344).
- Default `connectorDotStroke` = `"var(--border)"` (line 345).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 333, 338.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
