# FloatingLines

Category: Backgrounds. Public entry: [FloatingLines](https://reactbits.dev/backgrounds/floating-lines).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/FloatingLines/FloatingLines.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/FloatingLines/FloatingLines.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/FloatingLines/FloatingLines.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| linesGradient | string[] | ['#e945f5', '#ffffff'] | — |
| enabledWaves | Array<'top' \| 'middle' \| 'bottom'> | ['top', 'middle', 'bottom'] | — |
| lineCount | number \| number[] | 10 | 10 |
| lineDistance | number \| number[] | 6 | 6 |
| lineStyle | 'solid' \| 'dotted' \| 'dashed' | 'solid' | solid |
| lineWidth | number | 1 | 1 |
| glow | number | 1 | 1 |
| brightness | number | 1 | 1 |
| animationSpeed | number | 1 | 1 |
| amplitude | number | 1 | 1 |
| depthOfField | number | 0.5 | 0.5 |
| edgeFade | number | 0 | 0 |
| topWavePosition | { x: number; y: number; rotate: number } | { x: 10, y: 0.5, rotate: -0.4 } | — |
| middleWavePosition | { x: number; y: number; rotate: number } | { x: 5, y: 0, rotate: 0.2 } | — |
| bottomWavePosition | { x: number; y: number; rotate: number } | { x: 2, y: -0.7, rotate: -1 } | — |
| interactive | boolean | true | true |
| bendRadius | number | 5 | 5 |
| bendStrength | number | -0.5 | -0.5 |
| mouseDamping | number | 0.05 | 0.05 |
| parallax | boolean | true | true |
| parallaxStrength | number | 0.2 | 0.2 |
| clickSwirl | boolean | true | true |
| intro | boolean | true | true |
| mixBlendMode | CSSProperties['mixBlendMode'] | 'screen' | screen |
| backgroundColor | string | - | — |
| lightMode | boolean | false | false |
| opacity | number | 1 | 1 |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 575](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L575)
- [pointerdown, line 576](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L576)
- [pointerup, line 577](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L577)
- [pointercancel, line 578](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L578)
- [pointerleave, line 579](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L579)
- [visibilitychange, line 580](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.jsx#L580)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FloatingLines/FloatingLines.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
