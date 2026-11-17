# SwarmCursor

Category: Animations. Public entry: [SwarmCursor](https://reactbits.dev/animations/swarm-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/SwarmCursor/SwarmCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/SwarmCursor/SwarmCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/SwarmCursor/SwarmCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| count | number | 800 | 800 |
| size | number | 2.6 | 2.6 |
| shape | 'dot' \| 'streak' \| 'square' | 'dot' | dot |
| color | string | '#ffffff' | — |
| accentColor | string | color | — |
| spread | number | 90 | 90 |
| speed | number | 1 | 1 |
| swirl | number | 0.6 | 0.6 |
| tail | number | 0.5 | 0.5 |
| trail | number | 0.6 | 0.6 |
| wander | number | 0.5 | 0.5 |
| depth | number | 0.7 | 0.7 |
| targets | string | 'a, button, [data-swarm-target]' | a, button, [data-swarm-target] |
| idle | 'roam' \| 'gather' \| 'hide' | 'roam' | roam |
| clickEffect | 'burst' \| 'pulse' \| 'none' | 'burst' | burst |
| hideCursor | boolean | false | false |
| intro | boolean | true | true |
| enabled | boolean | true | true |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 903](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L903)
- [pointerdown, line 904](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L904)
- [pointerup, line 905](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L905)
- [pointercancel, line 906](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L906)
- [pointerleave, line 907](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L907)
- [visibilitychange, line 908](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.jsx#L908)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SwarmCursor/SwarmCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
