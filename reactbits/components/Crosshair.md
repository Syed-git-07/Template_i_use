# Crosshair

Category: Animations. Public entry: [Crosshair](https://reactbits.dev/animations/crosshair).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/Crosshair/Crosshair.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/Crosshair/Crosshair.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/Crosshair/Crosshair.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#ffffff' | #ffffff |
| containerRef | RefObject<HTMLElement> | null | — |
| thickness | number | 1 | 1 |
| opacity | number | 0.85 | 0.85 |
| lineStyle | 'solid' \| 'dashed' \| 'dotted' | 'solid' | solid |
| gap | number | 0 | 0 |
| fade | number | 0 | 0 |
| smoothing | number | 0.35 | 0.35 |
| showCoordinates | boolean | true | true |
| targetEffect | 'lock' \| 'glitch' \| 'none' | 'lock' | lock |
| targetSelector | string | 'a, button, [data-crosshair-target]' | a, button, [data-crosshair-target] |
| clickPulse | boolean | true | true |
| hideCursor | boolean | false | false |
| blendMode | 'normal' \| 'difference' | 'normal' | normal |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 395](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L395)
- [pointerdown, line 396](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L396)
- [pointerup, line 397](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L397)
- [pointercancel, line 398](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L398)
- [scroll, line 399](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L399)
- [pointerleave, line 400](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L400)
- [pointerout, line 401](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Crosshair/Crosshair.jsx#L401)

## Motion locations


## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
