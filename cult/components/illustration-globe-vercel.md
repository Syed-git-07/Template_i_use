# illustration-globe-vercel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-globe-vercel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-globe-vercel.tsx); SHA-256 `a4db75ebcc5e27b26f75290c641020172d16da0cc5d89b2b8c4c9dc0e9661631`; 1036 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| d | string | False | 18 |
| viewBox | string | True | 18 |
| id | string | False | 21 |
| trajectory | TrajectoryStep[] | False | 22 |
| icon | NodeIcon | True | 23 |
| pathD | string | False | 27 |
| waypoints | { x: number; y: number }[] | False | 28 |
| x | number | False | 28 |
| y | number | False | 28 |
| endPt | { x: number; y: number } | False | 29 |
| x | number | False | 29 |
| y | number | False | 29 |
| status | DeployStatus | True | 33 |
| nodes | DeployNode[] | True | 34 |
| accentColor | string | True | 35 |
| duration | number | True | 36 |
| className | string | True | 37 |
| onReplay | () => void | True | 38 |
| cx | number | False | 210 |
| cy | number | False | 211 |
| radius | number | False | 212 |
| wireColor | string | False | 213 |
| pathD | string | False | 266 |
| waypoints | { x: number; y: number }[] | False | 267 |
| x | number | False | 267 |
| y | number | False | 267 |
| accent | string | False | 268 |
| duration | number | False | 269 |
| id | string | False | 270 |
| x | number | False | 384 |
| y | number | False | 385 |
| accent | string | False | 386 |
| wireColor | string | False | 387 |
| duration | number | False | 388 |
| waypointCount | number | False | 389 |
| icon | NodeIcon | True | 390 |
| animationKey | number | False | 476 |
| width | number | False | 477 |
| height | number | False | 478 |
| children | React.ReactNode | False | 479 |
| statusLabel | string | False | 499 |
| onReplay | () => void | False | 500 |
| status | DeployStatus | False | 673 |
| accent | string | False | 674 |
| preset | NodePresetName | False | 675 |
| onStatusChange | (status: DeployStatus) => void | False | 676 |
| onPresetChange | (preset: NodePresetName) => void | False | 677 |
| onAccentChange | (color: string) => void | False | 678 |

### Defaults and motion

- Default `status` = `"deployed"` (line 571).
- Default `duration` = `4.5` (line 574).
- Default `className` = `""` (line 575).

### Input, style and lifecycle

Events: onClick (line 531); onMouseEnter (line 532); onMouseLeave (line 536); onReplay (line 660); onClick (line 734); onMouseDown (line 735); onMouseLeave (line 738); onMouseUp (line 741); onClick (line 777); onMouseDown (line 778); onMouseLeave (line 781); onMouseUp (line 784); onClick (line 819); onMouseDown (line 820); onMouseLeave (line 823); onMouseUp (line 826); onAccentChange (line 997); onPresetChange (line 998); onStatusChange (line 999).

Typography/style anchors: 519, 547, 692, 693, 840, 987.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
