# ElasticMesh

Category: Animations. Public entry: [ElasticMesh](https://reactbits.dev/animations/elastic-mesh).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ElasticMesh/ElasticMesh.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ElasticMesh/ElasticMesh.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ElasticMesh/ElasticMesh.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'Squish' | Squish |
| src | string | '' |  |
| fontFamily | string | 'system-ui, sans-serif' | system-ui, sans-serif |
| fontWeight | number | 900 | 900 |
| color | string | '#3b5bff' | #3b5bff |
| imageColors | boolean | true | true |
| material | 'balloon' \| 'chrome' \| 'jelly' \| 'clay' | 'balloon' | balloon |
| inflate | number | 1 | 1 |
| stiffness | number | 0.5 | 0.5 |
| wobble | number | 0.6 | 0.6 |
| grabRadius | number | 70 | 70 |
| stretch | number | 0.5 | 0.5 |
| press | number | 0.5 | 0.5 |
| shadow | number | 0.5 | 0.5 |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerdown, line 1330](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1330)
- [pointermove, line 1331](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1331)
- [pointerup, line 1332](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1332)
- [pointercancel, line 1333](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1333)
- [pointerleave, line 1334](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1334)
- [visibilitychange, line 1335](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L1335)

## Motion locations

- [stiffness, line 509](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L509): computed; read the linked expression
- [delay, line 906](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.jsx#L906): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElasticMesh/ElasticMesh.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
