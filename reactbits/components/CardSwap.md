# CardSwap

Category: Components. Public entry: [CardSwap](https://reactbits.dev/components/card-swap).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/CardSwap/CardSwap.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/CardSwap/CardSwap.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/CardSwap/CardSwap.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | CardSwapItem[] | Sample cards | — |
| children | ReactNode | undefined | — |
| width | number | 460 | 460 |
| height | number | 340 | 340 |
| cardDistance | number | 60 | 60 |
| verticalDistance | number | 70 | 70 |
| depth | number | 90 | 90 |
| skewAmount | number | 6 | 6 |
| visibleCards | number | 4 | 4 |
| delay | number | 4000 | 4000 |
| autoplay | boolean | true | true |
| pauseOnHover | boolean | true | true |
| draggable | boolean | true | true |
| speed | number | 1 | 1 |
| bounce | number | 0.35 | 0.35 |
| parallax | number | 0.5 | 0.5 |
| hoverSpread | number | 0.12 | 0.12 |
| dim | number | 0.5 | 0.5 |
| cardRadius | number | 18 | 18 |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| onCardClick | (index: number) => void | undefined | — |
| onChange | (index: number) => void | undefined | — |
| ref | { next, prev } | undefined | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointermove, line 704](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L704)
- [pointerleave, line 705](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L705)
- [pointerdown, line 706](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L706)
- [pointerup, line 707](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L707)
- [pointercancel, line 708](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L708)
- [click, line 709](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L709)
- [visibilitychange, line 710](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L710)
- [onKeyDown, line 765](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L765)

## Motion locations

- [bounce, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L205): computed; read the linked expression
- [delay, line 273](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L273): computed; read the linked expression
- [duration, line 686](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.jsx#L686): 420

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardSwap/CardSwap.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
