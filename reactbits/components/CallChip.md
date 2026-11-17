# CallChip

Category: Micro. Public entry: [CallChip](https://reactbits.dev/micro/call-chip).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/CallChip/CallChip.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/CallChip/CallChip.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/CallChip/CallChip.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| icon | "terminal" \| "file" \| "search" \| "edit" \| ReactNode | "terminal" | terminal |
| name | string | "bash" | bash |
| argument | string | "npm test" | npm test |
| status | "idle" \| "running" \| "done" \| "error" | "running" | running |
| expectedMs | number | 2500 | 2500 |
| size | number | 34 | 34 |
| radius | number | 10 | 10 |
| color | string | "currentColor" | currentColor |
| surfaceColor | string | "#27272a" | #27272a |
| progressColor | string | "currentColor" | currentColor |
| progressOpacity | number | 0.08 | 0.08 |
| doneColor | string | "#22c55e" | #22c55e |
| errorColor | string | "#ef4444" | #ef4444 |
| washOpacity | number | 0.14 | 0.14 |
| shake | number | 6 | 6 |
| showTimer | boolean | true | true |
| onRetry | () => void | - | — |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onClick, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx#L202)
- [onPointerDown, line 203](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx#L203)
- [onPointerUp, line 204](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx#L204)
- [onPointerCancel, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx#L205)

## Motion locations

- [duration, line 86](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.jsx#L86): 450

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/CallChip/CallChip.css); motion-related lines: 34, 56, 62, 70, 75, 100, 108, 167, 170.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
