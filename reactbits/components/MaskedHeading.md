# MaskedHeading

Category: TextAnimations. Public entry: [MaskedHeading](https://reactbits.dev/text-animations/masked-heading).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/MaskedHeading/MaskedHeading.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/MaskedHeading/MaskedHeading.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/MaskedHeading/MaskedHeading.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'Designed in the details' | Designed in the details |
| tag | string | 'h2' | h2 |
| mediaType | "image" \| "video" | "image" | image |
| src | string | '' |  |
| poster | string | '' |  |
| reveal | "rise" \| "scale" \| "blur" \| "wipe" \| "fade" \| "none" | "rise" | rise |
| trigger | "view" \| "mount" \| "hover" | "view" | view |
| duration | number | 1.1 | 1.1 |
| stagger | number | 0.09 | 0.09 |
| spotlight | boolean | false | false |
| spotlightRadius | number | 160 | 160 |
| outline | boolean | false | false |
| outlineColor | string | '' |  |
| outlineWidth | number | 1 | 1 |
| fillScale | number | 1.25 | 1.25 |
| parallax | number | 26 | 26 |
| drift | number | 18 | 18 |
| hoverZoom | number | 0 | 0 |
| brightness | number | 1 | 1 |
| saturation | number | 1 | 1 |
| grayscale | boolean | false | false |
| tint | string | '' |  |
| align | "left" \| "center" \| "right" | "center" | center |
| weight | number | 700 | 700 |
| tracking | number | -0.03 | -0.03 |
| lineHeight | number | 1.06 | 1.06 |
| textScale | number | 0.115 | 0.115 |
| className | string | '' |  |
| style | object | — | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [pointermove, line 325](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L325)
- [pointerenter, line 326](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L326)
- [pointerleave, line 327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L327)
- [pointerenter, line 482](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L482)

## Motion locations

- [ease, line 423](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L423): "power4.out"
- [ease, line 431](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L431): "expo.out"
- [duration, line 440](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L440): computed; read the linked expression
- [ease, line 440](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L440): "expo.out"
- [duration, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L446): computed; read the linked expression
- [ease, line 447](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L447): "power2.out"
- [ease, line 464](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L464): "power3.inOut"
- [ease, line 475](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L475): "power3.out"
- [threshold, line 499](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.jsx#L499): 0.25

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/MaskedHeading/MaskedHeading.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
