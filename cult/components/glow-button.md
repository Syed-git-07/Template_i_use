# glow-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/glow-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/glow-button.tsx); SHA-256 `9a1d58b159e9d1766e3f8b7f7148d9df04bbcdc565115cc28078b62a794438a6`; 107 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| href | string | False | 7 |
| text | string | False | 8 |
| glowColor | string | True | 9 |
| textColor | string | True | 10 |
| backgroundColor | string | True | 11 |

### Defaults and motion

- Default `glowColor` = `"#FFAA81"` (line 17).
- Default `textColor` = `"black"` (line 18).
- Default `backgroundColor` = `"#d1d1d1"` (line 19).

### Input, style and lifecycle

Events: mousemove (line 37); onMouseEnter (line 64); onMouseLeave (line 65).

Typography/style anchors: 72.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
