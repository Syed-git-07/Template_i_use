# CircularText

Category: TextAnimations. Public entry: [CircularText](https://reactbits.dev/text-animations/circular-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/CircularText/CircularText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/CircularText/CircularText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/CircularText/CircularText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | '' | — |
| spinDuration | number | 20 | 20 |
| onHover | 'slowDown' \| 'speedUp' \| 'pause' \| 'goBonkers' | 'speedUp' | speedUp |
| direction | 'clockwise' \| 'counterclockwise' | 'clockwise' | clockwise |
| draggable | boolean | false | false |
| hoverTilt | number | 0 | 0 |
| tilt | number | 0 | 0 |
| size | number | 200 | 200 |
| fontSize | number | 24 | 24 |
| fontWeight | number | 900 | 900 |
| letterSpacing | number | 0 | 0 |
| color | string | '' |  |
| startAngle | number | 0 | 0 |
| fill | boolean | true | true |
| repeat | number | 1 | 1 |
| ring | boolean | false | false |
| ringColor | string | '' |  |
| children | ReactNode | - | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onPointerEnter, line 246](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L246)
- [onPointerLeave, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L247)
- [onPointerMove, line 248](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L248)
- [onPointerDown, line 249](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L249)
- [onPointerUp, line 250](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L250)
- [onPointerCancel, line 251](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L251)

## Motion locations

- [stiffness, line 52](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L52): 60
- [damping, line 52](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L52): 18
- [stiffness, line 53](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L53): 300
- [damping, line 53](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L53): 20
- [stiffness, line 54](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L54): 150
- [damping, line 54](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L54): 18
- [stiffness, line 55](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L55): 150
- [damping, line 55](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.jsx#L55): 18

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CircularText/CircularText.css); motion-related lines: 21, 32, 41.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
