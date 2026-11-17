# RippleDistortion

Category: Animations. Public entry: [RippleDistortion](https://reactbits.dev/animations/ripple-distortion).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/RippleDistortion/RippleDistortion.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/RippleDistortion/RippleDistortion.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/RippleDistortion/RippleDistortion.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/RippleDistortion/RippleDistortion.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | 'https://images.unsplash.com/...' | https://images.unsplash.com/photo-1782977389500-dd7adad33ebe?q=80&w=3416&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D |
| brushSize | number | 150 | 150 |
| strength | number | 0.2 | 0.2 |
| swirl | number | 1 | 1 |
| rings | number | 4 | 4 |
| spread | number | 5 | 5 |
| fade | number | 3 | 3 |
| spacing | number | 15 | 15 |
| dispersion | number | 0 | 0 |
| glint | number | 0 | 0 |
| tint | string | #a855f7 | #a855f7 |
| tintAmount | number | 0.1 | 0.1 |
| highlightColor | string | #ffffff | #ffffff |
| grayscale | boolean | true | true |
| trigger | 'hover' \| 'click' \| 'both' | 'hover' | hover |
| clickStrength | number | 2 | 2 |
| quality | 'low' \| 'medium' \| 'high' | 'low' | low |
| enabled | boolean | true | true |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 360](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/RippleDistortion/RippleDistortion.jsx#L360)
- [pointerdown, line 361](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/RippleDistortion/RippleDistortion.jsx#L361)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/RippleDistortion/RippleDistortion.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
