# BorderGlow

Category: Components. Public entry: [BorderGlow](https://reactbits.dev/components/border-glow).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/BorderGlow/BorderGlow.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/BorderGlow/BorderGlow.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/BorderGlow/BorderGlow.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| className | string | "" |  |
| edgeSensitivity | number | 30 | 30 |
| glowColor | string | "40 80 80" | 40 80 80 |
| backgroundColor | string | "#120F17" | #120F17 |
| borderRadius | number | 28 | 28 |
| glowRadius | number | 40 | 40 |
| glowIntensity | number | 1.0 | 1 |
| coneSpread | number | 25 | 25 |
| animated | boolean | false | false |
| colors | string[] | [...] | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [onPointerMove, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L162)

## Motion locations

- [duration, line 137](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L137): 500
- [ease, line 138](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L138): computed; read the linked expression
- [duration, line 138](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L138): 1500
- [ease, line 141](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L141): computed; read the linked expression
- [delay, line 141](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L141): 1500
- [duration, line 141](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L141): 2250
- [ease, line 144](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L144): computed; read the linked expression
- [delay, line 144](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L144): 2500
- [duration, line 144](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.jsx#L144): 1500

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BorderGlow/BorderGlow.css); motion-related lines: 46, 54.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
