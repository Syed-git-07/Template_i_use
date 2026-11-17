# GlowCursor

Category: Animations. Public entry: [GlowCursor](https://reactbits.dev/animations/glow-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/GlowCursor/GlowCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/GlowCursor/GlowCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/GlowCursor/GlowCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#5f8bff' | #5f8bff |
| secondaryColor | string | - | — |
| intensity | number | 1.3 | 1.3 |
| trailWidth | number | 3 | 3 |
| linger | number | 1.4 | 1.4 |
| glow | number | 1.2 | 1.2 |
| hotspot | number | 0.8 | 0.8 |
| followSpeed | number | 0.6 | 0.6 |
| grain | number | 0 | 0 |
| clickBurst | boolean | true | true |
| quality | 'low' \| 'medium' \| 'high' | 'high' | high |
| theme | 'dark' \| 'light' | 'dark' | dark |
| blendMode | string | auto | — |
| maxDevicePixelRatio | number | 2 | 2 |
| enabled | boolean | true | true |
| children | ReactNode | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 919](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx#L919)
- [pointerdown, line 920](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx#L920)
- [pointerleave, line 921](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx#L921)
- [visibilitychange, line 922](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx#L922)

## Motion locations

- [velocity, line 543](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.jsx#L543): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlowCursor/GlowCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
