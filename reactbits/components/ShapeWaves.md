# ShapeWaves

Category: Backgrounds. Public entry: [ShapeWaves](https://reactbits.dev/backgrounds/shape-waves).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/ShapeWaves/ShapeWaves.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/ShapeWaves/ShapeWaves.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/ShapeWaves/ShapeWaves.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | '' |  |
| fontFamily | string | 'Geist, "Geist Sans", system-ui, sans-serif' | Geist, "Geist Sans", system-ui, sans-serif |
| fontWeight | string \| number | 500 | 500 |
| textSize | number | 0.6 | 0.6 |
| shapes | string | 'mixed' | mixed |
| cellSize | number | 10 | 10 |
| dotSize | number | 0.75 | 0.75 |
| color | string | '#929292' | #929292 |
| hoverColor | string | '#ffffff' | #ffffff |
| backgroundColor | string | '#000000' | #000000 |
| speed | number | 1 | 1 |
| scale | number | 1 | 1 |
| contrast | number | 1 | 1 |
| brightness | number | 0.4 | 0.4 |
| flow | number | 0 | 0 |
| direction | number | 0 | 0 |
| fade | number | 0.25 | 0.25 |
| interactive | boolean | true | true |
| splashRadius | number | 40 | 40 |
| splashStrength | number | 0.4 | 0.4 |
| glow | number | 0.35 | 0.35 |
| intro | boolean | true | true |
| introDuration | number | 1.6 | 1.6 |
| introKey | string \| number | 0 | 0 |
| paused | boolean | false | false |
| onError | (error: Error) => void | undefined | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, vgpu

## Interaction locations

- [visibilitychange, line 805](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx#L805)
- [change, line 806](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx#L806)
- [pointermove, line 807](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx#L807)
- [scroll, line 808](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx#L808)

## Motion locations

- [threshold, line 802](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.jsx#L802): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeWaves/ShapeWaves.css); motion-related lines: 17, 25, 27.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
