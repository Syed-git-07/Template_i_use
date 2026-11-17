# FuzzyText

Category: TextAnimations. Public entry: [FuzzyText](https://reactbits.dev/text-animations/fuzzy-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/FuzzyText/FuzzyText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/FuzzyText/FuzzyText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/FuzzyText/FuzzyText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | React.ReactNode | - | — |
| fontSize | number \| string | 'clamp(2rem, 8vw, 8rem)' | clamp(2rem, 8vw, 8rem) |
| fontWeight | string \| number | 900 | 900 |
| fontFamily | string | 'inherit' | inherit |
| color | string | 'currentColor' | currentColor |
| colorSplit | number | 0 | 0 |
| trigger | 'hover' \| 'always' \| 'click' | 'hover' | hover |
| enableHover | boolean | true | true |
| baseIntensity | number | 0.18 | 0.18 |
| hoverIntensity | number | 0.5 | 0.5 |
| fuzzRange | number | 30 | 30 |
| sliceSize | number | 1 | 1 |
| fps | number | 60 | 60 |
| direction | 'horizontal' \| 'vertical' \| 'both' | 'horizontal' | horizontal |
| transitionDuration | number | 0 | 0 |
| intro | boolean | false | false |
| introDuration | number | 1400 | 1400 |
| clickEffect | boolean | false | false |
| glitchMode | boolean | false | false |
| glitchInterval | number | 2000 | 2000 |
| glitchDuration | number | 200 | 200 |
| gradient | string[] \| null | null | — |
| letterSpacing | number | 0 | 0 |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 459](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L459)
- [pointerdown, line 460](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L460)
- [pointerup, line 461](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L461)
- [pointerleave, line 462](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L462)
- [pointercancel, line 463](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L463)
- [click, line 464](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L464)
- [resize, line 465](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FuzzyText/FuzzyText.jsx#L465)

## Motion locations


## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
