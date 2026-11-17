# background-gradient-animation

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-gradient-animation/components/ui/background-gradient-animation.tsx

[Original source](https://ui.aceternity.com/registry/background-gradient-animation.json); SHA-256 `162bb2955384e56b221a375c42f8980569888e7d0bcdac5ebbc94450ce09004e`; 182 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gradientBackgroundStart | string | True | 21 |
| gradientBackgroundEnd | string | True | 22 |
| firstColor | string | True | 23 |
| secondColor | string | True | 24 |
| thirdColor | string | True | 25 |
| fourthColor | string | True | 26 |
| fifthColor | string | True | 27 |
| pointerColor | string | True | 28 |
| size | string | True | 29 |
| blendingValue | string | True | 30 |
| children | React.ReactNode | True | 31 |
| className | string | True | 32 |
| interactive | boolean | True | 33 |
| containerClassName | string | True | 34 |

### Defaults and motion

- Default `gradientBackgroundStart` = `"rgb(108, 0, 162)"` (line 6).
- Default `gradientBackgroundEnd` = `"rgb(0, 17, 82)"` (line 7).
- Default `firstColor` = `"18, 113, 255"` (line 8).
- Default `secondColor` = `"221, 74, 255"` (line 9).
- Default `thirdColor` = `"100, 220, 255"` (line 10).
- Default `fourthColor` = `"200, 50, 50"` (line 11).
- Default `fifthColor` = `"180, 180, 50"` (line 12).
- Default `pointerColor` = `"140, 100, 255"` (line 13).
- Default `size` = `"80%"` (line 14).
- Default `blendingValue` = `"hard-light"` (line 15).
- Default `interactive` = `true` (line 18).

### Input, style and lifecycle

Events: onMouseMove (line 170).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
