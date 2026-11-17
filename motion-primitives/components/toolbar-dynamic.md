# toolbar-dynamic

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/toolbar-dynamic.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/toolbar-dynamic.tsx); SHA-256 `c1d464222bde2a891f00a01cbd8d512ff6e43bbf17041fd1750a8c3c02a3e3c8`; 91 lines.

Imports: `react`, `motion/react`, `@/hooks/useClickOutside`, `lucide-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 19 |
| onClick | () => void | True | 20 |
| disabled | boolean | True | 21 |
| ariaLabel | string | True | 22 |

### Defaults and motion

- `bounce`: 0.1 (line 9).
- `duration`: 0.2 (line 10).

### Input, style and lifecycle

Events: onClick (line 28); onClick (line 63); onClick (line 71).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
