# animated-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/animated-background.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/animated-background.tsx); SHA-256 `60fe0b560827e4e6a00b2f1c2a8892203ae66a7871a8f9115d881efc60fb6bab`; 91 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | \| ReactElement<{ 'data-id': string }>[]     \| ReactElement<{ 'data-id': string }> | False | 14 |
| 'data-id' | string | False | 15 |
| 'data-id' | string | False | 16 |
| defaultValue | string | True | 17 |
| onValueChange | (newActiveId: string \| null) => void | True | 18 |
| className | string | True | 19 |
| transition | Transition | True | 20 |
| enableHover | boolean | True | 21 |

### Defaults and motion

- Default `enableHover` = `false` (line 30).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
