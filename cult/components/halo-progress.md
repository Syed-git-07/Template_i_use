# halo-progress

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-progress.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-progress.tsx); SHA-256 `39ee25bf1fbcd0ff3922ee20ff18050c2fe3da4eacc4c5c2ed6350da286a93e2`; 191 lines.

Imports: `react`, `@base-ui/react/progress`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 26 |
| reduceMotion | boolean | False | 27 |
| label | ReactNode | True | 60 |
| showValue | boolean | True | 62 |
| translucent | boolean | True | 64 |
| trackClassName | string | True | 65 |
| indicatorClassName | string | True | 66 |

### Defaults and motion

- Default `translucent` = `true` (line 73).
- Default `min` = `0` (line 77).
- Default `max` = `100` (line 78).
- `bounce`: 0.12 (line 17).
- `damping`: 34 (line 18).
- `stiffness`: 420 (line 19).
- `duration`: computed; inspect expression (line 48).
- `ease`: "easeInOut" (line 49).
- `duration`: 0.22 (line 130).
- `ease`: "easeOut" (line 130).
- `duration`: computed; inspect expression (line 140).
- `ease`: "easeInOut" (line 141).
- `duration`: 0 (line 176).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, async, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
