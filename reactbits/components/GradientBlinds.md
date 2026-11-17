# GradientBlinds

Category: Backgrounds. Public entry: [GradientBlinds](https://reactbits.dev/backgrounds/gradient-blinds).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/GradientBlinds/GradientBlinds.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/GradientBlinds/GradientBlinds.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/GradientBlinds/GradientBlinds.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| gradientColors | string[] | ['#FF9FFC', '#5227FF'] | — |
| angle | number | 0 | 0 |
| blindCount | number | 16 | 16 |
| blindMinWidth | number | 60 | 60 |
| shineDirection | 'left' \| 'right' | 'left' | left |
| lightColor | string | '#ffffff' | #ffffff |
| spotlightRadius | number | 0.5 | 0.5 |
| spotlightSoftness | number | 1 | 1 |
| spotlightOpacity | number | 1 | 1 |
| shine | number | 0.4 | 0.4 |
| relief | number | 0.5 | 0.5 |
| glow | number | 0.4 | 0.4 |
| sway | number | 0.35 | 0.35 |
| speed | number | 1 | 1 |
| hoverTilt | number | 0.6 | 0.6 |
| clickEffect | 'ripple' \| 'none' | 'ripple' | ripple |
| idle | 'drift' \| 'center' \| 'stay' | 'drift' | drift |
| perspective | number | 0 | 0 |
| gradientSpeed | number | 0 | 0 |
| mirrorGradient | boolean | false | false |
| distortAmount | number | 0 | 0 |
| noise | number | 0.3 | 0.3 |
| mouseDampening | number | 0.15 | 0.15 |
| intro | boolean | true | true |
| paused | boolean | false | false |
| mixBlendMode | string | 'lighten' | lighten |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 550](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.jsx#L550)
- [pointerdown, line 551](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.jsx#L551)
- [pointerleave, line 552](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.jsx#L552)
- [visibilitychange, line 553](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.jsx#L553)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/GradientBlinds/GradientBlinds.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
