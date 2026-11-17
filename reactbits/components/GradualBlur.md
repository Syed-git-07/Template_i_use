# GradualBlur

Category: Animations. Public entry: [GradualBlur](https://reactbits.dev/animations/gradual-blur).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/GradualBlur/GradualBlur.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/GradualBlur/GradualBlur.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/GradualBlur/GradualBlur.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| position | 'top' \| 'bottom' \| 'left' \| 'right' | 'bottom' | bottom |
| target | 'parent' \| 'page' | 'parent' | parent |
| height | string \| number | '6rem' | 6rem |
| width | string \| number | - | — |
| strength | number | 2 | 2 |
| layers | number | 8 | 8 |
| curve | 'linear' \| 'bezier' \| 'ease-in' \| 'ease-out' \| 'ease-in-out' | 'linear' | linear |
| exponential | boolean | true | true |
| opacity | number | 1 | 1 |
| saturation | number | 1 | 1 |
| tint | string | 'transparent' | transparent |
| autoHide | boolean | false | false |
| container | string \| HTMLElement \| RefObject | - | — |
| hoverIntensity | number | 1 | 1 |
| duration | number \| string | 0.3 | 0.3 |
| easing | string | 'ease-out' | ease-out |
| zIndex | number | 1000 | 1000 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [scroll, line 160](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.jsx#L160)
- [resize, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.jsx#L161)
- [pointermove, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.jsx#L202)
- [pointerleave, line 203](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.jsx#L203)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GradualBlur/GradualBlur.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
