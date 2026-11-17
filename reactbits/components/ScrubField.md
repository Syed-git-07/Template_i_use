# ScrubField

Category: Micro. Public entry: [ScrubField](https://reactbits.dev/micro/scrub-field).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/ScrubField/ScrubField.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/ScrubField/ScrubField.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/ScrubField/ScrubField.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | string | "Radius" | Radius |
| suffix | string | "px" | px |
| value | number | undefined | — |
| defaultValue | number | 24 | 24 |
| min | number | 0 | 0 |
| max | number | 100 | 100 |
| step | number | 1 | 1 |
| size | "sm" \| "md" \| "lg" | "md" | md |
| sensitivity | number | 2 | 2 |
| rubberReach | number | 8 | 8 |
| returnDuration | number | 300 | 300 |
| coarseMultiplier | number | 10 | 10 |
| fineMultiplier | number | 0.1 | 0.1 |
| showDelta | boolean | true | true |
| showDirty | boolean | false | false |
| showFill | boolean | true | true |
| accent | string | "#f5f5f5" | #f5f5f5 |
| chipColor | string | "#27272a" | #27272a |
| disabled | boolean | false | false |
| onChange | (value: number) => void | - | — |
| onCommit | (value: number) => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [keydown, line 168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L168)
- [onPointerDown, line 294](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L294)
- [onPointerMove, line 295](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L295)
- [onPointerUp, line 296](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L296)
- [onPointerCancel, line 297](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L297)
- [onLostPointerCapture, line 298](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L298)
- [onClick, line 318](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L318)
- [onFocus, line 337](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L337)
- [onChange, line 338](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L338)
- [onKeyDown, line 339](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L339)
- [onBlur, line 340](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L340)

## Motion locations

- [duration, line 16](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L16): 0.3
- [bounce, line 16](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L16): 0
- [duration, line 220](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.jsx#L220): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ScrubField/ScrubField.css); motion-related lines: 31, 38, 77, 109, 143, 153, 156, 161.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
