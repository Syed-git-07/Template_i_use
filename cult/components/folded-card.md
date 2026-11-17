# folded-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/folded-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/folded-card.tsx); SHA-256 `31d1735832870dabb6d8641055102ce243993489427e7889d03f049db133bd74`; 313 lines.

Imports: `react`, `next/link`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 16 |
| isLight | boolean | True | 17 |
| side | "left" \| "right" | True | 18 |
| rows | number | True | 190 |
| columns | number | True | 191 |

### Defaults and motion

- Default `isLight` = `true` (line 13).
- Default `side` = `"left"` (line 14).
- Default `rows` = `4` (line 196).
- Default `columns` = `4` (line 197).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
