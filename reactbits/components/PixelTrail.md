# PixelTrail

Category: Animations. Public entry: [PixelTrail](https://reactbits.dev/animations/pixel-trail).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/PixelTrail/PixelTrail.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/PixelTrail/PixelTrail.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/PixelTrail/PixelTrail.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| gridSize | number | 40 | 40 |
| trailSize | number | 0.1 | 0.1 |
| maxAge | number | 250 | 250 |
| interpolate | number | 5 | 5 |
| easingFunction | (x: number) => number | x => x | — |
| color | string | '#ffffff' | #ffffff |
| trailColor | string | undefined | — |
| gooeyFilter | { strength: number } \| false | { strength: 2 } | — |
| shape | 'square' \| 'circle' \| 'diamond' | 'square' | square |
| gap | number | 0.08 | 0.08 |
| decay | 'fade' \| 'shrink' \| 'dither' | 'fade' | fade |
| flow | number | 0 | 0 |
| gravity | number | 0 | 0 |
| sparkle | number | 0 | 0 |
| shine | number | 0.6 | 0.6 |
| glow | number | 0.4 | 0.4 |
| clickBurst | boolean | false | false |
| imageSrc | string | undefined | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 657](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L657)
- [pointermove, line 658](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L658)
- [pointerdown, line 659](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L659)
- [pointerleave, line 660](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L660)
- [blur, line 661](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L661)

## Motion locations

- [ease, line 272](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.jsx#L272): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTrail/PixelTrail.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
