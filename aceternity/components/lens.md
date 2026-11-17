# lens

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/lens/components/ui/lens.tsx

[Original source](https://ui.aceternity.com/registry/lens.json); SHA-256 `873148d3feed8f2241ab707d2a5a37d1f5ee1113f81b08919f1ff0e5dbf8e662`; 127 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 7 |
| zoomFactor | number | True | 8 |
| lensSize | number | True | 9 |
| position | {     x: number;     y: number;   } | True | 10 |
| x | number | False | 11 |
| y | number | False | 12 |
| isStatic | boolean | True | 14 |
| isFocusing | () => void | True | 15 |
| hovering | boolean | True | 16 |
| setHovering | (hovering: boolean) => void | True | 17 |

### Defaults and motion

- Default `zoomFactor` = `1.5` (line 22).
- Default `lensSize` = `170` (line 23).
- Default `isStatic` = `false` (line 24).
- `duration`: 0.3 (line 64).
- `ease`: "easeOut" (line 64).
- `duration`: 0.3 (line 95).
- `ease`: "easeOut" (line 95).

### Input, style and lifecycle

Events: onMouseEnter (line 50); onMouseLeave (line 53); onMouseMove (line 54).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
