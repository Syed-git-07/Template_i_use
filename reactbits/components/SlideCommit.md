# SlideCommit

Category: Micro. Public entry: [SlideCommit](https://reactbits.dev/micro/slide-commit).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SlideCommit/SlideCommit.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SlideCommit/SlideCommit.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SlideCommit/SlideCommit.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | ReactNode | "Slide to pay" | Slide to pay |
| doneLabel | ReactNode | "Paid" | Paid |
| errorLabel | ReactNode | "Payment failed" | Payment failed |
| onConfirm | () => void \| Promise<unknown> | - | — |
| onDone | () => void | - | — |
| onError | (reason: unknown) => void | - | — |
| trackColor | string | "#262626" | #262626 |
| handleColor | string | "#f5f5f5" | #f5f5f5 |
| successColor | string | "#22c55e" | #22c55e |
| dangerColor | string | "#e5484d" | #e5484d |
| width | number | 280 | 280 |
| height | number | 56 | 56 |
| radius | number | 28 | 28 |
| speed | number | 50 | 50 |
| returnBounce | number | 0.38 | 0.38 |
| landingDip | number | 0.026 | 0.026 |
| holdMs | number | 1500 | 1500 |
| disabled | boolean | false | false |
| icon | ReactNode | undefined | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointermove, line 224](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L224)
- [pointerup, line 225](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L225)
- [pointercancel, line 226](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L226)
- [onPointerDown, line 315](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L315)
- [onPointerEnter, line 333](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L333)
- [onPointerLeave, line 336](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L336)
- [onKeyDown, line 337](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L337)

## Motion locations

- [stiffness, line 88](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L88): computed; read the linked expression
- [damping, line 88](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L88): computed; read the linked expression
- [damping, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L89): computed; read the linked expression
- [duration, line 137](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L137): 0.2
- [ease, line 137](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L137): computed; read the linked expression
- [velocity, line 138](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L138): computed; read the linked expression
- [duration, line 143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L143): 0.2
- [delay, line 143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L143): 0.12
- [duration, line 145](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L145): 0.3
- [bounce, line 145](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L145): 0
- [duration, line 151](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L151): 0.12
- [duration, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L156): 0.46
- [ease, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L156): computed; read the linked expression
- [delay, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L156): 0.1
- [duration, line 166](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L166): 0.12
- [duration, line 167](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L167): 0.2
- [delay, line 167](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L167): 0.12
- [duration, line 170](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L170): 0.45
- [ease, line 170](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L170): computed; read the linked expression
- [duration, line 191](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L191): 0.12
- [duration, line 196](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L196): 0.2
- [duration, line 197](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L197): 0.2
- [duration, line 351](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L351): 0.2
- [ease, line 351](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.jsx#L351): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SlideCommit/SlideCommit.css); motion-related lines: 64, 94, 143, 155, 156, 160, 163, 181, 183, 184, 188, 191.

## Observed source structure

Literal state assignments: setPhase → idle (line 142); setPhase → done (line 149); setPhase → error (line 164); setPhase → idle (line 175); setPhase → pending (line 195).

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
