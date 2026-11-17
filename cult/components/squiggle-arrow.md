# squiggle-arrow

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/squiggle-arrow.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/squiggle-arrow.tsx); SHA-256 `8051715d53603ffee5db10cdfd38320194453e8f06dbc00df797b839e3fa4335`; 76 lines.

Imports: `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| width | number | True | 4 |
| height | number | True | 5 |
| strokeWidth | number | True | 6 |
| className | string | True | 7 |
| direction | "right" \| "left" \| "up" \| "down" | True | 8 |
| variant | "wavy" \| "bouncy" \| "smooth" | True | 9 |

### Defaults and motion

- Default `width` = `200` (line 13).
- Default `height` = `100` (line 14).
- Default `strokeWidth` = `2.5` (line 15).
- Default `direction` = `"right"` (line 17).
- Default `variant` = `"wavy"` (line 18).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
