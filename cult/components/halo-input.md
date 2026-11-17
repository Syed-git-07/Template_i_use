# halo-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-input.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-input.tsx); SHA-256 `015a53eddaa289eff7c980a441968dd5f09b4e3c0773a1aa4fb22b83b97624d4`; 285 lines.

Imports: `react`, `@base-ui/react/input`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | False | 20 |
| className | string | True | 21 |
| translucent | boolean | True | 22 |
| invalid | boolean | True | 23 |
| innerClassName | string | True | 25 |
| translucent | boolean | True | 154 |
| invalid | boolean | True | 155 |
| leadingSlot | ReactNode | True | 156 |
| trailingSlot | ReactNode | True | 157 |
| shellClassName | string | True | 158 |
| innerRowClassName | string | True | 160 |
| translucent | boolean | True | 225 |
| invalid | boolean | True | 226 |
| shellClassName | string | True | 227 |
| innerClassName | string | True | 228 |

### Defaults and motion

- Default `translucent` = `true` (line 32).
- Default `translucent` = `true` (line 170).
- Default `translucent` = `true` (line 238).
- Default `rows` = `4` (line 243).
- `duration`: 0.25 (line 78).
- `ease`: "easeOut" (line 78).
- `duration`: computed; inspect expression (line 88).
- `ease`: "easeInOut" (line 89).
- `duration`: computed; inspect expression (line 100).
- `ease`: "easeInOut" (line 101).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
