# CometDial

Category: Micro. Public entry: [CometDial](https://reactbits.dev/micro/comet-dial).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/CometDial/CometDial.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/CometDial/CometDial.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/CometDial/CometDial.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | undefined | — |
| defaultValue | number | 62 | 62 |
| min | number | 0 | 0 |
| max | number | 100 | 100 |
| step | number | 1 | 1 |
| unit | string | "%" | % |
| label | string | "Level" | Level |
| accent | string | "#f5f5f5" | #f5f5f5 |
| ink | string | "#fdfdfd" | #fdfdfd |
| size | number | 250 | 250 |
| sweep | number | 320 | 320 |
| thickness | number | 5 | 5 |
| speed | number | 25 | 25 |
| tapBounce | number | 0.2 | 0.2 |
| flickBounce | number | 0.1 | 0.1 |
| momentum | number | 1 | 1 |
| cometReach | number | 180 | 180 |
| cometWidth | number | 12 | 12 |
| disabled | boolean | false | false |
| onChange | (value: number) => void | - | — |
| onChangeEnd | (value: number, detail: { velocity: number; bounce: number }) => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [pointermove, line 260](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L260)
- [pointerup, line 261](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L261)
- [pointercancel, line 262](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L262)
- [onPointerDown, line 355](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L355)
- [onKeyDown, line 356](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L356)

## Motion locations

- [velocity, line 94](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L94): 0
- [bounce, line 94](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L94): computed; read the linked expression
- [stiffness, line 115](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L115): computed; read the linked expression
- [damping, line 116](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L116): computed; read the linked expression
- [mass, line 117](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L117): 1
- [velocity, line 233](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.jsx#L233): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CometDial/CometDial.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
