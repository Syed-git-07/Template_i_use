# ScrambledText

Category: TextAnimations. Public entry: [ScrambledText](https://reactbits.dev/text-animations/scrambled-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ScrambledText/ScrambledText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ScrambledText/ScrambledText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ScrambledText/ScrambledText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| effect | 'scramble' \| 'lift' \| 'blur' \| 'magnify' | 'scramble' | scramble |
| radius | number | 100 | 100 |
| strength | number | 1 | 1 |
| trail | number | 0.6 | 0.6 |
| duration | number | 1.2 | 1.2 |
| speed | number | 0.5 | 0.5 |
| clickBurst | boolean | true | true |
| scrambleChars | string | '.:' | .: |
| scrambleColor | string | '' |  |
| color | string | '' |  |
| fontFamily | string | '' |  |
| intro | boolean | true | true |
| className | string | '' |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap, gsap/SplitText, gsap/ScrambleTextPlugin

## Interaction locations

- [pointerenter, line 336](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L336)
- [pointermove, line 337](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L337)
- [pointerleave, line 338](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L338)
- [pointerdown, line 339](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L339)

## Motion locations

- [duration, line 101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L101): computed; read the linked expression
- [ease, line 102](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.jsx#L102): "none"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrambledText/ScrambledText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
