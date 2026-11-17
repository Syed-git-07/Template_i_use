# spotlight

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/spotlight.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/spotlight.tsx); SHA-256 `37e53afea62615a781bc6a583670dcd896df18b53289304b4e738dfab72e5107`; 86 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 7 |
| size | number | True | 8 |
| springOptions | SpringOptions | True | 9 |

### Defaults and motion

- Default `size` = `200` (line 14).
- `bounce`: 0 (line 15).

### Input, style and lifecycle

Events: mousemove (line 53); mouseenter (line 56); mouseleave (line 59).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
