# BubbleMenu

Category: Components. Public entry: [BubbleMenu](https://reactbits.dev/components/bubble-menu).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/BubbleMenu/BubbleMenu.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/BubbleMenu/BubbleMenu.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/BubbleMenu/BubbleMenu.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| logo | ReactNode \| string | — | — |
| onMenuClick | (open: boolean) => void | — | — |
| className | string | — | — |
| style | CSSProperties | — | — |
| menuAriaLabel | string | "Toggle menu" | Toggle menu |
| menuBg | string | "#fff" | #fff |
| menuContentColor | string | "#111" | #111 |
| useFixedPosition | boolean | false | false |
| items | MenuItem[] | DEFAULT_ITEMS | — |
| animationEase | string | "back.out(1.5)" | back.out(1.5) |
| animationDuration | number | 0.5 | 0.5 |
| staggerDelay | number | 0.12 | 0.12 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [resize, line 150](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L150)
- [onClick, line 166](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L166)

## Motion locations

- [duration, line 98](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L98): computed; read the linked expression
- [ease, line 99](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L99): computed; read the linked expression
- [duration, line 107](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L107): computed; read the linked expression
- [ease, line 108](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L108): "power3.out"
- [duration, line 119](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L119): 0.2
- [ease, line 120](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L120): "power3.in"
- [duration, line 124](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L124): 0.2
- [ease, line 125](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.jsx#L125): "power3.in"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/BubbleMenu/BubbleMenu.css); motion-related lines: 96, 203.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
