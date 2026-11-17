# Antigravity

Category: Backgrounds. Public entry: [Antigravity](https://reactbits.dev/backgrounds/antigravity).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Antigravity/Antigravity.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Antigravity/Antigravity.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Antigravity/Antigravity.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#5227FF', '#FF9FFC', '#B497CF'] | — |
| color | string | - | — |
| colorMode | 'conic' \| 'radial' \| 'random' | 'conic' | conic |
| colorSpeed | number | 0.05 | 0.05 |
| particleShape | 'capsule' \| 'sphere' \| 'box' \| 'tetrahedron' | 'capsule' | capsule |
| count | number | 1500 | 1500 |
| particleSize | number | 0.9 | 0.9 |
| particleVariance | number | 1 | 1 |
| magnetRadius | number | 9 | 9 |
| ringRadius | number | 7 | 7 |
| fieldStrength | number | 10 | 10 |
| waveAmplitude | number | 1 | 1 |
| waveCount | number | 3 | 3 |
| waveSpeed | number | 0.4 | 0.4 |
| rotationSpeed | number | 0 | 0 |
| pulseSpeed | number | 3 | 3 |
| depthFactor | number | 1 | 1 |
| ambient | number | 0.25 | 0.25 |
| lerpSpeed | number | 0.05 | 0.05 |
| autoAnimate | boolean | true | true |
| interactive | boolean | true | true |
| clickBurst | boolean | true | true |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 727](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L727)
- [pointerdown, line 728](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L728)
- [pointerup, line 729](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L729)
- [pointercancel, line 730](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L730)
- [pointerleave, line 731](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L731)
- [webglcontextlost, line 740](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L740)
- [webglcontextrestored, line 741](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L741)
- [visibilitychange, line 759](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L759)

## Motion locations

- [delay, line 441](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.jsx#L441): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Antigravity/Antigravity.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
