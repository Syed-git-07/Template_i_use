# PixelSnow

Category: Backgrounds. Public entry: [PixelSnow](https://reactbits.dev/backgrounds/pixel-snow).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PixelSnow/PixelSnow.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/PixelSnow/PixelSnow.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/PixelSnow/PixelSnow.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/PixelSnow/PixelSnow.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| color | string | '#ffffff' | #ffffff |
| variant | 'snowflake' \| 'square' \| 'round' | 'snowflake' | snowflake |
| density | number | 0.5 | 0.5 |
| speed | number | 1 | 1 |
| wind | number | 0.25 | 0.25 |
| sway | number | 0.5 | 0.5 |
| flakeSize | number | 1 | 1 |
| pixelSize | number | 3 | 3 |
| depth | number | 0.6 | 0.6 |
| brightness | number | 1 | 1 |
| glow | number | 0.8 | 0.8 |
| twinkle | number | 0.35 | 0.35 |
| accumulate | boolean | false | false |
| mouseInteraction | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0 | 0 |
| opacity | number | 1 | 1 |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 792](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PixelSnow/PixelSnow.jsx#L792)
- [pointerleave, line 793](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PixelSnow/PixelSnow.jsx#L793)
- [visibilitychange, line 794](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PixelSnow/PixelSnow.jsx#L794)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PixelSnow/PixelSnow.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
