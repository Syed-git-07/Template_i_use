# text-generate-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/text-generate-effect/components/ui/text-generate-effect.tsx

[Original source](https://ui.aceternity.com/registry/text-generate-effect.json); SHA-256 `f2a73f7adcb16395da2323b2485b2eed0c59caddcdb3b6ac2c0fadae81d1c22f`; 63 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| words | string | False | 12 |
| className | string | True | 13 |
| filter | boolean | True | 14 |
| duration | number | True | 15 |

### Defaults and motion

- Default `filter` = `true` (line 9).
- Default `duration` = `0.5` (line 10).
- `duration`: computed; inspect expression (line 27).
- `delay`: computed; inspect expression (line 28).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
