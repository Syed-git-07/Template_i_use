# circuit-board

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/circuit-board.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/circuit-board.tsx); SHA-256 `9f2dc0ae8302c8e94c2bad7a5c700eec336e80eb7ad427de000b4939b19e4df2`; 882 lines.

Imports: `react`, `lucide-react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 686 |
| href | string | False | 687 |
| icon | React.ReactNode | False | 688 |
| description | React.ReactNode | False | 689 |
| glowColor | string | False | 690 |
| glowDelay | number | False | 691 |

### Defaults and motion

- `stiffness`: 300 (line 7).
- `damping`: 24 (line 7).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 13, 26, 36, 706, 714.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
