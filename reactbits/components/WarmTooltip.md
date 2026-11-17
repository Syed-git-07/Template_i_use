# WarmTooltip

Category: Micro. Public entry: [WarmTooltip](https://reactbits.dev/micro/warm-tooltip).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/WarmTooltip/WarmTooltip.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/WarmTooltip/WarmTooltip.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/WarmTooltip/WarmTooltip.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| content | ReactNode | - | — |
| shortcut | ReactNode | undefined | — |
| children | ReactElement | - | — |
| side | "top" \| "bottom" \| "left" \| "right" | "top" | top |
| delay | number | 400 | — |
| warmWindow | number | 300 | — |
| surfaceColor | string | "#f5f5f5" | #f5f5f5 |
| inkColor | string | "#18181b" | #18181b |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 8 | 8 |
| gap | number | 8 | 8 |
| arrow | boolean | true | true |
| popDuration | number | 160 | 160 |
| popScale | number | 0.94 | 0.94 |
| popBlur | number | 4 | 4 |
| showFuse | boolean | false | false |
| longPress | number | 500 | 500 |
| disabled | boolean | false | false |
| className | string | "" |  |
| WarmTooltipGroup | component | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, react-dom, motion/react

## Interaction locations

- [scroll, line 284](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L284)
- [resize, line 285](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L285)
- [visibilitychange, line 286](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L286)
- [pointerdown, line 455](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L455)

## Motion locations

- [stiffness, line 31](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L31): 260
- [damping, line 31](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L31): 22
- [mass, line 31](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L31): 0.4
- [duration, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L202): computed; read the linked expression
- [ease, line 202](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L202): computed; read the linked expression
- [duration, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L247): computed; read the linked expression
- [bounce, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L247): 0.1
- [duration, line 252](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L252): 0.12
- [ease, line 252](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L252): computed; read the linked expression
- [duration, line 261](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L261): computed; read the linked expression
- [ease, line 261](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L261): computed; read the linked expression
- [duration, line 340](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L340): computed; read the linked expression
- [ease, line 340](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.jsx#L340): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/WarmTooltip/WarmTooltip.css); motion-related lines: 30, 66.

## Observed source structure

Literal state assignments: setState → closed (line 161); setState → open (line 184); setState → closing (line 192); setFuse → idle (line 418); setFuse → arming (line 427); setFuse → idle (line 429); setFuse → idle (line 439); setFuse → arming (line 487); setFuse → idle (line 492).

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
