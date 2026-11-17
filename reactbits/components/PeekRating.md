# PeekRating

Category: Micro. Public entry: [PeekRating](https://reactbits.dev/micro/peek-rating).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/PeekRating/PeekRating.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/PeekRating/PeekRating.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/PeekRating/PeekRating.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | undefined | — |
| defaultValue | number | 0 | 0 |
| onChange | (value: number) => void | - | — |
| onPreview | (value: number \| null) => void | - | — |
| count | number | 5 | 5 |
| shape | "star" \| "heart" \| "bolt" | "star" | star |
| icon | ReactNode | undefined | — |
| labels | string[] | [] | — |
| activeColor | string | "#f5b400" | #f5b400 |
| idleColor | string | "#52525b" | #52525b |
| tipColor | string | "#27272a" | #27272a |
| tipTextColor | string | "#f5f5f5" | #f5f5f5 |
| size | number | 28 | 28 |
| lift | number | 6 | 6 |
| magnify | number | 1.15 | 1.15 |
| riseDuration | number | 320 | 320 |
| popScale | number | 1.3 | 1.3 |
| showTip | boolean | true | true |
| allowClear | boolean | true | true |
| readOnly | boolean | false | false |
| disabled | boolean | false | false |
| ariaLabel | string | "Rating" | Rating |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [visibilitychange, line 228](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L228)
- [blur, line 229](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L229)
- [onKeyDown, line 257](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L257)
- [onPointerEnter, line 262](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L262)
- [onPointerDown, line 263](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L263)
- [onPointerMove, line 264](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L264)
- [onPointerUp, line 265](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L265)
- [onPointerCancel, line 266](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L266)
- [onLostPointerCapture, line 267](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L267)
- [onPointerLeave, line 268](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L268)

## Motion locations

- [duration, line 130](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.jsx#L130): 300

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PeekRating/PeekRating.css); motion-related lines: 72, 80, 112, 124, 127, 129, 133.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
