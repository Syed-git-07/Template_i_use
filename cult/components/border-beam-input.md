# border-beam-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/border-beam-input.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/border-beam-input.tsx); SHA-256 `862b090aa6d3aac5c1fbd4d7970eadf3d1458f939fefb572d2792b060b620975`; 233 lines.

Imports: `react`, `react`, `@base-ui/react/input`, `border-beam`, `@/lib/utils`, `@/components/ui/input-group`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| beamSize | BorderBeamSize | True | 58 |
| borderBeamClassName | string | True | 59 |
| borderBeamStyle | CSSProperties | True | 60 |
| pill | boolean | True | 66 |
| pill | boolean | True | 137 |

### Defaults and motion

- Default `beamSize` = `"line"` (line 72).
- Default `theme` = `"auto"` (line 75).
- Default `beamSize` = `"line"` (line 145).
- Default `theme` = `"auto"` (line 148).

### Input, style and lifecycle

Events: onActivate (line 107); onDeactivate (line 108); onActivate (line 175); onDeactivate (line 176).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
