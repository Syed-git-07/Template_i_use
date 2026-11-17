# navbar-menu

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/navbar-menu/components/ui/navbar-menu.tsx

[Original source](https://ui.aceternity.com/registry/navbar-menu.json); SHA-256 `6c9650ea81a0c364eb9cd06230ced52170de240518fb9426d5e495b9b5afb2cc`; 122 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| setActive | (item: string) => void | False | 22 |
| active | string \| null | False | 23 |
| item | string | False | 24 |
| children | React.ReactNode | True | 25 |
| setActive | (item: string \| null) => void | False | 67 |
| children | React.ReactNode | False | 68 |
| title | string | False | 86 |
| description | string | False | 87 |
| href | string | False | 88 |
| src | string | False | 89 |

### Defaults and motion

- `mass`: 0.5 (line 9).
- `damping`: 11.5 (line 10).
- `stiffness`: 100 (line 11).
- `restDelta`: 0.001 (line 12).
- `restSpeed`: 0.001 (line 13).
- `duration`: 0.3 (line 30).

### Input, style and lifecycle

Events: onMouseEnter (line 28); onMouseLeave (line 72).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
