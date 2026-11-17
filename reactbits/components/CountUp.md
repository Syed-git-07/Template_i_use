# CountUp

Category: TextAnimations. Public entry: [CountUp](https://reactbits.dev/text-animations/count-up).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/CountUp/CountUp.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/CountUp/CountUp.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/CountUp/CountUp.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| to | number | — | — |
| from | number | 0 | 0 |
| mode | "count" \| "roll" | "count" | count |
| easing | "easeOut" \| "linear" \| "expo" \| "spring" | "easeOut" | easeOut |
| format | "standard" \| "compact" | "standard" | standard |
| decimals | number | undefined | — |
| direction | string | "up" | up |
| trigger | "view" \| "load" | "view" | view |
| replayOnHover | boolean | false | false |
| delay | number | 0 | 0 |
| duration | number | 2 | 2 |
| className | string | "" |  |
| style | CSSProperties | undefined | — |
| startWhen | boolean | true | true |
| separator | string | "" |  |
| prefix | string | "" |  |
| suffix | string | "" |  |
| onStart | function | — | — |
| onEnd | function | — | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: motion/react, react

## Interaction locations

- [onPointerEnter, line 362](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L362)

## Motion locations

- [duration, line 192](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L192): computed; read the linked expression
- [ease, line 240](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L240): computed; read the linked expression
- [duration, line 333](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L333): computed; read the linked expression
- [delay, line 334](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L334): computed; read the linked expression
- [ease, line 335](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/CountUp/CountUp.jsx#L335): "linear"

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
