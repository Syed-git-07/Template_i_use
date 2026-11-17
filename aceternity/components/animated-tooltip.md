# animated-tooltip

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/animated-tooltip/components/ui/animated-tooltip.tsx

[Original source](https://ui.aceternity.com/registry/animated-tooltip.json); SHA-256 `5ac351d14d3890b4af055f2a0588c1499d905d144abe4f47aa2fbd887c44a3ea`; 100 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | {     id: number;     name: string;     designation: string;     image: string;   }[] | False | 15 |
| id | number | False | 16 |
| name | string | False | 17 |
| designation | string | False | 18 |
| image | string | False | 19 |

### Defaults and motion

- `stiffness`: 100 (line 23).
- `damping`: 15 (line 23).
- `stiffness`: 260 (line 66).
- `damping`: 10 (line 67).

### Input, style and lifecycle

Events: onMouseEnter (line 53); onMouseLeave (line 54); onMouseMove (line 88).

Typography/style anchors: 64.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
