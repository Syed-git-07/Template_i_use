# Lightfall

Category: Backgrounds. Public entry: [Lightfall](https://reactbits.dev/backgrounds/lightfall).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Lightfall/Lightfall.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Lightfall/Lightfall.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Lightfall/Lightfall.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#ffffff'] | — |
| backgroundColor | string | '#94a3b8' | #94a3b8 |
| speed | number | 0.3 | 0.3 |
| streakCount | number | 2 | 2 |
| streakWidth | number | 0.8 | 0.8 |
| streakLength | number | 1 | 1 |
| density | number | 0.6 | 0.6 |
| twinkle | number | 0.3 | 0.3 |
| glow | number | 1 | 1 |
| backgroundGlow | number | 0.1 | 0.1 |
| headGlow | number | 0.6 | 0.6 |
| depth | number | 0.5 | 0.5 |
| bloom | number | 0.35 | 0.35 |
| zoom | number | 3 | 3 |
| opacity | number | 1 | 1 |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 0.4 | 0.4 |
| mouseRadius | number | 0.45 | 0.45 |
| mouseDampening | number | 0.15 | 0.15 |
| lens | number | 0.5 | 0.5 |
| holdToWarp | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0 | 0 |
| lightMode | boolean | false | false |
| mixBlendMode | string | undefined | — |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 394](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L394)
- [webglcontextrestored, line 395](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L395)
- [pointermove, line 690](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L690)
- [pointerdown, line 691](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L691)
- [pointerup, line 692](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L692)
- [pointercancel, line 693](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L693)
- [pointerleave, line 694](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L694)
- [visibilitychange, line 695](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.jsx#L695)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Lightfall/Lightfall.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
