# spinning-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/spinning-text.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/spinning-text.tsx); SHA-256 `61217d08709eaf1c82d89fae4c7030ba39e6cc6f2e45bc8f4fe3cde954186a59`; 105 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 7 |
| style | CSSProperties | True | 8 |
| duration | number | True | 9 |
| className | string | True | 10 |
| reverse | boolean | True | 11 |
| fontSize | number | True | 12 |
| radius | number | True | 13 |
| transition | Transition | True | 14 |
| variants | {     container?: Variants;     item?: Variants;   } | True | 15 |
| container | Variants | True | 16 |
| item | Variants | True | 17 |
| duration | number | True | 52 |

### Defaults and motion

- Default `duration` = `10` (line 37).
- Default `reverse` = `false` (line 40).
- Default `fontSize` = `1` (line 41).
- Default `radius` = `5` (line 42).
- `ease`: "linear" (line 23).
- `duration`: computed; inspect expression (line 52).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 87, 92.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
