# dialog

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/dialog.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/dialog.tsx); SHA-256 `655db3c05e82a0beb4324beb034bb67f34a397be8ff6b9cb5f17083bf870f0c8`; 336 lines.

Imports: `motion/react`, `react`, `@/lib/utils`, `react`, `react-dom`, `lucide-react`, `@/hooks/usePreventScroll`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 11 |
| setIsOpen | (open: boolean) => void | False | 12 |
| dialogRef | React.RefObject<HTMLDialogElement \| null> | False | 13 |
| variants | Variants | False | 14 |
| transition | Transition | True | 15 |
| ids | {     dialog: string;     title: string;     description: string;   } | False | 16 |
| dialog | string | False | 17 |
| title | string | False | 18 |
| description | string | False | 19 |
| onAnimationComplete | (definition: string) => void | False | 21 |
| handleTrigger | () => void | False | 22 |
| children | React.ReactNode | False | 42 |
| variants | Variants | True | 43 |
| transition | Transition | True | 44 |
| className | string | True | 45 |
| defaultOpen | boolean | True | 46 |
| onOpenChange | (open: boolean) => void | True | 47 |
| open | boolean | True | 48 |
| children | React.ReactNode | False | 144 |
| className | string | True | 145 |
| children | React.ReactNode | False | 168 |
| container | HTMLElement \| null | True | 169 |
| children | React.ReactNode | False | 193 |
| className | string | True | 194 |
| container | HTMLElement | True | 195 |
| children | React.ReactNode | False | 250 |
| className | string | True | 251 |
| children | React.ReactNode | False | 261 |
| className | string | True | 262 |
| children | React.ReactNode | False | 280 |
| className | string | True | 281 |
| className | string | True | 299 |
| children | React.ReactNode | True | 300 |
| disabled | boolean | True | 301 |

### Defaults and motion

- `ease`: "easeOut" (line 37).
- `duration`: 0.2 (line 38).

### Input, style and lifecycle

Events: cancel (line 95); onClick (line 154); onClick (line 222); onAnimationComplete (line 232); onClick (line 310).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
