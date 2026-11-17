# Cubes

Category: Animations. Public entry: [Cubes](https://reactbits.dev/animations/cubes).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/Cubes/Cubes.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/Cubes/Cubes.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/Cubes/Cubes.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| gridSize | number | 10 | 10 |
| gap | number | 0.18 | 0.18 |
| faceColor | string | '#120F17' | #120F17 |
| edgeColor | string | '#ffffff' | #ffffff |
| edgeWidth | number | 1 | 1 |
| edgeStyle | 'solid' \| 'dashed' \| 'dotted' \| 'none' | 'solid' | solid |
| faceOpacity | number | 1 | 1 |
| shading | number | 0.6 | 0.6 |
| maxAngle | number | 45 | 45 |
| radius | number | 3 | 3 |
| speed | number | 1 | 1 |
| bounce | number | 0.4 | 0.4 |
| brush | number | 1 | 1 |
| perspective | number | 0 | 0 |
| autoAnimate | boolean | true | true |
| rippleOnClick | boolean | true | true |
| rippleColor | string | '#ffffff' | #ffffff |
| rippleSpeed | number | 1 | 1 |
| intro | boolean | true | true |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 626](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx#L626)
- [pointerleave, line 627](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx#L627)
- [pointerdown, line 628](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx#L628)
- [visibilitychange, line 629](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx#L629)

## Motion locations

- [bounce, line 255](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.jsx#L255): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Cubes/Cubes.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
