# SwipeRow

Category: Micro. Public entry: [SwipeRow](https://reactbits.dev/micro/swipe-row).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SwipeRow/SwipeRow.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SwipeRow/SwipeRow.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SwipeRow/SwipeRow.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| actions | SwipeAction[] | [{ id: "delete", label: "Delete" }] | — |
| actionColor | string | "#e5484d" | #e5484d |
| drawerColor | string | "#3f3f46" | #3f3f46 |
| rowColor | string | "#27272a" | #27272a |
| textColor | string | "#f5f5f5" | #f5f5f5 |
| height | number | 64 | 64 |
| radius | number | 16 | 16 |
| actionWidth | number | 80 | 80 |
| direction | "left" \| "right" | "left" | left |
| snapBounce | number | 0.2 | 0.2 |
| resistance | number | 0.55 | 0.55 |
| collapseMs | number | 200 | 200 |
| commitAt | number | 0.6 | 0.6 |
| fullSwipe | boolean | true | true |
| disabled | boolean | false | false |
| open | boolean | undefined | — |
| onOpenChange | (open: boolean) => void | - | — |
| onAction | (action: SwipeAction) => void | - | — |
| onCommit | (action: SwipeAction) => void | - | — |
| closeOnAction | boolean | true | true |
| haptic | boolean | true | true |
| label | string | "List item" | List item |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointermove, line 44](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L44)
- [pointerup, line 45](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L45)
- [pointercancel, line 46](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L46)
- [onClick, line 371](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L371)
- [onClick, line 390](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L390)
- [onPointerDown, line 402](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L402)
- [onKeyDown, line 411](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L411)
- [onClick, line 412](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L412)

## Motion locations

- [duration, line 15](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L15): 0.3
- [bounce, line 15](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L15): 0
- [duration, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L161): 0.2
- [ease, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L161): computed; read the linked expression
- [duration, line 169](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L169): 0.4
- [bounce, line 169](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L169): computed; read the linked expression
- [velocity, line 169](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L169): computed; read the linked expression
- [velocity, line 170](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L170): computed; read the linked expression
- [duration, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L202): 0.2
- [ease, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L202): computed; read the linked expression
- [velocity, line 209](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.jsx#L209): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SwipeRow/SwipeRow.css); motion-related lines: 18, 82, 98, 221.

## Observed source structure

Literal state assignments: setPhase → committing (line 184); setPhase → collapsing (line 188).

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
