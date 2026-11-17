# CRTWarp

Category: Backgrounds. Public entry: [CRTWarp](https://reactbits.dev/backgrounds/crt-warp).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/CRTWarp/CRTWarp.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/CRTWarp/CRTWarp.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/CRTWarp/CRTWarp.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#c755f7' | #c755f7 |
| backgroundColor | string | '#120f17' | #120f17 |
| lightMode | boolean | false | false |
| mask | 'aperture' \| 'shadow' \| 'slot' \| 'none' | 'aperture' | aperture |
| speed | number | 0.5 | 0.5 |
| variation | number | 0 | 0 |
| waveAmplitude | number | 0.3 | 0.3 |
| waveFrequency | number | 2.5 | 2.5 |
| levels | number | 3 | 3 |
| columns | number | 80 | 80 |
| persistence | number | 0.4 | 0.4 |
| curvature | number | 0.25 | 0.25 |
| corners | number | 0 | 0 |
| scanlineStrength | number | 0.6 | 0.6 |
| scanlineFrequency | number | 200 | 200 |
| maskStrength | number | 0.3 | 0.3 |
| bloom | number | 1.5 | 1.5 |
| bloomRadius | number | 1 | 1 |
| rgbShift | number | 0.003 | 0.003 |
| noise | number | 0.1 | 0.1 |
| flicker | number | 0.15 | 0.15 |
| interference | number | 0.2 | 0.2 |
| vignette | number | 0.3 | 0.3 |
| brightness | number | 1 | 1 |
| intro | boolean | true | true |
| mouseReact | boolean | true | true |
| mouseStrength | number | 0.5 | 0.5 |
| changeOnClick | boolean | true | true |
| dpr | number | 2 | 2 |
| fps | number | 60 | 60 |
| paused | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 807](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.jsx#L807)
- [pointerdown, line 808](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.jsx#L808)
- [pointerleave, line 809](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.jsx#L809)
- [webglcontextlost, line 810](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.jsx#L810)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/CRTWarp/CRTWarp.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
