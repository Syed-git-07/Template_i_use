# apple-keyboard

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/apple-keyboard.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/apple-keyboard.tsx); SHA-256 `9f944a9739b889d5961edd13dc8ebd88b3478892b7333e194879f3d3662511a7`; 530 lines.

Imports: `react`, `@tabler/icons-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | True | 48 |
| size | KeySize | True | 49 |
| symbol | string | True | 50 |
| secondaryLabel | string | True | 51 |
| icon | ReactNode | True | 52 |
| corner | CornerPosition | True | 53 |
| className | string | True | 54 |
| iconWithLabel | boolean | True | 55 |

### Defaults and motion

- Default `size` = `"1u"` (line 79).
- Default `corner` = `"none"` (line 83).
- Default `iconWithLabel` = `false` (line 85).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
