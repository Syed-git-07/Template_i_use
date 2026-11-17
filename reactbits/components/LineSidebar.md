# LineSidebar

Category: Components. Public entry: [LineSidebar](https://reactbits.dev/components/line-sidebar).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/LineSidebar/LineSidebar.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/LineSidebar/LineSidebar.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/LineSidebar/LineSidebar.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/LineSidebar/LineSidebar.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | string[] | [...] | — |
| accentColor | string | "#A855F7" | #A855F7 |
| textColor | string | "#c4c4c4" | #c4c4c4 |
| markerColor | string | "#6c6c6c" | #6c6c6c |
| showIndex | boolean | true | true |
| showMarker | boolean | true | true |
| proximityRadius | number | 100 | 100 |
| maxShift | number | 30 | 30 |
| falloff | "linear" \| "smooth" \| "sharp" | "smooth" | smooth |
| markerLength | number | 60 | 60 |
| markerGap | number | 0 | 0 |
| tickScale | number | 0.5 | 0.5 |
| scaleTick | boolean | true | true |
| itemGap | number | 20 | 20 |
| fontSize | number | 1.1 | 1.1 |
| smoothing | number | 100 | 100 |
| defaultActive | number \| null | null | — |
| onItemClick | (index, label) => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [onPointerMove, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/LineSidebar/LineSidebar.jsx#L158)
- [onPointerLeave, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/LineSidebar/LineSidebar.jsx#L158)
- [onClick, line 167](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/LineSidebar/LineSidebar.jsx#L167)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/LineSidebar/LineSidebar.css); motion-related lines: 33.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
