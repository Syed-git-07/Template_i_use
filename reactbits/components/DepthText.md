# DepthText

Category: TextAnimations. Public entry: [DepthText](https://reactbits.dev/text-animations/depth-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/DepthText/DepthText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/DepthText/DepthText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/DepthText/DepthText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Elevate" | Elevate |
| layers | number | 34 | 34 |
| depth | number | 2.4 | 2.4 |
| faceColor | string | "currentColor" | currentColor |
| depthColor | string | "#7c3aed" | #7c3aed |
| gradientDepth | boolean | false | false |
| tilt | number | 7.5 | 7.5 |
| pointerTracking | boolean | true | true |
| smoothing | number | 0.14 | 0.14 |
| perspective | number | 900 | 900 |
| autoOrbit | boolean | true | true |
| orbitSpeed | number | 0.35 | 0.35 |
| hoverPush | number | 0 | 0 |
| float | boolean | false | false |
| fontSize | string | "clamp(3rem, 12vw, 7rem)" | clamp(3rem, 12vw, 7rem) |
| fontWeight | number \| string | 900 | 900 |
| shadow | boolean | true | true |
| outline | boolean | false | false |
| intro | boolean | true | true |
| className | string | "" |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 265](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L265)
- [pointerout, line 266](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L266)
- [blur, line 267](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L267)
- [pointerenter, line 271](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L271)
- [pointerleave, line 272](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L272)
- [pointerdown, line 273](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L273)
- [pointerup, line 274](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L274)
- [pointercancel, line 275](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L275)

## Motion locations

- [velocity, line 66](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.jsx#L66): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DepthText/DepthText.css); motion-related lines: 63.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
