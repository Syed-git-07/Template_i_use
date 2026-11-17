# text-animate

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/text-animate.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/text-animate.tsx); SHA-256 `6ae1081393fb86cb273bf22f50eb2c4ffba1ac83a1079714a55414bc094b219b`; 287 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 17 |
| type | AnimationType | True | 18 |
| delay | number | True | 19 |
| duration | number | True | 20 |

### Defaults and motion

- Default `type` = `"whipInUp"` (line 202).
- `damping`: 12 (line 38).
- `stiffness`: 100 (line 39).
- `duration`: 0.5 (line 54).
- `damping`: 15 (line 70).
- `stiffness`: 400 (line 70).
- `ease`: computed; inspect expression (line 86).
- `duration`: 0.85 (line 87).
- `ease`: computed; inspect expression (line 93).
- `duration`: 0.75 (line 94).
- `ease`: computed; inspect expression (line 114).
- `duration`: 0.6 (line 115).
- `duration`: 0.8 (line 121).
- `ease`: computed; inspect expression (line 122).
- `ease`: computed; inspect expression (line 139).
- `duration`: 0.45 (line 140).
- `ease`: computed; inspect expression (line 146).
- `duration`: 0.75 (line 147).
- `duration`: 0.65 (line 166).
- `ease`: computed; inspect expression (line 167).
- `duration`: 0.45 (line 189).
- `ease`: computed; inspect expression (line 193).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 29, 36, 50, 54, 63, 70, 79, 85, 92, 107, 113, 120, 132, 138, 145, 165, 188.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
