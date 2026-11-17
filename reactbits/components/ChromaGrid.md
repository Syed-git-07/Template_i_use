# ChromaGrid

Category: Components. Public entry: [ChromaGrid](https://reactbits.dev/components/chroma-grid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ChromaGrid/ChromaGrid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ChromaGrid/ChromaGrid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ChromaGrid/ChromaGrid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | ChromaItem[] | Sample photos | — |
| reveal | 'spotlight' \| 'card' | 'spotlight' | spotlight |
| columns | number | 3 | 3 |
| minCardWidth | number | 180 | 180 |
| gap | number | 12 | 12 |
| radius | number | 260 | 260 |
| softness | number | 0.6 | 0.6 |
| damping | number | 0.45 | 0.45 |
| fadeOut | number | 0.6 | 0.6 |
| grayscale | number | 1 | 1 |
| dim | number | 0.12 | 0.12 |
| glow | number | 0.5 | 0.5 |
| borderGlow | number | 1 | 1 |
| aspectRatio | string | '3 / 2' | 3 / 2 |
| cardRadius | number | 22 | 22 |
| showInfo | boolean | true | true |
| frame | boolean | false | false |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 191](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.jsx#L191)
- [pointerdown, line 192](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.jsx#L192)
- [pointerleave, line 193](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.jsx#L193)
- [pointercancel, line 194](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.jsx#L194)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ChromaGrid/ChromaGrid.css); motion-related lines: 60, 193, 198, 203, 208.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
