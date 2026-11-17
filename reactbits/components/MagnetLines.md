# MagnetLines

Category: Backgrounds. Public entry: [MagnetLines](https://reactbits.dev/backgrounds/magnet-lines).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/MagnetLines/MagnetLines.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/MagnetLines/MagnetLines.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/MagnetLines/MagnetLines.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| spacing | number | 30 | 30 |
| rows | number | - | — |
| columns | number | - | — |
| containerSize | number \| string | - | — |
| lineColor | string | '#efefef' | #efefef |
| accentColor | string | - | — |
| lineWidth | number \| string | 2 | 2 |
| lineHeight | number \| string | 18 | 18 |
| baseAngle | number | -10 | -10 |
| mode | 'orbit' \| 'attract' \| 'spiral' \| 'dipole' | 'orbit' | orbit |
| shape | 'line' \| 'arrow' \| 'needle' | 'line' | line |
| rainbow | boolean | false | false |
| radius | number | 200 | 200 |
| fade | number | 0.65 | 0.65 |
| edgeFade | number | 0 | 0 |
| stretch | number | 0.4 | 0.4 |
| reach | number | 0 | 0 |
| scatter | number | 0 | 0 |
| inertia | number | 0.35 | 0.35 |
| bounce | number | 0.3 | 0.3 |
| ripple | number | 0.3 | 0.3 |
| clickPulse | boolean | true | true |
| intro | boolean | true | true |
| idle | boolean | false | false |
| tiltX | number | 0 | 0 |
| tiltY | number | 0 | 0 |
| maxDevicePixelRatio | number | 2 | 2 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 996](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L996)
- [pointerdown, line 997](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L997)
- [pointerleave, line 998](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L998)
- [webglcontextlost, line 1007](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L1007)
- [webglcontextrestored, line 1008](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L1008)
- [resize, line 1019](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L1019)
- [visibilitychange, line 1031](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L1031)

## Motion locations

- [bounce, line 451](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.jsx#L451): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MagnetLines/MagnetLines.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
