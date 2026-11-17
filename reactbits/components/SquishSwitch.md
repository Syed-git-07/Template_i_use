# SquishSwitch

Category: Micro. Public entry: [SquishSwitch](https://reactbits.dev/micro/squish-switch).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SquishSwitch/SquishSwitch.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SquishSwitch/SquishSwitch.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SquishSwitch/SquishSwitch.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| checked | boolean | undefined | — |
| defaultChecked | boolean | false | false |
| onChange | (checked: boolean) => void | - | — |
| label | string | "" |  |
| disabled | boolean | false | false |
| trackColor | string | "#27272a" | #27272a |
| trackOnColor | string | "#f5f5f5" | #f5f5f5 |
| thumbColor | string | "" |  |
| thumbOnColor | string | "" |  |
| width | number | 76 | 76 |
| height | number | 38 | 38 |
| radius | number | 19 | 19 |
| speed | number | 50 | 50 |
| stretch | number | 36 | 36 |
| hoverScale | number | 1.035 | 1.035 |
| colorDuration | number | 320 | 320 |
| ariaLabel | string | - | — |
| className | string | "" |  |
| id | string | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onPointerDown, line 174](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L174)
- [onPointerMove, line 175](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L175)
- [onPointerUp, line 176](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L176)
- [onPointerCancel, line 177](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L177)
- [onPointerEnter, line 178](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L178)
- [onPointerLeave, line 181](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L181)
- [onKeyDown, line 182](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L182)
- [onClick, line 186](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L186)

## Motion locations

- [stiffness, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L9): 320
- [damping, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L9): 40
- [mass, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L9): 0.6
- [stiffness, line 10](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L10): 520
- [damping, line 10](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L10): 34
- [mass, line 10](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L10): 0.6
- [stiffness, line 81](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L81): computed; read the linked expression
- [damping, line 82](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L82): 21.5
- [mass, line 83](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L83): 0.9
- [restDelta, line 84](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L84): 0.001
- [restSpeed, line 85](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.jsx#L85): 0.01

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SquishSwitch/SquishSwitch.css); motion-related lines: 57, 72, 85, 88.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
