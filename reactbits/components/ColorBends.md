# ColorBends

Category: Backgrounds. Public entry: [ColorBends](https://reactbits.dev/backgrounds/color-bends).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ColorBends/ColorBends.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/ColorBends/ColorBends.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/ColorBends/ColorBends.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/ColorBends/ColorBends.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| rotation | number | 90 | 90 |
| autoRotate | number | 0 | 0 |
| speed | number | 0.2 | 0.2 |
| colors | string[] | [] | — |
| transparent | boolean | true | true |
| scale | number | 1 | 1 |
| frequency | number | 1 | 1 |
| warpStrength | number | 1 | 1 |
| mouseInfluence | number | 1 | 1 |
| parallax | number | 0.5 | 0.5 |
| noise | number | 0.15 | 0.15 |
| iterations | number | 1 | 1 |
| intensity | number | 1.5 | 1.5 |
| bandWidth | number | 6 | 6 |
| className | string | '' | — |
| style | React.CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, three

## Interaction locations

- [resize, line 231](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ColorBends/ColorBends.jsx#L231)
- [visibilitychange, line 279](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ColorBends/ColorBends.jsx#L279)
- [pointermove, line 364](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ColorBends/ColorBends.jsx#L364)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/ColorBends/ColorBends.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
