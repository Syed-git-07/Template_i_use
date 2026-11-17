# pixel-paragraph-words

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/pixel-paragraph-words.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/pixel-paragraph-words.tsx); SHA-256 `cd36c1b4b9023c608b8aa028c01212f1e55c8eae21211167b0c8f52880c999d8`; 185 lines.

Imports: `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "plain" | False | 85 |
| text | string | False | 85 |
| type | "pixel" | False | 85 |
| text | string | False | 85 |
| text | string | False | 128 |
| pixelWords | string[] | True | 133 |
| as | "p" \| "span" \| "div" | True | 135 |
| font | PixelFont | True | 137 |
| pixelWordClassName | string | True | 139 |

### Defaults and motion

- Default `Tag` = `"p"` (line 157).
- Default `font` = `"square"` (line 159).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
