# liquid-glass

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/liquid-glass/components/ui/liquid-glass.tsx

[Original source](https://ui.aceternity.com/registry/liquid-glass.json); SHA-256 `f72a0351d1bbeefa54680bfe10d3ed8d863ae48c5c1341ee2fefe745ed202a6c`; 400 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| contentClassName | string | True | 14 |
| radius | number | True | 16 |
| bevelDepth | number | True | 18 |
| scale | number | True | 20 |
| aberration | number | True | 22 |
| frost | number | True | 24 |
| tint | number | True | 26 |
| id | string | False | 52 |
| svg | string | False | 52 |
| width | number | False | 205 |
| height | number | False | 206 |
| radius | number | False | 207 |
| bevelDepth | number | False | 208 |
| gain | number | True | 209 |
| light | { x: number; y: number } | True | 210 |
| x | number | False | 210 |
| y | number | False | 210 |
| dpr | number | True | 211 |
| id | string | False | 353 |
| mapUrl | string | False | 354 |
| width | number | False | 355 |
| height | number | False | 356 |
| scale | number | False | 357 |
| aberration | number | False | 358 |
| frost | number | False | 359 |

### Defaults and motion

- Default `radius` = `999` (line 39).
- Default `bevelDepth` = `14` (line 40).
- Default `scale` = `48` (line 41).
- Default `aberration` = `4` (line 42).
- Default `frost` = `0.4` (line 43).
- Default `tint` = `0.12` (line 44).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
