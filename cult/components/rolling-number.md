# rolling-number

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/rolling-number.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/rolling-number.tsx); SHA-256 `e4df8960bc641aacffb23112e67dfbeb70c60477c8dceddb9864539df6b39ff9`; 43 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | number | False | 7 |
| mass | number | True | 8 |
| stiffness | number | True | 9 |
| damping | number | True | 10 |
| precision | number | True | 11 |
| format | (value: number) => string | True | 12 |
| onAnimationStart | () => void | True | 13 |
| onAnimationComplete | () => void | True | 14 |

### Defaults and motion

- Default `mass` = `0.8` (line 19).
- Default `stiffness` = `75` (line 20).
- Default `damping` = `15` (line 21).
- Default `precision` = `0` (line 22).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
