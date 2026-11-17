# edge-blur

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/edge-blur.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/edge-blur.tsx); SHA-256 `65679275361254a0f021dd27f0d076e0e1d5c0ec73525715c1b2da6a780cceef`; 42 lines.

Imports:

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| position | "top" \| "bottom" | True | 4 |
| height | number | True | 5 |
| height | number | True | 35 |
| height | number | True | 39 |

### Defaults and motion

- Default `position` = `"bottom"` (line 8).
- Default `height` = `75` (line 8).
- Default `height` = `75` (line 35).
- Default `height` = `75` (line 39).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
