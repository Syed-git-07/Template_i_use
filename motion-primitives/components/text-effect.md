# text-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-effect.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-effect.tsx); SHA-256 `3ff9d64037d8a56eb46ddf378358ddbe7e2d4612d9d3d66a56d54708e6305778`; 295 lines.

Imports: `@/lib/utils`, `motion/react`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 20 |
| per | PerType | True | 21 |
| as | keyof React.JSX.IntrinsicElements | True | 22 |
| variants | {     container?: Variants;     item?: Variants;   } | True | 23 |
| container | Variants | True | 24 |
| item | Variants | True | 25 |
| className | string | True | 27 |
| preset | PresetType | True | 28 |
| delay | number | True | 29 |
| speedReveal | number | True | 30 |
| speedSegment | number | True | 31 |
| trigger | boolean | True | 32 |
| onAnimationComplete | () => void | True | 33 |
| onAnimationStart | () => void | True | 34 |
| segmentWrapperClassName | string | True | 35 |
| containerTransition | Transition | True | 36 |
| segmentTransition | Transition | True | 37 |
| style | React.CSSProperties | True | 38 |
| container | Variants | False | 70 |
| item | Variants | False | 70 |
| segment | string | False | 115 |
| variants | Variants | False | 116 |
| per | 'line' \| 'word' \| 'char' | False | 117 |
| segmentWrapperClassName | string | True | 118 |
| transition | Transition | True | 170 |
| exit | Transition | True | 179 |

### Defaults and motion

- Default `per` = `"word"` (line 211).
- Default `as` = `"p"` (line 212).
- Default `preset` = `"fade"` (line 215).
- Default `delay` = `0` (line 216).
- Default `speedReveal` = `1` (line 217).
- Default `speedSegment` = `1` (line 218).
- Default `trigger` = `true` (line 219).
- `duration`: computed; inspect expression (line 262).

### Input, style and lifecycle

Events: onAnimationComplete (line 276); onAnimationStart (line 277).

Typography/style anchors: 51, 56, 189, 198.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
