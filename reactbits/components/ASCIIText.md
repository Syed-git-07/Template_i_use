# ASCIIText

Category: TextAnimations. Public entry: [ASCIIText](https://reactbits.dev/text-animations/ascii-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ASCIIText/ASCIIText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ASCIIText/ASCIIText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ASCIIText/ASCIIText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ASCIIText/ASCIIText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'Hey!' | Hey! |
| asciiFontSize | number | 8 | 8 |
| charset | string | ' .'`^",:;Il!i~+_-?][}{1)(\|/...' |  .'`^",:;Il!i~+_-?][}{1)(\|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$ |
| colors | string[] | ['#ff6188', '#fc9867', '#ffd866'] | — |
| textColor | string | '#fdf9f3' | #fdf9f3 |
| fontFamily | string | 'IBM Plex Mono', ui-monospace, ... | 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace |
| fontWeight | number | 600 | 600 |
| textScale | number | 1 | 1 |
| blocks | number | 0.9 | 0.9 |
| waves | number | 1 | 1 |
| waveSpeed | number | 1 | 1 |
| chroma | number | 1 | 1 |
| tilt | number | 1 | 1 |
| hueShift | number | 1 | 1 |
| scramble | number | 0.6 | 0.6 |
| clickRipple | boolean | true | true |
| intro | boolean | true | true |
| idle | boolean | true | true |
| interactive | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 505](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ASCIIText/ASCIIText.jsx#L505)
- [pointerdown, line 506](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ASCIIText/ASCIIText.jsx#L506)
- [pointerleave, line 507](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ASCIIText/ASCIIText.jsx#L507)
- [loadingdone, line 542](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ASCIIText/ASCIIText.jsx#L542)

## Motion locations


## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
