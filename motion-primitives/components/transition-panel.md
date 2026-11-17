# transition-panel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/transition-panel.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/transition-panel.tsx); SHA-256 `786a7ed5dd39c86912796e1928b621c57d94bc35bf49a18b1ecbcb168ef65cb0`; 49 lines.

Imports: `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode[] | False | 12 |
| className | string | True | 13 |
| transition | Transition | True | 14 |
| activeIndex | number | False | 15 |
| variants | { enter: Variant; center: Variant; exit: Variant } | True | 16 |
| enter | Variant | False | 16 |
| center | Variant | False | 16 |
| exit | Variant | False | 16 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
