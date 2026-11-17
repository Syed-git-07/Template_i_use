# TiltedCard

Category: Components. Public entry: [TiltedCard](https://reactbits.dev/components/tilted-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/TiltedCard/TiltedCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/TiltedCard/TiltedCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/TiltedCard/TiltedCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| imageSrc | string | - | — |
| altText | string | 'Tilted card image' | Tilted card image |
| children | ReactNode | - | — |
| captionText | string | '' |  |
| showTooltip | boolean | true | true |
| overlayContent | ReactNode | null | — |
| displayOverlayContent | boolean | false | false |
| overlayDepth | number | 30 | 30 |
| backContent | ReactNode | null | — |
| flipOnClick | boolean | true | true |
| flipped | boolean | - | — |
| onFlip | (flipped: boolean) => void | - | — |
| onClick | (event) => void | - | — |
| containerWidth | number \| string | '100%' | 100% |
| containerHeight | number \| string | '300px' | 300px |
| imageWidth | number \| string | '300px' | 300px |
| imageHeight | number \| string | '300px' | 300px |
| rotateAmplitude | number | 12 | 12 |
| scaleOnHover | number | 1.05 | 1.05 |
| perspective | number \| string | 800 | 800 |
| radius | number \| string | 15 | 15 |
| smoothness | number | 0.6 | 0.6 |
| glare | number | 0.5 | 0.5 |
| glareColor | string | '#ffffff' | #ffffff |
| shadow | number | 0.5 | 0.5 |
| parallax | number | 1 | 1 |
| axis | 'both' \| 'horizontal' \| 'vertical' | 'both' | both |
| reverse | boolean | false | false |
| trackWindow | boolean | false | false |
| floating | boolean | false | false |
| gyroscope | boolean | true | true |
| intro | boolean | true | true |
| introDelay | number | 0 | 0 |
| className | string | '' |  |
| style | CSSProperties | - | — |
| TiltedCardLayer | component | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 416](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L416)
- [pointermove, line 417](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L417)
- [pointerleave, line 418](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L418)
- [pointerdown, line 419](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L419)
- [focus, line 420](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L420)
- [blur, line 421](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L421)
- [pointerup, line 422](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L422)
- [pointercancel, line 423](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L423)
- [pointermove, line 424](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L424)
- [pointerleave, line 425](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L425)
- [deviceorientation, line 426](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L426)
- [onClick, line 499](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L499)
- [onKeyDown, line 500](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.jsx#L500)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/TiltedCard/TiltedCard.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
