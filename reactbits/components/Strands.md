# Strands

Category: Animations. Public entry: [Strands](https://reactbits.dev/animations/strands).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/Strands/Strands.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/Strands/Strands.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/Strands/Strands.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | Siri palette | — |
| count | number | 3 | 3 |
| speed | number | 1 | 1 |
| amplitude | number | 1 | 1 |
| waviness | number | 1 | 1 |
| energy | number | 0.65 | 0.65 |
| thickness | number | 1 | 1 |
| spread | number | 1 | 1 |
| glow | number | 1 | 1 |
| taper | number | 1 | 1 |
| intensity | number | 1 | 1 |
| saturation | number | 1 | 1 |
| hueShift | number | 0 | 0 |
| scale | number | 1 | 1 |
| glass | boolean | true | true |
| glassSize | number | 1 | 1 |
| refraction | number | 1 | 1 |
| rim | number | 1 | 1 |
| dispersion | number | 1 | 1 |
| listening | boolean | false | false |
| level | number | undefined | — |
| interactive | boolean | true | true |
| clickPulse | boolean | true | true |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 631](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L631)
- [webglcontextrestored, line 632](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L632)
- [pointermove, line 633](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L633)
- [pointerleave, line 634](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L634)
- [pointerdown, line 635](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L635)
- [visibilitychange, line 655](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.jsx#L655)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Strands/Strands.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
