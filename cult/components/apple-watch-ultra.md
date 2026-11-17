# apple-watch-ultra

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/apple-watch-ultra.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/apple-watch-ultra.tsx); SHA-256 `9ad25de6d7c58ac5606e3c760239bb8663d196fc4781bbdd632cc66034eb1140`; 528 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| position | "top-left" \| "top-right" \| "bottom-left" \| "bottom-right" | False | 488 |
| icon | React.ReactNode | False | 489 |
| value | string | False | 490 |
| label | string | False | 491 |
| isActive | boolean | False | 492 |
| onClick | () => void | False | 493 |
| ariaLabel | string | False | 494 |

### Defaults and motion

- `duration`: 0.2 (line 15).
- `ease`: computed; inspect expression (line 15).
- `duration`: 0.34 (line 18).
- `bounce`: 0.22 (line 19).
- `duration`: 0.01 (line 30).

### Input, style and lifecycle

Events: onClick (line 179); onClick (line 220); onExitComplete (line 330); onClick (line 423); onClick (line 433); onClick (line 443); onClick (line 453); onClick (line 513).

Typography/style anchors: 365, 402.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
