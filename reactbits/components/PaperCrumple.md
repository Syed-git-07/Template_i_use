# PaperCrumple

Category: Micro. Public entry: [PaperCrumple](https://reactbits.dev/micro/paper-crumple).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/PaperCrumple/PaperCrumple.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/PaperCrumple/PaperCrumple.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/PaperCrumple/PaperCrumple.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| src | string | - | — |
| alt | string | 'Crumplable image' | Crumplable image |
| backSrc | string | '' |  |
| width | number | 320 | 320 |
| height | number | 400 | 400 |
| sceneHeight | number | 560 | 560 |
| imageFit | 'cover' \| 'contain' | 'cover' | cover |
| releaseBehavior | 'stay' \| 'restore' \| 'creased' | 'restore' | restore |
| crumpleAmount | number | 0.85 | 0.85 |
| crumpleDuration | number | 0.55 | 0.55 |
| releaseDuration | number | 0.4 | 0.4 |
| foldCount | number | 6 | 6 |
| foldSharpness | number | 0.6 | 0.6 |
| wrinkleDepth | number | 0.65 | 0.65 |
| creaseStrength | number | 0.18 | 0.18 |
| paperColor | string | '#f4f0e8' | #f4f0e8 |
| roughness | number | 0.92 | 0.92 |
| paperTexture | number | 0.08 | 0.08 |
| lightIntensity | number | 1.8 | 1.8 |
| lightAngle | number | -35 | -35 |
| shadow | boolean | true | true |
| shadowOpacity | number | 0.08 | 0.08 |
| draggable | boolean | true | true |
| dragRotation | number | 10 | 10 |
| dragRadius | number | 180 | 180 |
| returnToOrigin | boolean | true | true |
| rotation | number | 0 | 0 |
| seed | number | 7 | 7 |
| detail | number | 64 | 64 |
| disabled | boolean | false | false |
| resetKey | number \| string | 0 | 0 |
| onStateChange | (state: PaperCrumpleState) => void | - | — |
| onError | (error: Error) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, three

## Interaction locations

- [pointerdown, line 928](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L928)
- [pointermove, line 929](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L929)
- [pointerup, line 930](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L930)
- [pointercancel, line 931](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L931)
- [lostpointercapture, line 932](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L932)
- [keydown, line 933](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L933)
- [keyup, line 934](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L934)
- [blur, line 935](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L935)
- [blur, line 936](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L936)
- [visibilitychange, line 937](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L937)
- [change, line 938](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L938)
- [webglcontextlost, line 939](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L939)
- [webglcontextrestored, line 940](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L940)

## Motion locations

- [velocity, line 6](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.jsx#L6): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PaperCrumple/PaperCrumple.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: setStatus → loading (line 316); setStatus → error (line 334); setStatus → error (line 917); setStatus → ready (line 923); setStatus → ready (line 1001); setStatus → error (line 1007); setStatus → error (line 1011).

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
