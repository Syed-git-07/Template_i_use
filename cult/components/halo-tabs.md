# halo-tabs

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-tabs.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-tabs.tsx); SHA-256 `195cb5b70400c7f21e20fb06c00094eec3040e738086a334530b9250e714ab6f`; 158 lines.

Imports: `react`, `@base-ui/react/tabs`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | HaloTabsVariant | True | 42 |
| variant | HaloTabsVariant | True | 89 |

### Defaults and motion

- Default `variant` = `"underline"` (line 39).
- Default `variant` = `"underline"` (line 86).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
