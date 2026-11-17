# StickerPeel

Category: Animations. Public entry: [StickerPeel](https://reactbits.dev/animations/sticker-peel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/StickerPeel/StickerPeel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/StickerPeel/StickerPeel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/StickerPeel/StickerPeel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| imageSrc | string | required | — |
| width | number | 200 | 200 |
| rotate | number | 0 | 0 |
| finish | 'gloss' \| 'matte' \| 'holo' | 'gloss' | gloss |
| peelBackHoverPct | number | 25 | 25 |
| peelBackActivePct | number | 40 | 40 |
| peelDirection | number | 0 | 0 |
| followPointer | boolean | true | true |
| curlRadius | number | 12 | 12 |
| backColor | string | '#d4d4d8' | #d4d4d8 |
| lightingIntensity | number | 0.5 | 0.5 |
| shadowIntensity | number | 0.6 | 0.6 |
| draggable | boolean | true | true |
| swing | number | 1 | 1 |
| friction | number | 0.5 | 0.5 |
| bounce | number | 0.35 | 0.35 |
| intro | boolean | true | true |
| initialPosition | 'center' \| { x: number; y: number } | 'center' | center |
| onDragStart | () => void | - | — |
| onDragEnd | () => void | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 985](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L985)
- [pointerleave, line 986](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L986)
- [visibilitychange, line 987](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L987)
- [pointermove, line 988](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L988)
- [pointerleave, line 989](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L989)
- [pointerdown, line 990](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L990)
- [pointerup, line 991](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L991)
- [pointercancel, line 992](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L992)

## Motion locations

- [friction, line 335](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L335): computed; read the linked expression
- [bounce, line 336](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.jsx#L336): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StickerPeel/StickerPeel.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
