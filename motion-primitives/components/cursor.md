# cursor

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/cursor.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/cursor.tsx); SHA-256 `a9bad288fc856b36c52aaee87bfbb1ed94704415767ee92b1fd25c0e652578d5`; 135 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 15 |
| className | string | True | 16 |
| springConfig | SpringOptions | True | 17 |
| attachToParent | boolean | True | 18 |
| transition | Transition | True | 19 |
| variants | {     initial: Variant;     animate: Variant;     exit: Variant;   } | True | 20 |
| initial | Variant | False | 21 |
| animate | Variant | False | 22 |
| exit | Variant | False | 23 |
| onPositionChange | (x: number, y: number) => void | True | 25 |

### Defaults and motion

- `duration`: 0 (line 69).
- `duration`: 0 (line 70).

### Input, style and lifecycle

Events: mousemove (line 62); mouseenter (line 80); mouseleave (line 84).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
