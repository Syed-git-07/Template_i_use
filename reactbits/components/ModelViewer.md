# ModelViewer

Category: Components. Public entry: [ModelViewer](https://reactbits.dev/components/model-viewer).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ModelViewer/ModelViewer.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ModelViewer/ModelViewer.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ModelViewer/ModelViewer.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| url | string | - | — |
| width | number \| string | 400 | 400 |
| height | number \| string | 400 | 400 |
| environment | string | 'studio' | studio |
| environmentIntensity | number | 1 | 1 |
| exposure | number | 1 | 1 |
| intro | 'rise' \| 'spin' \| 'fade' \| 'none' | 'rise' | rise |
| autoRotate | boolean | true | true |
| autoRotateSpeed | number | 0.4 | 0.4 |
| autoRotateDelay | number | 2 | 2 |
| dragRotate | boolean | true | true |
| turntable | boolean | false | false |
| zoom | boolean | true | true |
| minZoom | number | 0.7 | 0.7 |
| maxZoom | number | 2 | 2 |
| hoverTilt | number | 0.15 | 0.15 |
| float | number | 0.3 | 0.3 |
| shadow | boolean | true | true |
| shadowOpacity | number | 0.45 | 0.45 |
| fit | number | 0.8 | 0.8 |
| offsetX | number | 0 | 0 |
| offsetY | number | 0 | 0 |
| startAngle | number | -30 | -30 |
| tilt | number | 10 | 10 |
| resetOnDoubleClick | boolean | true | true |
| onModelLoaded | () => void | - | — |
| ref | Ref | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @react-three/fiber, @react-three/drei, three/examples/jsm/loaders/OBJLoader.js, three

## Interaction locations

- [pointerdown, line 237](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L237)
- [pointermove, line 238](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L238)
- [pointerup, line 239](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L239)
- [pointercancel, line 240](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L240)
- [pointerleave, line 241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L241)
- [wheel, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L242)
- [dblclick, line 243](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L243)
- [onCreated, line 458](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L458)
- [onReady, line 476](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ModelViewer/ModelViewer.jsx#L476)

## Motion locations


## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, webgl.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
