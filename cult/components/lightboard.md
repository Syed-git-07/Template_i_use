# lightboard

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/lightboard.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/lightboard.tsx); SHA-256 `a03574f9d4d7b21374d37461e1f8c7ae6bfa41038d75efef9d6b9fcd1d27dba4`; 695 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gap | number | True | 9 |
| rows | number | True | 10 |
| lightSize | number | True | 11 |
| updateInterval | number | True | 12 |
| text | string | False | 13 |
| font | "default" \| "7segment" | True | 14 |
| colors | Partial<LightBoardColors> | True | 15 |
| disableDrawing | boolean | True | 16 |
| controlledDrawState | PatternCell | True | 17 |
| onDrawStateChange | (newState: PatternCell) => void | True | 18 |
| controlledHoverState | boolean | True | 19 |
| onHoverStateChange | (isHovered: boolean) => void | True | 20 |
| drawLine | string | False | 24 |
| background | string | False | 25 |
| textDim | string | False | 26 |
| textBright | string | False | 27 |
| x | number | False | 166 |
| y | number | False | 166 |

### Defaults and motion

- Default `gap` = `1` (line 131).
- Default `lightSize` = `4` (line 132).
- Default `rows` = `5` (line 133).
- Default `font` = `"default"` (line 134).
- Default `updateInterval` = `10` (line 135).
- Default `disableDrawing` = `true` (line 138).

### Input, style and lifecycle

Events: resize (line 189); onMouseDown (line 460); onMouseUp (line 461); onMouseMove (line 462); onMouseEnter (line 463); onMouseLeave (line 466); onTouchStart (line 470); onTouchEnd (line 471); onTouchMove (line 472).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
