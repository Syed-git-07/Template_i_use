# card-spotlight

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/card-spotlight/components/ui/card-spotlight.tsx

[Original source](https://ui.aceternity.com/registry/card-spotlight.json); SHA-256 `d1a4634badf0688668ad28471f032159c52dc3d32e7cc1d7d158812d24af3b56`; 75 lines.

Imports: `motion/react`, `react`, `@/components/ui/canvas-reveal-effect`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| radius | number | True | 15 |
| color | string | True | 16 |
| children | React.ReactNode | False | 17 |

### Defaults and motion

- Default `radius` = `350` (line 10).
- Default `color` = `"#262626"` (line 11).

### Input, style and lifecycle

Events: onMouseMove (line 41); onMouseEnter (line 42); onMouseLeave (line 43).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
