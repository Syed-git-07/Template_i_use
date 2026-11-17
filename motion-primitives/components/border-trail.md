# border-trail

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/border-trail.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/border-trail.tsx); SHA-256 `76ff37e0a1eba249e6ba325902602f3fc271679e0b6f386cd2739d779dcfd157`; 44 lines.

Imports: `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 6 |
| size | number | True | 7 |
| transition | Transition | True | 8 |
| onAnimationComplete | () => void | True | 9 |
| style | React.CSSProperties | True | 10 |

### Defaults and motion

- Default `size` = `60` (line 15).
- `duration`: 5 (line 22).
- `ease`: "linear" (line 23).

### Input, style and lifecycle

Events: onAnimationComplete (line 39).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
