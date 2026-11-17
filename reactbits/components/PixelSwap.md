# PixelSwap

Category: Animations. Public entry: [PixelSwap](https://reactbits.dev/animations/pixel-swap).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/PixelSwap/PixelSwap.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/PixelSwap/PixelSwap.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/PixelSwap/PixelSwap.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| firstContent | ReactNode | - | — |
| secondContent | ReactNode | - | — |
| pattern | 'pointer' \| 'random' \| 'center' \| 'edges' \| 'left-to-right' \| 'right-to-left' \| 'top-to-bottom' \| 'bottom-to-top' \| 'diagonal' \| 'spiral' | 'pointer' | pointer |
| pixelSize | number | 48 | 48 |
| gap | number | 0 | 0 |
| pixelRadius | number | 0 | 0 |
| pixelScale | number | 0 | 0 |
| pixelSpin | number | 0 | 0 |
| duration | number | 400 | 400 |
| pixelDuration | number | 350 | 350 |
| randomness | number | 0.2 | 0.2 |
| bounce | number | 0.3 | 0.3 |
| trigger | 'hover' \| 'click' \| 'none' | 'hover' | hover |
| intro | boolean | true | true |
| initialActive | boolean | false | false |
| active | boolean | - | — |
| onActiveChange | (active: boolean) => void | - | — |
| onComplete | (active: boolean) => void | - | — |
| aspectRatio | string | '16 / 10' | 16 / 10 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [load, line 342](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx#L342)
- [error, line 343](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx#L343)

## Motion locations

- [duration, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx#L158): computed; read the linked expression
- [bounce, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx#L161): computed; read the linked expression
- [velocity, line 264](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.jsx#L264): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelSwap/PixelSwap.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
