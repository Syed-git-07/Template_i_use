# TrueFocus

Category: TextAnimations. Public entry: [TrueFocus](https://reactbits.dev/text-animations/true-focus).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TrueFocus/TrueFocus.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TrueFocus/TrueFocus.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TrueFocus/TrueFocus.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TrueFocus/TrueFocus.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| sentence | string | 'True Focus' | True Focus |
| separator | string | ' ' |   |
| focusStyle | 'brackets' \| 'box' \| 'underline' \| 'highlight' | 'brackets' | brackets |
| borderColor | string | 'green' | green |
| highlightColor | string | undefined | — |
| glowColor | string | 'transparent' | transparent |
| focusScale | number | 1 | 1 |
| blurAmount | number | 5 | 5 |
| unfocusedOpacity | number | 1 | 1 |
| easing | 'smooth' \| 'spring' | 'smooth' | smooth |
| order | 'sequential' \| 'random' | 'sequential' | sequential |
| manualMode | boolean | false | false |
| animationDuration | number | 0.5 | 0.5 |
| pauseBetweenAnimations | number | 1 | 1 |
| cornerSize | number | 16 | 16 |
| borderWidth | number | 3 | 3 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onMouseEnter, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TrueFocus/TrueFocus.jsx#L158)

## Motion locations

- [bounce, line 43](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TrueFocus/TrueFocus.jsx#L43): 0.38
- [ease, line 44](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TrueFocus/TrueFocus.jsx#L44): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TrueFocus/TrueFocus.css); motion-related lines: 17.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
