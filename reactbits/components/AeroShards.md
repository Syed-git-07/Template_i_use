# AeroShards

Category: Backgrounds. Public entry: [AeroShards](https://reactbits.dev/backgrounds/aero-shards).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/AeroShards/AeroShards.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/AeroShards/AeroShards.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/AeroShards/AeroShards.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| shardColor | string | '#896ABD' | #896ABD |
| accentColor | string | '#A855F7' | #A855F7 |
| backgroundColor | string | 'transparent' | transparent |
| lightMode | boolean | false | false |
| placement | 'full' \| 'left' \| 'right' \| 'center' | 'full' | full |
| material | 'glass' \| 'chrome' | 'glass' | glass |
| markers | 'plus' \| 'dots' \| 'none' | 'plus' | plus |
| count | number | 1300 | 1300 |
| shardSize | number | 1 | 1 |
| spread | number | 1 | 1 |
| twist | number | 1 | 1 |
| billow | number | 1 | 1 |
| speed | number | 1 | 1 |
| scale | number | 1 | 1 |
| depthOfField | number | 0.75 | 0.75 |
| glow | number | 0.35 | 0.35 |
| grain | number | 0.06 | 0.06 |
| vignette | number | 0.3 | 0.3 |
| intro | boolean | true | true |
| mouseInteraction | boolean | true | true |
| mouseStrength | number | 0.6 | 0.6 |
| parallax | number | 0.5 | 0.5 |
| pulseOnClick | boolean | true | true |
| holdToGather | boolean | true | true |
| paused | boolean | false | false |
| dpr | number | 2 | 2 |
| onError | (error: Error) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, vgpu

## Interaction locations

- [pointermove, line 2197](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L2197)
- [pointerdown, line 2198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L2198)
- [pointerup, line 2199](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L2199)
- [pointercancel, line 2200](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L2200)
- [pointerleave, line 2201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L2201)

## Motion locations

- [velocity, line 943](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.jsx#L943): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/AeroShards/AeroShards.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
