# FlyingPosters

Category: Components. Public entry: [FlyingPosters](https://reactbits.dev/components/flying-posters).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/FlyingPosters/FlyingPosters.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/FlyingPosters/FlyingPosters.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/FlyingPosters/FlyingPosters.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<string \| { image: string; link?: string; alt?: string }> | [] | — |
| planeWidth | number | 320 | 320 |
| planeHeight | number | 320 | 320 |
| distortion | number | 3 | 3 |
| scrollEase | number | 0.01 | 0.01 |
| cameraFov | number | 45 | 45 |
| cameraZ | number | 20 | 20 |
| gap | number | - | — |
| rotation | number | 180 | 180 |
| axis | 'vertical' \| 'horizontal' \| 'diagonal' | 'vertical' | vertical |
| columns | number | 1 | 1 |
| columnGap | number | 40 | 40 |
| alternate | boolean | true | true |
| radius | number | 0 | 0 |
| speed | number | 0 | 0 |
| lean | number | 0 | 0 |
| fade | number | 0 | 0 |
| shading | number | 0 | 0 |
| wheel | boolean | true | true |
| drag | boolean | true | true |
| pageScroll | number | 0 | 0 |
| onItemClick | (item, index) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [wheel, line 561](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L561)
- [pointerdown, line 562](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L562)
- [pointermove, line 563](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L563)
- [pointerup, line 564](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L564)
- [pointercancel, line 565](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L565)
- [scroll, line 566](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L566)

## Motion locations

- [velocity, line 291](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.jsx#L291): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlyingPosters/FlyingPosters.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
