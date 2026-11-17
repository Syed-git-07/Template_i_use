# sliding-number

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/sliding-number.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/sliding-number.tsx); SHA-256 `eb12663d39672a8c66e912069acdb33ed1fb5506c77044d3ec22d9fffb67fdc3`; 123 lines.

Imports: `react`, `motion/react`, `react-use-measure`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | number | False | 19 |
| place | number | False | 19 |
| mv | MotionValue<number> | False | 38 |
| number | number | False | 38 |
| value | number | False | 78 |
| padStart | boolean | True | 79 |
| decimalSeparator | string | True | 80 |

### Defaults and motion

- Default `padStart` = `false` (line 85).
- Default `decimalSeparator` = `"."` (line 86).
- `stiffness`: 280 (line 14).
- `damping`: 18 (line 15).
- `mass`: 0.3 (line 16).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
