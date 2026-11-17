# PixelTransition

Category: Animations. Public entry: [PixelTransition](https://reactbits.dev/animations/pixel-transition).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/PixelTransition/PixelTransition.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/PixelTransition/PixelTransition.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/PixelTransition/PixelTransition.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| firstContent | ReactNode | - | — |
| secondContent | ReactNode | - | — |
| gridSize | number | 10 | 10 |
| pixelColor | string | '#ffffff' | #ffffff |
| mosaic | number | 0 | 0 |
| animationStepDuration | number | 0.4 | 0.4 |
| pattern | 'random' \| 'dither' \| 'ripple' \| 'wipe' | 'random' | random |
| randomness | number | 0.3 | 0.3 |
| pixelAnimation | 'pop' \| 'grow' \| 'fade' | 'pop' | pop |
| pixelShape | 'square' \| 'rounded' \| 'circle' | 'square' | square |
| gap | number | 0 | 0 |
| fps | number | 0 | 0 |
| trigger | 'hover' \| 'click' | 'hover' | hover |
| active | boolean | - | — |
| once | boolean | false | false |
| onActiveChange | (active: boolean) => void | - | — |
| aspectRatio | string | '100%' | 100% |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [onPointerEnter, line 369](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L369)
- [onPointerLeave, line 370](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L370)
- [onPointerDown, line 371](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L371)
- [onClick, line 372](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L372)
- [onFocus, line 373](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L373)
- [onBlur, line 374](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L374)
- [onKeyDown, line 375](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L375)

## Motion locations

- [duration, line 61](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.jsx#L61): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/PixelTransition/PixelTransition.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
