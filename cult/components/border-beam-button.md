# border-beam-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/border-beam-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/border-beam-button.tsx); SHA-256 `445772d8fa8934177ee5c7890882c6ee920ad5cdce2821cdb09a59c39b854783`; 115 lines.

Imports: `react`, `react`, `border-beam`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| beamSize | BorderBeamSize | True | 33 |
| borderBeamClassName | string | True | 34 |
| borderBeamStyle | CSSProperties | True | 35 |

### Defaults and motion

- Default `beamSize` = `"sm"` (line 48).
- Default `theme` = `"auto"` (line 51).
- Default `size` = `"icon-sm"` (line 101).

### Input, style and lifecycle

Events: onActivate (line 80); onDeactivate (line 81).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
