# Ballpit

Category: Backgrounds. Public entry: [Ballpit](https://reactbits.dev/backgrounds/ballpit).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Ballpit/Ballpit.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Ballpit/Ballpit.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Ballpit/Ballpit.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| count | number | 200 | 200 |
| colors | Array<string \| number> | ['#ffffff'] | — |
| material | 'satin' \| 'matte' \| 'gloss' \| 'frosted' \| 'metal' | 'satin' | satin |
| minSize | number | 0.5 | 0.5 |
| maxSize | number | 1 | 1 |
| gravity | number | 0.5 | 0.5 |
| friction | number | 0.9975 | 0.9975 |
| wallBounce | number | 0.95 | 0.95 |
| bounce | number | 0.85 | 0.85 |
| depth | number | 2 | 2 |
| drift | number | 0 | 0 |
| followCursor | boolean | true | true |
| cursorSize | number | 1 | 1 |
| grab | boolean | true | true |
| clickEffect | 'burst' \| 'none' | 'burst' | burst |
| lightColor | string | '#ffffff' | #ffffff |
| lightIntensity | number | 1 | 1 |
| exposure | number | 1 | 1 |
| shadows | number | 0.6 | 0.6 |
| intro | boolean | true | true |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 1184](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1184)
- [pointerdown, line 1185](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1185)
- [pointerup, line 1186](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1186)
- [pointercancel, line 1187](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1187)
- [pointerleave, line 1188](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1188)
- [visibilitychange, line 1189](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1189)

## Motion locations

- [friction, line 275](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L275): computed; read the linked expression
- [bounce, line 277](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Ballpit/Ballpit.jsx#L277): computed; read the linked expression

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
