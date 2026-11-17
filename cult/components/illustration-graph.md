# illustration-graph

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-graph.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-graph.tsx); SHA-256 `fd85e0739c3caf1a3a6b5f398096430389087cf3d99751f603e01c116cbc7236`; 526 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| x | number | False | 8 |
| y | number | False | 9 |
| width | number | True | 14 |
| height | number | True | 15 |
| backgroundColor | string | True | 16 |
| borderColor | string | True | 17 |
| cardFill | string | True | 18 |
| cardStroke | string | True | 19 |
| gridLineColor | string | True | 20 |
| primaryLineColor | string | True | 21 |
| errorLineColor | string | True | 22 |
| errorBadgeColor | string | True | 23 |
| errorBadgeTextColor | string | True | 24 |
| highlightAreaColor | string | True | 25 |
| highlightBorderColor | string | True | 26 |
| textColor | string | True | 27 |
| mutedTextColor | string | True | 28 |
| badgeText | string | True | 29 |
| headerText | string | True | 30 |
| footerText | string | True | 31 |
| yAxisLabels | string[] | True | 32 |
| dataPoints | DataPoint[] | True | 33 |
| errorRegion | { start: number; end: number } | True | 34 |
| start | number | False | 34 |
| end | number | False | 34 |
| showHighlightArea | boolean | True | 35 |
| customBadgeIcon | ReactNode | True | 36 |
| footerShadowId | string | False | 70 |
| chartShadowId | string | False | 71 |
| shadowId | string | False | 154 |
| cardFill | string | False | 155 |
| cardStroke | string | False | 156 |
| mutedTextColor | string | False | 157 |
| footerText | string | False | 158 |
| shadowId | string | False | 246 |
| cardFill | string | False | 247 |
| cardStroke | string | False | 248 |
| gridLineColor | string | False | 249 |
| errorBadgeColor | string | False | 250 |
| errorBadgeTextColor | string | False | 251 |
| highlightAreaColor | string | False | 252 |
| highlightBorderColor | string | False | 253 |
| mutedTextColor | string | False | 254 |
| badgeText | string | False | 255 |
| headerText | string | False | 256 |
| yAxisLabels | string[] | False | 257 |
| errorRegion | { start: number; end: number } | False | 258 |
| start | number | False | 258 |
| end | number | False | 258 |
| showHighlightArea | boolean | False | 259 |
| customBadgeIcon | ReactNode | True | 260 |
| textColor | string | False | 261 |
| fullPath | string | False | 402 |
| errorPath | string | False | 403 |
| primaryLineColor | string | False | 404 |
| errorLineColor | string | False | 405 |
| showHighlightArea | boolean | False | 406 |

### Defaults and motion

- Default `width` = `450` (line 429).
- Default `height` = `185` (line 430).
- Default `backgroundColor` = `"transparent"` (line 431).
- Default `cardFill` = `"var(--card)"` (line 433).
- Default `cardStroke` = `"var(--border)"` (line 434).
- Default `gridLineColor` = `"var(--border)"` (line 435).
- Default `primaryLineColor` = `"#0070F3"` (line 436).
- Default `errorLineColor` = `"var(--destructive)"` (line 437).
- Default `errorBadgeColor` = `"var(--destructive)"` (line 438).
- Default `errorBadgeTextColor` = `"var(--destructive)"` (line 439).
- Default `highlightAreaColor` = `"color-mix(in srgb, var(--destructive) 8%, transparent)"` (line 440).
- Default `highlightBorderColor` = `"color-mix(in srgb, var(--destructive) 25%, transparent)"` (line 441).
- Default `textColor` = `"var(--card-foreground)"` (line 442).
- Default `mutedTextColor` = `"var(--muted-foreground)"` (line 443).
- Default `badgeText` = `"5xx"` (line 444).
- Default `headerText` = `"api / api/error rate / error rate"` (line 445).
- Default `footerText` = `"Investigate 12h ago / now"` (line 446).
- Default `showHighlightArea` = `true` (line 450).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 220, 289, 299, 309, 319, 329, 376, 386.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
