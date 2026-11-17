# BranchedMenu

Category: Micro. Public entry: [BranchedMenu](https://reactbits.dev/micro/branched-menu).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BranchedMenu/BranchedMenu.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/BranchedMenu/BranchedMenu.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/BranchedMenu/BranchedMenu.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/BranchedMenu/BranchedMenu.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | BranchedMenuItem[] | DEFAULT_ITEMS | — |
| defaultOpen | number \| number[] | 0 | 0 |
| defaultActive | string | "" |  |
| onSelect | (value, item) => void | - | — |
| onToggle | (index, open) => void | - | — |
| color | string | "#f5f5f5" | #f5f5f5 |
| accentColor | string | "#f5f5f5" | #f5f5f5 |
| lineColor | string | "#3f3f46" | #3f3f46 |
| width | number | 240 | 240 |
| rowHeight | number | 36 | 36 |
| indent | number | 40 | 40 |
| trunk | number | 14 | 14 |
| radius | number | 10 | 10 |
| lineWidth | number | 1.5 | 1.5 |
| fontSize | number | 14 | 14 |
| drawDuration | number | 400 | 400 |
| foldDuration | number | 300 | 300 |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onClick, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BranchedMenu/BranchedMenu.jsx#L161)
- [onClick, line 194](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BranchedMenu/BranchedMenu.jsx#L194)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BranchedMenu/BranchedMenu.css); motion-related lines: 48, 76, 93, 118, 123, 140, 160, 183, 185, 189, 193.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
