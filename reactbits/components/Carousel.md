# Carousel

Category: Components. Public entry: [Carousel](https://reactbits.dev/components/carousel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Carousel/Carousel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Carousel/Carousel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Carousel/Carousel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<CarouselItem \| string \| ReactNode> | DEFAULT_ITEMS | — |
| baseWidth | number \| string | 300 | 300 |
| aspectRatio | number | 1.25 | 1.25 |
| peek | number | 0 | 0 |
| gap | number | 16 | 16 |
| radius | number | 12 | 12 |
| frame | boolean | true | true |
| effect | 'tilt' \| 'slide' \| 'scale' \| 'fade' \| 'cube' | 'tilt' | tilt |
| indicator | 'dots' \| 'bars' \| 'counter' \| 'none' | 'dots' | dots |
| arrows | boolean | false | false |
| autoplay | boolean | false | false |
| autoplayDelay | number | 3000 | 3000 |
| pauseOnHover | boolean | false | false |
| loop | boolean | false | false |
| draggable | boolean | true | true |
| round | boolean | false | false |
| initialIndex | number | 0 | 0 |
| theme | 'dark' \| 'light' | 'dark' | dark |
| onChange | (index: number) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerdown, line 555](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L555)
- [pointermove, line 556](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L556)
- [pointerup, line 557](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L557)
- [pointercancel, line 558](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L558)
- [click, line 559](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L559)
- [wheel, line 560](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L560)
- [keydown, line 561](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L561)
- [mouseenter, line 562](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L562)
- [mouseleave, line 563](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L563)
- [focusin, line 564](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L564)
- [focusout, line 565](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L565)
- [visibilitychange, line 566](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L566)
- [onClick, line 646](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L646)
- [onClick, line 661](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L661)
- [onClick, line 678](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L678)
- [onClick, line 712](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L712)
- [onClick, line 776](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L776)

## Motion locations

- [duration, line 628](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.jsx#L628): 320

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Carousel/Carousel.css); motion-related lines: 102, 248, 262, 294, 329.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
