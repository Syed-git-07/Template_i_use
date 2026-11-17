# grid-beam

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/grid-beam.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/grid-beam.tsx); SHA-256 `e85dafee451c49e23b2d93662f3128a41457ed0079c217a7ae36870479ed31b6`; 772 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| color | RGB | False | 23 |
| op | number | False | 24 |
| h | readonly PaletteBand[] | False | 28 |
| v | readonly PaletteBand[] | False | 29 |
| rows | number | False | 240 |
| cols | number | False | 241 |
| palette | GridBeamPaletteLayers | False | 242 |
| active | boolean | False | 243 |
| fadingOut | boolean | False | 244 |
| fadeStart | number \| null | False | 245 |
| duration | number | False | 246 |
| strength | number | False | 247 |
| breathe | boolean | False | 248 |
| rows | number | True | 526 |
| cols | number | True | 527 |
| colorVariant | GridBeamPaletteKey | True | 528 |
| theme | GridBeamThemeProp | True | 530 |
| active | boolean | True | 531 |
| duration | number | True | 532 |
| strength | number | True | 533 |
| breathe | boolean | True | 534 |
| canvasRef | RefObject<HTMLCanvasElement \| null> | False | 538 |
| palette | GridBeamPaletteLayers | False | 539 |
| resolvedScheme | GridBeamColorScheme | False | 540 |
| rows | number | False | 541 |
| cols | number | False | 542 |
| fadingOut | boolean | False | 543 |
| fadeStart | number \| null | False | 544 |
| rows | number | False | 625 |
| cols | number | False | 626 |
| dividerStroke | string | True | 628 |
| borderRadius | number | True | 684 |
| borderRadius | number | True | 722 |

### Defaults and motion

- Default `rowsProp` = `3` (line 552).
- Default `colsProp` = `4` (line 553).
- Default `colorVariant` = `"colorful"` (line 554).
- Default `theme` = `"dark"` (line 555).
- Default `active` = `true` (line 556).
- Default `duration` = `3` (line 557).
- Default `strength` = `1` (line 558).
- Default `breathe` = `true` (line 559).
- Default `dividerStroke` = `"var(--border)"` (line 635).

### Input, style and lifecycle

Events: change (line 198).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
