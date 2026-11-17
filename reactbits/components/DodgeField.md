# DodgeField

Category: Micro. Public entry: [DodgeField](https://reactbits.dev/micro/dodge-field).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/DodgeField/DodgeField.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/DodgeField/DodgeField.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/DodgeField/DodgeField.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode \| (state) => ReactNode | undefined | — |
| taunts | string[] | ["Catch me", "Nope", "Too slow", "Almost", "Okay, okay"] | — |
| notice | string | "" |  |
| inkColor | string | "#f5f5f5" | #f5f5f5 |
| contrastColor | string | "#18181b" | #18181b |
| fieldHeight | number | 240 | 240 |
| reach | number | 72 | 72 |
| radius | number | 120 | 120 |
| falloff | number | 2 | 2 |
| fleeDuration | number | 130 | 130 |
| returnDuration | number | 620 | 620 |
| returnBounce | number | 0.1 | 0.1 |
| axis | "both" \| "x" \| "y" | "both" | both |
| wall | "clamp" \| "bounce" | "clamp" | clamp |
| patience | number | 4 | 4 |
| disabled | boolean | false | false |
| onDodge | (count: number) => void | - | — |
| onRelent | () => void | - | — |
| onCatch | () => void | - | — |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [change, line 147](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L147)
- [pointermove, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L161)
- [scroll, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L162)
- [pointerleave, line 163](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L163)
- [blur, line 164](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L164)
- [onClick, line 237](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L237)

## Motion locations

- [duration, line 135](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L135): computed; read the linked expression
- [bounce, line 135](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L135): 0
- [duration, line 136](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L136): computed; read the linked expression
- [bounce, line 136](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.jsx#L136): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/DodgeField/DodgeField.css); motion-related lines: 40, 77, 97, 99.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
