# GridMotion

Category: Backgrounds. Public entry: [GridMotion](https://reactbits.dev/backgrounds/grid-motion).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/GridMotion/GridMotion.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/GridMotion/GridMotion.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/GridMotion/GridMotion.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<string \| ReactNode \| { src: string; alt?: string }> | [] | — |
| rows | number | 4 | 4 |
| aspectRatio | number | 1.33 | 1.33 |
| gap | number | 16 | 16 |
| radius | number | 14 | 14 |
| angle | number | -12 | -12 |
| tilt | number | 0 | 0 |
| speed | number | 24 | 24 |
| direction | 'alternate' \| 'left' \| 'right' | 'alternate' | alternate |
| parallax | number | 0.5 | 0.5 |
| spotlight | number | 0.6 | 0.6 |
| dim | number | 0.35 | 0.35 |
| grayscale | boolean | false | false |
| fade | number | 0.5 | 0.5 |
| tileColor | string | - | — |
| textColor | string | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 160](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx#L160)
- [pointerdown, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx#L161)
- [pointerup, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx#L162)
- [blur, line 163](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx#L163)
- [pointerleave, line 164](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.jsx#L164)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridMotion/GridMotion.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
