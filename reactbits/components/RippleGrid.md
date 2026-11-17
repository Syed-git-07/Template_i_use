# RippleGrid

Category: Backgrounds. Public entry: [RippleGrid](https://reactbits.dev/backgrounds/ripple-grid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/RippleGrid/RippleGrid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/RippleGrid/RippleGrid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/RippleGrid/RippleGrid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#ffffff' | #ffffff |
| variant | 'lines' \| 'dots' \| 'cross' | 'lines' | lines |
| cellSize | number | 48 | 48 |
| lineWidth | number | 1 | 1 |
| glow | number | 0.6 | 0.6 |
| rippleStrength | number | 1 | 1 |
| rippleSpeed | number | 1 | 1 |
| rippleSize | number | 1 | 1 |
| autoRipple | 'center' \| 'random' \| 'none' | 'center' | center |
| rippleInterval | number | 2.6 | 2.6 |
| tilt | number | 0 | 0 |
| rotation | number | 0 | 0 |
| mouseInteraction | boolean | true | true |
| clickRipple | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0.5 | 0.5 |
| opacity | number | 1 | 1 |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 450](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.jsx#L450)
- [pointerdown, line 451](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.jsx#L451)
- [pointerleave, line 452](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.jsx#L452)
- [visibilitychange, line 453](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.jsx#L453)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/RippleGrid/RippleGrid.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
