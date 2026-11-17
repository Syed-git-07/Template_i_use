# CircularGallery

Category: Components. Public entry: [CircularGallery](https://reactbits.dev/components/circular-gallery).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/CircularGallery/CircularGallery.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/CircularGallery/CircularGallery.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/CircularGallery/CircularGallery.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ image: string; text?: string; description?: string; alt?: string }> | 12 sample photos | — |
| bend | number | 3 | 3 |
| itemSize | number | 1 | 1 |
| itemAspect | number | 0.78 | 0.78 |
| gap | number | 0.26 | 0.26 |
| borderRadius | number | 0.05 | 0.05 |
| wave | number | 1 | 1 |
| fadeEdges | number | 0.12 | 0.12 |
| shadow | number | 0.25 | 0.25 |
| textColor | string | '#ffffff' | #ffffff |
| font | string | 'bold 30px Figtree' | bold 30px Figtree |
| fontUrl | string | undefined | — |
| showTitles | boolean | true | true |
| scrollSpeed | number | 2 | 2 |
| scrollEase | number | 0.05 | 0.05 |
| snap | boolean | true | true |
| autoScroll | number | 0 | 0 |
| grayscale | boolean | false | false |
| openOnClick | boolean | true | true |
| intro | boolean | true | true |
| onItemClick | (item, index) => void | - | — |
| onActiveChange | (index) => void | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerdown, line 993](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L993)
- [pointermove, line 994](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L994)
- [pointerup, line 995](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L995)
- [pointercancel, line 996](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L996)
- [pointerleave, line 997](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L997)
- [wheel, line 998](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L998)
- [keydown, line 999](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L999)
- [focusin, line 1000](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1000)
- [focusout, line 1001](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1001)
- [visibilitychange, line 1002](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1002)
- [keydown, line 1003](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1003)
- [pointerdown, line 1004](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1004)
- [onClick, line 1083](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1083)
- [onFocus, line 1100](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1100)
- [onClick, line 1101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L1101)

## Motion locations

- [velocity, line 377](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.jsx#L377): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CircularGallery/CircularGallery.css); motion-related lines: 75.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, network, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
