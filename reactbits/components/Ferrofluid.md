# Ferrofluid

Category: Backgrounds. Public entry: [Ferrofluid](https://reactbits.dev/backgrounds/ferrofluid).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Ferrofluid/Ferrofluid.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Ferrofluid/Ferrofluid.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Ferrofluid/Ferrofluid.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#ffffff', '#ffffff', '#ffffff'] | — |
| brightness | number | 1 | 1 |
| scale | number | 1.6 | 1.6 |
| spikeHeight | number | 1 | 1 |
| sharpness | number | 2.5 | 2.5 |
| tilt | number | 48 | 48 |
| turbulence | number | 1 | 1 |
| fluidity | number | 0.5 | 0.5 |
| speed | number | 0.5 | 0.5 |
| magnetism | number | 1 | 1 |
| variation | number | 0 | 0 |
| flowDirection | 'down' \| 'up' \| 'left' \| 'right' \| 'none' | 'down' | down |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 1 | 1 |
| mouseRadius | number | 0.22 | 0.22 |
| mouseDampening | number | 0.15 | 0.15 |
| clickPulse | boolean | true | true |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| transparent | boolean | true | true |
| color | string | '#120f17' | — |
| opacity | number | 1 | 1 |
| paused | boolean | false | false |
| mixBlendMode | string | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 850](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L850)
- [pointerdown, line 851](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L851)
- [pointerup, line 852](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L852)
- [pointercancel, line 853](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L853)
- [pointerleave, line 854](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L854)
- [visibilitychange, line 855](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.jsx#L855)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ferrofluid/Ferrofluid.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
