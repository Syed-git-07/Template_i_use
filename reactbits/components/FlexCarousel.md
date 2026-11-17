# FlexCarousel

Category: Components. Public entry: [FlexCarousel](https://reactbits.dev/components/flex-carousel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/FlexCarousel/FlexCarousel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/FlexCarousel/FlexCarousel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/FlexCarousel/FlexCarousel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ src: string; alt?: string; title?: string; subtitle?: string }> | 12 sample photos | — |
| preset | 'liquid' \| 'ribbon' \| 'vortex' \| 'arch' | 'liquid' | liquid |
| intro | 'rise' \| 'bloom' \| 'spin' \| 'deal' \| 'none' | 'rise' | rise |
| fit | 'natural' \| 'portrait' \| 'square' \| 'landscape' | 'natural' | natural |
| cardHeight | number | 0.5 | 0.5 |
| gap | number | 12 | 12 |
| radius | number | 0 | 0 |
| lensWidth | number | from preset | — |
| lensHeight | number | from preset | — |
| tilt | number | from preset | — |
| roundness | number | from preset | — |
| bend | number | from preset | — |
| reach | number | from preset | — |
| curl | 'twist' \| 'rise' \| 'fall' | from preset | — |
| dispersion | number | from preset | — |
| liquid | number | from preset | — |
| followCursor | boolean | from preset | — |
| squeeze | number | 0.2 | 0.2 |
| focusOnClick | boolean | true | true |
| autoplay | boolean | false | false |
| interval | number | 4 | 4 |
| captions | boolean | true | true |
| captureWheel | boolean | true | true |
| onChange | (index: number, item) => void | - | — |
| onSelect | (index: number, item) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointerdown, line 1193](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1193)
- [pointermove, line 1194](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1194)
- [pointerup, line 1195](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1195)
- [pointerleave, line 1196](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1196)
- [pointercancel, line 1197](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1197)
- [wheel, line 1198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1198)
- [keydown, line 1199](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1199)
- [focus, line 1200](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1200)
- [blur, line 1201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1201)
- [visibilitychange, line 1202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.jsx#L1202)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlexCarousel/FlexCarousel.css); motion-related lines: 43, 54, 70, 90, 113, 124, 133, 136, 140.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
