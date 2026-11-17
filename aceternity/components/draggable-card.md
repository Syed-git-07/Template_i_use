# draggable-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/draggable-card/components/ui/draggable-card.tsx

[Original source](https://ui.aceternity.com/registry/draggable-card.json); SHA-256 `a248f4cc3f94a08accb0a57117ad4748308867c19b01aade8331bc2eafb7a81a`; 192 lines.

Imports: `@/lib/utils`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 18 |
| children | React.ReactNode | True | 19 |
| className | string | True | 185 |
| children | React.ReactNode | True | 186 |

### Defaults and motion

- `stiffness`: 100 (line 37).
- `damping`: 20 (line 38).
- `mass`: 0.5 (line 39).
- `duration`: 0.8 (line 136).
- `ease`: computed; inspect expression (line 137).
- `stiffness`: 50 (line 140).
- `damping`: 15 (line 141).
- `mass`: 0.8 (line 142).
- `duration`: 0.8 (line 146).
- `ease`: computed; inspect expression (line 147).
- `stiffness`: 50 (line 150).
- `damping`: 15 (line 151).
- `mass`: 0.8 (line 152).

### Input, style and lifecycle

Events: resize (line 77); onDragStart (line 112); onDragEnd (line 115); onMouseMove (line 163); onMouseLeave (line 164).

Typography/style anchors: 121.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
