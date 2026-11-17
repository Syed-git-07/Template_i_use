# RefineFrame

Category: Micro. Public entry: [RefineFrame](https://reactbits.dev/micro/refine-frame).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RefineFrame/RefineFrame.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/RefineFrame/RefineFrame.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/RefineFrame/RefineFrame.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/RefineFrame/RefineFrame.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| status | 'queued' \| 'generating' \| 'refining' \| 'complete' \| 'error' | 'generating' | generating |
| children | ReactNode | - | — |
| aspectRatio | string | "4 / 3" | 4 / 3 |
| width | number | 320 | 320 |
| radius | number | 16 | 16 |
| background | string | "#27272a" | #27272a |
| color | string | "#f5f5f5" | #f5f5f5 |
| stageDuration | number | 400 | 400 |
| sweep | boolean | true | true |
| showStatus | boolean | true | true |
| hideAfter | number | 1200 | 1200 |
| labels | Partial<Record<status, string>> | DEFAULT_LABELS | — |
| retryLabel | string | "Retry" | Retry |
| onRetry | () => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [change, line 206](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RefineFrame/RefineFrame.jsx#L206)
- [load, line 223](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RefineFrame/RefineFrame.jsx#L223)
- [onClick, line 289](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RefineFrame/RefineFrame.jsx#L289)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/RefineFrame/RefineFrame.css); motion-related lines: 35, 42, 45, 59, 84, 107, 112, 115, 141, 159, 166, 173, 176, 204, 236, 238, 242, 247, 251, 256.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
