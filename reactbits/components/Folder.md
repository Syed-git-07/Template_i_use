# Folder

Category: Components. Public entry: [Folder](https://reactbits.dev/components/folder).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Folder/Folder.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Folder/Folder.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Folder/Folder.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | FolderItem[] | Three sample documents | — |
| children | ReactNode | undefined | — |
| mode | 'flap' \| 'book' | 'flap' | flap |
| variant | 'solid' \| 'glass' \| 'matte' | 'solid' | solid |
| layout | 'spread' \| 'stack' \| 'row' | 'spread' | spread |
| color | string | '#3d8bff' | #3d8bff |
| paperColor | string | '#ffffff' | #ffffff |
| label | string | undefined | — |
| tabPosition | 'left' \| 'center' \| 'right' | 'right' | right |
| openOn | 'click' \| 'hover' | 'click' | click |
| open | boolean | undefined | — |
| defaultOpen | boolean | false | false |
| onOpenChange | (open: boolean) => void | undefined | — |
| onItemClick | (item, index: number) => void | undefined | — |
| onItemDrop | (item, index: number, inside: boolean) => void | undefined | — |
| draggable | boolean | true | true |
| zoomOnClick | boolean | true | true |
| peek | boolean | true | true |
| intro | boolean | true | true |
| size | number | 1 | 1 |
| frost | number | 0.25 | 0.25 |
| tilt | number | 0.5 | 0.5 |
| speed | number | 1 | 1 |
| bounce | number | 0.4 | 0.4 |
| closeOnOutsideClick | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [load, line 1342](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1342)
- [pointermove, line 1693](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1693)
- [pointerleave, line 1694](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1694)
- [pointerdown, line 1695](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1695)
- [pointerup, line 1696](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1696)
- [pointercancel, line 1697](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1697)
- [pointerdown, line 1698](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1698)
- [keydown, line 1699](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1699)
- [webglcontextlost, line 1772](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1772)
- [onClick, line 1851](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1851)
- [onKeyDown, line 1852](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1852)
- [onClick, line 1889](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1889)
- [onKeyDown, line 1890](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1890)

## Motion locations

- [bounce, line 872](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L872): computed; read the linked expression
- [velocity, line 894](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L894): 0
- [threshold, line 1715](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.jsx#L1715): 0.2

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Folder/Folder.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
