# canvas-reveal-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/canvas-reveal-effect/components/ui/canvas-reveal-effect.tsx

[Original source](https://ui.aceternity.com/registry/canvas-reveal-effect.json); SHA-256 `7d49ce5826dc2b9a20439778c62bb6cf15547fd7472baa4d57de25eea2d40692`; 309 lines.

Imports: `@/lib/utils`, `@react-three/fiber`, `react`, `three`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| animationSpeed | number | True | 19 |
| opacities | number[] | True | 20 |
| colors | number[][] | True | 21 |
| containerClassName | string | True | 22 |
| dotSize | number | True | 23 |
| showGradient | boolean | True | 24 |
| colors | number[][] | True | 52 |
| opacities | number[] | True | 53 |
| totalSize | number | True | 54 |
| dotSize | number | True | 55 |
| shader | string | True | 56 |
| center | ("x" \| "y")[] | True | 57 |
| value | number[] \| number[][] \| number | False | 180 |
| type | string | False | 181 |
| source | string | False | 189 |
| hovered | boolean | True | 190 |
| maxFps | number | True | 191 |
| uniforms | Uniforms | False | 192 |
| source | string | False | 300 |
| uniforms | {     [key: string]: {       value: number[] \| number[][] \| number;       type: string;     };   } | False | 301 |
| value | number[] \| number[][] \| number | False | 303 |
| type | string | False | 304 |
| maxFps | number | True | 307 |

### Defaults and motion

- Default `animationSpeed` = `0.4` (line 8).
- Default `showGradient` = `true` (line 13).
- Default `totalSize` = `4` (line 63).
- Default `dotSize` = `2` (line 64).
- Default `shader` = `""` (line 65).
- Default `maxFps` = `60` (line 187).
- Default `maxFps` = `60` (line 292).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## components/card-spotlight/components/ui/canvas-reveal-effect.tsx

[Original source](https://ui.aceternity.com/registry/card-spotlight.json); SHA-256 `7d49ce5826dc2b9a20439778c62bb6cf15547fd7472baa4d57de25eea2d40692`; 309 lines.

Imports: `@/lib/utils`, `@react-three/fiber`, `react`, `three`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| animationSpeed | number | True | 19 |
| opacities | number[] | True | 20 |
| colors | number[][] | True | 21 |
| containerClassName | string | True | 22 |
| dotSize | number | True | 23 |
| showGradient | boolean | True | 24 |
| colors | number[][] | True | 52 |
| opacities | number[] | True | 53 |
| totalSize | number | True | 54 |
| dotSize | number | True | 55 |
| shader | string | True | 56 |
| center | ("x" \| "y")[] | True | 57 |
| value | number[] \| number[][] \| number | False | 180 |
| type | string | False | 181 |
| source | string | False | 189 |
| hovered | boolean | True | 190 |
| maxFps | number | True | 191 |
| uniforms | Uniforms | False | 192 |
| source | string | False | 300 |
| uniforms | {     [key: string]: {       value: number[] \| number[][] \| number;       type: string;     };   } | False | 301 |
| value | number[] \| number[][] \| number | False | 303 |
| type | string | False | 304 |
| maxFps | number | True | 307 |

### Defaults and motion

- Default `animationSpeed` = `0.4` (line 8).
- Default `showGradient` = `true` (line 13).
- Default `totalSize` = `4` (line 63).
- Default `dotSize` = `2` (line 64).
- Default `shader` = `""` (line 65).
- Default `maxFps` = `60` (line 187).
- Default `maxFps` = `60` (line 292).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
