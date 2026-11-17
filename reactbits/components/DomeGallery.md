# DomeGallery

Category: Components. Public entry: [DomeGallery](https://reactbits.dev/components/dome-gallery).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/DomeGallery/DomeGallery.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/DomeGallery/DomeGallery.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/DomeGallery/DomeGallery.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| images | (string \| { src: string; alt?: string })[] | DEFAULT_IMAGES | — |
| fit | number | 0.5 | 0.5 |
| fitBasis | 'auto' \| 'min' \| 'max' \| 'width' \| 'height' | 'auto' | auto |
| minRadius | number | 600 | 600 |
| maxRadius | number | Infinity | — |
| padFactor | number | 0.25 | 0.25 |
| overlayBlurColor | string | '#120F17' | #120F17 |
| maxVerticalRotationDeg | number | 5 | — |
| dragSensitivity | number | 20 | — |
| enlargeTransitionMs | number | 300 | — |
| segments | number | 35 | — |
| dragDampening | number | 2 | 2 |
| openedImageWidth | string | '400px' | 400px |
| openedImageHeight | string | '400px' | 400px |
| imageBorderRadius | string | '30px' | 30px |
| openedImageBorderRadius | string | '30px' | 30px |
| grayscale | boolean | true | true |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @use-gesture/react

## Interaction locations

- [transitionend, line 438](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L438)
- [click, line 440](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L440)
- [keydown, line 444](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L444)
- [transitionend, line 557](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L557)
- [transitionend, line 559](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L559)
- [onClick, line 631](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L631)
- [onPointerUp, line 632](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.jsx#L632)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DomeGallery/DomeGallery.css); motion-related lines: 81, 95, 149, 163.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
