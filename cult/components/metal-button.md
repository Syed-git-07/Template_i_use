# metal-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/metal-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/metal-button.tsx); SHA-256 `5fa781598dd02fffff6ed10c237fa40f418c911c6f19ce8c568ea45d7699cc7f`; 157 lines.

Imports: `react`, `react`, `class-variance-authority`, `metal-fx`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| metalVariant | MetalFxVariant | True | 66 |
| metalFxClassName | string | True | 67 |
| metalFxStyle | CSSProperties | True | 68 |

### Defaults and motion

- Default `metalVariant` = `"button"` (line 78).
- Default `preset` = `"chromatic"` (line 81).
- Default `theme` = `"auto"` (line 82).
- Default `strength` = `0.9` (line 83).
- Default `normalizeHostStyles` = `true` (line 91).
- Default `variant` = `"default"` (line 92).
- Default `size` = `"icon-sm"` (line 138).
- Default `metalVariant` = `"circle"` (line 138).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
