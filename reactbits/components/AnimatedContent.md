# AnimatedContent

Category: Animations. Public entry: [AnimatedContent](https://reactbits.dev/animations/animated-content).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/AnimatedContent/AnimatedContent.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/AnimatedContent/AnimatedContent.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/AnimatedContent/AnimatedContent.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/AnimatedContent/AnimatedContent.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| container | string \| HTMLElement | window | — |
| distance | number | 100 | 100 |
| direction | 'vertical' \| 'horizontal' | 'vertical' | vertical |
| reverse | boolean | false | false |
| duration | number | 0.8 | 0.8 |
| ease | string | 'power3.out' | power3.out |
| initialOpacity | number | 0 | 0 |
| animateOpacity | boolean | true | true |
| scale | number | 1 | 1 |
| blur | number | 0 | 0 |
| rotate | number | 0 | 0 |
| tilt | number | 0 | 0 |
| wipe | 'none' \| 'up' \| 'down' \| 'left' \| 'right' \| 'center' | 'none' | none |
| threshold | number | 0.1 | 0.1 |
| delay | number | 0 | 0 |
| stagger | number | 0 | 0 |
| staggerFrom | 'start' \| 'end' \| 'center' \| 'edges' \| 'random' | 'start' | start |
| trigger | 'scroll' \| 'mount' | 'scroll' | scroll |
| once | boolean | true | true |
| scrub | boolean \| number | false | false |
| disappearAfter | number | 0 | 0 |
| disappearDuration | number | 0.5 | 0.5 |
| disappearEase | string | 'power3.in' | power3.in |
| onStart | () => void | - | — |
| onComplete | () => void | - | — |
| onDisappearanceComplete | () => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations


## Motion locations

- [delay, line 125](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/AnimatedContent/AnimatedContent.jsx#L125): computed; read the linked expression
- [duration, line 126](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/AnimatedContent/AnimatedContent.jsx#L126): computed; read the linked expression
- [ease, line 127](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/AnimatedContent/AnimatedContent.jsx#L127): computed; read the linked expression

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
