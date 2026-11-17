# DotGrid

Category: Backgrounds. Public entry: [DotGrid](https://reactbits.dev/backgrounds/dot-grid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/DotGrid/DotGrid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/DotGrid/DotGrid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/DotGrid/DotGrid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| baseColor | string | '#3a3446' | #3a3446 |
| activeColor | string | '#ffffff' | #ffffff |
| shape | 'circle' \| 'square' | 'circle' | circle |
| dotSize | number | 5 | 5 |
| gap | number | 18 | 18 |
| proximity | number | 140 | 140 |
| strength | number | 1 | 1 |
| bounce | number | 0.6 | 0.6 |
| tension | number | 0.4 | 0.4 |
| returnDuration | number | 0.8 | 0.8 |
| shockRadius | number | 320 | 320 |
| shockStrength | number | 5 | 5 |
| swell | number | 0.8 | 0.8 |
| stretch | number | 0.5 | 0.5 |
| glow | number | 0.5 | 0.5 |
| fade | number | 0 | 0 |
| opacity | number | 1 | 1 |
| intro | boolean | true | true |
| mouseInteraction | boolean | true | true |
| clickShock | boolean | true | true |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 568](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx#L568)
- [pointerdown, line 569](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx#L569)
- [pointerout, line 570](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx#L570)
- [blur, line 571](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx#L571)
- [visibilitychange, line 593](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.jsx#L593)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotGrid/DotGrid.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
