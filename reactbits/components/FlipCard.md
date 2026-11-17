# FlipCard

Category: Micro. Public entry: [FlipCard](https://reactbits.dev/micro/flip-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/FlipCard/FlipCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/FlipCard/FlipCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/FlipCard/FlipCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| front | ReactNode | null | — |
| back | ReactNode | null | — |
| flipped | boolean | - | — |
| defaultFlipped | boolean | false | false |
| onFlipChange | (flipped: boolean) => void | - | — |
| axis | 'y' \| 'x' | 'y' | y |
| flipOnClick | boolean | true | true |
| draggable | boolean | true | true |
| dragDistance | number | 0 | 0 |
| tilt | boolean | true | true |
| tiltMax | number | 12 | 12 |
| glare | boolean | true | true |
| glareOpacity | number | 0.22 | 0.22 |
| hoverScale | number | 1.03 | 1.03 |
| perspective | number | 1100 | 1100 |
| stiffness | number | 170 | 170 |
| damping | number | 20 | 20 |
| width | number | 300 | 300 |
| height | number | 400 | 400 |
| radius | number | 22 | 22 |
| background | string | "#27272a" | #27272a |
| color | string | "#f5f5f5" | #f5f5f5 |
| shadow | boolean | true | true |
| shadowColor | string | "#000000" | #000000 |
| shadowOpacity | number | 0.45 | 0.45 |
| disabled | boolean | false | false |
| ariaLabel | string | "Flip card" | Flip card |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onPointerDown, line 223](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L223)
- [onPointerMove, line 224](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L224)
- [onPointerUp, line 225](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L225)
- [onPointerCancel, line 226](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L226)
- [onLostPointerCapture, line 227](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L227)
- [onPointerEnter, line 228](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L228)
- [onPointerLeave, line 231](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L231)
- [onKeyDown, line 234](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L234)
- [onClick, line 235](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L235)
- [onDragStart, line 236](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L236)

## Motion locations

- [stiffness, line 17](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L17): 240
- [damping, line 17](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L17): 24
- [mass, line 17](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L17): 0.6
- [stiffness, line 18](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L18): 320
- [damping, line 18](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L18): 26
- [restDelta, line 90](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L90): 0.05
- [restDelta, line 114](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.jsx#L114): 0.05

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlipCard/FlipCard.css); motion-related lines: 103.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
