# PulseHeart

Category: Micro. Public entry: [PulseHeart](https://reactbits.dev/micro/pulse-heart).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/PulseHeart/PulseHeart.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/PulseHeart/PulseHeart.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/PulseHeart/PulseHeart.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| liked | boolean | undefined | — |
| defaultLiked | boolean | false | false |
| count | number | 0 | 0 |
| onChange | (liked: boolean, count: number) => void | - | — |
| showCount | boolean | true | true |
| icon | "heart" \| "star" \| "thumb" \| ReactNode | "heart" | heart |
| idleOutline | boolean | true | true |
| size | number | 40 | 40 |
| corner | number | 32 | 32 |
| likedColor | string | "#ff4d6d" | #ff4d6d |
| idleColor | string | "#8b8b93" | #8b8b93 |
| pillColor | string | "#232326" | #232326 |
| textColor | string | "#f5f5f5" | #f5f5f5 |
| duration | number | 560 | 560 |
| dotSize | number | 0.3 | 0.3 |
| overshoot | number | 1.7 | 1.7 |
| beat | number | 3 | 3 |
| rollDuration | number | 350 | 350 |
| disabled | boolean | false | false |
| label | string | "Like" | Like |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerDown, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L213)
- [onPointerUp, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L214)
- [onPointerLeave, line 215](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L215)
- [onPointerCancel, line 216](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L216)
- [onKeyDown, line 217](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L217)
- [onClick, line 218](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.jsx#L218)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PulseHeart/PulseHeart.css); motion-related lines: 30, 68, 94, 126, 160, 162, 166, 170.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
