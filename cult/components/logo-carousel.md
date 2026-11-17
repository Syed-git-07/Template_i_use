# logo-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/logo-carousel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/logo-carousel.tsx); SHA-256 `3d4ddd95e0b5e7065d1078bcf0028c6a4049b8c9eb2a6fb69aa18f7c56229854`; 574 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 14 |
| id | number | False | 15 |
| img | React.ComponentType<React.SVGProps<SVGSVGElement>> | False | 16 |
| logos | Logo[] | False | 54 |
| index | number | False | 55 |
| currentTime | number | False | 56 |
| columnCount | number | True | 130 |

### Defaults and motion

- Default `columnCount` = `2` (line 130).
- `delay`: computed; inspect expression (line 82).
- `duration`: 0.5 (line 83).
- `ease`: "easeOut" (line 84).
- `stiffness`: 300 (line 102).
- `damping`: 20 (line 103).
- `mass`: 1 (line 104).
- `bounce`: 0.2 (line 105).
- `duration`: 0.5 (line 106).
- `ease`: "easeIn" (line 116).
- `duration`: 0.3 (line 117).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 100, 114.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
