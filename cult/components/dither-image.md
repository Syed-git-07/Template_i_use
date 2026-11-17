# dither-image

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/dither-image.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/dither-image.tsx); SHA-256 `421d254ee5be44f27104eb610c0acd21d1f03ec804a852ffdf1b1c181e515551`; 485 lines.

Imports: `react`, `next/image`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| "--dither-gray" | number \| string | True | 122 |
| "--dither-contrast" | number \| string | True | 123 |
| "--dither-bright" | number \| string | True | 124 |
| "--dither-blur" | string | True | 125 |
| "--dither-cell" | string | True | 126 |
| "--dither-opacity" | number \| string | True | 127 |
| "--dither-image" | string | True | 128 |
| invertOnDark | boolean | False | 133 |
| size | DitherSize | True | 164 |
| aspectRatio | DitherAspectRatio | True | 166 |
| grayscale | number | True | 168 |
| contrast | number | True | 170 |
| brightness | number | True | 172 |
| blur | number \| string | True | 174 |
| opacity | number | True | 176 |
| rounded | boolean \| string | True | 178 |
| invertOnDark | boolean | True | 183 |
| style | CSSProperties & DitherVars | True | 185 |
| size | number \| string | True | 268 |
| direction | DitherRevealDirection | True | 323 |
| from | number | True | 325 |
| to | number | True | 327 |
| maskClassName | string | True | 329 |
| style | CSSProperties | True | 330 |

### Defaults and motion

- Default `size` = `"lg"` (line 197).
- Default `rounded` = `true` (line 204).
- Default `invertOnDark` = `false` (line 205).
- Default `direction` = `"r"` (line 392).
- Default `from` = `0` (line 393).
- Default `to` = `65` (line 394).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
