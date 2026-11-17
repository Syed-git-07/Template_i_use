# Magnet

Category: Animations. Public entry: [Magnet](https://reactbits.dev/animations/magnet).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/Magnet/Magnet.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/Magnet/Magnet.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/Magnet/Magnet.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| padding | number | 100 | 100 |
| magnetStrength | number | 2 | 2 |
| exclusive | boolean | true | true |
| axis | 'both' \| 'x' \| 'y' | 'both' | both |
| maxOffset | number | - | — |
| tilt | number | 0 | 0 |
| scale | number | 1 | 1 |
| spring | { stiffness?: number; damping?: number; mass?: number } | { stiffness: 170, damping: 16, mass: 1 } | — |
| disabled | boolean | false | false |
| onActiveChange | (active: boolean) => void | - | — |
| wrapperClassName | string | '' |  |
| innerClassName | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 62](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L62)
- [scroll, line 63](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L63)
- [pointerleave, line 64](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L64)
- [blur, line 65](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L65)

## Motion locations

- [stiffness, line 5](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L5): 170
- [damping, line 5](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L5): 16
- [mass, line 5](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L5): 1
- [stiffness, line 103](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L103): computed; read the linked expression
- [damping, line 104](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L104): computed; read the linked expression
- [mass, line 105](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Magnet/Magnet.jsx#L105): computed; read the linked expression

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
