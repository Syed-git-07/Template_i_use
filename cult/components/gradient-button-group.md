# gradient-button-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/gradient-button-group.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/gradient-button-group.tsx); SHA-256 `6f9351e3ab6639ff9e9d4e4b820bda04ba1fa20c09ec3643ab35adb25295f305`; 428 lines.

Imports: `react`, `motion/react`, `motion/react-client`, `next-themes`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 43 |
| icon | React.ReactNode | False | 44 |
| label | string | False | 45 |
| isOverlayActive | boolean | False | 137 |
| isDarkMode | boolean | False | 138 |

### Defaults and motion

- `delay`: computed; inspect expression (line 144).
- `duration`: computed; inspect expression (line 145).
- `ease`: "easeOut" (line 146).
- `duration`: 0.16 (line 172).
- `ease`: "easeOut" (line 173).
- `stiffness`: 400 (line 292).
- `damping`: 30 (line 293).
- `stiffness`: 400 (line 306).
- `damping`: 30 (line 307).
- `stiffness`: 400 (line 327).
- `damping`: 30 (line 328).
- `stiffness`: 380 (line 356).
- `damping`: 30 (line 357).
- `delay`: computed; inspect expression (line 358).

### Input, style and lifecycle

Events: onClick (line 268); onLayoutAnimationComplete (line 301); onClick (line 375).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
