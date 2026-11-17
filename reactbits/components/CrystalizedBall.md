# CrystalizedBall

Category: Animations. Public entry: [CrystalizedBall](https://reactbits.dev/animations/crystalized-ball).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/CrystalizedBall/CrystalizedBall.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/CrystalizedBall/CrystalizedBall.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/CrystalizedBall/CrystalizedBall.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| preset | 'plasma' \| 'aurora' \| 'nebula' \| 'ember' \| 'frost' \| 'solar' \| 'eclipse' \| 'abyss' | 'plasma' | plasma |
| color | string | from preset | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| size | number | 0.7 | 0.7 |
| strands | number | from preset | — |
| crackle | number | from preset | — |
| flares | number | from preset | — |
| glow | number | from preset | — |
| sparks | number | from preset | — |
| particleCount | number | from preset | — |
| fill | number | from preset | — |
| motion | 'rise' \| 'fall' \| 'drift' \| 'orbit' | from preset | — |
| particleShape | 'square' \| 'round' | from preset | — |
| depth | number | from preset | — |
| sway | number | from preset | — |
| twinkle | number | from preset | — |
| haze | number | from preset | — |
| speed | number | 1 | 1 |
| dustSpeed | number | from preset | — |
| interactive | boolean | true | true |
| hoverStrength | number | 0.7 | 0.7 |
| intro | boolean | true | true |
| paused | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 1424](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1424)
- [pointerdown, line 1425](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1425)
- [pointerout, line 1426](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1426)
- [pointerup, line 1427](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1427)
- [blur, line 1428](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1428)
- [visibilitychange, line 1429](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1429)

## Motion locations

- [velocity, line 1143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1143): 0
- [duration, line 1168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.jsx#L1168): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/CrystalizedBall/CrystalizedBall.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
