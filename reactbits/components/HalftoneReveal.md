# HalftoneReveal

Category: Animations. Public entry: [HalftoneReveal](https://reactbits.dev/animations/halftone-reveal).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/HalftoneReveal/HalftoneReveal.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/HalftoneReveal/HalftoneReveal.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/HalftoneReveal/HalftoneReveal.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | 'https://images.unsplash.com/...' | https://images.unsplash.com/photo-1693250707557-a846a014b321?q=80&w=1400&auto=format&fit=crop |
| fit | 'contain' \| 'cover' | 'cover' | cover |
| mode | 'mono' \| 'duotone' \| 'color' | 'mono' | mono |
| shape | 'dot' \| 'ellipse' \| 'square' \| 'diamond' \| 'line' \| 'cross' | 'dot' | dot |
| cellSize | number | 6 | 6 |
| angle | number | 45 | 45 |
| dotScale | number | 1 | 1 |
| inkColor | string | '#120f17' | #120f17 |
| accentColor | string | '#ff4f2a' | #ff4f2a |
| paperColor | string | '#ffffff' | #ffffff |
| contrast | number | 1.1 | 1.1 |
| brightness | number | 0 | 0 |
| invert | boolean | false | false |
| roughness | number | 0 | 0 |
| misregistration | number | 0 | 0 |
| revealRadius | number | 160 | 160 |
| softness | number | 0.6 | 0.6 |
| linger | number | 1.2 | 1.2 |
| reverse | boolean | false | false |
| wander | boolean | false | false |
| clickBurst | boolean | true | true |
| intro | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 780](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L780)
- [pointerenter, line 781](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L781)
- [pointerdown, line 782](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L782)
- [pointerleave, line 783](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L783)
- [pointercancel, line 784](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L784)
- [visibilitychange, line 785](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.jsx#L785)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/HalftoneReveal/HalftoneReveal.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
