# BlobCursor

Category: Animations. Public entry: [BlobCursor](https://reactbits.dev/animations/blob-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/BlobCursor/BlobCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/BlobCursor/BlobCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/BlobCursor/BlobCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| material | 'chrome' \| 'jelly' \| 'pearl' \| 'ink' | 'chrome' | chrome |
| color | string | '#3B82F6' | #3B82F6 |
| blend | 'normal' \| 'difference' \| 'exclusion' \| 'multiply' \| 'screen' \| 'overlay' | 'normal' | normal |
| size | number | 140 | 140 |
| morph | number | 0 | 0 |
| morphSpeed | number | 0.4 | 0.4 |
| depth | number | 1 | 1 |
| trail | number | 16 | 16 |
| lag | number | 0.55 | 0.55 |
| goo | number | 1 | 1 |
| stretch | number | 0.6 | 0.6 |
| wobble | number | 1 | 1 |
| drip | number | 0 | 0 |
| shine | number | 1 | 1 |
| splash | boolean | true | true |
| splashCount | number | 6 | 6 |
| splashSpeed | number | 0.5 | 0.5 |
| splashSize | number | 0.5 | 0.5 |
| splashGravity | number | 0 | 0 |
| regrow | number | 0.5 | 0.5 |
| shadow | boolean | false | false |
| hideCursor | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, three, three/examples/jsm/environments/RoomEnvironment.js

## Interaction locations

- [pointermove, line 819](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L819)
- [pointerdown, line 820](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L820)
- [pointerup, line 821](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L821)
- [pointercancel, line 822](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L822)
- [pointerout, line 823](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L823)
- [blur, line 824](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L824)

## Motion locations

- [velocity, line 302](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.jsx#L302): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/BlobCursor/BlobCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
