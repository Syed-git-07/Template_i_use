# svg-bands

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/svg-bands.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/svg-bands.tsx); SHA-256 `422463ccecc2941e126e7497055b75000ef461731898f34435533ec41d55e672`; 569 lines.

Imports: `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| path | string | False | 16 |
| viewBox | string | False | 17 |
| flip | BandShapeFlip | True | 18 |
| className | string | True | 19 |
| title | string | True | 21 |
| className | string | True | 49 |
| className | string | True | 107 |
| className | string | True | 122 |
| className | string | True | 143 |
| className | string | True | 197 |
| teeth | number | True | 198 |
| className | string | True | 216 |
| className | string | True | 234 |
| className | string | True | 252 |
| className | string | True | 270 |
| className | string | True | 294 |
| className | string | True | 316 |
| className | string | True | 334 |
| className | string | True | 355 |
| className | string | True | 376 |
| className | string | True | 397 |
| className | string | True | 418 |
| className | string | True | 438 |
| className | string | True | 456 |
| className | string | True | 477 |
| className | string | True | 495 |
| className | string | True | 516 |
| className | string | True | 546 |

### Defaults and motion

- Default `flip` = `"none"` (line 31).
- Default `title` = `"Decorative section shape"` (line 33).
- Default `teeth` = `12` (line 195).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
