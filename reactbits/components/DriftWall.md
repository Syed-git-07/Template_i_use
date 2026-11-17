# DriftWall

Category: Components. Public entry: [DriftWall](https://reactbits.dev/components/drift-wall).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/DriftWall/DriftWall.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/DriftWall/DriftWall.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/DriftWall/DriftWall.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | array | 15 demo tiles | — |
| columns | number | 5 | 5 |
| tileWidth | number | 200 | 200 |
| tileHeight | number | 132 | 132 |
| gap | number | 18 | 18 |
| radius | number | 14 | 14 |
| tilt | number | 16 | 16 |
| turn | number | -14 | -14 |
| roll | number | 0 | 0 |
| perspective | number | 1200 | 1200 |
| depth | number | 120 | 120 |
| speed | number | 42 | 42 |
| direction | "up" \| "down" | "up" | up |
| variance | number | 0.45 | 0.45 |
| parallax | number | 0.6 | 0.6 |
| pauseOnHover | boolean | false | false |
| lift | number | 64 | 64 |
| fade | number | 0.6 | 0.6 |
| dim | number | 0.55 | 0.55 |
| grayscale | boolean | false | false |
| overlayColor | string | "#060010" | #060010 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 70](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.jsx#L70)
- [onPointerMove, line 264](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.jsx#L264)
- [onPointerEnter, line 265](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.jsx#L265)
- [onPointerLeave, line 268](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.jsx#L268)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DriftWall/DriftWall.css); motion-related lines: 72, 84, 95, 121.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
