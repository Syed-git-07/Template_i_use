# Shredder

Category: Micro. Public entry: [Shredder](https://reactbits.dev/micro/shredder).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/Shredder/Shredder.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/Shredder/Shredder.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/Shredder/Shredder.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | T[] | [] | — |
| renderItem | (item: T, index: number) => ReactNode | - | — |
| onShred | (item: T) => void | - | — |
| onReorder | (items: T[]) => void | - | — |
| width | number | 340 | 340 |
| height | number | 460 | 460 |
| inset | number | 14 | 14 |
| gap | number | 10 | 10 |
| slitHeight | number | 4 | 4 |
| fallHeight | number | 140 | 140 |
| feedSpeed | number | 180 | 180 |
| bite | number | 18 | 18 |
| autoFeed | boolean | true | true |
| stripWidth | number | 10 | 10 |
| curl | number | 1 | 1 |
| autoAnimate | boolean | false | false |
| loop | boolean | false | false |
| loopAfterDelete | boolean | false | false |
| dragTilt | number | 6 | 6 |
| lift | number | 1.02 | 1.02 |
| slitColor | string | "#3f3f46" | #3f3f46 |
| color | string | "#f5f5f5" | #f5f5f5 |
| disabled | boolean | false | false |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, react-dom

## Interaction locations

- [onPointerDown, line 1006](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1006)
- [onPointerMove, line 1007](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1007)
- [onPointerUp, line 1008](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1008)
- [onPointerCancel, line 1009](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1009)
- [onLostPointerCapture, line 1010](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1010)
- [onKeyDown, line 1011](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1011)
- [onDragStart, line 1012](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L1012)

## Motion locations

- [delay, line 290](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.jsx#L290): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/Shredder/Shredder.css); motion-related lines: 56, 104, 106.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, network, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
