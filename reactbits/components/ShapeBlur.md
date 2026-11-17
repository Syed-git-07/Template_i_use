# ShapeBlur

Category: Animations. Public entry: [ShapeBlur](https://reactbits.dev/animations/shape-blur).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ShapeBlur/ShapeBlur.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/ShapeBlur/ShapeBlur.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/ShapeBlur/ShapeBlur.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/ShapeBlur/ShapeBlur.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| shape | 'rect' \| 'circle' \| 'polygon' \| 'star' | 'rect' | rect |
| src | string | - | — |
| sides | number | 6 | 6 |
| size | number | 0.8 | 0.8 |
| roundness | number | 0.2 | 0.2 |
| thickness | number | 2 | 2 |
| fill | boolean | false | false |
| echoes | number | 1 | 1 |
| spacing | number | 12 | 12 |
| color | string | '#ffffff' | #ffffff |
| blur | number | 16 | 16 |
| lensSize | number | 0.3 | 0.3 |
| lensSoftness | number | 0.7 | 0.7 |
| focus | boolean | false | false |
| chroma | number | 0.3 | 0.3 |
| rotation | number | 0 | 0 |
| spin | number | 0 | 0 |
| idle | boolean | true | true |
| children | ReactNode | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 717](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ShapeBlur/ShapeBlur.jsx#L717)
- [pointerleave, line 718](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ShapeBlur/ShapeBlur.jsx#L718)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/ShapeBlur/ShapeBlur.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
