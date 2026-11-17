# FlowingMenu

Category: Components. Public entry: [FlowingMenu](https://reactbits.dev/components/flowing-menu).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/FlowingMenu/FlowingMenu.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/FlowingMenu/FlowingMenu.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/FlowingMenu/FlowingMenu.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ text, link?, image?, marquee?, meta? }> | [] | — |
| speed | number | 60 | 60 |
| direction | 'left' \| 'right' \| 'alternate' | 'left' | left |
| followCursor | number | 0.4 | 0.4 |
| duration | number | 0.5 | 0.5 |
| stretch | number | 0.6 | 0.6 |
| magnet | number | 0.25 | 0.25 |
| bandInset | number | 0 | 0 |
| carryContent | boolean | false | false |
| bandRadius | number | 0 | 0 |
| textColor | string | '#ffffff' | #ffffff |
| bgColor | string | '#120F17' | #120F17 |
| marqueeBgColor | string | '#ffffff' | #ffffff |
| marqueeTextColor | string | '#120F17' | #120F17 |
| borderColor | string | 'rgba(255, 255, 255, 0.14)' | rgba(255, 255, 255, 0.14) |
| dividers | boolean | true | true |
| dimInactive | boolean | false | false |
| align | 'center' \| 'left' | 'center' | center |
| showIndex | boolean | false | false |
| showArrow | boolean | false | false |
| imageShape | 'pill' \| 'rounded' \| 'circle' | 'pill' | pill |
| intro | boolean | true | true |
| activeIndex | number | - | — |
| onItemClick | (item, index, event) => void | - | — |
| ariaLabel | string | 'Menu' | Menu |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerMove, line 551](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L551)
- [onPointerLeave, line 551](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L551)

## Motion locations

- [duration, line 98](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L98): computed; read the linked expression
- [duration, line 437](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L437): 900
- [delay, line 438](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L438): computed; read the linked expression
- [duration, line 445](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L445): 700
- [delay, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L446): computed; read the linked expression
- [duration, line 453](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L453): 1100
- [delay, line 454](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.jsx#L454): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/FlowingMenu/FlowingMenu.css); motion-related lines: 56.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
