# StrokeText

Category: TextAnimations. Public entry: [StrokeText](https://reactbits.dev/text-animations/stroke-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/StrokeText/StrokeText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/StrokeText/StrokeText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/StrokeText/StrokeText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Draw Attention" | Draw Attention |
| strokeColor | string | "#A78BFA" | #A78BFA |
| fillColor | string | "currentColor" | currentColor |
| strokeWidth | number | 1.4 | 1.4 |
| drawDuration | number | 1.6 | 1.6 |
| fillDelay | number | 0.2 | 0.2 |
| stagger | number | 0.05 | 0.05 |
| ease | string | "power2.out" | power2.out |
| trigger | "mount" \| "hover" \| "scroll" \| "loop" | "mount" | mount |
| fillMode | "fade" \| "wipe" \| "none" | "wipe" | wipe |
| wipeFrom | "left" \| "right" \| "top" \| "bottom" | "left" | left |
| fontSize | number | 128 | 128 |
| fontWeight | number \| string | 800 | 800 |
| fontFamily | string | "inherit" | inherit |
| letterSpacing | number | -4 | -4 |
| reverse | boolean | false | false |
| strokeStyle | "solid" \| "dashed" \| "dotted" | "solid" | solid |
| dashLength | number | 10 | 10 |
| marching | boolean | false | false |
| hoverRedraw | boolean | false | false |
| shadow | boolean | false | false |
| shadowColor | string | - | — |
| className | string | "" |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations

- [pointerenter, line 227](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L227)

## Motion locations

- [duration, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L198): computed; read the linked expression
- [duration, line 201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L201): computed; read the linked expression
- [ease, line 201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L201): "power2.inOut"
- [duration, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L205): computed; read the linked expression
- [ease, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L205): "power2.out"
- [duration, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L213): computed; read the linked expression
- [ease, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L213): "power3.out"
- [duration, line 257](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L257): 0.2
- [ease, line 257](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L257): "power1.out"
- [duration, line 259](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L259): computed; read the linked expression
- [duration, line 269](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L269): computed; read the linked expression
- [ease, line 269](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.jsx#L269): "none"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/StrokeText/StrokeText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
