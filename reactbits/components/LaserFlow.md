# LaserFlow

Category: Animations. Public entry: [LaserFlow](https://reactbits.dev/animations/laser-flow).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LaserFlow/LaserFlow.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/LaserFlow/LaserFlow.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/LaserFlow/LaserFlow.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/LaserFlow/LaserFlow.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| surfaceRef | RefObject<HTMLElement> | - | — |
| beamPosition | number | 0.6 | 0.6 |
| surfaceLevel | number | 1 | 1 |
| color | string | '#3847ff' | #3847ff |
| intensity | number | 1.8 | 1.8 |
| beamWidth | number | 1.5 | 1.5 |
| flare | number | 1.5 | 1.5 |
| spread | number | 1.5 | 1.5 |
| spill | number | 1 | 1 |
| fog | number | 0.2 | 0.2 |
| dust | number | 1.6 | 1.6 |
| streaks | number | 1.5 | 1.5 |
| dots | number | 1 | 1 |
| pulse | number | 1.5 | 1.5 |
| speed | number | 1.5 | 1.5 |
| seed | number | 3 | 3 |
| mouseInteraction | boolean | true | true |
| revealImage | string | - | — |
| revealRadius | number | 220 | 220 |
| revealOpacity | number | 0.6 | 0.6 |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 848](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LaserFlow/LaserFlow.jsx#L848)
- [pointerleave, line 849](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LaserFlow/LaserFlow.jsx#L849)
- [visibilitychange, line 850](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LaserFlow/LaserFlow.jsx#L850)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LaserFlow/LaserFlow.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
