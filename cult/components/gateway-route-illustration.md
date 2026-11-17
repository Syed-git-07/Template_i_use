# gateway-route-illustration

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/gateway-route-illustration.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/gateway-route-illustration.tsx); SHA-256 `94b0e418cef66a0232d7275de89cb4b2ed3d02715947df8a9a8124f5d849e94d`; 368 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| clip | string | False | 8 |
| gradientRingClip | string | False | 9 |
| width | number | True | 14 |
| height | number | True | 15 |
| backgroundColor | string | True | 16 |
| borderColor | string | True | 17 |
| iconBoxFill | string | True | 18 |
| iconBoxStroke | string | True | 19 |
| logoColor | string | True | 20 |
| innerCircleColor | string | True | 21 |
| topArcColor | string | True | 22 |
| bottomArcColor | string | True | 23 |
| leftArcColor | string | True | 24 |
| iconColor | string | True | 25 |
| topIcon | React.ReactNode | True | 26 |
| leftIcon | React.ReactNode | True | 27 |
| rightIcon | React.ReactNode | True | 28 |
| showGradientRing | boolean | True | 29 |
| gradientColor | string | True | 30 |
| ids | GatewayRoutingIds | False | 61 |
| ids | GatewayRoutingIds | False | 77 |
| backgroundColor | string | False | 88 |
| ids | GatewayRoutingIds | False | 104 |
| gradientColor | string | False | 105 |
| topArcColor | string | False | 133 |
| bottomArcColor | string | False | 134 |
| leftArcColor | string | False | 135 |
| x | number | False | 170 |
| y | number | False | 171 |
| fill | string | False | 172 |
| stroke | string | False | 173 |
| logoColor | string | False | 193 |
| innerCircleColor | string | False | 194 |
| color | string | True | 296 |
| color | string | True | 309 |
| color | string | True | 344 |

### Defaults and motion

- Default `width` = `264` (line 43).
- Default `height` = `120` (line 44).
- Default `width` = `264` (line 218).
- Default `height` = `120` (line 219).
- Default `backgroundColor` = `"transparent"` (line 221).
- Default `borderColor` = `"#EAEAEA"` (line 222).
- Default `iconBoxFill` = `"white"` (line 223).
- Default `iconBoxStroke` = `"#EAEAEA"` (line 224).
- Default `logoColor` = `"black"` (line 225).
- Default `innerCircleColor` = `"#C9C9C9"` (line 226).
- Default `topArcColor` = `"#0067D6"` (line 227).
- Default `bottomArcColor` = `"#CA2A30"` (line 228).
- Default `leftArcColor` = `"#FFB224"` (line 229).
- Default `iconColor` = `"#171717"` (line 230).
- Default `showGradientRing` = `true` (line 234).
- Default `gradientColor` = `"#1F1F1F"` (line 235).
- Default `color` = `"#171717"` (line 296).
- Default `color` = `"#171717"` (line 309).
- Default `color` = `"#171717"` (line 344).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
