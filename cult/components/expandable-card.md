# expandable-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/expandable-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/expandable-card.tsx); SHA-256 `ae79899c8b0c5c4a9a9ad90637446bec77ff196a7b0f489f470953fb960e2824`; 556 lines.

Imports: `react`, `motion/react`, `react-use-measure`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isExpanded | boolean | False | 25 |
| toggleExpand | () => void | False | 26 |
| expandDirection | "vertical" \| "horizontal" \| "both" | False | 27 |
| expandBehavior | "replace" \| "push" | False | 28 |
| transitionDuration | number | False | 29 |
| easeType | \| "easeInOut"     \| "easeIn"     \| "easeOut"     \| "linear"     \| [number, number, number, number] | False | 30 |
| initialDelay | number | False | 36 |
| onExpandEnd | () => void | True | 37 |
| onCollapseEnd | () => void | True | 38 |
| children | ReactNode \| ((props: { isExpanded: boolean }) => ReactNode) | False | 58 |
| isExpanded | boolean | False | 58 |
| expanded | boolean | True | 59 |
| onToggle | () => void | True | 60 |
| transitionDuration | number | True | 61 |
| easeType | \| "easeInOut"     \| "easeIn"     \| "easeOut"     \| "linear"     \| [number, number, number, number] | True | 62 |
| expandDirection | "vertical" \| "horizontal" \| "both" | True | 68 |
| expandBehavior | "replace" \| "push" | True | 69 |
| initialDelay | number | True | 70 |
| onExpandStart | () => void | True | 71 |
| onExpandEnd | () => void | True | 72 |
| onCollapseStart | () => void | True | 73 |
| onCollapseEnd | () => void | True | 74 |
| initial | { [key: string]: any } | False | 150 |
| animate | { [key: string]: any } | False | 151 |
| exit | { [key: string]: any } | False | 152 |
| initial | { [key: string]: number \| string } | False | 211 |
| animate | { [key: string]: number \| string } | False | 212 |
| exit | { [key: string]: number \| string } | False | 213 |
| initial | TargetAndTransition | True | 218 |
| animate | TargetAndTransition | True | 219 |
| exit | TargetAndTransition | True | 220 |
| transition | any | True | 221 |
| preset | keyof typeof ANIMATION_PRESETS | True | 249 |
| animateIn | AnimationProps | True | 250 |
| animateOut | AnimationProps | True | 251 |
| stagger | boolean | True | 252 |
| staggerChildren | number | True | 253 |
| keepMounted | boolean | True | 254 |
| children | ReactNode | False | 352 |
| className | string | True | 353 |
| collapsedSize | { width?: number; height?: number } | True | 354 |
| width | number | True | 354 |
| height | number | True | 354 |
| expandedSize | { width?: number; height?: number } | True | 355 |
| width | number | True | 355 |
| height | number | True | 355 |
| hoverToExpand | boolean | True | 356 |
| expandDelay | number | True | 357 |
| collapseDelay | number | True | 358 |

### Defaults and motion

- Default `transitionDuration` = `0.3` (line 83).
- Default `expandDirection` = `"vertical"` (line 85).
- Default `expandBehavior` = `"replace"` (line 86).
- Default `initialDelay` = `0` (line 87).
- Default `stagger` = `false` (line 263).
- Default `staggerChildren` = `0.1` (line 264).
- Default `keepMounted` = `false` (line 265).
- Default `className` = `""` (line 365).
- Default `hoverToExpand` = `false` (line 368).
- Default `expandDelay` = `0` (line 369).
- Default `collapseDelay` = `0` (line 370).
- `stiffness`: 200 (line 22).
- `damping`: 20 (line 22).
- `bounce`: 0.2 (line 22).
- `duration`: computed; inspect expression (line 134).
- `ease`: computed; inspect expression (line 135).
- `delay`: computed; inspect expression (line 136).
- `duration`: computed; inspect expression (line 297).
- `ease`: computed; inspect expression (line 297).
- `duration`: computed; inspect expression (line 309).
- `ease`: computed; inspect expression (line 309).

### Input, style and lifecycle

Events: onHoverStart (line 436); onHoverEnd (line 437); onClick (line 487); onKeyDown (line 488).

Typography/style anchors: 317.

Source signals: keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
