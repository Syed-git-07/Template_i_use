# Threads

Category: Backgrounds. Public entry: [Threads](https://reactbits.dev/backgrounds/threads).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Threads/Threads.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Threads/Threads.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Threads/Threads.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Threads/Threads.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string \| number[] | [1, 1, 1] | — |
| accentColor | string \| number[] | - | — |
| lineCount | number | 90 | 90 |
| thickness | number | 0.6 | 0.6 |
| softness | number | 1.3 | 1.3 |
| amplitude | number | 1.7 | 1.7 |
| distance | number | 0.4 | 0.4 |
| waves | number | 1.05 | 1.05 |
| speed | number | 0.6 | 0.6 |
| split | number | 0.04 | 0.04 |
| fray | number | 0.5 | 0.5 |
| angle | number | 25 | 25 |
| taper | number | 0.85 | 0.85 |
| brightness | number | 1.4 | 1.4 |
| parting | number | 0 | 0 |
| enableMouseInteraction | boolean | false | false |
| fade | number | 0 | 0 |
| opacity | number | 1 | 1 |
| seed | number | 0 | 0 |
| paused | boolean | false | false |
| className | string | '' | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 498](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Threads/Threads.jsx#L498)
- [pointerleave, line 499](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Threads/Threads.jsx#L499)
- [visibilitychange, line 500](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Threads/Threads.jsx#L500)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Threads/Threads.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
