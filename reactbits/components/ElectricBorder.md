# ElectricBorder

Category: Animations. Public entry: [ElectricBorder](https://reactbits.dev/animations/electric-border).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ElectricBorder/ElectricBorder.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ElectricBorder/ElectricBorder.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ElectricBorder/ElectricBorder.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| color | string | '#7df9ff' | #7df9ff |
| glowColor | string | - | — |
| speed | number | 1 | 1 |
| chaos | number | 0.5 | 0.5 |
| spread | number | 0.6 | 0.6 |
| thickness | number | 1.5 | 1.5 |
| strands | number | 3 | 3 |
| glow | number | 0.6 | 0.6 |
| intensity | number | 0.8 | 0.8 |
| arcs | number | 1 | 1 |
| flicker | number | 0.5 | 0.5 |
| borderRadius | number | 24 | 24 |
| offset | number | 0 | 0 |
| active | boolean | true | true |
| intro | boolean | true | true |
| interactive | boolean | true | true |
| cursorRadius | number | 90 | 90 |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 708](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L708)
- [pointerdown, line 709](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L709)
- [pointerleave, line 710](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L710)
- [webglcontextlost, line 719](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L719)
- [webglcontextrestored, line 720](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L720)
- [visibilitychange, line 738](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.jsx#L738)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ElectricBorder/ElectricBorder.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
