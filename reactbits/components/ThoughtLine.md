# ThoughtLine

Category: Micro. Public entry: [ThoughtLine](https://reactbits.dev/micro/thought-line).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/ThoughtLine/ThoughtLine.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/ThoughtLine/ThoughtLine.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/ThoughtLine/ThoughtLine.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | string | "Thinking…" | Thinking… |
| doneLabel | string | "" |  |
| renderLabel | (text, working) => ReactNode | - | — |
| glyph | 'sparkle' \| 'dot' \| 'none' \| ReactNode | 'sparkle' | sparkle |
| steps | string[] | [] | — |
| collapsible | boolean | true | true |
| collapseOnSettle | boolean | true | true |
| color | string | "currentColor" | currentColor |
| glyphColor | string | "" |  |
| fontSize | number | 16 | 16 |
| breathPeriod | number | 1.6 | 1.6 |
| breathDepth | number | 0.45 | 0.45 |
| shimmer | boolean | true | true |
| shimmerDuration | number | 1.8 | 1.8 |
| settleDuration | number | 350 | 350 |
| settleBlur | number | 2 | 2 |
| working | boolean | true | true |
| settleAfter | number | 0 | 0 |
| elapsed | number | undefined | — |
| showTimer | boolean | true | true |
| onSettle | (seconds) => void | - | — |
| className | string | "" |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onClick, line 232](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L232)

## Motion locations

- [duration, line 82](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L82): computed; read the linked expression
- [ease, line 82](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L82): computed; read the linked expression
- [duration, line 87](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L87): 0.2
- [ease, line 87](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L87): computed; read the linked expression
- [duration, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L89): 0.2
- [ease, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L89): computed; read the linked expression
- [duration, line 100](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L100): 0.2
- [ease, line 100](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L100): computed; read the linked expression
- [duration, line 101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L101): 0.2
- [ease, line 101](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L101): computed; read the linked expression
- [duration, line 104](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L104): computed; read the linked expression
- [ease, line 104](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L104): computed; read the linked expression
- [duration, line 105](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L105): computed; read the linked expression
- [ease, line 105](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.jsx#L105): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/ThoughtLine/ThoughtLine.css); motion-related lines: 77, 108, 111, 120, 133, 160, 190, 217, 220, 232, 239, 242, 246, 251, 255.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
