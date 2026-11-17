# bg-animated-gradient

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/bg-animated-gradient.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/bg-animated-gradient.tsx); SHA-256 `2d897f9f9e8fc91e82d4fa7d15bf0f6031e5b6e1bc7bdbff6cb4fbd3a60d14cd`; 56 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| color | string | False | 7 |
| position | number | False | 8 |
| stops | GradientStop[] | False | 12 |
| centerX | number | False | 13 |
| centerY | number | False | 14 |
| gradients | GradientType[] | False | 18 |
| animationDuration | number | False | 19 |
| className | string | True | 20 |

### Defaults and motion

- Default `className` = `""` (line 26).
- `duration`: computed; inspect expression (line 39).
- `ease`: "linear" (line 42).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 38.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
