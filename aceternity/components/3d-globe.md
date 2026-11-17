# 3d-globe

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/3d-globe/components/ui/3d-globe.tsx

[Original source](https://ui.aceternity.com/registry/3d-globe.json); SHA-256 `b017111cda6b02bc1c3996912150648b93d0d908da304698b0e2cac16e5b22e5`; 551 lines.

Imports: `react`, `@react-three/fiber`, `@react-three/drei`, `three`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| lat | number | False | 13 |
| lng | number | False | 14 |
| src | string | False | 15 |
| label | string | True | 16 |
| size | number | True | 17 |
| radius | number | True | 22 |
| globeColor | string | True | 24 |
| textureUrl | string | True | 26 |
| bumpMapUrl | string | True | 28 |
| showAtmosphere | boolean | True | 30 |
| atmosphereColor | string | True | 32 |
| atmosphereIntensity | number | True | 34 |
| atmosphereBlur | number | True | 36 |
| bumpScale | number | True | 38 |
| autoRotateSpeed | number | True | 40 |
| enableZoom | boolean | True | 42 |
| enablePan | boolean | True | 44 |
| minDistance | number | True | 46 |
| maxDistance | number | True | 48 |
| initialRotation | { x: number; y: number } | True | 50 |
| x | number | False | 50 |
| y | number | False | 50 |
| markerSize | number | True | 52 |
| showWireframe | boolean | True | 54 |
| wireframeColor | string | True | 56 |
| ambientIntensity | number | True | 58 |
| pointLightIntensity | number | True | 60 |
| backgroundColor | string \| null | True | 62 |
| markers | GlobeMarker[] | True | 67 |
| config | Globe3DConfig | True | 69 |
| className | string | True | 71 |
| onMarkerClick | (marker: GlobeMarker) => void | True | 73 |
| onMarkerHover | (marker: GlobeMarker \| null) => void | True | 75 |
| marker | GlobeMarker | False | 114 |
| radius | number | False | 115 |
| defaultSize | number | False | 116 |
| onClick | (marker: GlobeMarker) => void | True | 117 |
| onHover | (marker: GlobeMarker \| null) => void | True | 118 |
| config | Required<Globe3DConfig> | False | 255 |
| markers | GlobeMarker[] | False | 256 |
| onMarkerClick | (marker: GlobeMarker) => void | True | 257 |
| onMarkerHover | (marker: GlobeMarker \| null) => void | True | 258 |
| radius | number | False | 340 |
| color | string | False | 341 |
| intensity | number | False | 342 |
| blur | number | False | 343 |
| markers | GlobeMarker[] | False | 397 |
| config | Required<Globe3DConfig> | False | 398 |
| onMarkerClick | (marker: GlobeMarker) => void | True | 399 |
| onMarkerHover | (marker: GlobeMarker \| null) => void | True | 400 |

### Defaults and motion


### Input, style and lifecycle

Events: onMouseEnter (line 233); onMouseLeave (line 234); onClick (line 235); onClick (line 327); onHover (line 328); onMarkerClick (line 431); onMarkerHover (line 432); onMarkerClick (line 541); onMarkerHover (line 542).

Typography/style anchors: 221.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
