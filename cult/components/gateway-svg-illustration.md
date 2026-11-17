# gateway-svg-illustration

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/gateway-svg-illustration.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/gateway-svg-illustration.tsx); SHA-256 `156e0682db17d85ccc2460636e1ee149cc6e885dae451475818e085639e7d3be`; 511 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| base | string | False | 8 |
| left | string | False | 9 |
| right | string | False | 10 |
| bottom | string | False | 11 |
| clip | string | False | 12 |
| logoClip | string | False | 13 |
| top | string[] | False | 14 |
| width | number | True | 19 |
| height | number | True | 20 |
| backgroundColor | string | True | 21 |
| borderColor | string | True | 22 |
| leftLineColor | string | True | 23 |
| centerLineColor | string | True | 24 |
| rightLineColor | string | True | 25 |
| logoColor | string | True | 26 |
| iconColor | string | True | 27 |
| showBackgroundGrid | boolean | True | 28 |
| leftIcon | React.ReactNode | True | 29 |
| centerIcon | React.ReactNode | True | 30 |
| rightIcon | React.ReactNode | True | 31 |
| ids | GatewayOverheadIds | False | 35 |
| borderColor | string | False | 36 |
| backgroundColor | string | False | 37 |
| ids | GatewayOverheadIds | False | 41 |
| borderColor | string | False | 42 |
| ids | GatewayOverheadIds | False | 150 |
| backgroundColor | string | False | 161 |
| ids | GatewayOverheadIds | False | 299 |
| x | number | False | 313 |
| borderColor | string | False | 314 |
| iconColor | string | False | 330 |
| centerLineColor | string | False | 343 |
| rightLineColor | string | False | 357 |
| leftLineColor | string | False | 368 |
| ids | GatewayOverheadIds | False | 384 |
| backgroundColor | string | False | 385 |
| logoColor | string | False | 386 |
| color | string | True | 481 |

### Defaults and motion

- Default `width` = `264` (line 60).
- Default `height` = `120` (line 61).
- Default `width` = `264` (line 404).
- Default `height` = `120` (line 405).
- Default `backgroundColor` = `"transparent"` (line 407).
- Default `borderColor` = `"#EAEAEA"` (line 408).
- Default `leftLineColor` = `"#0067D6"` (line 409).
- Default `centerLineColor` = `"#FFB224"` (line 410).
- Default `rightLineColor` = `"#CA2A30"` (line 411).
- Default `logoColor` = `"#000000"` (line 412).
- Default `iconColor` = `"#171717"` (line 413).
- Default `showBackgroundGrid` = `true` (line 414).
- Default `color` = `"#171717"` (line 481).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
