# magnetic

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/magnetic.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/magnetic.tsx); SHA-256 `0831f2afde1c5bd0cfa6fdc00c5fd7c7eb62ed3e680d122a52cecf9d689f3ecf`; 113 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 14 |
| intensity | number | True | 15 |
| range | number | True | 16 |
| actionArea | 'self' \| 'parent' \| 'global' | True | 17 |
| springOptions | SpringOptions | True | 18 |

### Defaults and motion

- Default `intensity` = `0.6` (line 23).
- Default `range` = `100` (line 24).
- Default `actionArea` = `"self"` (line 25).
- `stiffness`: 26.7 (line 11).
- `damping`: 4.1 (line 11).
- `mass`: 0.2 (line 11).

### Input, style and lifecycle

Events: mousemove (line 59); mouseenter (line 73); mouseleave (line 74); onMouseEnter (line 102); onMouseLeave (line 103).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
