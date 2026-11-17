# toolbar-expandable

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/toolbar-expandable.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/toolbar-expandable.tsx); SHA-256 `4a4595fc2e1a52c1e763309346569af283d951e4edd5f72cb8f4b279dcdfc19b`; 187 lines.

Imports: `react`, `react-use-measure`, `motion/react`, `@/lib/utils`, `@/hooks/useClickOutside`, `lucide-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- `bounce`: 0.1 (line 12).
- `duration`: 0.25 (line 13).

### Input, style and lifecycle

Events: onClick (line 167).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
