# EvilEye

Category: Backgrounds. Public entry: not present in the current public catalogue.

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/EvilEye/EvilEye.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/EvilEye/EvilEye.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/EvilEye/EvilEye.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/EvilEye/EvilEye.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| eyeColor | string | "#FF6F37" | #FF6F37 |
| intensity | number | 1.5 | 1.5 |
| pupilSize | number | 0.6 | 0.6 |
| irisWidth | number | 0.25 | 0.25 |
| glowIntensity | number | 0.35 | 0.35 |
| scale | number | 0.8 | 0.8 |
| noiseScale | number | 1.0 | 1 |
| pupilFollow | number | 1.0 | 1 |
| flameSpeed | number | 1.0 | 1 |
| backgroundColor | string | "#000000" | #000000 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: ogl, react

## Interaction locations

- [mousemove, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/EvilEye/EvilEye.jsx#L213)
- [mouseleave, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/EvilEye/EvilEye.jsx#L214)
- [resize, line 230](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/EvilEye/EvilEye.jsx#L230)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/EvilEye/EvilEye.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
