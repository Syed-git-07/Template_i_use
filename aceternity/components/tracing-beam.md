# tracing-beam

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/tracing-beam/components/ui/tracing-beam.tsx

[Original source](https://ui.aceternity.com/registry/tracing-beam.json); SHA-256 `99378566d3354d734f4d7da530875e6e1746ce28a6bf819df971632990d4254f`; 127 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 16 |
| className | string | True | 17 |

### Defaults and motion

- `stiffness`: 500 (line 37).
- `damping`: 90 (line 38).
- `stiffness`: 500 (line 44).
- `damping`: 90 (line 45).
- `duration`: 0.2 (line 57).
- `delay`: 0.5 (line 58).
- `duration`: 0.2 (line 70).
- `delay`: 0.5 (line 71).
- `duration`: 10 (line 93).
- `duration`: 10 (line 103).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
