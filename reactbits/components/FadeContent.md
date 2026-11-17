# FadeContent

Category: Animations. Public entry: [FadeContent](https://reactbits.dev/animations/fade-content).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/FadeContent/FadeContent.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/FadeContent/FadeContent.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/FadeContent/FadeContent.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| container | string \| HTMLElement | window | — |
| effect | 'fade' \| 'focus' \| 'develop' \| 'dissolve' \| 'mist' \| 'pixel' | 'fade' | fade |
| blur | boolean \| number | false | false |
| duration | number | 1 | 1 |
| ease | string | 'power2.out' | power2.out |
| delay | number | 0 | 0 |
| threshold | number | 0.1 | 0.1 |
| initialOpacity | number | 0 | 0 |
| stagger | number | 0 | 0 |
| staggerFrom | 'start' \| 'end' \| 'center' \| 'edges' \| 'random' | 'start' | start |
| trigger | 'scroll' \| 'mount' | 'scroll' | scroll |
| once | boolean | true | true |
| exit | boolean | false | false |
| scrub | boolean \| number | false | false |
| disappearAfter | number | 0 | 0 |
| disappearDuration | number | 0.5 | 0.5 |
| disappearEase | string | 'power2.in' | power2.in |
| onStart | () => void | - | — |
| onComplete | () => void | - | — |
| onDisappearanceComplete | () => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations


## Motion locations

- [duration, line 219](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L219): computed; read the linked expression
- [duration, line 228](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L228): computed; read the linked expression
- [delay, line 263](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L263): computed; read the linked expression
- [duration, line 267](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L267): computed; read the linked expression
- [ease, line 268](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L268): computed; read the linked expression
- [duration, line 312](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L312): computed; read the linked expression
- [ease, line 312](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/FadeContent/FadeContent.jsx#L312): "power3.out"

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
