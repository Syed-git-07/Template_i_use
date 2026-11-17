# WakeSlider

Category: Micro. Public entry: [WakeSlider](https://reactbits.dev/micro/wake-slider).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/WakeSlider/WakeSlider.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/WakeSlider/WakeSlider.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/WakeSlider/WakeSlider.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | undefined | — |
| defaultValue | number | 50 | 50 |
| onChange | (value: number) => void | - | — |
| min | number | 0 | 0 |
| max | number | 100 | 100 |
| step | number | 1 | 1 |
| bars | number | 32 | 32 |
| height | number | 56 | 56 |
| restHeight | number | 12 | 12 |
| gap | number | 4 | 4 |
| fillColor | string | "#f5f5f5" | #f5f5f5 |
| trackColor | string | "#27272a" | #27272a |
| crestColor | string | "" |  |
| sensitivity | number | 1 | 1 |
| reach | number | 6 | 6 |
| skew | number | 0.6 | 0.6 |
| glide | number | 0.3 | 0.3 |
| smoothing | number | 100 | 100 |
| showValue | boolean | false | false |
| formatValue | (value: number) => string | - | — |
| disabled | boolean | false | false |
| ariaLabel | string | "Value" | Value |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onPointerDown, line 211](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L211)
- [onPointerMove, line 212](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L212)
- [onPointerUp, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L213)
- [onPointerCancel, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L214)
- [onLostPointerCapture, line 215](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L215)
- [onKeyDown, line 230](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L230)

## Motion locations

- [stiffness, line 68](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L68): computed; read the linked expression
- [damping, line 68](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L68): computed; read the linked expression
- [mass, line 68](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L68): 1
- [stiffness, line 71](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L71): computed; read the linked expression
- [damping, line 71](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L71): computed; read the linked expression
- [mass, line 71](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.jsx#L71): 1

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WakeSlider/WakeSlider.css); motion-related lines: 55, 63, 96.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
