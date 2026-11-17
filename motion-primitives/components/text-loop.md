# text-loop

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-loop.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-loop.tsx); SHA-256 `073105bf91802dc83d63cfae538544d78b1bc227f76c5eba91c0ce3385fdd7c6`; 73 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode[] | False | 13 |
| className | string | True | 14 |
| interval | number | True | 15 |
| transition | Transition | True | 16 |
| variants | Variants | True | 17 |
| onIndexChange | (index: number) => void | True | 18 |
| trigger | boolean | True | 19 |
| mode | AnimatePresenceProps['mode'] | True | 20 |

### Defaults and motion

- Default `interval` = `2` (line 26).
- Default `trigger` = `true` (line 30).
- Default `mode` = `"popLayout"` (line 31).
- `duration`: 0.3 (line 27).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
