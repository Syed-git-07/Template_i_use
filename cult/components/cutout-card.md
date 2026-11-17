# cutout-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/cutout-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/cutout-card.tsx); SHA-256 `33095f87b54d59a6a85b91372f788151694d25aefffd59d851f00946ade38bf8`; 393 lines.

Imports: `react`, `next/image`, `@radix-ui/react-use-controllable-state`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| hovered | boolean | False | 85 |
| setHovered | (next: boolean) => void | False | 86 |
| hovered | boolean | True | 112 |
| defaultHovered | boolean | True | 114 |
| onHoveredChange | (hovered: boolean) => void | True | 116 |
| trackPointerHover | boolean | True | 121 |
| size | number | True | 292 |
| revealOnHover | boolean | True | 358 |

### Defaults and motion

- Default `defaultHovered` = `false` (line 127).
- Default `trackPointerHover` = `true` (line 129).
- Default `alt` = `""` (line 217).
- Default `fill` = `true` (line 218).
- Default `sizes` = `"(max-width: 768px) 100vw, 28rem"` (line 219).
- Default `size` = `32` (line 297).
- Default `viewBox` = `"0 0 200 200"` (line 298).
- Default `revealOnHover` = `true` (line 363).
- `duration`: 0.2 (line 52).
- `ease`: computed; inspect expression (line 52).
- `duration`: 0.48 (line 71).
- `bounce`: 0.14 (line 71).
- `duration`: 0.22 (line 185).
- `ease`: computed; inspect expression (line 185).
- `duration`: 0.36 (line 186).
- `ease`: computed; inspect expression (line 186).
- `duration`: 0.15 (line 386).
- `ease`: computed; inspect expression (line 386).
- `duration`: 0.24 (line 387).
- `ease`: computed; inspect expression (line 387).

### Input, style and lifecycle

Events: onMouseEnter (line 181); onMouseLeave (line 182).

Typography/style anchors: 25, 27, 45, 52, 62, 71.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
