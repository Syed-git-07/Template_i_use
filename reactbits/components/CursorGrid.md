# CursorGrid

Category: Animations. Public entry: [CursorGrid](https://reactbits.dev/animations/cursor-grid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/CursorGrid/CursorGrid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/CursorGrid/CursorGrid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/CursorGrid/CursorGrid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#ffffff' | — |
| gridColor | string | '#ffffff' | — |
| cellSize | number | 60 | 60 |
| highlight | 'area' \| 'cell' | 'area' | area |
| gridStyle | 'lines' \| 'dashed' \| 'dots' \| 'crosses' | 'lines' | lines |
| radius | number | 140 | 140 |
| falloff | 'smooth' \| 'linear' \| 'sharp' | 'smooth' | smooth |
| holdTime | number | 400 | 400 |
| fadeDuration | number | 800 | 800 |
| lineWidth | number | 1 | 1 |
| maxOpacity | number | 1 | 1 |
| fillOpacity | number | 0.06 | 0.06 |
| gridOpacity | number | 0.08 | 0.08 |
| spotlight | number | 0.6 | 0.6 |
| cellGap | number | 0 | 0 |
| cellRadius | number | 0 | 0 |
| clickPulse | boolean | true | true |
| pulseSpeed | number | 600 | 600 |
| ambient | number | 0 | 0 |
| edgeFade | number | 0.2 | 0.2 |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| children | ReactNode | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 552](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.jsx#L552)
- [pointerdown, line 553](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.jsx#L553)
- [pointerleave, line 554](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.jsx#L554)
- [visibilitychange, line 555](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.jsx#L555)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CursorGrid/CursorGrid.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
