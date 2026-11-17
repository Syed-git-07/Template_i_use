# carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/carousel.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/carousel.tsx); SHA-256 `8d4648c85575d0f777050c41c0ec691d6b407be3e33a35f5b1bb246cf2cc6e75`; 352 lines.

Imports: `react`, `motion/react`, `@/lib/utils`, `lucide-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| index | number | False | 16 |
| setIndex | (newIndex: number) => void | False | 17 |
| itemsCount | number | False | 18 |
| setItemsCount | (newItemsCount: number) => void | False | 19 |
| disableDrag | boolean | False | 20 |
| children | ReactNode | False | 36 |
| initialIndex | number | True | 37 |
| onIndexChange | (newIndex: number) => void | True | 38 |
| disableDrag | boolean | True | 39 |
| children | ReactNode | False | 76 |
| className | string | True | 77 |
| initialIndex | number | True | 78 |
| index | number | True | 79 |
| onIndexChange | (newIndex: number) => void | True | 80 |
| disableDrag | boolean | True | 81 |
| className | string | True | 117 |
| classNameButton | string | True | 118 |
| alwaysShow | boolean | True | 119 |
| className | string | True | 191 |
| classNameButton | string | True | 192 |
| children | ReactNode | False | 230 |
| className | string | True | 231 |
| transition | Transition | True | 232 |
| children | ReactNode | False | 327 |
| className | string | True | 328 |

### Defaults and motion

- Default `initialIndex` = `0` (line 44).
- Default `disableDrag` = `false` (line 46).
- Default `initialIndex` = `0` (line 87).
- Default `disableDrag` = `false` (line 90).
- `threshold`: 0.5 (line 253).
- `damping`: 18 (line 308).
- `stiffness`: 90 (line 309).
- `duration`: 0.2 (line 311).

### Input, style and lifecycle

Events: onIndexChange (line 106); onClick (line 150); onClick (line 175); onClick (line 214); onDragEnd (line 305).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: visibility, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
