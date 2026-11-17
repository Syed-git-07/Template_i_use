# ImageTrail

Category: Animations. Public entry: [ImageTrail](https://reactbits.dev/animations/image-trail).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ImageTrail/ImageTrail.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ImageTrail/ImageTrail.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ImageTrail/ImageTrail.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | string[] | [] | — |
| size | number \| string | 190 | 190 |
| aspectRatio | number | 1.1 | 1.1 |
| radius | number \| string | 15 | 15 |
| threshold | number | 80 | 80 |
| lifetime | number | 0.4 | 0.4 |
| appearScale | number | 1 | 1 |
| zoom | number | 1 | 1 |
| flash | number | 0 | 0 |
| exitScale | number | 0.2 | 0.2 |
| drift | number | 0 | 0 |
| rotation | number | 0 | 0 |
| sizeVariance | number | 0 | 0 |
| alignToMotion | boolean | false | false |
| stack | number | 0 | 0 |
| tilt | number | 0 | 0 |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [mousemove, line 180](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L180)
- [touchmove, line 181](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L181)

## Motion locations

- [duration, line 39](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L39): 0.4
- [ease, line 40](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L40): "power4"
- [duration, line 96](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L96): computed; read the linked expression
- [ease, line 97](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L97): computed; read the linked expression
- [duration, line 111](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L111): 0.5
- [ease, line 111](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L111): "power1"
- [duration, line 129](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L129): 0.4
- [ease, line 130](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L130): computed; read the linked expression
- [duration, line 140](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L140): 1.5
- [ease, line 141](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.jsx#L141): "power4"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ImageTrail/ImageTrail.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
