# DepthCarousel

Category: Components. Public entry: [DepthCarousel](https://reactbits.dev/components/depth-carousel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/DepthCarousel/DepthCarousel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/DepthCarousel/DepthCarousel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/DepthCarousel/DepthCarousel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<string \| { image: string; alt?: string }> | 6 sample images | — |
| cardWidth | number | 300 | 300 |
| cardHeight | number | 380 | 380 |
| radius | number | 18 | 18 |
| tint | string | "#05060a" | #05060a |
| depth | number | 220 | 220 |
| spread | number | 90 | 90 |
| tilt | number | 22 | 22 |
| tiltDirection | "left" \| "right" | "right" | right |
| perspective | number | 1400 | 1400 |
| visibleCards | number | 4 | 4 |
| falloff | number | 0.2 | 0.2 |
| blur | number | 6 | 6 |
| duration | number | 700 | 700 |
| ease | string | "power3.out" | power3.out |
| autoplay | boolean | false | false |
| autoplayDelay | number | 3200 | 3200 |
| loop | boolean | true | true |
| showControls | boolean | true | true |
| showIndicators | boolean | true | true |
| onChange | (index: number, item) => void | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [wheel, line 209](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L209)
- [mouseenter, line 317](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L317)
- [mouseleave, line 318](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L318)
- [focusin, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L319)
- [focusout, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L320)
- [onPointerDown, line 353](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L353)
- [onPointerMove, line 354](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L354)
- [onPointerUp, line 355](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L355)
- [onPointerCancel, line 356](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L356)
- [onKeyDown, line 357](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L357)
- [onClick, line 369](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L369)
- [onClick, line 387](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L387)
- [onClick, line 404](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L404)
- [onClick, line 430](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L430)

## Motion locations

- [duration, line 141](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L141): computed; read the linked expression
- [ease, line 142](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.jsx#L142): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DepthCarousel/DepthCarousel.css); motion-related lines: 81, 126, 136, 142.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
