# FolderFloat

Category: Micro. Public entry: [FolderFloat](https://reactbits.dev/micro/folder-float).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/FolderFloat/FolderFloat.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/FolderFloat/FolderFloat.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/FolderFloat/FolderFloat.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<string \| { label, value }> | DEFAULT_ITEMS | — |
| label | string | "Design feedback" | Design feedback |
| sublabel | string | "" |  |
| trigger | 'hover' \| 'click' | 'hover' | hover |
| defaultOpen | boolean | false | false |
| closeOnSelect | boolean | true | true |
| physics | boolean | true | true |
| drift | number | 0.5 | 0.5 |
| onSelect | (value, index) => void | - | — |
| onOpenChange | (open) => void | - | — |
| folderColor | string | "#3f3f46" | #3f3f46 |
| frontColor | string | "#52525b" | #52525b |
| paperColor | string | "#f5f5f5" | #f5f5f5 |
| itemColor | string | "#f5f5f5" | #f5f5f5 |
| itemTextColor | string | "#18181b" | #18181b |
| labelColor | string | "#f5f5f5" | #f5f5f5 |
| width | number | 200 | 200 |
| height | number | 148 | 148 |
| radius | number | 14 | 14 |
| spread | number | 180 | 180 |
| lift | number | 26 | 26 |
| tilt | number | 8 | 8 |
| flapAngle | number | 34 | 34 |
| restAngle | number | 16 | 16 |
| openDuration | number | 520 | 520 |
| stagger | number | 45 | 45 |
| bounce | number | 0.3 | 0.3 |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, matter-js

## Interaction locations

- [change, line 248](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L248)
- [onPointerEnter, line 330](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L330)
- [onPointerLeave, line 331](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L331)
- [onKeyDown, line 338](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L338)
- [onPointerDown, line 385](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L385)
- [onPointerMove, line 386](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L386)
- [onPointerUp, line 387](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L387)
- [onPointerCancel, line 388](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L388)
- [onClick, line 389](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L389)
- [onClick, line 410](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L410)

## Motion locations

- [friction, line 164](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.jsx#L164): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FolderFloat/FolderFloat.css); motion-related lines: 71, 95, 132, 176, 186, 194, 212, 217, 218, 219, 223, 228, 231, 242, 252, 255, 267, 271, 275.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
