# Radar

Category: Backgrounds. Public entry: [Radar](https://reactbits.dev/backgrounds/radar).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Radar/Radar.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Radar/Radar.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Radar/Radar.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#3ef09a' | #3ef09a |
| backgroundColor | string | 'transparent' | transparent |
| mode | 'sweep' \| 'pulse' | 'sweep' | sweep |
| speed | number | 1 | 1 |
| trail | number | 0.35 | 0.35 |
| scale | number | 0.9 | 0.9 |
| ringCount | number | 6 | 6 |
| spokeCount | number | 12 | 12 |
| ticks | boolean | true | true |
| targets | number | 6 | 6 |
| clutter | number | 0.35 | 0.35 |
| glow | number | 1 | 1 |
| brightness | number | 1 | 1 |
| gridOpacity | number | 1 | 1 |
| lineWidth | number | 1 | 1 |
| tilt | number | 0 | 0 |
| centerX | number | 0.5 | 0.5 |
| centerY | number | 0.5 | 0.5 |
| mouseInteraction | boolean | true | true |
| intro | boolean | true | true |
| grain | number | 0.03 | 0.03 |
| fade | number | 0 | 0 |
| opacity | number | 1 | 1 |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 872](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.jsx#L872)
- [pointerleave, line 873](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.jsx#L873)
- [visibilitychange, line 874](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.jsx#L874)

## Motion locations

- [velocity, line 391](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.jsx#L391): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Radar/Radar.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
