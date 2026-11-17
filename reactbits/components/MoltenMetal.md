# MoltenMetal

Category: Backgrounds. Public entry: [MoltenMetal](https://reactbits.dev/backgrounds/molten-metal).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MoltenMetal/MoltenMetal.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/MoltenMetal/MoltenMetal.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/MoltenMetal/MoltenMetal.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/MoltenMetal/MoltenMetal.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#5227FF', '#FF9FFC'] | — |
| coreColor | string | '#FFFFFF' | #FFFFFF |
| backgroundColor | string | 'transparent' | transparent |
| lightMode | boolean | false | false |
| speed | number | 0.35 | 0.35 |
| scale | number | 4 | 4 |
| detail | number | 3 | 3 |
| glow | number | 1.6 | 1.6 |
| thickness | number | 1 | 1 |
| swirl | number | 1 | 1 |
| turbulence | number | 0.2 | 0.2 |
| haze | number | 0.75 | 0.75 |
| brightness | number | 1.3 | 1.3 |
| colorMode | 'molten' \| 'ember' \| 'frost' | 'molten' | molten |
| rotation | number | 0 | 0 |
| offsetX | number | 0 | 0 |
| offsetY | number | 0 | 0 |
| drift | number | 0.3 | 0.3 |
| grain | number | 0.05 | 0.05 |
| opacity | number | 1 | 1 |
| intro | boolean | true | true |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 0.5 | 0.5 |
| flareOnClick | boolean | true | true |
| paused | boolean | false | false |
| dpr | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 585](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MoltenMetal/MoltenMetal.jsx#L585)
- [pointerdown, line 586](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MoltenMetal/MoltenMetal.jsx#L586)
- [pointerleave, line 587](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MoltenMetal/MoltenMetal.jsx#L587)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MoltenMetal/MoltenMetal.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
