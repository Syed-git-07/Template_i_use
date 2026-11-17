# PixelCard

Category: Components. Public entry: [PixelCard](https://reactbits.dev/components/pixel-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/PixelCard/PixelCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/PixelCard/PixelCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/PixelCard/PixelCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| variant | 'default' \| 'blue' \| 'yellow' \| 'pink' | 'default' | default |
| colors | string \| string[] | From variant | — |
| glowColor | string | From variant | — |
| gap | number | From variant | — |
| pixelSize | number | 2 | 2 |
| speed | number | From variant | — |
| shape | 'square' \| 'circle' \| 'diamond' | 'square' | square |
| origin | 'center' \| 'pointer' | 'center' | center |
| revealDuration | number | 600 | 600 |
| spotlight | number | 0.5 | 0.5 |
| glow | number | 0.5 | 0.5 |
| opacity | number | 1 | 1 |
| fade | number | 0 | 0 |
| trigger | 'hover' \| 'click' \| 'always' | 'hover' | hover |
| clickPulse | boolean | true | true |
| intro | boolean | true | true |
| introDelay | number | 0 | 0 |
| noFocus | boolean | From variant | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| radius | number | 24 | 24 |
| className | string | '' |  |
| style | CSSProperties | - | — |
| children | ReactNode | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 520](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L520)
- [pointermove, line 521](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L521)
- [pointerleave, line 522](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L522)
- [pointerdown, line 523](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L523)
- [keydown, line 524](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L524)
- [pointerdown, line 525](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L525)
- [onFocus, line 583](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L583)
- [onBlur, line 584](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L584)

## Motion locations

- [delay, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.jsx#L161): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PixelCard/PixelCard.css); motion-related lines: 40.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
