# TargetCursor

Category: Animations. Public entry: [TargetCursor](https://reactbits.dev/animations/target-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/TargetCursor/TargetCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/TargetCursor/TargetCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/TargetCursor/TargetCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| targetSelector | string | '.cursor-target' | .cursor-target |
| cursorColor | string | '#ffffff' | #ffffff |
| cursorColorOnTarget | string | - | — |
| spinDuration | number | 2 | 2 |
| hoverDuration | number | 0.2 | 0.2 |
| parallaxOn | boolean | true | true |
| hideDefaultCursor | boolean | true | true |
| size | number | 36 | 36 |
| cornerSize | number | 12 | 12 |
| thickness | number | 3 | 3 |
| padding | number | 6 | 6 |
| matchRadius | boolean | true | true |
| dotSize | number | 4 | 4 |
| blendMode | string | 'difference' | difference |
| showLabel | boolean | true | true |
| clickEffect | boolean | true | true |
| container | RefObject \| HTMLElement | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, react-dom

## Interaction locations

- [change, line 71](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L71)
- [pointermove, line 326](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L326)
- [pointerdown, line 327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L327)
- [pointerup, line 328](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L328)
- [scroll, line 329](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L329)
- [pointerleave, line 330](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L330)
- [blur, line 331](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.jsx#L331)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/TargetCursor/TargetCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
