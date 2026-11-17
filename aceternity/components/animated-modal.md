# animated-modal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/animated-modal/components/ui/animated-modal.tsx

[Original source](https://ui.aceternity.com/registry/animated-modal.json); SHA-256 `9d4166aa1229b45725c62bbde513a7198639df9365253c9e7be604b00bf1ea20`; 244 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| open | boolean | False | 14 |
| setOpen | (open: boolean) => void | False | 15 |
| children | ReactNode | False | 20 |
| children | ReactNode | False | 38 |
| children | ReactNode | False | 46 |
| className | string | True | 47 |
| children | ReactNode | False | 67 |
| className | string | True | 68 |
| children | ReactNode | False | 145 |
| className | string | True | 146 |
| children | ReactNode | False | 159 |
| className | string | True | 160 |
| className | string | True | 174 |

### Defaults and motion

- `stiffness`: 260 (line 128).
- `damping`: 15 (line 129).

### Input, style and lifecycle

Events: onClick (line 56); onClick (line 197); mousedown (line 235); touchstart (line 236).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
