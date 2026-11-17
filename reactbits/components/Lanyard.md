# Lanyard

Category: Components. Public entry: [Lanyard](https://reactbits.dev/components/lanyard).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Lanyard/Lanyard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Lanyard/Lanyard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Lanyard/Lanyard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| frontImage | string | undefined | — |
| backImage | string | undefined | — |
| imageFit | 'cover' \| 'contain' | 'cover' | cover |
| cardColor | string | '#ffffff' | #ffffff |
| orientation | 'portrait' \| 'landscape' | 'portrait' | portrait |
| finish | 'glossy' \| 'matte' \| 'holographic' \| 'metallic' | 'glossy' | glossy |
| cornerRadius | number | 0.3 | 0.3 |
| size | number | 0.6 | 0.6 |
| anchor | 'left' \| 'center' \| 'right' | 'center' | center |
| strapLength | number | 0.5 | 0.5 |
| strapImage | string | undefined | — |
| strapColor | string | '#111111' | #111111 |
| strapWidth | number | 0.65 | 0.65 |
| metal | 'graphite' \| 'silver' \| 'gold' | 'silver' | silver |
| gravity | number | 1 | 1 |
| damping | number | 0.5 | 0.5 |
| elasticity | number | 0.5 | 0.5 |
| breeze | number | 0.5 | 0.5 |
| interactive | boolean | true | true |
| intro | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, three

## Interaction locations

- [pointerdown, line 1239](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1239)
- [pointermove, line 1240](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1240)
- [pointerup, line 1241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1241)
- [pointercancel, line 1242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1242)
- [lostpointercapture, line 1243](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1243)
- [touchstart, line 1244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1244)
- [visibilitychange, line 1265](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1265)

## Motion locations

- [velocity, line 475](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L475): computed; read the linked expression
- [mass, line 479](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L479): 1
- [stiffness, line 1113](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.jsx#L1113): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Lanyard/Lanyard.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: setCursor → grabbing (line 1204).

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
