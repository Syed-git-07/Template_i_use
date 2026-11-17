# dock

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/dock.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/dock.tsx); SHA-256 `c200860fe8909b6c6b44de5a195b77477b50d46283bd81f6b75855fd695e0e4e`; 227 lines.

Imports: `motion/react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 30 |
| className | string | True | 31 |
| distance | number | True | 32 |
| panelHeight | number | True | 33 |
| magnification | number | True | 34 |
| spring | SpringOptions | True | 35 |
| className | string | True | 39 |
| children | React.ReactNode | False | 40 |
| onClick | () => void | True | 41 |
| className | string | True | 45 |
| children | React.ReactNode | False | 46 |
| className | string | True | 50 |
| children | React.ReactNode | False | 51 |
| mouseX | MotionValue | False | 55 |
| spring | SpringOptions | False | 56 |
| magnification | number | False | 57 |
| distance | number | False | 58 |
| children | React.ReactNode | False | 62 |
| value | DocContextType | False | 63 |

### Defaults and motion

- `mass`: 0.1 (line 83).
- `stiffness`: 150 (line 83).
- `damping`: 12 (line 83).
- `duration`: 0.2 (line 195).

### Input, style and lifecycle

Events: onMouseMove (line 107); onMouseLeave (line 111); onHoverStart (line 155); onHoverEnd (line 156); onFocus (line 157); onBlur (line 158); onClick (line 166).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
