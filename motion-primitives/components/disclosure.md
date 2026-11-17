# disclosure

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/disclosure.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/disclosure.tsx); SHA-256 `05fe9162f95724dc70125337526d6b5cb1076764904f82f62ccf4940a66cb126`; 192 lines.

Imports: `react`, `motion/react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| open | boolean | False | 15 |
| toggle | () => void | False | 16 |
| variants | { expanded: Variant; collapsed: Variant } | True | 17 |
| expanded | Variant | False | 17 |
| collapsed | Variant | False | 17 |
| children | React.ReactNode | False | 25 |
| open | boolean | False | 26 |
| onOpenChange | (open: boolean) => void | True | 27 |
| variants | { expanded: Variant; collapsed: Variant } | True | 28 |
| expanded | Variant | False | 28 |
| collapsed | Variant | False | 28 |
| open | boolean | True | 73 |
| onOpenChange | (open: boolean) => void | True | 74 |
| children | React.ReactNode | False | 75 |
| className | string | True | 76 |
| variants | { expanded: Variant; collapsed: Variant } | True | 77 |
| expanded | Variant | False | 77 |
| collapsed | Variant | False | 77 |
| transition | Transition | True | 78 |
| children | React.ReactNode | False | 109 |
| className | string | True | 110 |
| key | string | False | 123 |
| preventDefault | () => void | False | 123 |
| children | React.ReactNode | False | 145 |
| className | string | True | 146 |

### Defaults and motion

- Default `openProp` = `false` (line 82).

### Input, style and lifecycle

Events: onOpenChange (line 94).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
