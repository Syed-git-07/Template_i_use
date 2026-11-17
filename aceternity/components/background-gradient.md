# background-gradient

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-gradient/components/ui/background-gradient.tsx

[Original source](https://ui.aceternity.com/registry/background-gradient.json); SHA-256 `b00bbd960069dac2740889af5bdffcc4eaa245b465de7433a145742e628799f4`; 73 lines.

Imports: `@/lib/utils`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 11 |
| className | string | True | 12 |
| containerClassName | string | True | 13 |
| animate | boolean | True | 14 |

### Defaults and motion

- Default `animate` = `true` (line 9).
- `duration`: 5 (line 33).
- `duration`: 5 (line 54).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
