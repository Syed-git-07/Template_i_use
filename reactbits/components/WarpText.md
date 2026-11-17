# WarpText

Category: TextAnimations. Public entry: [WarpText](https://reactbits.dev/text-animations/warp-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/WarpText/WarpText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/WarpText/WarpText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/WarpText/WarpText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Bend the moment" | Bend the moment |
| color | string | "currentColor" | currentColor |
| warpStrength | number | 0.08 | 0.08 |
| warpScale | number | 1.7 | 1.7 |
| speed | number | 0.55 | 0.55 |
| lens | "bulge" \| "pinch" \| "swirl" | "bulge" | bulge |
| pointerInfluence | number | 0.42 | 0.42 |
| pointerStrength | number | 0.38 | 0.38 |
| idleDrift | number | 0.2 | 0.2 |
| chromatic | number | 0 | 0 |
| refraction | number | 0.018 | 0.018 |
| ripple | boolean | true | true |
| clickRipple | boolean | true | true |
| intro | boolean | true | true |
| fontSize | string \| number | "clamp(3rem, 10vw, 9rem)" | clamp(3rem, 10vw, 9rem) |
| fontWeight | string \| number | 800 | 800 |
| fontFamily | string | "inherit" | inherit |
| letterSpacing | string \| number | "-0.06em" | -0.06em |
| lineHeight | string \| number | 0.9 | 0.9 |
| className | string | "" |  |
| style | React.CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 626](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L626)
- [pointerleave, line 627](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L627)
- [pointerdown, line 628](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L628)
- [webglcontextlost, line 629](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L629)
- [visibilitychange, line 630](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L630)
- [change, line 631](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L631)

## Motion locations

- [threshold, line 622](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.jsx#L622): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/WarpText/WarpText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
