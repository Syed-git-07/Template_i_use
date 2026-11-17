# MicroSlats

Category: Backgrounds. Public entry: [MicroSlats](https://reactbits.dev/backgrounds/micro-slats).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/MicroSlats/MicroSlats.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/MicroSlats/MicroSlats.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/MicroSlats/MicroSlats.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| preset | 'swell' \| 'tide' \| 'storm' \| 'signal' | 'swell' | swell |
| color | string | '#A855F7' | #A855F7 |
| glintColor | string | '#ffffff' | #ffffff |
| backgroundColor | string | '#000000' | #000000 |
| slatWidth | number | 10 | 10 |
| slatHeight | number | 25 | 25 |
| gap | number | 3 | 3 |
| roundness | number | 0.75 | 0.75 |
| scale | number | from preset | — |
| speed | number | from preset | — |
| direction | number | from preset | — |
| chop | number | from preset | — |
| stretch | number | from preset | — |
| glint | number | from preset | — |
| contrast | number | from preset | — |
| perspective | number | from preset | — |
| fog | number | from preset | — |
| interactive | boolean | true | true |
| cursorStrength | number | 1 | 1 |
| cursorSize | number | 40 | 40 |
| swirl | number | 0 | 0 |
| trail | number | 1.4 | 1.4 |
| lean | number | 0 | 0 |
| intro | boolean | true | true |
| introDuration | number | 1.5 | 1.5 |
| paused | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 889](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L889)
- [pointerdown, line 890](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L890)
- [pointerout, line 891](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L891)
- [blur, line 892](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L892)
- [visibilitychange, line 893](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L893)

## Motion locations

- [velocity, line 620](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.jsx#L620): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/MicroSlats/MicroSlats.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
