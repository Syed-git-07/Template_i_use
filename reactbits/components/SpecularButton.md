# SpecularButton

Category: Components. Public entry: [SpecularButton](https://reactbits.dev/components/specular-button).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/SpecularButton/SpecularButton.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/SpecularButton/SpecularButton.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/SpecularButton/SpecularButton.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | 'Get Started' | Get Started |
| size | 'sm' \| 'md' \| 'lg' | 'lg' | lg |
| radius | number | 18 | 18 |
| tint | string | '#ffffff' | #ffffff |
| tintOpacity | number | 0.04 | 0.04 |
| blur | number | 0 | 0 |
| textColor | string | '#f5f5f5' | #f5f5f5 |
| lineColor | string | '#ffffff' | #ffffff |
| baseColor | string | '#525252' | #525252 |
| intensity | number | 1 | 1 |
| idleIntensity | number | 0.35 | 0.35 |
| shineSize | number | 10 | 10 |
| shineFade | number | 34 | 34 |
| thickness | number | 1.2 | 1.2 |
| glow | number | 1 | 1 |
| followMouse | boolean | true | true |
| proximity | number | 250 | 250 |
| autoAnimate | boolean | false | false |
| speed | number | 0.35 | 0.35 |
| disabled | boolean | false | false |
| onClick | MouseEventHandler | - | — |
| type | 'button' \| 'submit' \| 'reset' | 'button' | button |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 403](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L403)
- [pointerup, line 404](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L404)
- [pointercancel, line 405](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L405)
- [pointerleave, line 406](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L406)
- [pointerdown, line 407](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L407)
- [onClick, line 437](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.jsx#L437)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpecularButton/SpecularButton.css); motion-related lines: 29.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
