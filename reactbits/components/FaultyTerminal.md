# FaultyTerminal

Category: Backgrounds. Public entry: [FaultyTerminal](https://reactbits.dev/backgrounds/faulty-terminal).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/FaultyTerminal/FaultyTerminal.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/FaultyTerminal/FaultyTerminal.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/FaultyTerminal/FaultyTerminal.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| tint | string | '#ffffff' | #ffffff |
| glyphs | 'blocks' \| 'dots' \| 'characters' | 'blocks' | blocks |
| scale | number | 1 | 1 |
| gridMul | [number, number] | [2, 1] | — |
| digitSize | number | 1.5 | 1.5 |
| timeScale | number | 0.3 | 0.3 |
| brightness | number | 1 | 1 |
| glow | number | 0.5 | 0.5 |
| persistence | number | 0.5 | 0.5 |
| mouseReact | boolean | true | true |
| mouseStrength | number | 0.2 | 0.2 |
| mouseGlow | number | 0.6 | 0.6 |
| scramble | number | 0.5 | 0.5 |
| clickEffect | 'glitch' \| 'degauss' \| 'none' | 'glitch' | glitch |
| scanlineIntensity | number | 0.3 | 0.3 |
| glitchAmount | number | 1 | 1 |
| flickerAmount | number | 1 | 1 |
| noiseAmp | number | 1 | 1 |
| chromaticAberration | number | 0 | 0 |
| curvature | number | 0.2 | 0.2 |
| vignette | number | 0.25 | 0.25 |
| dither | number \| boolean | 0 | 0 |
| pageLoadAnimation | boolean | true | true |
| pause | boolean | false | false |
| variation | number | random | — |
| lightMode | boolean | false | false |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 828](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.jsx#L828)
- [pointerdown, line 829](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.jsx#L829)
- [pointerleave, line 830](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.jsx#L830)
- [visibilitychange, line 831](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.jsx#L831)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/FaultyTerminal/FaultyTerminal.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
