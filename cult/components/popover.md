# popover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/popover.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/popover.tsx); SHA-256 `c868d836944ea4eedbbb07f173a5d47d80b3354fa536388f98eb49d5e6b91eb3`; 353 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 41 |
| openPopover | () => void | False | 42 |
| closePopover | () => void | False | 43 |
| uniqueId | string | False | 44 |
| note | string | False | 45 |
| setNote | (note: string) => void | False | 46 |
| children | React.ReactNode | False | 74 |
| className | string | True | 75 |
| children | React.ReactNode | False | 98 |
| className | string | True | 99 |
| children | React.ReactNode | False | 126 |
| className | string | True | 127 |
| children | React.ReactNode | False | 175 |
| onSubmit | (note: string) => void | True | 176 |
| className | string | True | 177 |
| children | React.ReactNode | False | 204 |
| className | string | True | 205 |
| className | string | True | 229 |
| children | React.ReactNode | False | 249 |
| className | string | True | 250 |
| className | string | True | 265 |
| className | string | True | 284 |
| children | React.ReactNode | False | 306 |
| className | string | True | 307 |
| children | React.ReactNode | False | 325 |
| className | string | True | 326 |
| children | React.ReactNode | False | 337 |
| onClick | () => void | True | 338 |
| className | string | True | 339 |

### Defaults and motion

- `bounce`: 0.05 (line 18).
- `duration`: 0.3 (line 19).

### Input, style and lifecycle

Events: mousedown (line 33); onClick (line 116); keydown (line 143); onSubmit (line 196); onChange (line 243); onClick (line 275); onClick (line 347).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
