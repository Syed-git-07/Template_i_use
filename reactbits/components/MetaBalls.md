# MetaBalls

Category: Animations. Public entry: [MetaBalls](https://reactbits.dev/animations/meta-balls).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/MetaBalls/MetaBalls.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/MetaBalls/MetaBalls.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/MetaBalls/MetaBalls.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#ffffff' | #ffffff |
| cursorBallColor | string | '#ffffff' | #ffffff |
| variant | 'solid' \| 'outline' \| 'contour' | 'solid' | solid |
| motion | 'orbit' \| 'drift' \| 'lava' | 'orbit' | orbit |
| speed | number | 0.3 | 0.3 |
| animationSize | number | 30 | 30 |
| ballCount | number | 15 | 15 |
| clumpFactor | number | 1 | 1 |
| gooeyness | number | 0.5 | 0.5 |
| stickiness | number | 0.5 | 0.5 |
| stretch | number | 0.5 | 0.5 |
| wobble | number | 0.5 | 0.5 |
| enableMouseInteraction | boolean | true | true |
| cursorBallSize | number | 3 | 3 |
| hoverSmoothness | number | 0.1 | 0.1 |
| clickBurst | boolean | true | true |
| lineWidth | number | 1.5 | 1.5 |
| rings | number | 4 | 4 |
| intro | boolean | true | true |
| enableTransparency | boolean | false | false |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 587](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L587)
- [pointerdown, line 588](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L588)
- [pointerout, line 589](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L589)
- [pointerup, line 590](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L590)
- [pointercancel, line 591](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L591)

## Motion locations

- [delay, line 136](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L136): computed; read the linked expression
- [threshold, line 239](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L239): computed; read the linked expression
- [threshold, line 351](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.jsx#L351): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/MetaBalls/MetaBalls.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
