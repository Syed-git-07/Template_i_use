# MagicRings

Category: Backgrounds. Public entry: [MagicRings](https://reactbits.dev/backgrounds/magic-rings).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/MagicRings/MagicRings.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/MagicRings/MagicRings.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/MagicRings/MagicRings.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#A855F7' | #A855F7 |
| colorTwo | string | '#6366F1' | #6366F1 |
| ringCount | number | 6 | 6 |
| motion | 'pulse' \| 'ripple' \| 'breathe' | 'pulse' | pulse |
| speed | number | 1 | 1 |
| lineThickness | number | 2 | 2 |
| glow | number | 1 | 1 |
| baseRadius | number | 0.35 | 0.35 |
| radiusStep | number | 0.1 | 0.1 |
| expansion | number | 0.1 | 0.1 |
| taper | number | 1.5 | 1.5 |
| rotation | number | 0 | 0 |
| spin | number | 0 | 0 |
| tilt | number | 0 | 0 |
| dispersion | number | 0 | 0 |
| grain | number | 0 | 0 |
| opacity | number | 1 | 1 |
| followMouse | boolean | false | false |
| mouseInfluence | number | 0.2 | 0.2 |
| hoverScale | number | 1.2 | 1.2 |
| hoverIntensity | number | 1 | 1 |
| parallax | number | 0.05 | 0.05 |
| clickBurst | boolean | true | true |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 861](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L861)
- [pointerdown, line 862](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L862)
- [pointerup, line 863](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L863)
- [pointercancel, line 864](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L864)
- [pointerleave, line 865](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L865)
- [webglcontextlost, line 874](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L874)
- [webglcontextrestored, line 875](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L875)
- [visibilitychange, line 890](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.jsx#L890)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagicRings/MagicRings.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
