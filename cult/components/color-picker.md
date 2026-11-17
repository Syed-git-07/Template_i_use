# color-picker

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/color-picker.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/color-picker.tsx); SHA-256 `3b5827e2cf938fab58fdcf14f3087e097ba09187ab455313bf0125ee75b2c3b5`; 270 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/components/ui/button`, `@/components/ui/input`, `@/components/ui/label`, `@/components/ui/popover`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| color | string | False | 83 |
| onChange | (color: string) => void | False | 84 |

### Defaults and motion

- `duration`: 0.2 (line 178).
- `duration`: 0.2 (line 254).

### Input, style and lifecycle

Events: onOpenChange (line 159); onClick (line 190); onChange (line 208); onChange (line 227); onClick (line 245).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
