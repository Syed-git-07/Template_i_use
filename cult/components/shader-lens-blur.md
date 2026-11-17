# shader-lens-blur

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/shader-lens-blur.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/shader-lens-blur.tsx); SHA-256 `2517095eda43b3b31169683487cda0e25a77a509647c4f359aaa21ba1e664b29`; 732 lines.

Imports: `react`, `jotai`, `motion/react`, `next-themes`, `three`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variation | number | False | 127 |
| color1 | string | False | 128 |
| color2 | string | False | 129 |
| color3 | string | False | 130 |
| color4 | string | False | 131 |
| enableHover | boolean | False | 132 |
| invertMouse | boolean | False | 133 |
| width | string | False | 134 |
| height | string | False | 135 |

### Defaults and motion

- `duration`: 0.5 (line 356).

### Input, style and lifecycle

Events: pointermove (line 321); touchmove (line 322); pointerdown (line 323); pointerup (line 324); touchstart (line 325); touchend (line 326).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
