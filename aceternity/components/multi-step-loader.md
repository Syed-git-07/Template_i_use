# multi-step-loader

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/multi-step-loader/components/ui/multi-step-loader.tsx

[Original source](https://ui.aceternity.com/registry/multi-step-loader.json); SHA-256 `12abf9ff2c8b8893c57e85e9bee90b8eb2850b512aa1a150cdf38b00149a3d27`; 147 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 6 |
| className | string | True | 21 |
| text | string | False | 39 |
| loadingStates | LoadingState[] | False | 46 |
| value | number | True | 47 |
| loadingStates | LoadingState[] | False | 98 |
| loading | boolean | True | 99 |
| duration | number | True | 100 |
| loop | boolean | True | 101 |

### Defaults and motion

- Default `value` = `0` (line 44).
- Default `duration` = `2000` (line 95).
- Default `loop` = `true` (line 96).
- `duration`: 0.5 (line 61).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
