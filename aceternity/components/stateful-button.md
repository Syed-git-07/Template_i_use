# stateful-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/stateful-button/components/ui/stateful-button.tsx

[Original source](https://ui.aceternity.com/registry/stateful-button.json); SHA-256 `b19e3cee5986e376b9bffb740b77747ffd3c149d150c9e36b73c395ba7cb2ef9`; 169 lines.

Imports: `@/lib/utils`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 7 |
| children | React.ReactNode | False | 8 |

### Defaults and motion

- `duration`: 0.2 (line 23).
- `duration`: 0.2 (line 37).
- `duration`: 0.2 (line 48).
- `delay`: 2 (line 60).
- `duration`: 0.2 (line 61).
- `duration`: 0.3 (line 119).
- `ease`: "linear" (line 121).

### Input, style and lifecycle

Events: onClick (line 92).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
