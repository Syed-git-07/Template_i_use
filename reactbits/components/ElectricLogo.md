# ElectricLogo

Category: Animations. Public entry: [ElectricLogo](https://reactbits.dev/animations/electric-logo).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ElectricLogo/ElectricLogo.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ElectricLogo/ElectricLogo.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ElectricLogo/ElectricLogo.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | lightning bolt | — |
| color | string | '#ecc7ff' | #ecc7ff |
| glowColor | string | '#ad6dff' | #ad6dff |
| scale | number | 0.7 | 0.7 |
| intensity | number | 1 | 1 |
| glow | number | 1 | 1 |
| thickness | number | 1.5 | 1.5 |
| strands | number | 4 | 4 |
| bend | number | 0.6 | 0.6 |
| crackle | number | 1.5 | 1.5 |
| arcs | number | 1 | 1 |
| flicker | number | 0.6 | 0.6 |
| fill | number | 0 | 0 |
| speed | number | 2.5 | 2.5 |
| interactive | boolean | true | true |
| cursorIntensity | number | 0.75 | 0.75 |
| cursorRadius | number | 100 | 100 |
| theme | 'dark' \| 'light' | 'dark' | dark |
| onRender | (canvas: HTMLCanvasElement) => void | undefined | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 985](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.jsx#L985)
- [pointerdown, line 986](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.jsx#L986)
- [pointerleave, line 987](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.jsx#L987)
- [pointercancel, line 988](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.jsx#L988)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricLogo/ElectricLogo.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
