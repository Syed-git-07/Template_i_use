# merging-bubbles

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/merging-bubbles.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/merging-bubbles.tsx); SHA-256 `3d1abaede275e90bb834d8f2f2ee9851c6e559b959d5d0d16ac8e3b0bfb67bb0`; 208 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "xs" \| "sm" \| "md" \| "lg" | True | 8 |
| className | string | True | 9 |
| startIcon | React.ReactNode | True | 10 |
| endIcon | React.ReactNode | True | 11 |
| showPlus | boolean | True | 12 |
| className | string | True | 120 |
| className | string | True | 183 |

### Defaults and motion

- Default `size` = `"md"` (line 23).
- Default `showPlus` = `true` (line 27).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
