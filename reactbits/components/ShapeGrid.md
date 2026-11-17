# ShapeGrid

Category: Backgrounds. Public entry: [ShapeGrid](https://reactbits.dev/backgrounds/shape-grid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/ShapeGrid/ShapeGrid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/ShapeGrid/ShapeGrid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/ShapeGrid/ShapeGrid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| shape | 'square' \| 'tile' \| 'hexagon' \| 'triangle' \| 'diamond' \| 'circle' \| 'cross' \| 'dot' | 'square' | square |
| cellSize | number | 40 | 40 |
| lineWidth | number | 1 | 1 |
| direction | 'diagonal' \| 'up' \| 'down' \| 'left' \| 'right' \| 'none' | 'diagonal' | diagonal |
| speed | number | 0.5 | 0.5 |
| lineColor | string | '#2a2734' | #2a2734 |
| hoverColor | string | '#ffffff' | #ffffff |
| hoverFillColor | string | hoverColor | — |
| fillOpacity | number | 0.15 | 0.15 |
| rainbow | boolean | false | false |
| tiltX | number | 0 | 0 |
| tiltY | number | 0 | 0 |
| radius | number | 1.5 | 1.5 |
| trail | number | 0.6 | 0.6 |
| glow | number | 0.35 | 0.35 |
| twinkle | number | 0 | 0 |
| fade | number | 1 | 1 |
| clickCascade | boolean | true | true |
| intro | boolean | true | true |
| opacity | number | 1 | 1 |
| backgroundColor | string | 'transparent' | transparent |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 713](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.jsx#L713)
- [pointerdown, line 714](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.jsx#L714)
- [pointerleave, line 715](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.jsx#L715)
- [blur, line 716](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.jsx#L716)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ShapeGrid/ShapeGrid.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
