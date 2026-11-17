# analytics-chart

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/analytics-chart.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/analytics-chart.tsx); SHA-256 `77b1e1d67b7ded0a5dbc539e538eb0772903180ab9e25e36f95513dc2495fc44`; 485 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| date | string | False | 22 |
| label | string | False | 23 |
| value | number | False | 24 |
| offset | string | False | 28 |
| color | string | False | 29 |
| x | number | False | 87 |
| y | number | False | 88 |
| formattedDate | string | False | 89 |
| color | string | False | 90 |
| point | AnalyticsTooltipPoint | False | 94 |
| color | string | False | 95 |
| px | number | False | 96 |
| py | number | False | 97 |
| side | "top" \| "bottom" | False | 98 |
| valueLabel | string | False | 99 |
| show | boolean | False | 100 |
| isHovered | boolean | True | 102 |
| data | AnalyticsDataPoint[] | True | 231 |
| gradientStops | AnalyticsGradientStop[] | True | 232 |
| dotColors | string[] | True | 233 |
| gridLines | number | True | 234 |
| height | number | True | 235 |
| pinnedIndices | number[] | True | 236 |
| valueLabel | string | True | 237 |
| className | string | True | 238 |

### Defaults and motion

- Default `isHovered` = `false` (line 113).
- Default `gridLines` = `5` (line 245).
- Default `height` = `280` (line 246).
- Default `valueLabel` = `"clicks"` (line 248).

### Input, style and lifecycle

Events: onMouseLeave (line 375); onMouseMove (line 376).

Typography/style anchors: 133, 203, 409, 430, 450.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
