# RubberSegment

Category: Micro. Public entry: [RubberSegment](https://reactbits.dev/micro/rubber-segment).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/RubberSegment/RubberSegment.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/RubberSegment/RubberSegment.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/RubberSegment/RubberSegment.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | (string \| { value: string; label: ReactNode; icon?: ReactNode })[] | - | — |
| value | string | undefined | — |
| defaultValue | string | undefined | — |
| onChange | (value: string, index: number) => void | - | — |
| trackColor | string | "#27272a" | #27272a |
| thumbColor | string | "#fafafa" | #fafafa |
| textColor | string | "#fafafa" | #fafafa |
| activeTextColor | string | "#18181b" | #18181b |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 10 | 10 |
| inset | number | 3 | 3 |
| equalSlots | boolean | true | true |
| stretch | number | 100 | 100 |
| squash | number | 3 | 3 |
| speed | number | 1 | 1 |
| glide | number | 75 | 75 |
| draggable | boolean | true | true |
| disabled | boolean | false | false |
| className | string | "" |  |
| aria-label | string | "Segmented control" | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onPointerMove, line 326](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L326)
- [onPointerUp, line 327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L327)
- [onPointerCancel, line 328](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L328)
- [onLostPointerCapture, line 329](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L329)
- [onPointerDown, line 343](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L343)
- [onKeyDown, line 344](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L344)

## Motion locations

- [duration, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L9): 0.3
- [bounce, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L9): 0
- [duration, line 10](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L10): 0.4
- [bounce, line 10](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L10): 0.2
- [duration, line 11](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L11): 0.16
- [bounce, line 11](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L11): 0
- [duration, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L162): computed; read the linked expression
- [velocity, line 163](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L163): computed; read the linked expression
- [duration, line 167](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L167): computed; read the linked expression
- [velocity, line 167](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L167): computed; read the linked expression
- [duration, line 170](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L170): computed; read the linked expression
- [velocity, line 170](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L170): computed; read the linked expression
- [duration, line 171](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L171): computed; read the linked expression
- [duration, line 187](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L187): computed; read the linked expression
- [ease, line 187](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.jsx#L187): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RubberSegment/RubberSegment.css); motion-related lines: 63, 117, 119.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
