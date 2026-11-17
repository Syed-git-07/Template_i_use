# kanban-board

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/kanban-board.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/kanban-board.tsx); SHA-256 `99b3316a3f9566c184e4e79b81f0777e23e02b4c1a5dbd59da5d0da7b5da91fa`; 440 lines.

Imports: `react`, `next/image`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | string | False | 80 |
| variant | TagVariant | False | 81 |
| name | string | False | 85 |
| avatar | string | True | 86 |
| id | string | False | 90 |
| title | string | False | 91 |
| tags | CardTag[] | True | 92 |
| assignee | Assignee | True | 93 |
| date | string | True | 94 |
| id | ColumnStatus | False | 98 |
| title | string | False | 99 |
| status | ColumnStatus | False | 100 |
| cards | CardData[] | False | 101 |
| cardId | string | False | 105 |
| fromColumn | ColumnStatus | False | 106 |
| label | string | False | 110 |
| variant | TagVariant | False | 111 |
| src | string | True | 115 |
| name | string | True | 116 |
| card | CardData | False | 120 |
| isDone | boolean | False | 121 |
| index | number | False | 122 |
| onDragStart | () => void | False | 123 |
| onDragEnd | () => void | False | 124 |
| isDragging | boolean | False | 125 |
| isActive | boolean | False | 129 |
| column | ColumnData | False | 133 |
| onDrop | (     cardId: string,     fromColumnId: ColumnStatus,     toColumnId: ColumnStatus   ) => void | False | 134 |
| dragState | DragState | False | 139 |
| setDragState | React.Dispatch<React.SetStateAction<DragState>> | False | 140 |

### Defaults and motion

- `stiffness`: 500 (line 145).
- `damping`: 30 (line 146).
- `stiffness`: 300 (line 150).
- `damping`: 26 (line 151).
- `delay`: computed; inspect expression (line 251).
- `stiffness`: 400 (line 259).
- `damping`: 20 (line 259).
- `stiffness`: 500 (line 333).
- `damping`: 28 (line 333).
- `delay`: 0.05 (line 384).
- `stiffness`: 400 (line 417).
- `damping`: 24 (line 417).

### Input, style and lifecycle

Events: onDragEnd (line 236); onDragStart (line 237); onDragLeave (line 414); onDragOver (line 415); onDrop (line 416); onDragEnd (line 429); onDragStart (line 430).

Typography/style anchors: 259, 280, 389.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
