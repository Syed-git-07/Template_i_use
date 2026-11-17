# loading-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/loading-carousel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/loading-carousel.tsx); SHA-256 `e1058c8b6ee9d9a8d5fe815668ee1b111a7dad71364c2b10d09043117d6f0ae9`; 367 lines.

Imports: `react`, `next/image`, `embla-carousel-autoplay`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/carousel`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 27 |
| image | string | False | 28 |
| url | string | True | 29 |
| tips | Tip[] | True | 33 |
| className | string | True | 34 |
| autoplayInterval | number | True | 35 |
| showNavigation | boolean | True | 36 |
| showIndicators | boolean | True | 37 |
| showProgress | boolean | True | 38 |
| aspectRatio | "video" \| "square" \| "wide" | True | 39 |
| textPosition | "top" \| "bottom" | True | 40 |
| onTipChange | (index: number) => void | True | 41 |
| backgroundTips | boolean | True | 42 |
| backgroundGradient | boolean | True | 43 |
| shuffleTips | boolean | True | 44 |

### Defaults and motion

- Default `showProgress` = `true` (line 118).
- Default `aspectRatio` = `"video"` (line 119).
- Default `showNavigation` = `false` (line 120).
- Default `showIndicators` = `true` (line 121).
- Default `backgroundTips` = `false` (line 122).
- Default `textPosition` = `"bottom"` (line 123).
- Default `autoplayInterval` = `4500` (line 124).
- Default `backgroundGradient` = `false` (line 125).
- Default `shuffleTips` = `false` (line 126).
- `delay`: 0.3 (line 105).
- `duration`: 0.5 (line 105).
- `delay`: computed; inspect expression (line 139).
- `duration`: 0 (line 182).
- `duration`: 0.8 (line 183).
- `ease`: "easeOut" (line 183).
- `duration`: 0 (line 211).
- `duration`: 0.8 (line 212).
- `ease`: "easeInOut" (line 212).
- `duration`: 0 (line 306).
- `duration`: computed; inspect expression (line 308).
- `ease`: "linear" (line 309).

### Input, style and lifecycle

Events: onClick (line 291).

Typography/style anchors: 105.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
