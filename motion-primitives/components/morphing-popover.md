# morphing-popover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/morphing-popover.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/morphing-popover.tsx); SHA-256 `f0802888849403bad7a55b5ebb33dd6e791a7c9727774db93f3db3cef01f0e45`; 225 lines.

Imports: `react`, `motion/react`, `@/hooks/useClickOutside`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 29 |
| open | () => void | False | 30 |
| close | () => void | False | 31 |
| uniqueId | string | False | 32 |
| variants | Variants | True | 33 |
| defaultOpen | boolean | True | 44 |
| open | boolean | True | 45 |
| onOpenChange | (open: boolean) => void | True | 46 |
| children | React.ReactNode | False | 71 |
| transition | Transition | True | 72 |
| defaultOpen | boolean | True | 73 |
| open | boolean | True | 74 |
| onOpenChange | (open: boolean) => void | True | 75 |
| variants | Variants | True | 76 |
| className | string | True | 77 |
| asChild | boolean | True | 108 |
| children | React.ReactNode | False | 109 |
| className | string | True | 110 |
| children | React.ReactNode | False | 166 |
| className | string | True | 167 |

### Defaults and motion

- Default `defaultOpen` = `false` (line 40).
- Default `asChild` = `false` (line 116).
- `bounce`: 0.1 (line 24).
- `duration`: 0.4 (line 25).

### Input, style and lifecycle

Events: onClick (line 135); onClick (line 149); keydown (line 191).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
