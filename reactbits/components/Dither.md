# Dither

Category: Backgrounds. Public entry: [Dither](https://reactbits.dev/backgrounds/dither).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Dither/Dither.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Dither/Dither.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Dither/Dither.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| waveColor | string \| [number, number, number] | [0.5, 0.5, 0.5] | — |
| backgroundColor | string \| [number, number, number] | [0, 0, 0] | — |
| ditherMode | 'bayer' \| 'bayer4' \| 'bayer2' \| 'halftone' \| 'lines' \| 'crosshatch' \| 'noise' \| 'none' | 'bayer' | bayer |
| palette | string[] | - | — |
| colorNum | number | 4 | 4 |
| pixelSize | number | 2 | 2 |
| scale | number | 1 | 1 |
| waveSpeed | number | 0.05 | 0.05 |
| waveFrequency | number | 3 | 3 |
| waveAmplitude | number | 0.3 | 0.3 |
| contrast | number | 1 | 1 |
| brightness | number | 0 | 0 |
| enableMouseInteraction | boolean | true | true |
| mouseEffect | 'erase' \| 'reveal' \| 'ripple' | 'erase' | erase |
| mouseRadius | number | 1 | 1 |
| mouseStrength | number | 1 | 1 |
| trail | number | 0.5 | 0.5 |
| clickRipple | boolean | true | true |
| intro | boolean | true | true |
| disableAnimation | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 616](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L616)
- [pointerdown, line 617](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L617)
- [pointerup, line 618](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L618)
- [pointercancel, line 619](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L619)
- [pointerleave, line 620](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L620)
- [visibilitychange, line 621](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.jsx#L621)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Dither/Dither.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
