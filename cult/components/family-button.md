# family-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/family-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/family-button.tsx); SHA-256 `fa4794f48a2d87a7ec3309c0c496ed24fe6e25cde2a69103e903562e6fa908a3`; 166 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 12 |
| isExpanded | boolean | False | 61 |
| toggleExpand | () => void | False | 62 |
| children | ReactNode | False | 63 |

### Defaults and motion

- `delay`: 0.3 (line 42).
- `duration`: 0.4 (line 43).
- `ease`: "easeOut" (line 44).
- `damping`: 25 (line 91).
- `stiffness`: 400 (line 92).
- `ease`: "easeOut" (line 112).
- `duration`: 0.3 (line 113).
- `duration`: 0.4 (line 130).
- `duration`: 0.4 (line 152).

### Input, style and lifecycle

Events: onClick (line 124); onClick (line 146).

Typography/style anchors: 41, 89, 110, 129, 151.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
