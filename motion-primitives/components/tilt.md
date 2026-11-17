# tilt

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/tilt.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/tilt.tsx); SHA-256 `aeeee396523e7f063fb4c4aab132f02cc8daeb91d40ea8693eb97917d7023331`; 93 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 15 |
| className | string | True | 16 |
| style | MotionStyle | True | 17 |
| rotationFactor | number | True | 18 |
| isRevese | boolean | True | 19 |
| springOptions | SpringOptions | True | 20 |

### Defaults and motion

- Default `rotationFactor` = `15` (line 27).
- Default `isRevese` = `false` (line 28).

### Input, style and lifecycle

Events: onMouseMove (line 86); onMouseLeave (line 87).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
