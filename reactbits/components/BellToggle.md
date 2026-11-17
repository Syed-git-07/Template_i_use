# BellToggle

Category: Micro. Public entry: [BellToggle](https://reactbits.dev/micro/bell-toggle).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/BellToggle/BellToggle.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/BellToggle/BellToggle.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/BellToggle/BellToggle.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| offLabel | string | "Notify me" | Notify me |
| onLabel | string | "You'll be notified" | You'll be notified |
| icon | ReactNode | undefined | — |
| label | string | undefined | — |
| color | string | "#f5f5f5" | #f5f5f5 |
| background | string | "#27272a" | #27272a |
| onColor | string | "#18181b" | #18181b |
| onBackground | string | "#f5f5f5" | #f5f5f5 |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 22 | 22 |
| ringAmplitude | number | 17 | 17 |
| ringPasses | number | 5 | 5 |
| ringDecay | number | 1 | 1 |
| ringDuration | number | 820 | 820 |
| ringPivot | number | 16 | 16 |
| crossfadeMs | number | 200 | 200 |
| revealBounce | number | 0 | 0 |
| count | number | 0 | 0 |
| badge | boolean | true | true |
| badgeColor | string | "#ef4444" | #ef4444 |
| badgeTextColor | string | "#ffffff" | #ffffff |
| waves | boolean | true | true |
| clapper | boolean | false | false |
| pressed | boolean | undefined | — |
| defaultPressed | boolean | false | false |
| onChange | (pressed: boolean) => void | - | — |
| disabled | boolean | false | false |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerDown, line 194](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L194)
- [onPointerUp, line 195](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L195)
- [onPointerCancel, line 196](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L196)
- [onPointerLeave, line 197](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L197)
- [onKeyDown, line 198](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L198)
- [onClick, line 199](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L199)

## Motion locations

- [duration, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L9): 0.3
- [bounce, line 9](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L9): 0
- [duration, line 13](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L13): 420
- [delay, line 108](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L108): 70
- [duration, line 123](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L123): 380
- [delay, line 123](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L123): computed; read the linked expression
- [bounce, line 132](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.jsx#L132): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/BellToggle/BellToggle.css); motion-related lines: 26, 64, 165, 173, 182, 206, 217, 224, 229, 234.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
