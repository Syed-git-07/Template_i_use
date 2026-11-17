# accordion

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/accordion.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/accordion.tsx); SHA-256 `12c5bb95afbb65c3c91334aade4d2aa0ae3b3c1e23db7b1e2ee75d3539354a80`; 198 lines.

Imports: `motion/react`, `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| expandedValue | React.Key \| null | False | 14 |
| toggleItem | (value: React.Key) => void | False | 15 |
| variants | { expanded: Variant; collapsed: Variant } | True | 16 |
| expanded | Variant | False | 16 |
| collapsed | Variant | False | 16 |
| children | ReactNode | False | 32 |
| variants | { expanded: Variant; collapsed: Variant } | True | 33 |
| expanded | Variant | False | 33 |
| collapsed | Variant | False | 33 |
| expandedValue | React.Key \| null | True | 34 |
| onValueChange | (value: React.Key \| null) => void | True | 35 |
| children | ReactNode | False | 69 |
| className | string | True | 70 |
| transition | Transition | True | 71 |
| variants | { expanded: Variant; collapsed: Variant } | True | 72 |
| expanded | Variant | False | 72 |
| collapsed | Variant | False | 72 |
| expandedValue | React.Key \| null | True | 73 |
| onValueChange | (value: React.Key \| null) => void | True | 74 |
| value | React.Key | False | 101 |
| children | ReactNode | False | 102 |
| className | string | True | 103 |
| children | ReactNode | False | 130 |
| className | string | True | 131 |
| value | React.Key | True | 140 |
| children | ReactNode | False | 157 |
| className | string | True | 158 |
| value | React.Key | True | 167 |

### Defaults and motion


### Input, style and lifecycle

Events: onValueChange (line 91); onClick (line 145).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
