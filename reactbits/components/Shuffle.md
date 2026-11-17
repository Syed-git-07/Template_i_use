# Shuffle

Category: TextAnimations. Public entry: [Shuffle](https://reactbits.dev/text-animations/shuffle).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/Shuffle/Shuffle.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/Shuffle/Shuffle.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/Shuffle/Shuffle.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "" | — |
| className | string | "" |  |
| style | object | {} | — |
| effect | "slide" \| "flip" \| "blur" | "slide" | slide |
| shuffleDirection | "left" \| "right" \| "up" \| "down" | "right" | right |
| duration | number | 0.35 | 0.35 |
| maxDelay | number | 0 | 0 |
| ease | string \| Function | "power3.out" | power3.out |
| threshold | number | 0.1 | 0.1 |
| rootMargin | string | "-100px" | -100px |
| tag | "h1" \| "h2" \| "h3" \| "h4" \| "h5" \| "h6" \| "p" \| "span" | "p" | p |
| textAlign | CSS text-align | "center" | center |
| onShuffleComplete | () => void | undefined | — |
| shuffleTimes | number | 1 | 1 |
| animationMode | "evenodd" \| "sequence" \| "center" \| "random" | "evenodd" | evenodd |
| loop | boolean | false | false |
| loopDelay | number | 0 | 0 |
| stagger | number | 0.03 | 0.03 |
| scrambleCharset | string | "" |  |
| motionBlur | boolean | false | false |
| color | string | undefined | — |
| accentColor | string | undefined | — |
| colorFrom | string | undefined | — |
| colorTo | string | undefined | — |
| triggerOnce | boolean | true | true |
| respectReducedMotion | boolean | true | true |
| triggerOnHover | boolean | true | true |
| hoverRadius | number | 0 | 0 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger, gsap/SplitText, @gsap/react

## Interaction locations

- [pointermove, line 545](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx#L545)
- [mouseenter, line 558](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx#L558)

## Motion locations

- [duration, line 375](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx#L375): computed; read the linked expression
- [duration, line 400](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx#L400): computed; read the linked expression
- [duration, line 418](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.jsx#L418): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/Shuffle/Shuffle.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
