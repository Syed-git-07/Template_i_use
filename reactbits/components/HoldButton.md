# HoldButton

Category: Micro. Public entry: [HoldButton](https://reactbits.dev/micro/hold-button).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/HoldButton/HoldButton.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/HoldButton/HoldButton.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/HoldButton/HoldButton.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | "Hold to delete" | Hold to delete |
| doneLabel | ReactNode | "Deleted" | Deleted |
| icon | ReactNode | null | — |
| doneIcon | ReactNode | null | — |
| backgroundColor | string | "#27272a" | #27272a |
| fillColor | string | "#5227FF" | #5227FF |
| textColor | string | "#f5f5f5" | #f5f5f5 |
| fillTextColor | string | "#ffffff" | #ffffff |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 14 | 14 |
| fillDirection | "right" \| "up" | "right" | right |
| holdTime | number | 2000 | 2000 |
| releaseTime | number | 200 | 200 |
| pressScale | number | 0.97 | 0.97 |
| wave | boolean | true | true |
| waveAmplitude | number | 6 | 6 |
| glow | boolean | true | true |
| resetAfter | number | 1200 | 1200 |
| disabled | boolean | false | false |
| onHold | () => void | - | — |
| onTap | () => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [blur, line 186](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L186)
- [visibilitychange, line 187](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L187)
- [onPointerDown, line 241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L241)
- [onPointerMove, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L242)
- [onPointerUp, line 243](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L243)
- [onPointerCancel, line 244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L244)
- [onLostPointerCapture, line 245](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L245)
- [onPointerLeave, line 246](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L246)
- [onKeyDown, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L247)
- [onKeyUp, line 248](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L248)
- [onContextMenu, line 249](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.jsx#L249)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/HoldButton/HoldButton.css); motion-related lines: 41, 81, 108, 111, 135, 241, 243, 253, 263, 267, 271.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
