# GlassIcons

Category: Components. Public entry: [GlassIcons](https://reactbits.dev/components/glass-icons).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/GlassIcons/GlassIcons.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/GlassIcons/GlassIcons.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/GlassIcons/GlassIcons.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | GlassIconsItem[] | [] | — |
| size | number | 82 | 82 |
| gap | number | 66 | 66 |
| columns | number | 3 | 3 |
| roundness | number | 0.6 | 0.6 |
| refraction | number | 0.8 | 0.8 |
| bevel | number | 0.6 | 0.6 |
| dispersion | number | 0 | 0 |
| frost | number | 0.2 | 0.2 |
| shine | number | 0.85 | 0.85 |
| tint | string | '#dfdfdf' | #dfdfdf |
| tintOpacity | number | 0.2 | 0.2 |
| iconColor | string | - | — |
| plate | 'tilt' \| 'offset' \| 'circle' \| 'none' | 'tilt' | tilt |
| tilt | number | 30 | 30 |
| spread | number | 0.5 | 0.5 |
| hover | 'lift' \| 'float' \| 'press' \| 'none' | 'press' | press |
| parallax | number | 1 | 1 |
| labels | 'hover' \| 'always' \| 'none' | 'hover' | hover |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 779](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L779)
- [onClick, line 949](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L949)
- [onPointerEnter, line 950](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L950)
- [onPointerMove, line 953](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L953)
- [onPointerLeave, line 954](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L954)
- [onPointerDown, line 955](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L955)
- [onPointerUp, line 956](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L956)
- [onPointerCancel, line 957](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L957)
- [onFocus, line 958](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L958)
- [onBlur, line 961](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L961)

## Motion locations

- [threshold, line 763](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.jsx#L763): 0.15

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/GlassIcons/GlassIcons.css); motion-related lines: 140, 169, 171.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
