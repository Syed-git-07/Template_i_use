# MetallicPaint

Category: Animations. Public entry: [MetallicPaint](https://reactbits.dev/animations/metallic-paint).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetallicPaint/MetallicPaint.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/MetallicPaint/MetallicPaint.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/MetallicPaint/MetallicPaint.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/MetallicPaint/MetallicPaint.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| imageSrc | string | undefined | — |
| text | string | undefined | — |
| fontFamily | string | 'system-ui, sans-serif' | system-ui, sans-serif |
| fontWeight | number | 800 | 800 |
| color | string | '#ffffff' | #ffffff |
| backgroundColor | string | 'transparent' | transparent |
| density | number | 2 | 2 |
| softness | number | 0.1 | 0.1 |
| dispersion | number | 0.3 | 0.3 |
| distortion | number | 0.07 | 0.07 |
| edgeBend | number | 0.6 | 0.6 |
| angle | number | 70 | 70 |
| speed | number | 1 | 1 |
| scale | number | 0.6 | 0.6 |
| rotation | number | 0 | 0 |
| mouseTilt | number | 0.5 | 0.5 |
| lightMode | boolean | false | false |
| intro | boolean | true | true |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 856](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetallicPaint/MetallicPaint.jsx#L856)
- [pointermove, line 857](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetallicPaint/MetallicPaint.jsx#L857)
- [pointerleave, line 858](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetallicPaint/MetallicPaint.jsx#L858)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetallicPaint/MetallicPaint.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, network, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
