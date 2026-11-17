# LightRays

Category: Backgrounds. Public entry: [LightRays](https://reactbits.dev/backgrounds/light-rays).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/LightRays/LightRays.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/LightRays/LightRays.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/LightRays/LightRays.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| raysOrigin | RaysOrigin | 'top-center' | top-center |
| raysColor | string | '#ffffff' | #ffffff |
| raysSpeed | number | 1 | 1 |
| lightSpread | number | 0.5 | 0.5 |
| rayLength | number | 3 | 3 |
| rayDensity | number | 1 | 1 |
| tilt | number | 0 | 0 |
| raySharpness | number | 0.35 | 0.35 |
| glow | number | 0.6 | 0.6 |
| haze | number | 0.25 | 0.25 |
| atmosphere | number | 1 | 1 |
| intensity | number | 1 | 1 |
| pulsating | boolean | false | false |
| fadeDistance | number | 1 | 1 |
| saturation | number | 1 | 1 |
| followMouse | boolean | true | true |
| mouseInfluence | number | 0.1 | 0.1 |
| cursorShadow | boolean | true | true |
| clickPulse | boolean | true | true |
| noiseAmount | number | 0 | 0 |
| distortion | number | 0 | 0 |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 502](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L502)
- [pointerdown, line 503](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L503)
- [pointerup, line 504](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L504)
- [pointercancel, line 505](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L505)
- [pointerleave, line 506](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L506)
- [webglcontextlost, line 515](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L515)
- [webglcontextrestored, line 516](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L516)
- [visibilitychange, line 534](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.jsx#L534)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LightRays/LightRays.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
