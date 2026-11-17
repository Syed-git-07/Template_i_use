# side-panel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/side-panel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/side-panel.tsx); SHA-256 `facbe55dea975eb4f30196188c51e239feabffba5692ef2e75150be7ce6b8fb9`; 129 lines.

Imports: `react`, `motion/react`, `react-use-measure`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| panelOpen | boolean | False | 10 |
| handlePanelOpen | () => void | False | 11 |
| className | string | True | 12 |
| videoUrl | string | True | 13 |
| renderButton | (handleToggle: () => void) => ReactNode | True | 14 |
| children | ReactNode | False | 15 |
| children | React.ReactNode | False | 97 |

### Defaults and motion

- `duration`: 0.3 (line 22).
- `ease`: computed; inspect expression (line 23).
- `duration`: 0.2 (line 29).
- `ease`: computed; inspect expression (line 29).
- `duration`: 0.6 (line 33).
- `ease`: computed; inspect expression (line 33).
- `duration`: 0.2 (line 48).
- `ease`: computed; inspect expression (line 48).
- `bounce`: 0.02 (line 53).
- `duration`: 0.65 (line 53).
- `duration`: computed; inspect expression (line 61).
- `ease`: computed; inspect expression (line 104).
- `duration`: 0.4 (line 105).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 21, 29.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
