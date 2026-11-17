# pixel-heading-character

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/pixel-heading-character.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/pixel-heading-character.tsx); SHA-256 `dd28d6608f0f0e2f5bc114d3099bc740f6f60638420835e602fb03144ac59c04`; 586 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 133 |
| as | "h1" \| "h2" \| "h3" \| "h4" \| "h5" \| "h6" | True | 161 |
| cycleInterval | number | True | 166 |
| defaultFontIndex | number | True | 171 |
| onFontIndexChange | (index: number) => void | True | 175 |
| showLabel | boolean | True | 180 |
| mode | PixelHeadingMode | True | 191 |
| staggerDelay | number | True | 198 |
| autoPlay | boolean | True | 205 |
| prefix | string | True | 211 |
| prefixFont | "square" \| "grid" \| "circle" \| "triangle" \| "line" \| "none" | True | 217 |
| isolate | Record<string, string> | True | 227 |

### Defaults and motion

- Default `Tag` = `"h1"` (line 287).
- Default `cycleInterval` = `150` (line 289).
- Default `defaultFontIndex` = `0` (line 290).
- Default `showLabel` = `false` (line 292).
- Default `mode` = `"multi"` (line 293).
- Default `staggerDelay` = `50` (line 294).
- Default `autoPlay` = `false` (line 295).
- Default `prefixFont` = `"none"` (line 297).

### Input, style and lifecycle

Events: onMouseEnter (line 499); onMouseLeave (line 500); onFocus (line 501); onBlur (line 502); onKeyDown (line 503).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
