# SplitText

Category: TextAnimations. Public entry: [SplitText](https://reactbits.dev/text-animations/split-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/SplitText/SplitText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/SplitText/SplitText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/SplitText/SplitText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| tag | string | "p" | p |
| text | string | "" | — |
| className | string | "" |  |
| effect | "rise" \| "fade" \| "blur" \| "flip" \| "pop" \| "skew" \| "wave" | "rise" | rise |
| trigger | "view" \| "load" \| "hover" \| "click" | "view" | view |
| loop | boolean | false | false |
| loopDelay | number | 1.5 | 1.5 |
| hoverEffect | "none" \| "lift" \| "wave" | "none" | none |
| color | string | undefined | — |
| accentColor | string | undefined | — |
| delay | number | 50 | 50 |
| duration | number | 1.25 | 1.25 |
| ease | string \| function | undefined | — |
| splitType | string | "chars" | chars |
| staggerFrom | "start" \| "center" \| "end" \| "edges" \| "random" | "start" | start |
| mask | boolean | false | false |
| from | object | undefined | — |
| to | object | undefined | — |
| threshold | number | 0.1 | 0.1 |
| rootMargin | string | "-100px" | -100px |
| textAlign | string | "center" | center |
| onLetterAnimationComplete | function | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger, gsap/SplitText, @gsap/react

## Interaction locations

- [pointerenter, line 357](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L357)
- [pointermove, line 358](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L358)
- [pointerleave, line 359](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L359)
- [click, line 360](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L360)

## Motion locations

- [ease, line 26](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L26): "power2.inOut"
- [ease, line 31](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L31): "power2.out"
- [ease, line 38](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L38): "power3.out"
- [ease, line 42](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L42): "back.out(1.6)"
- [ease, line 47](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L47): "expo.out"
- [ease, line 50](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L50): computed; read the linked expression
- [ease, line 52](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L52): "power3.out"
- [ease, line 168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L168): computed; read the linked expression
- [duration, line 177](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L177): computed; read the linked expression
- [ease, line 178](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L178): "power1.inOut"
- [duration, line 195](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L195): computed; read the linked expression
- [ease, line 195](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L195): "power2.in"
- [duration, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L198): computed; read the linked expression
- [ease, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitText/SplitText.jsx#L198): "power1.in"

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
