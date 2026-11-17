# bg-media

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/bg-media.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/bg-media.tsx); SHA-256 `6da7497c3776d14f38ce248a63489961aa4fde8d8a6bfb3e8731aa5f71de91cb`; 113 lines.

Imports: `react`, `class-variance-authority`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | OverlayVariant | True | 38 |
| type | MediaType | True | 39 |
| src | string | False | 40 |
| alt | string | True | 41 |

### Defaults and motion

- Default `variant` = `"light"` (line 45).
- Default `type` = `"image"` (line 46).
- Default `alt` = `""` (line 48).

### Input, style and lifecycle

Events: onClick (line 103).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
