# shift-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/shift-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/shift-card.tsx); SHA-256 `8b56ded589fdb858deb430e47c66b8c66977175c8e6feec9d5c86ce59a7eb8c0`; 136 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 10 |
| topContent | React.ReactNode | True | 11 |
| middleContent | React.ReactNode | True | 12 |
| topAnimateContent | React.ReactNode | True | 13 |
| bottomContent | React.ReactNode | True | 14 |
| isHovered | boolean | False | 28 |

### Defaults and motion

- `duration`: 0.3 (line 40).
- `delay`: 0.1 (line 40).
- `ease`: "circIn" (line 40).

### Input, style and lifecycle

Events: onMouseEnter (line 96); onMouseLeave (line 97); onClick (line 98); onTapCancel (line 99); onTap (line 100).

Typography/style anchors: 40.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
