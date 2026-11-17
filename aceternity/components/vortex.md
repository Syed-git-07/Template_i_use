# vortex

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/vortex/components/ui/vortex.tsx

[Original source](https://ui.aceternity.com/registry/vortex.json); SHA-256 `bcd5dbeee17f5124b3a07aa3de29c44e96188778c5a53d82e3523eb0495e38bf`; 269 lines.

Imports: `@/lib/utils`, `react`, `simplex-noise`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | any | True | 8 |
| className | string | True | 9 |
| containerClassName | string | True | 10 |
| particleCount | number | True | 11 |
| rangeY | number | True | 12 |
| baseHue | number | True | 13 |
| baseSpeed | number | True | 14 |
| rangeSpeed | number | True | 15 |
| baseRadius | number | True | 16 |
| rangeRadius | number | True | 17 |
| backgroundColor | string | True | 18 |

### Defaults and motion


### Input, style and lifecycle

Events: resize (line 242).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
