# Hyperspeed

Category: Backgrounds. Public entry: [Hyperspeed](https://reactbits.dev/backgrounds/hyperspeed).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Hyperspeed/Hyperspeed.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Hyperspeed/Hyperspeed.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Hyperspeed/Hyperspeed.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| tailColors | string[] | - | — |
| headColors | string[] | - | — |
| poleColors | string[] | - | — |
| curve | 'straight' \| 'gentle' \| 'winding' \| 'hills' \| 'racing' \| 'deep' | 'winding' | winding |
| curvature | number | 1 | 1 |
| speed | number | 1 | 1 |
| boost | number | 3 | 3 |
| fov | number | 90 | 90 |
| boostFov | number | 130 | 130 |
| lanes | number | 3 | 3 |
| roadWidth | number | 10 | 10 |
| medianWidth | number | 2 | 2 |
| density | number | 40 | 40 |
| trailLength | number | 1 | 1 |
| lightSize | number | 1 | 1 |
| poles | number | 20 | 20 |
| poleHeight | number | 1 | 1 |
| dust | number | 100 | 100 |
| glow | number | 0.6 | 0.6 |
| reflections | number | 0.5 | 0.5 |
| roadOpacity | number | 0.1 | 0.1 |
| steer | number | 0.35 | 0.35 |
| roadColor | string | - | — |
| lineColor | string | - | — |
| background | string | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| interactive | boolean | true | true |
| boosting | boolean | false | false |
| onBoostStart | () => void | - | — |
| onBoostEnd | () => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, three

## Interaction locations

- [pointerdown, line 1019](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1019)
- [pointermove, line 1020](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1020)
- [pointerleave, line 1021](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1021)
- [contextmenu, line 1022](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1022)
- [pointerup, line 1023](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1023)
- [pointercancel, line 1024](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1024)
- [blur, line 1025](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.jsx#L1025)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Hyperspeed/Hyperspeed.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
