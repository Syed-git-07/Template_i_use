# InfiniteMenu

Category: Components. Public entry: [InfiniteMenu](https://reactbits.dev/components/infinite-menu).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/InfiniteMenu/InfiniteMenu.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/InfiniteMenu/InfiniteMenu.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/InfiniteMenu/InfiniteMenu.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ image: string; title?: string; description?: string; link?: string }> | [] | — |
| count | number | 160 | 160 |
| tileSize | number | 0.63 | 0.63 |
| roundness | number | 0.2 | 0.2 |
| zoom | number | 1.65 | 1.65 |
| pullBack | number | 1 | 1 |
| stretch | number | 0.6 | 0.6 |
| inertia | number | 0.6 | 0.6 |
| autoplay | number | 3 | 3 |
| grayscale | boolean | true | true |
| dim | number | 0.5 | 0.5 |
| intro | boolean | true | true |
| showInfo | boolean | true | true |
| renderInfo | (item, index, moving) => ReactNode | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| accentColor | string | - | — |
| backgroundColor | string | - | — |
| onActiveChange | (item, index) => void | - | — |
| onItemClick | (item, index) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerdown, line 770](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L770)
- [pointermove, line 771](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L771)
- [pointerup, line 772](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L772)
- [pointercancel, line 773](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L773)
- [keydown, line 774](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L774)
- [pointerenter, line 775](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L775)
- [pointerleave, line 776](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L776)
- [focusin, line 777](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L777)
- [focusout, line 778](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L778)
- [onClick, line 876](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L876)
- [onClick, line 885](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L885)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteMenu/InfiniteMenu.css); motion-related lines: 40, 104, 110, 117.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
