# pixel-paragraph-words-inverse

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/pixel-paragraph-words-inverse.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/pixel-paragraph-words-inverse.tsx); SHA-256 `934e368cae94a307c25a9dbcce7d4a126e34e5a11028afd900468692d690d8cd`; 205 lines.

Imports: `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "pixel" | False | 95 |
| text | string | False | 95 |
| type | "plain" | False | 95 |
| text | string | False | 95 |
| text | string | False | 138 |
| plainWords | string[] | True | 144 |
| as | "p" \| "span" \| "div" | True | 146 |
| pixelFont | PixelFont | True | 148 |
| plainFont | PlainFont | True | 150 |
| plainWordClassName | string | True | 152 |

### Defaults and motion

- Default `Tag` = `"p"` (line 171).
- Default `pixelFont` = `"square"` (line 173).
- Default `plainFont` = `"sans"` (line 174).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
