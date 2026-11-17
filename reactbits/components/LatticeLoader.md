# LatticeLoader

Category: Micro. Public entry: [LatticeLoader](https://reactbits.dev/micro/lattice-loader).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/LatticeLoader/LatticeLoader.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/LatticeLoader/LatticeLoader.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/LatticeLoader/LatticeLoader.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/LatticeLoader/LatticeLoader.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | string | "Thinking" | Thinking |
| doneLabel | string | "Done in" | Done in |
| errorLabel | string | "Failed after" | Failed after |
| status | "working" \| "done" \| "error" | "working" | working |
| pattern | string \| { cells, loop?, scale? } | "orbit" | orbit |
| grid | 3 \| 4 | 3 | 3 |
| shape | "square" \| "round" | "round" | round |
| color | string | "currentColor" | currentColor |
| doneColor | string | "#22c55e" | #22c55e |
| errorColor | string | "#ef4444" | #ef4444 |
| cellSize | number | 6 | 6 |
| gap | number | 2 | 2 |
| fontSize | number | 14 | 14 |
| step | number | 90 | 90 |
| idleOpacity | number | 0.15 | 0.15 |
| glow | boolean | false | false |
| glowColor | string | "" |  |
| showTimer | boolean | true | true |
| elapsed | number | undefined | — |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations


## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/LatticeLoader/LatticeLoader.css); motion-related lines: 58, 62, 66, 70, 74, 78, 86, 92, 107, 113, 131, 161, 177, 193, 209, 225, 231, 232.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: none matched.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
