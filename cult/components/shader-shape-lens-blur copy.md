# shader-shape-lens-blur copy

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/shader-shape-lens-blur copy.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/shader-shape-lens-blur copy.tsx); SHA-256 `0270dfd4a30cadb02661d2f6c880a056086f50038fd91ce34ac4a1c22c3d38b0`; 887 lines.

Imports: `react`, `motion/react`, `three`, `@/components/ui/button`, `@/components/ui/card`, `@/components/ui/input`, `@/components/ui/label`, `@/components/ui/select`, `@/components/ui/switch`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| initialVariation | number | True | 137 |
| color1 | string | True | 138 |
| color2 | string | True | 139 |
| color3 | string | True | 140 |
| color4 | string | True | 141 |
| className | string | True | 142 |
| enableHover | boolean | True | 143 |
| invertMouse | boolean | True | 144 |
| width | string | True | 145 |
| height | string | True | 146 |
| variation | number | False | 150 |
| color1 | string | False | 151 |
| color2 | string | False | 152 |
| color3 | string | False | 153 |
| color4 | string | False | 154 |
| enableHover | boolean | False | 155 |
| invertMouse | boolean | False | 156 |
| width | string | False | 157 |
| height | string | False | 158 |
| config | ShaderConfig | False | 161 |
| variation | number | False | 359 |
| color1 | string | False | 360 |
| color2 | string | False | 361 |
| color3 | string | False | 362 |
| color4 | string | False | 363 |
| enableHover | boolean | False | 364 |
| invertMouse | boolean | False | 365 |
| width | string | False | 366 |
| height | string | False | 367 |
| type | "SET_VARIATION" | False | 371 |
| payload | number | False | 371 |
| type | "SET_COLOR" | False | 373 |
| payload | {         key: "color1" \| "color2" \| "color3" \| "color4"         value: string       } | False | 374 |
| key | "color1" \| "color2" \| "color3" \| "color4" | False | 375 |
| value | string | False | 376 |
| type | "TOGGLE_HOVER" | False | 379 |
| type | "TOGGLE_INVERT_MOUSE" | False | 380 |
| type | "SET_DIMENSION" | False | 382 |
| payload | { key: "width" \| "height"; value: string } | False | 383 |
| key | "width" \| "height" | False | 383 |
| value | string | False | 383 |

### Defaults and motion

- `duration`: 0.5 (line 337).

### Input, style and lifecycle

Events: pointermove (line 303); touchmove (line 304); pointerdown (line 305); pointerup (line 306); touchstart (line 307); touchend (line 308); onValueChange (line 449); onChange (line 472); onChange (line 478); onCheckedChange (line 489); onCheckedChange (line 497); onChange (line 508); onChange (line 516).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
