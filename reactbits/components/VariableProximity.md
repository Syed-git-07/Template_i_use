# VariableProximity

Category: TextAnimations. Public entry: [VariableProximity](https://reactbits.dev/text-animations/variable-proximity).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/VariableProximity/VariableProximity.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/VariableProximity/VariableProximity.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/VariableProximity/VariableProximity.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | string | "" |  |
| fromFontVariationSettings | string | 'wght' 400, 'opsz' 9 | 'wght' 400, 'opsz' 9 |
| toFontVariationSettings | string | 'wght' 1000, 'opsz' 40 | 'wght' 1000, 'opsz' 40 |
| containerRef | RefObject<HTMLElement> | undefined | — |
| radius | number | 50 | 50 |
| falloff | 'linear' \| 'exponential' \| 'gaussian' | "linear" | linear |
| smoothing | number | 0.2 | 0.2 |
| fromColor | string | undefined | — |
| toColor | string | undefined | — |
| scale | number | 1 | 1 |
| lift | number | 0 | 0 |
| idleWave | boolean | false | false |
| fontSize | number \| string | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [mousemove, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L319)
- [touchmove, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L320)
- [touchend, line 321](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L321)
- [touchcancel, line 322](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L322)
- [scroll, line 323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L323)
- [resize, line 324](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L324)
- [mouseleave, line 325](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L325)
- [onClick, line 375](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.jsx#L375)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/VariableProximity/VariableProximity.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
