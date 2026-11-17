# direction-aware-hover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/direction-aware-hover/components/ui/direction-aware-hover.tsx

[Original source](https://ui.aceternity.com/registry/direction-aware-hover.json); SHA-256 `8667bdfa7fe1e7ae0683cea7c09ee695de84fe9632ed25ccfa85ca8801736d70`; 170 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| imageUrl | string | False | 15 |
| children | React.ReactNode \| string | False | 16 |
| childrenClassName | string | True | 17 |
| imageClassName | string | True | 18 |
| className | string | True | 19 |

### Defaults and motion

- `duration`: 0.2 (line 85).
- `ease`: "easeOut" (line 86).
- `duration`: 0.5 (line 103).
- `ease`: "easeOut" (line 104).

### Input, style and lifecycle

Events: onMouseEnter (line 66).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
