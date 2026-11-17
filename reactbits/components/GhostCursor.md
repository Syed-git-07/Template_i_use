# GhostCursor

Category: Animations. Public entry: [GhostCursor](https://reactbits.dev/animations/ghost-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/GhostCursor/GhostCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/GhostCursor/GhostCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/GhostCursor/GhostCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#B497CF' | #B497CF |
| size | number | 80 | 80 |
| trailLength | number | 50 | 50 |
| inertia | number | 0.5 | 0.5 |
| turbulence | number | 0.5 | 0.5 |
| drift | number | 0.3 | 0.3 |
| detail | number | 1 | 1 |
| brightness | number | 1 | 1 |
| bloomStrength | number | 0.6 | 0.6 |
| bloomRadius | number | 1 | 1 |
| bloomThreshold | number | 0.025 | 0.025 |
| grainIntensity | number | 0.05 | 0.05 |
| edgeIntensity | number | 0 | 0 |
| clickPuff | boolean | true | true |
| intro | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| mixBlendMode | string | 'screen' (dark), 'normal' (light) | — |
| fadeDelayMs | number | 1000 (500 on touch) | — |
| fadeDurationMs | number | 1500 (1000 on touch) | — |
| maxDevicePixelRatio | number | 2 | 2 |
| targetPixels | number | 600000 (300000 on touch) | — |
| zIndex | number | 10 | 10 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 869](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L869)
- [pointerdown, line 870](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L870)
- [pointerleave, line 871](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L871)
- [webglcontextlost, line 880](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L880)
- [webglcontextrestored, line 881](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L881)
- [visibilitychange, line 899](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L899)

## Motion locations

- [threshold, line 415](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.jsx#L415): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GhostCursor/GhostCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, network, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
