# dock

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/dock.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/dock.tsx); SHA-256 `b43963891160667f283b1c0cfcd5dda2a59a7d1311bd36b2aa872109325f7d50`; 445 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| width | number | False | 28 |
| hovered | boolean | False | 29 |
| setIsZooming | (value: boolean) => void | False | 30 |
| zoomLevel | MotionValue<number> | False | 31 |
| mouseX | MotionValue<number> | False | 32 |
| animatingIndexes | number[] | False | 33 |
| setAnimatingIndexes | (indexes: number[]) => void | False | 34 |
| className | string | True | 56 |
| children | ReactNode | False | 57 |
| src | string | False | 133 |
| id | string | False | 134 |
| children | ReactNode | True | 135 |
| children | ReactNode | False | 195 |
| id | string | False | 196 |
| onChange | (position: { value: { x: number; y: number } }) => void | True | 390 |
| value | { x: number; y: number } | False | 390 |
| x | number | False | 390 |
| y | number | False | 390 |

### Defaults and motion

- `delay`: 0.2 (line 161).
- `duration`: 0 (line 167).
- `stiffness`: 320 (line 207).
- `damping`: 20 (line 208).
- `mass`: 0.1 (line 209).
- `stiffness`: 300 (line 214).
- `damping`: 20 (line 215).
- `duration`: 0.5 (line 263).
- `duration`: 0.5 (line 275).
- `mass`: 0.1 (line 296).
- `stiffness`: 150 (line 296).
- `damping`: 12 (line 296).
- `duration`: 0 (line 325).

### Input, style and lifecycle

Events: onMouseMove (line 108); onMouseLeave (line 116); onClick (line 304); resize (line 365); mousemove (line 423).

Typography/style anchors: 161, 167, 260, 275, 325.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
