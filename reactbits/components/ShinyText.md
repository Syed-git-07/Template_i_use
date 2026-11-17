# ShinyText

Category: TextAnimations. Public entry: [ShinyText](https://reactbits.dev/text-animations/shiny-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ShinyText/ShinyText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ShinyText/ShinyText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ShinyText/ShinyText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | - | — |
| color | string | "#b5b5b5" | #b5b5b5 |
| shineColor | string | "#ffffff" | #ffffff |
| speed | number | 2 | 2 |
| delay | number | 0 | 0 |
| angle | number | 120 | 120 |
| shineWidth | number | 40 | 40 |
| softness | number | 0.8 | 0.8 |
| bands | number | 1 | 1 |
| glow | number | 0 | 0 |
| direction | 'left' \| 'right' | "left" | left |
| easing | 'smooth' \| 'linear' \| 'snappy' | "smooth" | smooth |
| trigger | 'loop' \| 'hover' \| 'view' | "loop" | loop |
| yoyo | boolean | false | false |
| followPointer | boolean | false | false |
| pauseOnHover | boolean | false | false |
| disabled | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 317](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L317)
- [pointermove, line 318](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L318)
- [pointerleave, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L319)

## Motion locations

- [delay, line 78](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L78): computed; read the linked expression
- [ease, line 85](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L85): computed; read the linked expression
- [duration, line 109](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.jsx#L109): 1

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ShinyText/ShinyText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
