# bg-image-texture

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/bg-image-texture.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/bg-image-texture.tsx); SHA-256 `aeb1a109416eb9465717fa9f251b22a07709a5ea6e37c42b7e9a73acd09f2040`; 53 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | TextureVariant | True | 14 |
| opacity | number | True | 15 |
| className | string | True | 16 |
| children | React.ReactNode | True | 17 |

### Defaults and motion

- Default `variant` = `"fabric-of-squares"` (line 29).
- Default `opacity` = `0.5` (line 30).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
