# SideRays

Category: Backgrounds. Public entry: [SideRays](https://reactbits.dev/backgrounds/side-rays).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/SideRays/SideRays.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/SideRays/SideRays.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/SideRays/SideRays.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| rayColor1 | string | '#FFC46B' | #FFC46B |
| rayColor2 | string | '#96c8ff' | #96c8ff |
| blend | number | 0.6 | 0.6 |
| origin | 'top-right' \| 'top-left' \| 'bottom-right' \| 'bottom-left' \| 'right' \| 'left' | 'top-right' | top-right |
| speed | number | 2.5 | 2.5 |
| intensity | number | 2 | 2 |
| spread | number | 2 | 2 |
| density | number | 5 | 5 |
| sharpness | number | 0.5 | 0.5 |
| tilt | number | 0 | 0 |
| falloff | number | 1.6 | 1.6 |
| glow | number | 1 | 1 |
| saturation | number | 1 | 1 |
| dust | number | 0 | 0 |
| followMouse | boolean | true | true |
| mouseInfluence | number | 0.5 | 0.5 |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 407](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L407)
- [pointerup, line 408](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L408)
- [pointercancel, line 409](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L409)
- [pointerleave, line 410](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L410)
- [webglcontextlost, line 419](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L419)
- [webglcontextrestored, line 420](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L420)
- [visibilitychange, line 438](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L438)

## Motion locations

- [velocity, line 275](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.jsx#L275): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/SideRays/SideRays.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
