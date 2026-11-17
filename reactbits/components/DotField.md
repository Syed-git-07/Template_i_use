# DotField

Category: Backgrounds. Public entry: [DotField](https://reactbits.dev/backgrounds/dot-field).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/DotField/DotField.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/DotField/DotField.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/DotField/DotField.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| dotRadius | number | 1.5 | 1.5 |
| dotSpacing | number | 14 | 14 |
| pattern | 'grid' \| 'hex' \| 'spiral' \| 'scatter' | 'grid' | grid |
| gradientFrom | string | '#5227FF' | #5227FF |
| gradientTo | string | '#FF9FFC' | #FF9FFC |
| gradientAngle | number | 135 | 135 |
| cursorRadius | number | 240 | 240 |
| bulgeStrength | number | 0.6 | 0.6 |
| twist | number | 0 | 0 |
| glowColor | string | '#ffffff' | #ffffff |
| glowRadius | number | 160 | 160 |
| glowIntensity | number | 0.8 | 0.8 |
| baseOpacity | number | 0.55 | 0.55 |
| waveAmplitude | number | 0 | 0 |
| sparkle | boolean | false | false |
| speed | number | 1 | 1 |
| interactive | boolean | true | true |
| holdToZoom | boolean | true | true |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 586](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L586)
- [pointerdown, line 587](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L587)
- [pointerup, line 588](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L588)
- [pointercancel, line 589](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L589)
- [pointerleave, line 590](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L590)
- [webglcontextlost, line 599](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L599)
- [webglcontextrestored, line 600](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L600)
- [visibilitychange, line 618](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.jsx#L618)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/DotField/DotField.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
