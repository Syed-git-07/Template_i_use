# morph-surface

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/morph-surface.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/morph-surface.tsx); SHA-256 `5087789648a01ca9e2de59f34cffdbc0a40b29ed5eb37e7a0dc0892515075b1f`; 693 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "spring" | False | 17 |
| stiffness | number | False | 18 |
| damping | number | False | 19 |
| mass | number | True | 20 |
| delay | number | True | 21 |
| isOpen | boolean | False | 30 |
| onClick | () => void | False | 31 |
| className | string | True | 32 |
| isOpen | boolean | False | 36 |
| onClose | () => void | False | 37 |
| onSubmit | (data: FormData) => void \| Promise<void> | False | 38 |
| className | string | True | 39 |
| success | boolean | False | 43 |
| isOpen | boolean | False | 44 |
| className | string | True | 45 |
| collapsedWidth | number \| "auto" | True | 50 |
| collapsedHeight | number | True | 51 |
| expandedWidth | number | True | 52 |
| expandedHeight | number | True | 53 |
| animationSpeed | number | True | 56 |
| springConfig | SpringConfig | True | 57 |
| triggerLabel | string | True | 60 |
| triggerIcon | React.ReactNode | True | 61 |
| placeholder | string | True | 62 |
| submitLabel | string | True | 63 |
| onSubmit | (data: FormData) => void \| Promise<void> | True | 66 |
| onOpen | () => void | True | 67 |
| onClose | () => void | True | 68 |
| onSuccess | () => void | True | 69 |
| isOpen | boolean | True | 72 |
| onOpenChange | (open: boolean) => void | True | 73 |
| className | string | True | 76 |
| triggerClassName | string | True | 77 |
| contentClassName | string | True | 78 |
| renderTrigger | (props: TriggerProps) => React.ReactNode | True | 81 |
| renderContent | (props: ContentProps) => React.ReactNode | True | 82 |
| renderIndicator | (props: IndicatorProps) => React.ReactNode | True | 83 |
| showFeedback | boolean | False | 87 |
| success | boolean | False | 88 |
| openFeedback | () => void | False | 89 |
| closeFeedback | () => void | False | 90 |
| triggerLabel | string | False | 92 |
| triggerIcon | React.ReactNode | True | 93 |
| placeholder | string | False | 94 |
| submitLabel | string | False | 95 |
| onSubmit | (data: FormData) => void \| Promise<void> | True | 96 |
| onOpen | () => void | True | 97 |
| onClose | () => void | True | 98 |
| onSuccess | () => void | True | 99 |
| triggerClassName | string | True | 100 |
| contentClassName | string | True | 101 |
| renderTrigger | (props: TriggerProps) => React.ReactNode | True | 102 |
| renderContent | (props: ContentProps) => React.ReactNode | True | 103 |
| renderIndicator | (props: IndicatorProps) => React.ReactNode | True | 104 |
| animationSpeed | number | False | 105 |
| springConfig | SpringConfig | True | 106 |
| expandedWidth | number | False | 107 |
| expandedHeight | number | False | 108 |
| isOpen | boolean | True | 126 |
| onOpenChange | (open: boolean) => void | True | 127 |
| expandedWidth | number | True | 128 |
| expandedHeight | number | True | 129 |
| collapsedHeight | number | True | 130 |
| animationSpeed | number | True | 131 |
| onSuccess | () => void | False | 456 |
| children | string | False | 634 |
| className | string | True | 635 |

### Defaults and motion

- Default `collapsedHeight` = `44` (line 123).
- Default `collapsedHeight` = `44` (line 188).
- Default `triggerLabel` = `"Feedback"` (line 193).
- Default `placeholder` = `"What's on your mind?"` (line 195).
- `stiffness`: computed; inspect expression (line 328).
- `damping`: 45 (line 329).
- `mass`: 0.7 (line 330).
- `delay`: computed; inspect expression (line 331).
- `stiffness`: computed; inspect expression (line 361).
- `damping`: 35 (line 362).
- `stiffness`: computed; inspect expression (line 367).
- `damping`: 22 (line 368).
- `delay`: computed; inspect expression (line 395).
- `stiffness`: computed; inspect expression (line 474).
- `damping`: 45 (line 475).
- `mass`: 0.7 (line 476).
- `stiffness`: computed; inspect expression (line 481).
- `damping`: 35 (line 482).

### Input, style and lifecycle

Events: onClick (line 306); onSuccess (line 337); onClick (line 418); onKeyDown (line 543); onSubmit (line 573); pointerdown (line 682); click (line 683); touchend (line 684).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
