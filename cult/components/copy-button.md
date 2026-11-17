# copy-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/copy-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/copy-button.tsx); SHA-256 `458fc583b4f76811004f09f276f2d67ab5523e9ed9c20d3ed1637ae652b166f8`; 166 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 94 |
| src | string | True | 95 |
| layout | "inline" \| "overlay" | True | 97 |
| tooltip | string | True | 98 |

### Defaults and motion

- Default `variant` = `"ghost"` (line 89).
- Default `layout` = `"inline"` (line 90).
- `duration`: 0.3 (line 12).
- `bounce`: 0 (line 13).
- `duration`: 0 (line 22).

### Input, style and lifecycle

Events: onClick (line 125).

Typography/style anchors: 22, 29.

Source signals: reduced_motion, focus, async, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
