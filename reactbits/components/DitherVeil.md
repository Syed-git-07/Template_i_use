# DitherVeil

Category: Animations. Public entry: [DitherVeil](https://reactbits.dev/animations/dither-veil).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/DitherVeil/DitherVeil.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/DitherVeil/DitherVeil.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/DitherVeil/DitherVeil.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | 'https://images.unsplash.com/...' | https://images.unsplash.com/photo-1737071371043-761e02b1ef95?q=80&w=1400&auto=format&fit=crop |
| fit | 'contain' \| 'cover' | 'contain' | contain |
| pattern | 'bayer' \| 'noise' \| 'atkinson' \| 'floyd' \| 'lines' | 'floyd' | floyd |
| palette | 'duotone' \| 'rgb' | 'duotone' | duotone |
| pixelSize | number | 2 | 2 |
| levels | number | 2 | 2 |
| inkColor | string | '#120f17' | #120f17 |
| paperColor | string | '#f4f1ea' | #f4f1ea |
| contrast | number | 1.15 | 1.15 |
| brightness | number | 0 | 0 |
| revealRadius | number | 200 | 200 |
| softness | number | 0.6 | 0.6 |
| linger | number | 1 | 1 |
| rimColor | string | '#a78bfa' | #a78bfa |
| rim | number | 0 | 0 |
| reverse | boolean | false | false |
| wander | boolean | false | false |
| clickBurst | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 784](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx#L784)
- [pointerenter, line 785](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx#L785)
- [pointerdown, line 786](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx#L786)
- [pointerleave, line 787](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx#L787)
- [pointercancel, line 788](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.jsx#L788)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/DitherVeil/DitherVeil.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
