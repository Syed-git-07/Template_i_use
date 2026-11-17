# illustration-cursor

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-cursor.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-cursor.tsx); SHA-256 `e149b7a880440705c6f0c5ba838864ff8b6f507f9dabdf50fe08092e777ad502`; 245 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| flip | boolean | True | 20 |
| phaseX | number | False | 47 |
| phaseY | number | False | 48 |
| speedX | number | False | 49 |
| speedY | number | False | 50 |
| ampX | number | False | 51 |
| ampY | number | False | 52 |
| name | string | False | 104 |
| color | string | False | 105 |
| side | CursorSide | False | 106 |
| style | React.CSSProperties | True | 107 |
| delay | boolean | True | 108 |
| x | number | False | 178 |
| y | number | False | 178 |

### Defaults and motion

- Default `flip` = `false` (line 20).
- Default `delay` = `false` (line 102).
- `delay`: computed; inspect expression (line 209).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 133, 228.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
