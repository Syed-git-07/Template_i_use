# infinite-slider

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/infinite-slider.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/infinite-slider.tsx); SHA-256 `d2c44690dccc07991df041a7cf6efb3ade87a1cf37f220006d95d377be9d8243`; 114 lines.

Imports: `@/lib/utils`, `motion/react`, `react`, `react-use-measure`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 8 |
| gap | number | True | 9 |
| speed | number | True | 10 |
| speedOnHover | number | True | 11 |
| direction | 'horizontal' \| 'vertical' | True | 12 |
| reverse | boolean | True | 13 |
| className | string | True | 14 |

### Defaults and motion

- Default `gap` = `16` (line 19).
- Default `speed` = `100` (line 20).
- Default `direction` = `"horizontal"` (line 22).
- Default `reverse` = `false` (line 23).
- `ease`: "linear" (line 48).
- `duration`: computed; inspect expression (line 49).
- `ease`: "linear" (line 57).
- `duration`: computed; inspect expression (line 58).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
