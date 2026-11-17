# MorphSlider

Category: Components. Public entry: [MorphSlider](https://reactbits.dev/components/morph-slider).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/MorphSlider/MorphSlider.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/MorphSlider/MorphSlider.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/MorphSlider/MorphSlider.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ image: string; caption?: string }> | [...] | — |
| startIndex | number | 0 | 0 |
| transition | "melt" \| "ripple" \| "shear" \| "swirl" | "melt" | melt |
| duration | number | 1.1 | 1.1 |
| ease | string | "power2.inOut" | power2.inOut |
| intensity | number | 0.55 | 0.55 |
| scale | number | 2.4 | 2.4 |
| aberration | number | 0.35 | 0.35 |
| drift | number | 0.4 | 0.4 |
| autoplay | boolean | false | false |
| autoplayDelay | number | 4 | 4 |
| loop | boolean | true | true |
| radius | number | 16 | 16 |
| overlayColor | string | "#000000" | #000000 |
| showCaptions | boolean | true | true |
| showControls | boolean | true | true |
| showIndicators | boolean | true | true |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl, gsap

## Interaction locations

- [webglcontextlost, line 276](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L276)
- [pointerdown, line 570](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L570)
- [pointermove, line 571](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L571)
- [pointerup, line 572](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L572)
- [pointercancel, line 573](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L573)
- [onMouseEnter, line 606](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L606)
- [onMouseLeave, line 607](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L607)
- [onKeyDown, line 617](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L617)
- [onClick, line 638](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L638)
- [onClick, line 650](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L650)
- [onClick, line 675](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L675)

## Motion locations

- [ease, line 366](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L366): computed; read the linked expression
- [ease, line 441](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L441): "power2.out"
- [ease, line 449](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.jsx#L449): "power2.out"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MorphSlider/MorphSlider.css); motion-related lines: 58, 97, 138, 164, 168, 169.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
