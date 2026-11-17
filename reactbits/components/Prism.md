# Prism

Category: Backgrounds. Public entry: [Prism](https://reactbits.dev/backgrounds/prism).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Prism/Prism.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Prism/Prism.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Prism/Prism.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| animationType | 'rotate' \| '3drotate' \| 'hover' \| 'static' | 'rotate' | rotate |
| timeScale | number | 0.5 | 0.5 |
| colors | string[] | [] | — |
| glow | number | 1 | 1 |
| scale | number | 3.6 | 3.6 |
| height | number | 3.5 | 3.5 |
| baseWidth | number | 5.5 | 5.5 |
| hueShift | number | 0 | 0 |
| colorFrequency | number | 1 | 1 |
| saturation | number | 1.5 | 1.5 |
| noise | number | 0 | 0 |
| offset | { x?: number; y?: number } | { x: 0, y: 0 } | — |
| interactive | boolean | true | true |
| hoverStrength | number | 2 | 2 |
| inertia | number | 0.05 | 0.05 |
| intro | boolean | true | true |
| resolution | number | 0.5 | 0.5 |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 416](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.jsx#L416)
- [blur, line 417](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.jsx#L417)
- [pointerleave, line 418](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.jsx#L418)
- [visibilitychange, line 419](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.jsx#L419)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Prism/Prism.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
