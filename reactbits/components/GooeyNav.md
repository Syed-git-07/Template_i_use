# GooeyNav

Category: Components. Public entry: [GooeyNav](https://reactbits.dev/components/gooey-nav).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/GooeyNav/GooeyNav.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/GooeyNav/GooeyNav.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/GooeyNav/GooeyNav.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | { label: string; href?: string; icon?: ReactNode }[] | - | — |
| initialActiveIndex | number | 0 | 0 |
| activeIndex | number | - | — |
| onChange | (index: number, item) => void | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| color | string | - | — |
| activeTextColor | string | - | — |
| colors | string[] | [] | — |
| size | 'sm' \| 'md' \| 'lg' | 'md' | md |
| frame | boolean | true | true |
| animationTime | number | 600 | 600 |
| particleCount | number | 15 | 15 |
| spread | number | 56 | 56 |
| timeVariance | number | 300 | 300 |
| gooeyness | number | 0.5 | 0.5 |
| wobble | number | 0.5 | 0.5 |
| hoverEffect | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerover, line 700](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.jsx#L700)
- [pointerleave, line 701](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.jsx#L701)

## Motion locations

- [mass, line 363](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.jsx#L363): 0
- [velocity, line 363](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.jsx#L363): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GooeyNav/GooeyNav.css); motion-related lines: 98.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
