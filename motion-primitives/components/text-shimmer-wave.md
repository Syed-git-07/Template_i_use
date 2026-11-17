# text-shimmer-wave

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-shimmer-wave.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-shimmer-wave.tsx); SHA-256 `b30984d144d6c719df08492f8d142bfef52f0a7f29b31cac225fb6bd54bf0b27`; 90 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 7 |
| as | React.ElementType | True | 8 |
| className | string | True | 9 |
| duration | number | True | 10 |
| zDistance | number | True | 11 |
| xDistance | number | True | 12 |
| yDistance | number | True | 13 |
| spread | number | True | 14 |
| scaleDistance | number | True | 15 |
| rotateYDistance | number | True | 16 |
| transition | Transition | True | 17 |

### Defaults and motion

- Default `Component` = `"p"` (line 22).
- Default `duration` = `1` (line 24).
- Default `zDistance` = `10` (line 25).
- Default `xDistance` = `2` (line 26).
- Default `yDistance` = `-2` (line 27).
- Default `spread` = `1` (line 28).
- Default `scaleDistance` = `1.1` (line 29).
- Default `rotateYDistance` = `10` (line 30).
- `duration`: computed; inspect expression (line 75).
- `ease`: "easeInOut" (line 79).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
