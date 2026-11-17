# illustration-fluid-rendering

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-fluid-rendering.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-fluid-rendering.tsx); SHA-256 `cfff62e3296ca42e2723919b4e70035b9476df4ac073f833a0de6eb692bde731`; 622 lines.

Imports: `react`, `react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| width | number | True | 11 |
| height | number | True | 12 |
| cardFill | string | True | 14 |
| cardStroke | string | True | 15 |
| browserDotColor | string | True | 16 |
| placeholderFill | string | True | 17 |
| placeholderStroke | string | True | 18 |
| dashedStroke | string | True | 19 |
| imagePlaceholderFill | string | True | 20 |
| lineColorTeal | string | True | 22 |
| lineColorBlue | string | True | 23 |
| lineColorOrange | string | True | 24 |
| lineColorRed | string | True | 25 |
| connectorFill | string | True | 27 |
| connectorStroke | string | True | 28 |
| connectorLineColor | string | True | 29 |
| logoColor | string | True | 31 |
| textColor | string | True | 33 |
| mutedTextColor | string | True | 34 |
| topIcon | ReactNode | True | 36 |
| upperMidIcon | ReactNode | True | 37 |
| lowerMidIcon | ReactNode | True | 38 |
| bottomIcon | ReactNode | True | 39 |

### Defaults and motion

- Default `width` = `448` (line 89).
- Default `height` = `195` (line 90).
- Default `cardFill` = `"var(--card)"` (line 91).
- Default `cardStroke` = `"var(--border)"` (line 92).
- Default `browserDotColor` = `"color-mix(in oklab, var(--foreground) 12%, transparent)"` (line 93).
- Default `placeholderFill` = `"var(--card)"` (line 94).
- Default `placeholderStroke` = `"var(--border)"` (line 95).
- Default `dashedStroke` = `"color-mix(in oklab, var(--muted-foreground) 35%, transparent)"` (line 96).
- Default `imagePlaceholderFill` = `"var(--muted)"` (line 97).
- Default `lineColorTeal` = `"#45DEC4"` (line 98).
- Default `lineColorBlue` = `"#52AEFF"` (line 99).
- Default `lineColorOrange` = `"#FFB224"` (line 100).
- Default `lineColorRed` = `"#E5484D"` (line 101).
- Default `connectorFill` = `"var(--card)"` (line 102).
- Default `connectorStroke` = `"var(--border)"` (line 103).
- Default `connectorLineColor` = `"color-mix(in oklab, var(--muted-foreground) 60%, transparent)"` (line 104).
- Default `logoColor` = `"var(--card-foreground)"` (line 105).
- Default `textColor` = `"var(--foreground)"` (line 106).
- Default `mutedTextColor` = `"var(--muted-foreground)"` (line 107).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 93, 106, 491, 529, 567, 605.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
