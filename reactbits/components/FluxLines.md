# FluxLines

Category: Backgrounds. Public entry: [FluxLines](https://reactbits.dev/backgrounds/flux-lines).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/FluxLines/FluxLines.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/FluxLines/FluxLines.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/FluxLines/FluxLines.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#ffffff', '#ffffff', '#ffffff'] | — |
| speed | number | 0.5 | 0.5 |
| scale | number | 1.6 | 1.6 |
| turbulence | number | 1 | 1 |
| fluidity | number | 0.1 | 0.1 |
| rimWidth | number | 0.2 | 0.2 |
| sharpness | number | 2.5 | 2.5 |
| shimmer | number | 1.5 | 1.5 |
| glow | number | 2 | 2 |
| lineWidth | number | 1 | 1 |
| flowDirection | 'up' \| 'down' \| 'left' \| 'right' | 'down' | down |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 1 | 1 |
| mouseRadius | number | 0.35 | 0.35 |
| mouseDampening | number | 0.15 | 0.15 |
| clickSwirl | boolean | true | true |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| transparent | boolean | true | true |
| backgroundColor | string | '#120f17' | — |
| opacity | number | 1 | 1 |
| paused | boolean | false | false |
| mixBlendMode | string | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 430](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L430)
- [pointerdown, line 431](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L431)
- [pointerup, line 432](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L432)
- [pointercancel, line 433](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L433)
- [pointerleave, line 434](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L434)
- [visibilitychange, line 435](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.jsx#L435)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FluxLines/FluxLines.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
