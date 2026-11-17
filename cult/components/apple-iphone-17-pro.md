# apple-iphone-17-pro

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/apple-iphone-17-pro.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/apple-iphone-17-pro.tsx); SHA-256 `6b2277ed4327b15c1a540150016f67376fb334e0ea406c6fbaf72a141cd486f3`; 705 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | True | 33 |
| dynamicIslandSize | DynamicIslandSize | True | 35 |
| dynamicIslandContent | ReactNode | True | 37 |
| frameColor | "graphite" \| "silver" \| "gold" \| "blue" | True | 39 |
| showStatusBar | boolean | True | 41 |
| showHomeIndicator | boolean | True | 43 |
| time | string | True | 45 |
| batteryLevel | number | True | 47 |
| signalStrength | number | True | 49 |
| onDynamicIslandTap | () => void | True | 51 |
| onScreenTap | () => void | True | 53 |
| className | string | True | 55 |
| beforeShadow | string | False | 91 |
| afterClasses | string | False | 92 |
| boxShadow | string | False | 93 |
| frameColor | FrameColor | False | 133 |
| frameColorScheme | (typeof FRAME_COLORS)[FrameColor] | False | 134 |
| className | string | True | 135 |
| className | string | True | 472 |
| className | string | True | 487 |
| className | string | True | 500 |
| progress | number | True | 520 |
| className | string | True | 521 |
| size | DynamicIslandSize | False | 566 |

### Defaults and motion

- Default `dynamicIslandSize` = `"default"` (line 185).
- Default `frameColor` = `"graphite"` (line 187).
- Default `showStatusBar` = `true` (line 188).
- Default `showHomeIndicator` = `true` (line 189).
- Default `time` = `"9:41"` (line 190).
- Default `batteryLevel` = `94` (line 191).
- Default `signalStrength` = `2` (line 192).
- Default `className` = `""` (line 195).
- Default `progress` = `0.75` (line 517).
- `stiffness`: 400 (line 343).
- `damping`: 30 (line 344).
- `stiffness`: 400 (line 376).
- `damping`: 30 (line 377).

### Input, style and lifecycle

Events: onClick (line 270); onClick (line 337).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
