# image-comparison

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/image-comparison.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/image-comparison.tsx); SHA-256 `724cdc59efd05755f70357449a219de392fc6a6ed00ca73a258f74553449a1d9`; 148 lines.

Imports: `@/lib/utils`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| sliderPosition | number | False | 15 |
| setSliderPosition | (pos: number) => void | False | 16 |
| motionSliderPosition | MotionValue<number> | False | 17 |
| children | React.ReactNode | False | 23 |
| className | string | True | 24 |
| enableHover | boolean | True | 25 |
| springOptions | SpringOptions | True | 26 |
| className | string | True | 97 |
| alt | string | False | 98 |
| src | string | False | 99 |
| position | 'left' \| 'right' | False | 100 |
| className | string | False | 128 |
| children | React.ReactNode | True | 129 |

### Defaults and motion

- `bounce`: 0 (line 30).
- `duration`: 0 (line 31).

### Input, style and lifecycle

Events: onMouseMove (line 77); onMouseDown (line 78); onMouseUp (line 79); onMouseLeave (line 80); onTouchMove (line 81); onTouchStart (line 82); onTouchEnd (line 83).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
