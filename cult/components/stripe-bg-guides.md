# stripe-bg-guides

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/stripe-bg-guides.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/stripe-bg-guides.tsx); SHA-256 `3cbd782b34948c35df72a07168fde674715b155e49ace4aa8b14cf612c1b9aba`; 233 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| columnCount | number | True | 10 |
| className | string | True | 11 |
| solidLines | number[] | True | 12 |
| animated | boolean | True | 13 |
| animationDuration | number | True | 14 |
| animationDelay | number | True | 15 |
| glowColor | string | True | 16 |
| glowSize | string | True | 17 |
| glowOpacity | number | True | 18 |
| randomize | boolean | True | 19 |
| randomInterval | number | True | 20 |
| direction | AnimationDirection | True | 21 |
| easing | AnimationEasing | True | 22 |
| responsive | boolean | True | 23 |
| minColumnWidth | string | True | 24 |
| maxActiveColumns | number | True | 25 |
| darkMode | boolean | True | 26 |
| contained | boolean | True | 27 |

### Defaults and motion

- Default `columnCount` = `4` (line 39).
- Default `className` = `""` (line 40).
- Default `animated` = `true` (line 42).
- Default `animationDuration` = `62` (line 43).
- Default `animationDelay` = `0.8` (line 44).
- Default `glowColor` = `"hsl(var(--accent))"` (line 45).
- Default `glowSize` = `"10vh"` (line 47).
- Default `glowOpacity` = `0.4` (line 48).
- Default `randomize` = `true` (line 49).
- Default `randomInterval` = `9000` (line 50).
- Default `direction` = `"both"` (line 51).
- Default `easing` = `"spring"` (line 52).
- Default `responsive` = `false` (line 53).
- Default `minColumnWidth` = `"4rem"` (line 54).
- Default `maxActiveColumns` = `3` (line 55).
- Default `darkMode` = `false` (line 56).
- Default `contained` = `false` (line 57).
- `duration`: computed; inspect expression (line 217).
- `ease`: computed; inspect expression (line 219).
- `delay`: computed; inspect expression (line 220).

### Input, style and lifecycle

Events: resize (line 93).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
