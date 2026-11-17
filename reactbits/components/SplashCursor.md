# SplashCursor

Category: Animations. Public entry: [SplashCursor](https://reactbits.dev/animations/splash-cursor).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/SplashCursor/SplashCursor.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/SplashCursor/SplashCursor.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/SplashCursor/SplashCursor.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#4f8cff', '#2dd4bf', '#ffd166'] | — |
| rainbow | boolean | true | true |
| colorSpeed | number | 1 | 1 |
| intensity | number | 1 | 1 |
| size | number | 1 | 1 |
| force | number | 1 | 1 |
| swirl | number | 3 | 3 |
| trail | number | 1 | 1 |
| momentum | number | 1 | 1 |
| shading | number | 1 | 1 |
| glow | number | 0 | 0 |
| quality | 'low' \| 'medium' \| 'high' | 'high' | high |
| clickSplash | boolean | true | true |
| intro | boolean | true | true |
| contained | boolean | false | false |
| theme | 'dark' \| 'light' | 'dark' | dark |
| zIndex | number | 50 | 50 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 969](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L969)
- [pointerdown, line 970](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L970)
- [touchstart, line 971](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L971)
- [touchmove, line 972](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L972)
- [touchend, line 973](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L973)
- [touchcancel, line 974](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L974)
- [pointerleave, line 975](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L975)
- [webglcontextlost, line 976](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L976)
- [webglcontextrestored, line 977](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.jsx#L977)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/SplashCursor/SplashCursor.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
