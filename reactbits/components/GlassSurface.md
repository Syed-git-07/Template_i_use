# GlassSurface

Category: Components. Public entry: [GlassSurface](https://reactbits.dev/components/glass-surface).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassSurface/GlassSurface.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/GlassSurface/GlassSurface.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/GlassSurface/GlassSurface.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/GlassSurface/GlassSurface.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| width | number \| string | 200 | 200 |
| height | number \| string | 80 | 80 |
| borderRadius | number | 20 | 20 |
| shape | string | - | — |
| refraction | boolean | true | true |
| renderer | 'auto' \| 'svg' \| 'webgl' | 'auto' | auto |
| backdrop | RefObject<HTMLImageElement \| HTMLVideoElement \| HTMLCanvasElement> | - | — |
| distortionScale | number | -180 | -180 |
| borderWidth | number | 0.07 | 0.07 |
| blur | number | 11 | 11 |
| brightness | number | 50 | 50 |
| opacity | number | 0.93 | 0.93 |
| displace | number | 0 | 0 |
| redOffset | number | 0 | 0 |
| greenOffset | number | 10 | 10 |
| blueOffset | number | 20 | 20 |
| backgroundOpacity | number | 0 | 0 |
| saturation | number | 1 | 1 |
| xChannel | 'R' \| 'G' \| 'B' | 'R' | R |
| yChannel | 'R' \| 'G' \| 'B' | 'G' | G |
| mixBlendMode | BlendMode | 'difference' | difference |
| className | string | '' |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [visibilitychange, line 684](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassSurface/GlassSurface.jsx#L684)
- [webglcontextlost, line 685](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassSurface/GlassSurface.jsx#L685)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassSurface/GlassSurface.css); motion-related lines: 7.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
