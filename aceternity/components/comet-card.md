# comet-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/comet-card/components/ui/comet-card.tsx

[Original source](https://ui.aceternity.com/registry/comet-card.json); SHA-256 `43c862495a8c1c0a4f78d121d66b5837ca27afa5db6328895911497e7ed9b578`; 116 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| rotateDepth | number | True | 18 |
| translateDepth | number | True | 19 |
| className | string | True | 20 |
| children | React.ReactNode | False | 21 |

### Defaults and motion

- Default `rotateDepth` = `17.5` (line 13).
- Default `translateDepth` = `20` (line 14).
- `duration`: 0.2 (line 99).
- `duration`: 0.2 (line 110).

### Input, style and lifecycle

Events: onMouseMove (line 85); onMouseLeave (line 86).

Typography/style anchors: 99.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
