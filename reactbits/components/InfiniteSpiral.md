# InfiniteSpiral

Category: Components. Public entry: [InfiniteSpiral](https://reactbits.dev/components/infinite-spiral).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/InfiniteSpiral/InfiniteSpiral.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/InfiniteSpiral/InfiniteSpiral.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/InfiniteSpiral/InfiniteSpiral.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | (string \| SpiralItem)[] | [] | — |
| speed | number | 0.55 | 0.55 |
| direction | "up" \| "down" | "up" | up |
| animationMode | "auto" \| "drag" \| "scroll" \| "all" | "auto" | auto |
| radius | number | 170 | 170 |
| cardWidth | number | 100 | 100 |
| cardHeight | number | 100 | 100 |
| verticalSpacing | number | 60 | 60 |
| perspective | number | 1000 | 1000 |
| cardsPerTurn | number | 7 | 7 |
| rotation | number | 0 | 0 |
| cardTilt | number | 0 | 0 |
| cardRadius | number | 10 | 10 |
| centerScale | number | 1.2 | 1.2 |
| edgeFade | number | 0.3 | 0.3 |
| edgeBlur | number | 6 | 6 |
| pauseOnHover | boolean | true | true |
| imageFit | "cover" \| "contain" | "cover" | cover |
| grayscale | number | 0 | 0 |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [scroll, line 92](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L92)
- [onMouseEnter, line 201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L201)
- [onMouseLeave, line 204](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L204)
- [onPointerDown, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L207)
- [onPointerMove, line 216](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L216)
- [onPointerUp, line 223](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L223)
- [onPointerCancel, line 224](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L224)
- [onClickCapture, line 225](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L225)

## Motion locations

- [threshold, line 77](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.jsx#L77): 0.02

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/InfiniteSpiral/InfiniteSpiral.css); motion-related lines: 44, 46.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
