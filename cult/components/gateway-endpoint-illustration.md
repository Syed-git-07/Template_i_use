# gateway-endpoint-illustration

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/gateway-endpoint-illustration.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/gateway-endpoint-illustration.tsx); SHA-256 `e492b02c366cd8d5a1e2e9da30b76789af7a55ee117bd1a451486a1205b6834b`; 485 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| clip | string | False | 8 |
| circle1 | string | False | 9 |
| circle2 | string | False | 10 |
| circle3 | string | False | 11 |
| inputLine | string | False | 12 |
| width | number | True | 17 |
| height | number | True | 18 |
| backgroundColor | string | True | 19 |
| circleStrokeColor | string | True | 20 |
| centerCircleStroke | string | True | 21 |
| logoColor | string | True | 22 |
| iconColor | string | True | 23 |
| inputLineColor | string | True | 24 |
| topLeftLineColor | string | True | 25 |
| bottomLeftLineColor | string | True | 26 |
| topRightLineColor | string | True | 27 |
| bottomRightLineColor | string | True | 28 |
| iconBoxFill | string | True | 29 |
| iconBoxStroke | string | True | 30 |
| showRadialCircles | boolean | True | 31 |
| topLeftIcon | React.ReactNode | True | 32 |
| topRightIcon | React.ReactNode | True | 33 |
| bottomLeftIcon | React.ReactNode | True | 34 |
| bottomRightIcon | React.ReactNode | True | 35 |
| ids | GatewayEndpointIds | False | 75 |
| circleStrokeColor | string | False | 76 |
| backgroundColor | string | False | 77 |
| inputLineColor | string | False | 78 |
| ids | GatewayEndpointIds | False | 136 |
| backgroundColor | string | False | 147 |
| ids | GatewayEndpointIds | False | 159 |
| ids | GatewayEndpointIds | False | 187 |
| topLeftLineColor | string | False | 203 |
| bottomLeftLineColor | string | False | 204 |
| topRightLineColor | string | False | 205 |
| bottomRightLineColor | string | False | 206 |
| logoColor | string | False | 238 |
| centerCircleStroke | string | False | 239 |
| x | number | False | 262 |
| y | number | False | 263 |
| fill | string | False | 264 |
| stroke | string | False | 265 |
| children | React.ReactNode | False | 266 |
| color | string | True | 398 |
| color | string | True | 408 |
| color | string | True | 423 |
| color | string | True | 446 |
| color | string | True | 456 |

### Defaults and motion

- Default `width` = `264` (line 51).
- Default `height` = `120` (line 52).
- Default `width` = `264` (line 285).
- Default `height` = `120` (line 286).
- Default `backgroundColor` = `"transparent"` (line 288).
- Default `circleStrokeColor` = `"#EAEAEA"` (line 289).
- Default `centerCircleStroke` = `"#C9C9C9"` (line 290).
- Default `logoColor` = `"black"` (line 291).
- Default `iconColor` = `"#171717"` (line 292).
- Default `inputLineColor` = `"#C9C9C9"` (line 293).
- Default `topLeftLineColor` = `"#0067D6"` (line 294).
- Default `bottomLeftLineColor` = `"#067A6F"` (line 295).
- Default `topRightLineColor` = `"#CA2A30"` (line 296).
- Default `bottomRightLineColor` = `"#FFB224"` (line 297).
- Default `iconBoxFill` = `"white"` (line 298).
- Default `iconBoxStroke` = `"#EAEAEA"` (line 299).
- Default `showRadialCircles` = `true` (line 300).
- Default `color` = `"#171717"` (line 398).
- Default `color` = `"#171717"` (line 408).
- Default `color` = `"#171717"` (line 423).
- Default `color` = `"#171717"` (line 446).
- Default `color` = `"black"` (line 456).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
