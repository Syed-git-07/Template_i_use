# Scanner

Category: Backgrounds. Public entry: [Scanner](https://reactbits.dev/backgrounds/scanner).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Scanner/Scanner.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Scanner/Scanner.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Scanner/Scanner.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color1 | string | '#5227FF' | #5227FF |
| color2 | string | '#FF9FFC' | #FF9FFC |
| color3 | string | '#FFFFFF' | #FFFFFF |
| speed | number | 0.5 | 0.5 |
| sweepSpeed | number | 0.25 | 0.25 |
| sweepWidth | number | 1.6 | 1.6 |
| trail | number | 0.5 | 0.5 |
| reverse | boolean | false | false |
| scale | number | 1.5 | 1.5 |
| frequency | number | 2 | 2 |
| ripple | number | 0.22 | 0.22 |
| bandDensity | number | 11 | 11 |
| lineWidth | number | 1.2 | 1.2 |
| glow | number | 0.6 | 0.6 |
| scanDirection | 'vertical' \| 'horizontal' \| 'diagonal' | 'vertical' | vertical |
| colorSpread | number | 0.7 | 0.7 |
| brightness | number | 1 | 1 |
| vignette | number | 0.3 | 0.3 |
| scanline | boolean | true | true |
| scanlineIntensity | number | 0.5 | 0.5 |
| grain | boolean | true | true |
| grainIntensity | number | 0.04 | 0.04 |
| opacity | number | 1 | 1 |
| mouseInteraction | boolean | true | true |
| mouseMode | 'repel' \| 'attract' | 'repel' | repel |
| mouseRadius | number | 0.5 | 0.5 |
| mouseStrength | number | 0.7 | 0.7 |
| clickEffect | 'ping' \| 'none' | 'ping' | ping |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 477](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.jsx#L477)
- [pointerdown, line 478](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.jsx#L478)
- [pointerleave, line 479](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.jsx#L479)
- [visibilitychange, line 480](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.jsx#L480)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Scanner/Scanner.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
