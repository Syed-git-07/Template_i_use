# CircularCarousel

Category: Components. Public entry: [CircularCarousel](https://reactbits.dev/components/circular-carousel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/CircularCarousel/CircularCarousel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/CircularCarousel/CircularCarousel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/CircularCarousel/CircularCarousel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ src: string; alt?: string; title?: string; subtitle?: string }> | 10 sample photos | — |
| preset | 'cylinder' \| 'orbit' \| 'wheel' \| 'panorama' | 'cylinder' | cylinder |
| intro | 'assemble' \| 'rise' \| 'spin' \| 'none' | 'rise' | rise |
| cardWidth | number | 220 | 220 |
| aspectRatio | number | 1 | 1 |
| gap | number | 25 | 25 |
| curve | number | from preset | — |
| tilt | number | from preset | — |
| perspective | number | from preset | — |
| autoplay | 'drift' \| 'step' \| 'off' | 'drift' | drift |
| speed | number | 14 | 14 |
| interval | number | 3 | 3 |
| direction | 'left' \| 'right' | 'left' | left |
| draggable | boolean | true | true |
| momentum | number | 0.6 | 0.6 |
| snap | boolean | true | true |
| pauseOnHover | boolean | true | true |
| focusOnClick | boolean | true | true |
| parallax | number | 0.3 | 0.3 |
| stretch | number | 0.5 | 0.5 |
| depthFade | number | 0.55 | 0.55 |
| fadeColor | string | '#000000' | #000000 |
| innerShade | number | 0.6 | 0.6 |
| cornerRadius | number | 12 | 12 |
| captions | boolean | false | false |
| onChange | (index: number) => void | - | — |
| onItemClick | (item, index: number) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 173](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L173)
- [wheel, line 662](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L662)
- [visibilitychange, line 663](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L663)
- [onPointerDown, line 911](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L911)
- [onPointerMove, line 912](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L912)
- [onPointerUp, line 913](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L913)
- [onPointerCancel, line 914](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L914)
- [onPointerEnter, line 915](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L915)
- [onPointerLeave, line 916](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L916)
- [onClick, line 917](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L917)
- [onKeyDown, line 918](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L918)

## Motion locations

- [velocity, line 271](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.jsx#L271): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularCarousel/CircularCarousel.css); motion-related lines: 54, 106, 139, 150, 185, 201, 212, 221, 230, 233, 238.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
