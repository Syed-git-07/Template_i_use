# LetterGlitch

Category: Backgrounds. Public entry: [LetterGlitch](https://reactbits.dev/backgrounds/letter-glitch).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/LetterGlitch/LetterGlitch.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/LetterGlitch/LetterGlitch.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/LetterGlitch/LetterGlitch.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| glitchColors | string[] | ['#ffffff', '#61dca3'] | — |
| baseColor | string | '#ffffff' | — |
| characters | string | 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&*()-_+=/[]{};:<>.,0123456789' | ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&*()-_+=/[]{};:<>.,0123456789 |
| fontFamily | string | 'ui-monospace, ...' | ui-monospace, 'SF Mono', 'JetBrains Mono', Menlo, Consolas, 'Liberation Mono', monospace |
| fontSize | number | 14 | 14 |
| spacing | number | 0.6 | 0.6 |
| density | number | 0.9 | 0.9 |
| baseOpacity | number | 0.16 | 0.16 |
| glitchAmount | number | 0.5 | 0.5 |
| speed | number | 1 | 1 |
| flow | number | 0.5 | 0.5 |
| smooth | boolean | true | true |
| interactive | boolean | true | true |
| cursorRadius | number | 140 | 140 |
| clickEffect | 'tear' \| 'burst' \| 'none' | 'tear' | tear |
| edgeFade | number | 0 | 0 |
| centerFade | number | 0 | 0 |
| intro | boolean | true | true |
| lightMode | boolean | false | false |
| backgroundColor | string | - | — |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 898](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L898)
- [pointerdown, line 899](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L899)
- [pointerup, line 900](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L900)
- [pointercancel, line 901](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L901)
- [pointerleave, line 902](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L902)
- [visibilitychange, line 903](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L903)
- [loadingdone, line 904](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.jsx#L904)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/LetterGlitch/LetterGlitch.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
