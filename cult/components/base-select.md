# base-select

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/base-select.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/base-select.tsx); SHA-256 `c2908c8552e7193a018fb77a1f31ad8607687d985cb88c8258867478afbdf0e4`; 220 lines.

Imports: `react`, `@base-ui/react/select`, `@hugeicons/core-free-icons`, `@hugeicons/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "sm" \| "default" | True | 43 |

### Defaults and motion

- Default `size` = `"default"` (line 39).
- Default `side` = `"bottom"` (line 72).
- Default `sideOffset` = `4` (line 73).
- Default `align` = `"center"` (line 74).
- Default `alignOffset` = `0` (line 75).
- Default `alignItemWithTrigger` = `true` (line 76).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
