# magnetic-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/magnetic-button/components/ui/magnetic-button.tsx

[Original source](https://ui.aceternity.com/registry/magnetic-button.json); SHA-256 `92960c6a3390d4a74da91de2eeb506da2930a532783aa4c99c78fcee01758181`; 64 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| strength | number | True | 12 |
| maxDistance | number | True | 13 |

### Defaults and motion

- Default `strength` = `0.8` (line 8).
- Default `maxDistance` = `100` (line 9).
- `stiffness`: 150 (line 57).
- `damping`: 25 (line 57).
- `mass`: 0.1 (line 57).

### Input, style and lifecycle

Events: onMouseMove (line 44); onMouseLeave (line 45).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
