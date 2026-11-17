# SlingButton

Category: Micro. Public entry: [SlingButton](https://reactbits.dev/micro/sling-button).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SlingButton/SlingButton.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SlingButton/SlingButton.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SlingButton/SlingButton.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | undefined | — |
| onSend | () => void | - | — |
| padColor | string | "#f5f5f5" | #f5f5f5 |
| iconColor | string | "#18181b" | #18181b |
| accentColor | string | "#f5f5f5" | #f5f5f5 |
| wellColor | string | "#27272a" | #27272a |
| bandColor | string | "#52525b" | #52525b |
| size | number | 56 | 56 |
| strokeWidth | number | 3 | 3 |
| armAt | number | 48 | 48 |
| maxPull | number | 160 | 160 |
| launchSpeed | number | 2600 | 2600 |
| recoil | number | 0.2 | 0.2 |
| flight | number | 120 | 120 |
| particles | number | 14 | 14 |
| spread | number | 60 | 60 |
| axis | "any" \| "horizontal" \| "vertical" | "any" | any |
| tapSends | boolean | true | true |
| disabled | boolean | false | false |
| ariaLabel | string | "Send" | Send |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerDown, line 386](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L386)
- [onPointerMove, line 387](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L387)
- [onPointerUp, line 388](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L388)
- [onPointerCancel, line 389](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L389)
- [onLostPointerCapture, line 390](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L390)
- [onKeyDown, line 391](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L391)
- [onClick, line 394](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L394)

## Motion locations

- [duration, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L207): 0.4
- [bounce, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L207): computed; read the linked expression
- [velocity, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L207): computed; read the linked expression
- [duration, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L208): 0.4
- [bounce, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L208): computed; read the linked expression
- [velocity, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.jsx#L208): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlingButton/SlingButton.css); motion-related lines: 33, 45, 61, 117, 161, 164.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
