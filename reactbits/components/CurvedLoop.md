# CurvedLoop

Category: TextAnimations. Public entry: [CurvedLoop](https://reactbits.dev/text-animations/curved-loop).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/CurvedLoop/CurvedLoop.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/CurvedLoop/CurvedLoop.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/CurvedLoop/CurvedLoop.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| marqueeText | string | '' |  |
| shape | 'arc' \| 'wave' \| 'circle' \| 'line' | 'arc' | arc |
| color | string | 'currentColor' | currentColor |
| separator | string | '' |  |
| separatorColor | string | - | — |
| direction | 'left' \| 'right' | 'left' | left |
| speed | number | 2 | 2 |
| scrollBoost | number | 0 | 0 |
| curveAmount | number | 400 | 400 |
| fontSize | number | 96 | 96 |
| fontWeight | number \| string | 700 | 700 |
| letterSpacing | number | 0 | 0 |
| edgeFade | number | 0 | 0 |
| outline | boolean | false | false |
| interactive | boolean | true | true |
| pauseOnHover | boolean | false | false |
| className | string | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [loadingdone, line 166](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L166)
- [scroll, line 203](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L203)
- [onPointerDown, line 326](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L326)
- [onPointerMove, line 327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L327)
- [onPointerUp, line 328](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L328)
- [onPointerCancel, line 329](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L329)
- [onLostPointerCapture, line 330](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L330)
- [onPointerEnter, line 331](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L331)
- [onPointerLeave, line 334](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L334)

## Motion locations

- [velocity, line 119](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L119): 0
- [velocity, line 270](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.jsx#L270): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CurvedLoop/CurvedLoop.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
