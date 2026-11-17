# TearTicket

Category: Micro. Public entry: [TearTicket](https://reactbits.dev/micro/tear-ticket).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/TearTicket/TearTicket.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/TearTicket/TearTicket.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/TearTicket/TearTicket.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | null | — |
| stub | ReactNode | null | — |
| image | string | "" |  |
| imageAlt | string | "" |  |
| scrim | boolean | true | true |
| imageRadius | number | 8 | 8 |
| orientation | 'horizontal' \| 'vertical' | 'horizontal' | horizontal |
| torn | boolean | - | — |
| defaultTorn | boolean | false | false |
| onTear | () => void | - | — |
| width | number | 460 | 460 |
| height | number | 250 | 250 |
| stubSize | number | 150 | 150 |
| radius | number | 16 | 16 |
| holes | number | 12 | 12 |
| holeSize | number | 6 | 6 |
| notch | number | 3 | 3 |
| roughness | number | 0 | 0 |
| tearAngle | number | 30 | 30 |
| stretch | number | 30 | 30 |
| resistance | number | 0.45 | 0.45 |
| rotate | number | 4 | 4 |
| tilt | boolean | true | true |
| tiltMax | number | 9 | 9 |
| tiltReach | number | 260 | 260 |
| parallax | number | 6 | 6 |
| perspective | number | 1000 | 1000 |
| background | string | "#27272a" | #27272a |
| color | string | "#f5f5f5" | #f5f5f5 |
| border | boolean | true | true |
| borderColor | string | "" |  |
| borderWidth | number | 1 | 1 |
| stubBackground | string | "" |  |
| recenter | boolean | true | true |
| disabled | boolean | false | false |
| ariaLabel | string | "Tear off the stub" | Tear off the stub |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [pointermove, line 502](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L502)
- [onPointerDown, line 585](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L585)
- [onPointerMove, line 586](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L586)
- [onPointerUp, line 587](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L587)
- [onPointerCancel, line 588](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L588)
- [onLostPointerCapture, line 589](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L589)
- [onKeyDown, line 590](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L590)
- [onDragStart, line 591](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L591)

## Motion locations

- [stiffness, line 8](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L8): 220
- [damping, line 8](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L8): 24
- [mass, line 8](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.jsx#L8): 0.6

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/TearTicket/TearTicket.css); motion-related lines: 39, 121, 146, 177, 205, 207.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
