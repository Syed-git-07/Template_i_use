# BounceCards

Category: Components. Public entry: [BounceCards](https://reactbits.dev/components/bounce-cards).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/BounceCards/BounceCards.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/BounceCards/BounceCards.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/BounceCards/BounceCards.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| images | Array<string \| { src: string; alt?: string }> | [] | — |
| containerWidth | number | 400 | 400 |
| containerHeight | number | 400 | 400 |
| cardSize | number | 200 | 200 |
| spread | number | 85 | 85 |
| rotation | number | 10 | 10 |
| arc | number | 0 | 0 |
| pushDistance | number | 160 | 160 |
| hoverScale | number | 1.06 | 1.06 |
| bounciness | number | 0.6 | 0.6 |
| animationDelay | number | 0.5 | 0.5 |
| animationStagger | number | 0.06 | 0.06 |
| enableHover | boolean | true | true |
| borderWidth | number | 5 | 5 |
| borderColor | string | '#ffffff' | #ffffff |
| radius | number | 25 | 25 |
| shadow | boolean | true | true |
| onCardClick | (index: number) => void | - | — |
| transformStyles | string[] | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 256](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L256)
- [pointerdown, line 257](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L257)
- [pointerleave, line 258](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L258)
- [click, line 259](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L259)
- [focusin, line 260](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L260)
- [focusout, line 261](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L261)
- [keydown, line 262](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L262)

## Motion locations

- [delay, line 67](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.jsx#L67): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BounceCards/BounceCards.css); motion-related lines: 19.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
