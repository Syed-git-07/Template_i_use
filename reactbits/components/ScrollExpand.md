# ScrollExpand

Category: Animations. Public entry: [ScrollExpand](https://reactbits.dev/animations/scroll-expand).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ScrollExpand/ScrollExpand.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ScrollExpand/ScrollExpand.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ScrollExpand/ScrollExpand.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ScrollExpand/ScrollExpand.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | '' |  |
| mediaType | "image" \| "video" | "image" | image |
| poster | string | '' |  |
| alt | string | '' |  |
| title | string | '' |  |
| scrollHint | string | '' |  |
| startWidth | number | 42 | 42 |
| startHeight | number | 58 | 58 |
| startRadius | number | 24 | 24 |
| endRadius | number | 0 | 0 |
| mediaZoom | number | 1.35 | 1.35 |
| scrollDistance | number | 1.2 | 1.2 |
| holdDistance | number | 0.35 | 0.35 |
| smoothing | number | 0.1 | 0.1 |
| overlayScrim | number | 0.45 | 0.45 |
| useWindowScroll | boolean | false | false |
| enabled | boolean | true | true |
| children | React.ReactNode | — | — |
| className | string | '' |  |
| style | object | — | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [scroll, line 177](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ScrollExpand/ScrollExpand.jsx#L177)
- [resize, line 178](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ScrollExpand/ScrollExpand.jsx#L178)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ScrollExpand/ScrollExpand.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
