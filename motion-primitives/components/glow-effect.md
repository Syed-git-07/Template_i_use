# glow-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/glow-effect.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/glow-effect.tsx); SHA-256 `3e480f15fe6b701bc0a96cd6101d3be6386664a69637677613964b0d92ccd0db`; 152 lines.

Imports: `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 6 |
| style | React.CSSProperties | True | 7 |
| colors | string[] | True | 8 |
| mode | \| 'rotate'     \| 'pulse'     \| 'breathe'     \| 'colorShift'     \| 'flowHorizontal'     \| 'static' | True | 9 |
| blur | \| number     \| 'softest'     \| 'soft'     \| 'medium'     \| 'strong'     \| 'stronger'     \| 'strongest'     \| 'none' | True | 16 |
| transition | Transition | True | 25 |
| scale | number | True | 26 |
| duration | number | True | 27 |

### Defaults and motion

- Default `mode` = `"rotate"` (line 34).
- Default `blur` = `"medium"` (line 35).
- Default `scale` = `1` (line 37).
- Default `duration` = `5` (line 38).
- `duration`: computed; inspect expression (line 42).
- `ease`: "linear" (line 43).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 52, 63, 78, 90, 102.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
