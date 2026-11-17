# LightPillar

Category: Backgrounds. Public entry: [LightPillar](https://reactbits.dev/backgrounds/light-pillar).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/LightPillar/LightPillar.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/LightPillar/LightPillar.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/LightPillar/LightPillar.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| topColor | string | '#5227FF' | #5227FF |
| bottomColor | string | '#FF9FFC' | #FF9FFC |
| intensity | number | 1 | 1 |
| glowAmount | number | 0.002 | 0.002 |
| bloom | number | 0.5 | 0.5 |
| pillarWidth | number | 3 | 3 |
| pillarHeight | number | 0.4 | 0.4 |
| pillarRotation | number | 25 | 25 |
| twist | number | 0.4 | 0.4 |
| detail | number | 4 | 4 |
| rotationSpeed | number | 0.3 | 0.3 |
| flow | number | 1 | 1 |
| noiseIntensity | number | 0.5 | 0.5 |
| interactive | boolean | true | true |
| clickPulse | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0 | 0 |
| quality | 'low' \| 'medium' \| 'high' | 'high' | high |
| resolution | number | - | — |
| mixBlendMode | string | 'screen' | screen |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 307](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L307)
- [webglcontextrestored, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L308)
- [pointermove, line 566](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L566)
- [pointerdown, line 567](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L567)
- [pointerleave, line 568](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L568)
- [visibilitychange, line 569](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.jsx#L569)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightPillar/LightPillar.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
