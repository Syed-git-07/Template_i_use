# text-morph

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-morph.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-morph.tsx); SHA-256 `ba9f413805a59ccbdbf3d84964182b13b24e6921f44c405f6453700f2d018142`; 74 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 7 |
| as | React.ElementType | True | 8 |
| className | string | True | 9 |
| style | React.CSSProperties | True | 10 |
| variants | Variants | True | 11 |
| transition | Transition | True | 12 |

### Defaults and motion

- Default `Component` = `"p"` (line 17).
- `stiffness`: 280 (line 47).
- `damping`: 18 (line 48).
- `mass`: 0.3 (line 49).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
