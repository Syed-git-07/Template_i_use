# ScrollReveal

Category: TextAnimations. Public entry: [ScrollReveal](https://reactbits.dev/text-animations/scroll-reveal).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ScrollReveal/ScrollReveal.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ScrollReveal/ScrollReveal.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ScrollReveal/ScrollReveal.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| scrollContainerRef | RefObject<HTMLElement> | window | — |
| highlightColor | string | '' |  |
| mode | 'scrub' \| 'enter' | 'scrub' | scrub |
| splitBy | 'words' \| 'chars' \| 'lines' | 'words' | words |
| effect | 'fade' \| 'rise' \| 'flip' \| 'scale' | 'fade' | fade |
| stagger | number | 0.05 | 0.05 |
| duration | number | 0.8 | 0.8 |
| smoothing | number | 0 | 0 |
| enableBlur | boolean | true | true |
| blurStrength | number | 4 | 4 |
| baseOpacity | number | 0.1 | 0.1 |
| baseRotation | number | 3 | 3 |
| baseOffset | number | 0 | 0 |
| rotationEnd | string | 'bottom bottom' | bottom bottom |
| wordAnimationEnd | string | 'bottom bottom' | bottom bottom |
| containerClassName | string | '' |  |
| textClassName | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations


## Motion locations

- [duration, line 189](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L189): computed; read the linked expression
- [ease, line 189](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L189): "none"
- [duration, line 190](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L190): computed; read the linked expression
- [ease, line 190](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L190): "power3.out"
- [ease, line 219](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L219): "none"
- [ease, line 233](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.jsx#L233): "none"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollReveal/ScrollReveal.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
