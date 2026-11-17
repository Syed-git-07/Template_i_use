# globe

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/globe/components/ui/globe.tsx

[Original source](https://ui.aceternity.com/registry/globe.json); SHA-256 `f1c4370796ff294abd9be6169a5642ed710347e5ecba121da498459ce4db7e2b`; 310 lines.

Imports: `react`, `three`, `three-globe`, `@react-three/fiber`, `@react-three/drei`, `@/data/globe.json`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| threeGlobe | ThreeElements["mesh"] & {       new (): ThreeGlobe;     } | False | 10 |
| order | number | False | 23 |
| startLat | number | False | 24 |
| startLng | number | False | 25 |
| endLat | number | False | 26 |
| endLng | number | False | 27 |
| arcAlt | number | False | 28 |
| color | string | False | 29 |
| pointSize | number | True | 33 |
| globeColor | string | True | 34 |
| showAtmosphere | boolean | True | 35 |
| atmosphereColor | string | True | 36 |
| atmosphereAltitude | number | True | 37 |
| emissive | string | True | 38 |
| emissiveIntensity | number | True | 39 |
| shininess | number | True | 40 |
| polygonColor | string | True | 41 |
| ambientLight | string | True | 42 |
| directionalLeftLight | string | True | 43 |
| directionalTopLight | string | True | 44 |
| pointLight | string | True | 45 |
| arcTime | number | True | 46 |
| arcLength | number | True | 47 |
| rings | number | True | 48 |
| maxRings | number | True | 49 |
| initialPosition | {     lat: number;     lng: number;   } | True | 50 |
| lat | number | False | 51 |
| lng | number | False | 52 |
| autoRotate | boolean | True | 54 |
| autoRotateSpeed | number | True | 55 |
| globeConfig | GlobeConfig | False | 59 |
| data | Position[] | False | 60 |
| color | Color | False | 101 |
| emissive | Color | False | 102 |
| emissiveIntensity | number | False | 103 |
| shininess | number | False | 104 |
| r | number | False | 126 |
| g | number | False | 126 |
| b | number | False | 126 |
| startLat | number | False | 164 |
| startLng | number | False | 165 |
| endLat | number | False | 166 |
| endLng | number | False | 167 |
| color | string | False | 168 |
| arcAlt | number | False | 169 |
| order | number | False | 172 |
| color | string | False | 178 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
