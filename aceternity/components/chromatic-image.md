# chromatic-image

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/chromatic-image/components/ui/chromatic-image.tsx

[Original source](https://ui.aceternity.com/registry/chromatic-image.json); SHA-256 `2e111364d8fa42b9e510a26a2822eb828d6cc614d87023cf8bc85571730244e8`; 337 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | False | 7 |
| alt | string | False | 8 |
| children | React.ReactNode | True | 9 |
| className | string | True | 10 |
| backgroundColor | string | True | 11 |
| zoom | number | True | 12 |
| displacement | number | True | 13 |
| chromaticShift | number | True | 14 |
| tilt | number | True | 15 |

### Defaults and motion

- Default `backgroundColor` = `"#111111"` (line 113).
- Default `zoom` = `0.2` (line 114).
- Default `displacement` = `0.05` (line 115).
- Default `chromaticShift` = `0.01` (line 116).
- Default `tilt` = `0.3` (line 117).

### Input, style and lifecycle

Events: pointermove (line 289); pointerleave (line 290).

Typography/style anchors: 196.

Source signals: reduced_motion, cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
