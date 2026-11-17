# SwipeToast

Category: Micro. Public entry: [SwipeToast](https://reactbits.dev/micro/swipe-toast).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SwipeToast/SwipeToast.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SwipeToast/SwipeToast.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SwipeToast/SwipeToast.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| title | ReactNode | "File archived" | File archived |
| description | ReactNode | "" |  |
| icon | ReactNode | undefined | — |
| actionLabel | ReactNode | "" |  |
| onAction | () => void | - | — |
| open | boolean | true | true |
| onClose | (reason) => void | - | — |
| background | string | "#27272a" | #27272a |
| color | string | "#f5f5f5" | #f5f5f5 |
| fuseColor | string | "#f5a524" | #f5a524 |
| width | number | 356 | 356 |
| radius | number | 12 | 12 |
| slideMs | number | 400 | 400 |
| settleBounce | number | 0.2 | 0.2 |
| swipeDistance | number | 40 | 40 |
| duration | number | 4000 | 4000 |
| fuse | "bottom" \| "top" \| "none" | "bottom" | bottom |
| pauseOnHover | boolean | true | true |
| closeButton | boolean | false | false |
| inline | boolean | false | false |
| dismissible | boolean | true | true |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [visibilitychange, line 142](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L142)
- [onPointerDown, line 252](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L252)
- [onPointerMove, line 253](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L253)
- [onPointerUp, line 254](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L254)
- [onPointerCancel, line 255](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L255)
- [onPointerEnter, line 256](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L256)
- [onPointerLeave, line 262](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L262)
- [onFocus, line 268](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L268)
- [onBlur, line 272](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L272)
- [onKeyDown, line 278](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L278)
- [onClick, line 299](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L299)
- [onClick, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L308)

## Motion locations

- [duration, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L156): 0.3
- [bounce, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L156): 0
- [velocity, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L156): computed; read the linked expression
- [duration, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L158): 0.2
- [ease, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L158): computed; read the linked expression
- [duration, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L213): 0.2
- [ease, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L213): computed; read the linked expression
- [duration, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L214): 0.5
- [bounce, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L214): computed; read the linked expression
- [velocity, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.jsx#L214): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeToast/SwipeToast.css); motion-related lines: 38, 51, 55, 69, 93, 105, 178, 258, 261.

## Observed source structure

Literal state assignments: setPhase → gone (line 82); setPhase → closing (line 97); setPhase → open (line 106).

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
