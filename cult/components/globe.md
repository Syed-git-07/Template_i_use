# globe

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/globe.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/globe.tsx); SHA-256 `b76d213920cb58cc6ed37c65c3b3c9de0740d3c01279ee06fcd4647244348744`; 1483 lines.

Imports: `react`, `cobe`, `motion/react`, `next-themes`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| theta | number | False | 20 |
| dark | number | False | 21 |
| mapBrightness | number | False | 22 |
| markerColor | [number, number, number] | False | 23 |
| baseColor | [number, number, number] | False | 24 |
| arcColor | [number, number, number] | False | 25 |
| markerSize | number | False | 26 |
| markerElevation | number | False | 27 |
| id | string | False | 799 |
| location | [number, number] | False | 799 |
| update | (state: Record<string, unknown>) => void | False | 893 |
| destroy | () => void | False | 894 |
| content | React.ReactNode | False | 963 |
| splitWords | boolean | True | 964 |
| className | string | True | 1003 |
| title | string | False | 1004 |
| className | string | True | 1043 |
| globeSize | number | True | 1044 |
| title | string | True | 1045 |
| orbitPhrase | string | True | 1046 |
| hideCenterTitle | boolean | True | 1048 |
| x | number | False | 1064 |
| y | number | False | 1064 |
| x | number | False | 1065 |
| y | number | False | 1065 |
| t | number | False | 1065 |
| className | string | True | 1360 |
| srTitle | string | True | 1362 |
| title | string | True | 1364 |
| headingSubtitle | string | True | 1366 |
| subtitle | React.ReactNode | True | 1367 |
| orbitPhrase | string | True | 1368 |
| globeSize | number | True | 1369 |
| hideEyebrow | boolean | True | 1371 |

### Defaults and motion

- Default `splitWords` = `false` (line 961).
- Default `globeSize` = `520` (line 1053).
- Default `title` = `"CULT PRO"` (line 1054).
- Default `orbitPhrase` = `"Ship-ready sections · "` (line 1055).
- Default `hideCenterTitle` = `false` (line 1056).
- Default `title` = `"Cult Pro"` (line 1377).
- Default `headingSubtitle` = `"Sections you can ship today."` (line 1378).
- Default `globeSize` = `460` (line 1381).
- Default `hideEyebrow` = `false` (line 1382).
- `delay`: 0 (line 290).
- `delay`: 0.5 (line 291).
- `delay`: 1 (line 292).
- `delay`: 1.5 (line 293).
- `duration`: 0.65 (line 937).
- `bounce`: 0.14 (line 937).
- `duration`: 0.65 (line 946).
- `bounce`: 0.1 (line 946).
- `delay`: 0.18 (line 946).
- `duration`: 0.5 (line 955).
- `bounce`: 0.1 (line 955).
- `duration`: 0.9 (line 1282).
- `ease`: computed; inspect expression (line 1282).

### Input, style and lifecycle

Events: pointermove (line 1142); pointerup (line 1143); onPointerDown (line 1316); onPointerEnter (line 1317); onPointerLeave (line 1320).

Typography/style anchors: 912, 925, 937, 946, 955.

Source signals: reduced_motion, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
