# Waves

Category: Backgrounds. Public entry: [Waves](https://reactbits.dev/backgrounds/waves).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Waves/Waves.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Waves/Waves.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Waves/Waves.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| lineColor | string | '#ffffff' | #ffffff |
| accentColor | string | lineColor | — |
| backgroundColor | string | 'transparent' | transparent |
| lineStyle | 'solid' \| 'dashed' | 'solid' | solid |
| spacing | number | 10 | 10 |
| lineWidth | number | 1 | 1 |
| rotation | number | 0 | 0 |
| amplitude | number | 32 | 32 |
| scale | number | 1 | 1 |
| twist | number | 1 | 1 |
| speed | number | 1 | 1 |
| variation | number | 0 | 0 |
| mouseInteraction | boolean | true | true |
| mouseRadius | number | 175 | 175 |
| mouseStrength | number | 1 | 1 |
| bounce | number | 0.5 | 0.5 |
| returnDuration | number | 1.4 | 1.4 |
| clickRipple | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0 | 0 |
| opacity | number | 1 | 1 |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 666](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L666)
- [pointerdown, line 667](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L667)
- [pointerup, line 668](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L668)
- [pointercancel, line 669](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L669)
- [pointerleave, line 670](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L670)
- [visibilitychange, line 671](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L671)

## Motion locations

- [bounce, line 274](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.jsx#L274): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Waves/Waves.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
