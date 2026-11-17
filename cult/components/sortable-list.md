# sortable-list

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/sortable-list.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/sortable-list.tsx); SHA-256 `ed7f0f130577519a25de2181c4da602d1eaf94b5f6a4344a7a14eec39198b07f`; 297 lines.

Imports: `react`, `lucide-react`, `motion/react`, `react-use-measure`, `@/lib/utils`, `@/components/ui/checkbox`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 20 |
| checked | boolean | False | 21 |
| id | number | False | 22 |
| description | string | False | 23 |
| item | Item | False | 27 |
| order | number | False | 28 |
| onCompleteItem | (id: number) => void | False | 29 |
| onRemoveItem | (id: number) => void | False | 30 |
| renderExtra | (item: Item) => React.ReactNode | True | 31 |
| isExpanded | boolean | True | 32 |
| className | string | True | 33 |
| handleDrag | () => void | False | 34 |
| items | Item[] | False | 253 |
| setItems | Dispatch<SetStateAction<Item[]>> | False | 254 |
| onCompleteItem | (id: number) => void | False | 255 |
| renderItem | (     item: Item,     order: number,     onCompleteItem: (id: number) => void,     onRemoveItem: (id: number) => void   ) => ReactNode | False | 256 |

### Defaults and motion

- `bounce`: 0 (line 81).
- `duration`: 0.4 (line 82).
- `duration`: 0.05 (line 88).
- `bounce`: 0.1 (line 90).
- `duration`: 0.001 (line 125).
- `bounce`: 0.2 (line 153).
- `delay`: computed; inspect expression (line 154).
- `delay`: 0.17 (line 190).
- `duration`: 0.17 (line 191).
- `bounce`: 0.6 (line 193).
- `delay`: 0 (line 201).
- `duration`: 0 (line 202).
- `bounce`: 0 (line 204).
- `delay`: 0.3 (line 221).
- `duration`: 0.15 (line 222).
- `bounce`: 0.9 (line 224).
- `delay`: 0 (line 231).
- `duration`: 0.12 (line 231).

### Input, style and lifecycle

Events: onDragEnd (line 97); onCheckedChange (line 134); onPointerDown (line 176); onClick (line 238); onReorder (line 276).

Typography/style anchors: 79, 87, 189, 200, 220, 231.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
