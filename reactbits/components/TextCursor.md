# TextCursor

Category: TextAnimations. Public entry: [TextCursor](https://reactbits.dev/text-animations/text-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextCursor/TextCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TextCursor/TextCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TextCursor/TextCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TextCursor/TextCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'Hello' | Hello |
| mode | 'stamp' \| 'chain' \| 'ribbon' | 'stamp' | stamp |
| spacing | number | 88 | 88 |
| maxPoints | number | 7 | 7 |
| color | string | 'currentColor' | currentColor |
| fontSize | number | 28 | 28 |
| fontWeight | number \| string | 600 | 600 |
| fontFamily | string | 'inherit' | inherit |
| shrink | number | 0.5 | 0.5 |
| fade | number | 0.6 | 0.6 |
| smoothing | number | 0.3 | 0.3 |
| followMouseDirection | boolean | true | true |
| randomFloat | boolean | true | true |
| popIn | boolean | true | true |
| keepUpright | boolean | true | true |
| exitDuration | number | 0.5 | 0.5 |
| removalInterval | number | 30 | 30 |
| hideCursor | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 364](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextCursor/TextCursor.jsx#L364)
- [pointerdown, line 365](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextCursor/TextCursor.jsx#L365)
- [pointerleave, line 366](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextCursor/TextCursor.jsx#L366)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextCursor/TextCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
