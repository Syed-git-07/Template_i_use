# in-view

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/in-view.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/in-view.tsx); SHA-256 `bc6044180ee9cfe4674c8626c4d91a3198b4f033a5131d793c3751a33ac407e3`; 59 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | False | 12 |
| variants | {     hidden: Variant;     visible: Variant;   } | True | 13 |
| hidden | Variant | False | 14 |
| visible | Variant | False | 15 |
| transition | Transition | True | 17 |
| viewOptions | UseInViewOptions | True | 18 |
| as | React.ElementType | True | 19 |
| once | boolean | True | 20 |

### Defaults and motion

- Default `as` = `"div"` (line 33).

### Input, style and lifecycle

Events: onAnimationComplete (line 47).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
