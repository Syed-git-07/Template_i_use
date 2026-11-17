# FlyingButton

Category: Micro. Public entry: not present in the current public catalogue.

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/FlyingButton/FlyingButton.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/FlyingButton/FlyingButton.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/FlyingButton/FlyingButton.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | "Take off" | Take off |
| onClick | (event) => void | - | — |
| theme | "dark" \| "light" | "dark" | dark |
| size | "small" \| "medium" \| "large" \| "extra-large" | "medium" | medium |
| radius | number | undefined | — |
| altitude | number | 170 | 170 |
| hoverTime | number | 2.4 | 2.4 |
| jets | number | 2 | 2 |
| thrusters | boolean | true | true |
| trigger | "hover" \| "click" | "hover" | hover |
| carryCursor | boolean | true | true |
| smoke | number | 1 | 1 |
| turbulence | number | 1 | 1 |
| wobble | number | 1 | 1 |
| ramp | boolean | false | false |
| thrustColor | string | undefined | — |
| smokeColor | string | undefined | — |
| buttonColor | string | undefined | — |
| textColor | string | undefined | — |
| rampColor | string | undefined | — |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 1658](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1658)
- [pointerenter, line 1659](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1659)
- [pointerleave, line 1660](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1660)
- [pointerdown, line 1661](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1661)
- [pointerup, line 1662](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1662)
- [pointercancel, line 1663](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1663)
- [click, line 1664](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1664)
- [onClick, line 2117](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L2117)

## Motion locations

- [friction, line 568](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L568): 5
- [threshold, line 576](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L576): 0.035
- [delay, line 643](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L643): computed; read the linked expression
- [velocity, line 1800](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.jsx#L1800): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FlyingButton/FlyingButton.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
