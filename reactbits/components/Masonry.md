# Masonry

Category: Components. Public entry: [Masonry](https://reactbits.dev/components/masonry).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Masonry/Masonry.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Masonry/Masonry.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Masonry/Masonry.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ id, img, width?, height?, title?, description?, alt?, url?, span? }> | [] | — |
| columns | 'auto' \| number | 'auto' | auto |
| columnWidth | number | 240 | 240 |
| gap | number | 12 | 12 |
| radius | number | 12 | 12 |
| animateFrom | 'bottom' \| 'top' \| 'left' \| 'right' \| 'center' \| 'random' \| 'none' | 'bottom' | bottom |
| stagger | number | 0.05 | 0.05 |
| duration | number | 0.6 | 0.6 |
| bounce | number | 0.15 | 0.15 |
| blurToFocus | boolean | true | true |
| revealOnScroll | boolean | true | true |
| hoverEffect | 'zoom' \| 'lift' \| 'tilt' \| 'none' | 'zoom' | zoom |
| focusOnHover | boolean | false | false |
| captions | 'hover' \| 'always' \| 'none' | 'hover' | hover |
| parallax | number | 0 | 0 |
| lightbox | boolean | true | true |
| draggable | boolean | true | true |
| onItemClick | (item, index, event) => void | - | — |
| onReorder | (items) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, react-dom, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [scroll, line 559](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L559)
- [resize, line 560](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L560)
- [pointermove, line 689](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L689)
- [pointerup, line 690](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L690)
- [pointercancel, line 691](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L691)
- [keydown, line 850](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L850)
- [onLoad, line 892](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L892)
- [onError, line 893](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L893)
- [onClick, line 967](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L967)
- [onClick, line 975](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L975)
- [onClick, line 995](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L995)
- [onClick, line 1006](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L1006)
- [onClick, line 1015](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L1015)

## Motion locations

- [duration, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L162): computed; read the linked expression
- [bounce, line 163](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L163): computed; read the linked expression
- [duration, line 520](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L520): computed; read the linked expression
- [duration, line 757](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L757): 380
- [duration, line 759](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L759): 300
- [duration, line 762](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L762): 160
- [duration, line 802](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L802): computed; read the linked expression
- [duration, line 820](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L820): 520
- [duration, line 822](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L822): 360
- [duration, line 824](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.jsx#L824): 560

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Masonry/Masonry.css); motion-related lines: 39, 57, 104, 139, 225, 250.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
