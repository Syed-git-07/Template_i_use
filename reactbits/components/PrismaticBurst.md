# PrismaticBurst

Category: Backgrounds. Public entry: [PrismaticBurst](https://reactbits.dev/backgrounds/prismatic-burst).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/PrismaticBurst/PrismaticBurst.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/PrismaticBurst/PrismaticBurst.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/PrismaticBurst/PrismaticBurst.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | undefined | — |
| intensity | number | 2 | 2 |
| speed | number | 0.5 | 0.5 |
| animationType | "rotate" \| "rotate3d" \| "hover" | "rotate3d" | rotate3d |
| zoom | number | 1 | 1 |
| rayWidth | number | 1 | 1 |
| rayCount | number | 0 | 0 |
| distort | number | 0 | 0 |
| twist | number | 0 | 0 |
| flow | number | 0 | 0 |
| centerFade | number | 1 | 1 |
| glow | number | 0 | 0 |
| grain | number | 0.8 | 0.8 |
| offset | { x?: number \| string; y?: number \| string } | { x: 0, y: 0 } | — |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 0.5 | 0.5 |
| hoverDampness | number | 0.25 | 0.25 |
| clickBurst | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0 | 0 |
| quality | "low" \| "medium" \| "high" | "high" | high |
| resolution | number | undefined | — |
| lightMode | boolean | false | false |
| mixBlendMode | string | undefined | — |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 462](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L462)
- [webglcontextrestored, line 463](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L463)
- [pointermove, line 830](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L830)
- [pointerdown, line 831](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L831)
- [pointerleave, line 832](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L832)
- [visibilitychange, line 833](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.jsx#L833)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PrismaticBurst/PrismaticBurst.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
