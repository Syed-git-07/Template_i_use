# base-tooltip

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/base-tooltip.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/base-tooltip.tsx); SHA-256 `59fb3ea474b21a7531f2d71bc90ac1797aa709ec8bb3da2ff4cf8eb71d1a7240`; 101 lines.

Imports: `@base-ui/react/tooltip`, `@radix-ui/react-slot`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| delayDuration | number | True | 12 |
| delayDuration | number | True | 27 |
| asChild | boolean | True | 43 |

### Defaults and motion

- Default `asChild` = `false` (line 40).
- Default `side` = `"top"` (line 64).
- Default `sideOffset` = `4` (line 65).
- Default `align` = `"center"` (line 66).
- Default `alignOffset` = `0` (line 67).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
