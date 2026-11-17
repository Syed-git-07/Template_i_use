# text-scramble

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-scramble.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-scramble.tsx); SHA-256 `82c871355f351232f4fa3c3be96a96ceeb2b0aa321977d681dbb9707e485ace3`; 87 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 6 |
| duration | number | True | 7 |
| speed | number | True | 8 |
| characterSet | string | True | 9 |
| as | React.ElementType | True | 10 |
| className | string | True | 11 |
| trigger | boolean | True | 12 |
| onScrambleComplete | () => void | True | 13 |

### Defaults and motion

- Default `duration` = `0.8` (line 21).
- Default `speed` = `0.04` (line 22).
- Default `Component` = `"p"` (line 25).
- Default `trigger` = `true` (line 26).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
