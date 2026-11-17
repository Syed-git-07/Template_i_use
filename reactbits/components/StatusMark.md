# StatusMark

Category: Micro. Public entry: [StatusMark](https://reactbits.dev/micro/status-mark).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/StatusMark/StatusMark.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/StatusMark/StatusMark.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/StatusMark/StatusMark.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| status | "pending" \| "running" \| "done" \| "failed" \| "cancelled" | "pending" | pending |
| progress | number | undefined | — |
| label | ReactNode | undefined | — |
| color | string | "currentColor" | currentColor |
| doneColor | string | "#22c55e" | #22c55e |
| errorColor | string | "#ef4444" | #ef4444 |
| size | number | 20 | 20 |
| strokeWidth | number | 2 | 2 |
| dashes | number | 8 | 8 |
| fontSize | number | 14 | 14 |
| spinDuration | number | 1100 | 1100 |
| arcLength | number | 0.68 | 0.68 |
| drawDuration | number | 240 | 240 |
| fillOpacity | number | 0.06 | 0.06 |
| strike | boolean | true | true |
| strikeDelay | number | 60 | 60 |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations


## Motion locations

- [duration, line 8](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L8): 0.3
- [bounce, line 8](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L8): 0
- [duration, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L9): 0.3
- [ease, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L9): computed; read the linked expression
- [duration, line 101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L101): computed; read the linked expression
- [ease, line 101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.jsx#L101): "linear"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/StatusMark/StatusMark.css); motion-related lines: 29, 46, 66, 85, 95, 106, 136, 141, 153, 159, 161, 167, 173.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
