# border-beam-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/border-beam-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/border-beam-card.tsx); SHA-256 `81abf1d3ff90c8eecf963632fc95fc09f7eb6f32764060360f6626389b011cd3`; 179 lines.

Imports: `react`, `react`, `border-beam`, `@/lib/utils`, `@/components/ui/card`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 53 |
| size | "default" \| "sm" | True | 55 |
| beamSize | BorderBeamSize | True | 57 |
| cardClassName | string | True | 59 |
| contentClassName | string | True | 61 |

### Defaults and motion

- Default `cardSize` = `"default"` (line 71).
- Default `beamSize` = `"md"` (line 72).
- Default `theme` = `"auto"` (line 73).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
