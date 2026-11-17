# cloud-shader

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/cloud-shader/components/ui/cloud-shader.tsx

[Original source](https://ui.aceternity.com/registry/cloud-shader.json); SHA-256 `4a0fd073ef2939b05b7a1d796b43574c94acc17a6bf65f35f7933ab8156cd60e`; 369 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 7 |
| children | React.ReactNode | True | 8 |
| speed | number | True | 10 |
| count | number | True | 12 |
| cloudColor | string | True | 14 |
| skyTopColor | string | True | 16 |
| skyBottomColor | string | True | 18 |

### Defaults and motion

- Default `speed` = `1` (line 229).
- Default `count` = `6` (line 230).
- Default `cloudColor` = `"#fbf8f2"` (line 231).
- Default `skyTopColor` = `"#3876ba"` (line 232).
- Default `skyBottomColor` = `"#8cbfe8"` (line 233).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 298.

Source signals: reduced_motion, cleanup, resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
