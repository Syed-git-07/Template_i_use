# ClickSpark

Category: Animations. Public entry: [ClickSpark](https://reactbits.dev/animations/click-spark).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ClickSpark/ClickSpark.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ClickSpark/ClickSpark.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ClickSpark/ClickSpark.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ClickSpark/ClickSpark.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| sparkColor | string \| string[] | '#fff' | #fff |
| shape | 'line' \| 'streak' \| 'dot' \| 'star' | 'line' | line |
| sparkCount | number | 8 | 8 |
| sparkSize | number | 14 | 14 |
| sparkWidth | number | 2 | 2 |
| sparkRadius | number | 30 | 30 |
| duration | number | 500 | 500 |
| easing | 'ease-out' \| 'ease-in-out' \| 'ease-in' \| 'linear' \| 'spring' | 'ease-out' | ease-out |
| randomness | number | 0.2 | 0.2 |
| gravity | number | 0 | 0 |
| spread | number | 360 | 360 |
| direction | number | 0 | 0 |
| glow | number | 0 | 0 |
| ring | boolean | false | false |
| layer | 'front' \| 'back' | 'front' | front |
| extraScale | number | 1 | 1 |
| disabled | boolean | false | false |
| ref | { spark: (x?: number, y?: number) => void } | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |
| children | ReactNode | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerdown, line 368](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ClickSpark/ClickSpark.jsx#L368)
- [click, line 369](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ClickSpark/ClickSpark.jsx#L369)

## Motion locations

- [duration, line 98](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ClickSpark/ClickSpark.jsx#L98): computed; read the linked expression
- [ease, line 99](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ClickSpark/ClickSpark.jsx#L99): computed; read the linked expression

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
