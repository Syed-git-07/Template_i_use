# FoldText

Category: TextAnimations. Public entry: [FoldText](https://reactbits.dev/text-animations/fold-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/FoldText/FoldText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/FoldText/FoldText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/FoldText/FoldText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Design unfolds" | Design unfolds |
| foldStyle | "paper" \| "blinds" \| "flip" | "paper" | paper |
| splitBy | "char" \| "word" \| "line" | "char" | char |
| hinge | "top" \| "bottom" \| "left" \| "right" | "top" | top |
| foldAngle | number | 92 | 92 |
| duration | number | 0.65 | 0.65 |
| stagger | number | 0.045 | 0.045 |
| staggerFrom | "start" \| "center" \| "end" \| "edges" \| "random" | "start" | start |
| ease | string | "power3.out" | power3.out |
| perspective | number | 700 | 700 |
| creaseShading | number | 0.55 | 0.55 |
| trigger | "mount" \| "hover" \| "scroll" \| "loop" | "mount" | mount |
| loopDelay | number | 1.4 | 1.4 |
| hoverRefold | boolean | false | false |
| refoldRadius | number | 140 | 140 |
| refoldAngle | number | 45 | 45 |
| fontSize | string \| number | 80 | 80 |
| fontWeight | string \| number | 800 | 800 |
| color | string | "currentColor" | currentColor |
| className | string | "" |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations

- [mouseenter, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L213)
- [pointermove, line 298](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L298)
- [scroll, line 299](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L299)
- [pointerleave, line 300](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L300)

## Motion locations

- [duration, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L198): computed; read the linked expression
- [ease, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L198): "none"
- [duration, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L202): computed; read the linked expression
- [ease, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.jsx#L202): "none"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FoldText/FoldText.css); motion-related lines: 107.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
