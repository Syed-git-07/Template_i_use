# floating-panel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/floating-panel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/floating-panel.tsx); SHA-256 `c905a5f052adf798f6daf49ac95868030edacf7b2a62bb4d5e04f5fc9d270d48`; 949 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 23 |
| openFloatingPanel | (rect: DOMRect) => void | False | 24 |
| closeFloatingPanel | () => void | False | 25 |
| uniqueId | string | False | 26 |
| note | string | False | 27 |
| setNote | (note: string) => void | False | 28 |
| triggerRect | DOMRect \| null | False | 29 |
| title | string | False | 30 |
| setTitle | (title: string) => void | False | 31 |
| children | React.ReactNode | False | 78 |
| className | string | True | 79 |
| children | React.ReactNode | False | 98 |
| className | string | True | 99 |
| title | string | False | 100 |
| children | React.ReactNode | False | 149 |
| className | string | True | 150 |
| children | React.ReactNode | False | 228 |
| children | React.ReactNode | False | 251 |
| onSubmit | (note: string) => void | True | 252 |
| className | string | True | 253 |
| children | React.ReactNode | False | 280 |
| htmlFor | string | False | 281 |
| className | string | True | 282 |
| className | string | True | 307 |
| id | string | True | 308 |
| children | React.ReactNode | False | 332 |
| className | string | True | 333 |
| children | React.ReactNode | False | 356 |
| className | string | True | 357 |
| children | React.ReactNode | False | 377 |
| className | string | True | 378 |
| className | string | True | 398 |
| className | string | True | 421 |
| children | React.ReactNode | False | 444 |
| onClick | () => void | True | 445 |
| className | string | True | 446 |

### Defaults and motion

- `bounce`: 0.1 (line 18).
- `duration`: 0.4 (line 19).
- `delay`: 0.1 (line 348).
- `delay`: 0.2 (line 369).
- `delay`: 0.3 (line 390).

### Input, style and lifecycle

Events: onClick (line 127); mousedown (line 170); keydown (line 178); onSubmit (line 272); onChange (line 326); onClick (line 410); onClick (line 460).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
