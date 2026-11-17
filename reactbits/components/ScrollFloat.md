# ScrollFloat

Category: TextAnimations. Public entry: [ScrollFloat](https://reactbits.dev/text-animations/scroll-float).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ScrollFloat/ScrollFloat.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ScrollFloat/ScrollFloat.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ScrollFloat/ScrollFloat.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| scrollContainerRef | RefObject<HTMLElement> | window | — |
| effect | 'float' \| 'flip' \| 'scatter' \| 'blur' \| 'wave' | 'float' | float |
| splitBy | 'chars' \| 'words' | 'chars' | chars |
| direction | 'up' \| 'down' | 'up' | up |
| order | 'start' \| 'end' \| 'center' \| 'edges' \| 'random' | 'start' | start |
| fromColor | string | 'currentColor' | currentColor |
| animationDuration | number | 1 | 1 |
| ease | string | 'back.inOut(2)' | back.inOut(2) |
| stagger | number | 0.03 | 0.03 |
| distance | number | 120 | 120 |
| stretch | number | 2.3 | 2.3 |
| smoothing | number | 0 | 0 |
| scrollStart | string | 'center bottom+=50%' | center bottom+=50% |
| scrollEnd | string | 'bottom bottom-=40%' | bottom bottom-=40% |
| containerClassName | string | '' |  |
| textClassName | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/ScrollTrigger

## Interaction locations


## Motion locations

- [duration, line 149](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L149): computed; read the linked expression
- [ease, line 164](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L164): computed; read the linked expression
- [ease, line 176](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L176): computed; read the linked expression
- [ease, line 197](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L197): computed; read the linked expression
- [ease, line 199](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L199): computed; read the linked expression
- [ease, line 200](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L200): computed; read the linked expression
- [ease, line 215](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L215): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollFloat/ScrollFloat.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
