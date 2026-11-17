# CodeSlots

Category: Micro. Public entry: [CodeSlots](https://reactbits.dev/micro/code-slots).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/CodeSlots/CodeSlots.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/CodeSlots/CodeSlots.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/CodeSlots/CodeSlots.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| length | number | 6 | 6 |
| value | string | undefined | — |
| defaultValue | string | "" |  |
| onChange | (code: string) => void | - | — |
| onComplete | (code: string) => void | - | — |
| status | "idle" \| "error" \| "success" | "idle" | idle |
| mask | boolean | false | false |
| caret | boolean | true | true |
| disabled | boolean | false | false |
| autoFocus | boolean | false | false |
| accentColor | string | "#f5f5f5" | #f5f5f5 |
| inkColor | string | "#f5f5f5" | #f5f5f5 |
| slotColor | string | "#27272a" | #27272a |
| digitColor | string | "#18181b" | #18181b |
| dangerColor | string | "#ff3b30" | #ff3b30 |
| slotSize | number | 44 | 44 |
| gap | number | 8 | 8 |
| radius | number | 12 | 12 |
| bounce | number | 0.2 | 0.2 |
| settle | number | 0.3 | 0.3 |
| rise | number | 8 | 8 |
| cascade | number | 20 | 20 |
| ariaLabel | string | "One-time code" | One-time code |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onMouseDown, line 384](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L384)
- [onKeyDown, line 400](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L400)
- [onPaste, line 401](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L401)
- [onChange, line 402](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L402)
- [onFocus, line 403](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L403)
- [onBlur, line 404](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L404)

## Motion locations

- [duration, line 102](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L102): computed; read the linked expression
- [bounce, line 102](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L102): computed; read the linked expression
- [delay, line 102](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L102): computed; read the linked expression
- [duration, line 304](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L304): computed; read the linked expression
- [ease, line 304](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L304): computed; read the linked expression
- [duration, line 306](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L306): 0.3
- [bounce, line 306](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L306): 0
- [delay, line 306](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L306): computed; read the linked expression
- [duration, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L308): 0.35
- [bounce, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L308): computed; read the linked expression
- [delay, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L308): computed; read the linked expression
- [duration, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L319): 0.15
- [ease, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L319): computed; read the linked expression
- [duration, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L320): computed; read the linked expression
- [ease, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L320): computed; read the linked expression
- [delay, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L320): 0.06
- [duration, line 323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L323): 0.3
- [bounce, line 323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L323): 0
- [delay, line 323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.jsx#L323): 0.1

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CodeSlots/CodeSlots.css); motion-related lines: 24, 74, 85, 140, 143, 166, 170, 174, 179.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
