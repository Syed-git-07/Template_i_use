# HoloCard

Category: Components. Public entry: [HoloCard](https://reactbits.dev/components/holo-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/HoloCard/HoloCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/HoloCard/HoloCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/HoloCard/HoloCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| image | string | - | — |
| backImage | string | - | — |
| alt | string | '' |  |
| preset | 'bursts' \| 'stars' \| 'shards' \| 'cosmos' \| 'rainbow' \| 'swirl' \| 'glitter' \| 'gold' | 'bursts' | bursts |
| foilColor | string | '#e2e6ec' | #e2e6ec |
| intensity | number | 0.85 | 0.85 |
| scale | number | 1 | 1 |
| edgeSparkle | number | 0.8 | 0.8 |
| frame | number | 4 | 4 |
| glare | number | 0.5 | 0.5 |
| tiltMax | number | 14 | 14 |
| hoverScale | number | 1.04 | 1.04 |
| radius | number | 14 | 14 |
| width | number | 320 | 320 |
| idle | boolean | true | true |
| shadow | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [onPointerEnter, line 645](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L645)
- [onPointerMove, line 646](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L646)
- [onPointerDown, line 647](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L647)
- [onPointerLeave, line 648](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L648)
- [onPointerCancel, line 649](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L649)
- [onClick, line 650](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L650)
- [onKeyDown, line 651](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.jsx#L651)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/HoloCard/HoloCard.css); motion-related lines: 76.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
