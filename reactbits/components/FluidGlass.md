# FluidGlass

Category: Components. Public entry: [FluidGlass](https://reactbits.dev/components/fluid-glass).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/FluidGlass/FluidGlass.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/FluidGlass/FluidGlass.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/FluidGlass/FluidGlass.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'Look closer.' | Look closer. |
| src | string | - | — |
| fit | 'cover' \| 'contain' | 'cover' | cover |
| background | string | 'transparent' | transparent |
| textColor | string | Inherited | — |
| fontFamily | string | Inherited | — |
| fontWeight | number \| string | 600 | 600 |
| fontSize | number | Auto | — |
| shape | 'torus' \| 'lens' \| 'blob' \| 'pill' \| 'cube' \| 'prism' \| 'diamond' | 'torus' | torus |
| shapes | string[] | All shapes | — |
| morphOnClick | boolean | true | true |
| size | number | 260 | 260 |
| interaction | 'follow' \| 'drag' \| 'static' | 'follow' | follow |
| position | [number, number] | [0.5, 0.5] | — |
| refraction | number | 1 | 1 |
| dispersion | number | 0.35 | 0.35 |
| frost | number | 0 | 0 |
| color | string | '#ffffff' | #ffffff |
| tint | number | 0 | 0 |
| reflection | number | 1 | 1 |
| shadow | number | 0.5 | 0.5 |
| elevation | number | 0.4 | 0.4 |
| smoothness | number | 0.5 | 0.5 |
| wobble | number | 0.5 | 0.5 |
| spin | number | 0.3 | 0.3 |
| idle | boolean | true | true |
| intro | boolean | true | true |
| maxDevicePixelRatio | number | 2 | 2 |
| children | ReactNode | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [loadeddata, line 832](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L832)
- [pointermove, line 1323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1323)
- [pointerdown, line 1324](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1324)
- [pointerup, line 1325](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1325)
- [pointercancel, line 1326](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1326)
- [pointerleave, line 1327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1327)
- [webglcontextlost, line 1336](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1336)
- [webglcontextrestored, line 1337](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1337)
- [visibilitychange, line 1360](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.jsx#L1360)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FluidGlass/FluidGlass.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
