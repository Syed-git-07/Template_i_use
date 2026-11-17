# scroll-progress

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/scroll-progress.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/scroll-progress.tsx); SHA-256 `a08844e10e42a5fe06863ff3648db80e9e7028634e7e71db174bf244c6a6726a`; 43 lines.

Imports: `motion/react`, `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 8 |
| springOptions | SpringOptions | True | 9 |
| containerRef | RefObject<HTMLDivElement> | True | 10 |

### Defaults and motion

- `stiffness`: 200 (line 14).
- `damping`: 50 (line 15).
- `restDelta`: 0.001 (line 16).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
