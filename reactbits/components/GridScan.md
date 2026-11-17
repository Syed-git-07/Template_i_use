# GridScan

Category: Backgrounds. Public entry: [GridScan](https://reactbits.dev/backgrounds/grid-scan).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/GridScan/GridScan.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/GridScan/GridScan.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/GridScan/GridScan.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| linesColor | string | '#4d4757' | — |
| scanColor | string | '#7dd3fc' | — |
| cells | number | 8 | 8 |
| lineThickness | number | 1 | 1 |
| lineStyle | 'solid' \| 'dashed' \| 'dotted' | 'solid' | solid |
| depth | number | 3 | 3 |
| depthFade | number | 0.6 | 0.6 |
| parallax | number | 1 | 1 |
| shading | number | 0.7 | 0.7 |
| reflection | number | 0.35 | 0.35 |
| points | boolean | true | true |
| scanDirection | 'forward' \| 'backward' \| 'pingpong' | 'forward' | forward |
| scanDuration | number | 2.4 | 2.4 |
| scanDelay | number | 1.6 | 1.6 |
| scanWidth | number | 1 | 1 |
| trail | number | 0.5 | 0.5 |
| glow | number | 0.6 | 0.6 |
| autoScan | boolean | true | true |
| interactive | boolean | true | true |
| clickEffect | 'ping' \| 'scan' \| 'none' | 'ping' | ping |
| enableWebcam | boolean | false | false |
| showPreview | boolean | false | false |
| modelsPath | string | CDN URL | https://cdn.jsdelivr.net/gh/justadudewhohacks/face-api.js@0.22.2/weights |
| enableGyro | boolean | false | false |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 891](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L891)
- [pointerdown, line 892](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L892)
- [deviceorientation, line 893](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L893)
- [click, line 894](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L894)
- [pointerleave, line 895](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L895)
- [visibilitychange, line 896](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L896)

## Motion locations

- [duration, line 477](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L477): computed; read the linked expression
- [delay, line 478](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.jsx#L478): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GridScan/GridScan.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: setStatus → loading (line 948); setStatus → searching (line 965); setStatus → tracking (line 992); setStatus → searching (line 997); setStatus → blocked (line 1003).

Signals present: reduced_motion, visibility, cleanup, frame_loop, microphone, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
