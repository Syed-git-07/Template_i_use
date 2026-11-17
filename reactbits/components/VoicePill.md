# VoicePill

Category: Micro. Public entry: [VoicePill](https://reactbits.dev/micro/voice-pill).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/VoicePill/VoicePill.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/VoicePill/VoicePill.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/VoicePill/VoicePill.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| accentColor | string | "#f5f5f5" | #f5f5f5 |
| iconColor | string | "#a1a1aa" | #a1a1aa |
| background | string | "#27272a" | #27272a |
| size | number | 28 | 28 |
| shape | 'pill' \| 'rounded' | 'pill' | pill |
| reach | number | 8 | 8 |
| showTime | boolean | true | true |
| waveform | boolean | true | true |
| slideToCancel | boolean | true | true |
| cancelDistance | number | 64 | 64 |
| attack | number | 40 | 40 |
| release | number | 240 | 240 |
| sensitivity | number | 1 | 1 |
| floor | number | 0.1 | 0.1 |
| openDuration | number | 200 | 200 |
| pressScale | number | 0.95 | 0.95 |
| mode | 'auto' \| 'hold' \| 'toggle' | 'auto' | auto |
| holdAfter | number | 300 | 300 |
| reactive | 'simulated' \| 'mic' | 'simulated' | simulated |
| disabled | boolean | false | false |
| ariaLabel | string | "Dictate" | Dictate |
| onStart | ({ source }) => void | - | — |
| onStop | ({ reason, duration }) => void | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [blur, line 327](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L327)
- [visibilitychange, line 328](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L328)
- [onPointerDown, line 368](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L368)
- [onPointerMove, line 369](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L369)
- [onPointerUp, line 370](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L370)
- [onPointerCancel, line 371](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L371)
- [onLostPointerCapture, line 372](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L372)
- [onKeyDown, line 373](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L373)
- [onClick, line 374](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L374)
- [onContextMenu, line 375](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L375)

## Motion locations

- [duration, line 241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.jsx#L241): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/VoicePill/VoicePill.css); motion-related lines: 41, 74, 107, 128, 160, 170, 175, 210, 213, 216, 220, 226, 233.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, pointer_cancel, visibility, cleanup, frame_loop, microphone.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
