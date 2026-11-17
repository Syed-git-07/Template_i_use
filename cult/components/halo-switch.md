# halo-switch

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-switch.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-switch.tsx); SHA-256 `60478402779cef582fc7fd7549823c98c2bab9da85e9b592f2385eb23fb6b95d`; 267 lines.

Imports: `react`, `@base-ui/react/switch`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| current | T \| null | False | 50 |
| translucent | boolean | True | 58 |
| size | "sm" \| "default" | True | 59 |

### Defaults and motion

- Default `translucent` = `true` (line 64).
- Default `size` = `"default"` (line 65).
- `bounce`: 0.12 (line 26).
- `damping`: 34 (line 27).
- `stiffness`: 420 (line 28).
- `duration`: 0 (line 254).

### Input, style and lifecycle

Events: onCheckedChange (line 212).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
