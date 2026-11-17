# three-d-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/three-d-carousel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/three-d-carousel.tsx); SHA-256 `c4f04fe266c520eeb2afc717c62247ae618d0a1153bd7b818dfdba2494460eca`; 247 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| defaultValue | boolean | True | 16 |
| initializeWithValue | boolean | True | 17 |
| handleClick | (imgUrl: string, index: number) => void | False | 93 |
| controls | any | False | 94 |
| cards | string[] | False | 95 |
| isCarouselActive | boolean | False | 96 |

### Defaults and motion

- Default `defaultValue` = `false` (line 25).
- Default `initializeWithValue` = `true` (line 26).
- `ease`: computed; inspect expression (line 81).
- `duration`: 0.5 (line 84).
- `ease`: computed; inspect expression (line 84).
- `stiffness`: 100 (line 137).
- `damping`: 30 (line 138).
- `mass`: 0.1 (line 139).
- `delay`: 0.5 (line 223).
- `duration`: 0.5 (line 224).
- `ease`: computed; inspect expression (line 225).

### Input, style and lifecycle

Events: change (line 51); onDrag (line 127); onDragEnd (line 131); onClick (line 155); onClick (line 211).

Typography/style anchors: 135.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
