# PromptBar

Category: Micro. Public entry: [PromptBar](https://reactbits.dev/micro/prompt-bar).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/PromptBar/PromptBar.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/PromptBar/PromptBar.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/PromptBar/PromptBar.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| placeholder | string | "Ask anything" | Ask anything |
| sources | PromptBarSource[] | DEFAULT_SOURCES | — |
| commands | PromptBarCommand[] | DEFAULT_COMMANDS | — |
| models | PromptBarModel[] | DEFAULT_MODELS | — |
| efforts | string[] | DEFAULT_EFFORTS | — |
| defaultEffort | string | "" |  |
| onEffortChange | (effort) => void | - | — |
| defaultModel | string | "" |  |
| busy | boolean | false | false |
| onSend | (text, { attachments, model, effort }) => void | - | — |
| onStop | () => void | - | — |
| onAttach | () => string \| string[] \| Promise<string \| string[]> | - | — |
| onDictate | () => string \| Promise<string> | - | — |
| background | string | "#27272a" | #27272a |
| color | string | "#f5f5f5" | #f5f5f5 |
| menuBackground | string | "#323236" | #323236 |
| sparkColor | string | "#b39dff" | #b39dff |
| sparkBoost | number | 1 | 1 |
| width | number | 400 | 400 |
| radius | number | 16 | 16 |
| maxRows | number | 5 | 5 |
| morphDuration | number | 240 | 240 |
| squash | number | 0.12 | 0.12 |
| tilt | number | 8 | 8 |
| pressScale | number | 0.96 | 0.96 |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerdown, line 227](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L227)
- [onPointerDown, line 518](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L518)
- [onPointerMove, line 526](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L526)
- [onKeyDown, line 529](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L529)
- [onMouseDown, line 551](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L551)
- [onPointerEnter, line 552](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L552)
- [onClick, line 553](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L553)
- [onPointerDown, line 578](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L578)
- [onClick, line 581](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L581)
- [onClick, line 594](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L594)
- [onChange, line 610](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L610)
- [onFocus, line 618](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L618)
- [onKeyDown, line 619](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L619)
- [onMouseDown, line 629](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L629)
- [onClick, line 630](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L630)
- [onMouseDown, line 647](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L647)
- [onClick, line 648](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L648)
- [onMouseDown, line 668](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L668)
- [onClick, line 669](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L669)
- [onMouseDown, line 688](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L688)
- [onClick, line 689](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L689)
- [onMouseDown, line 709](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L709)
- [onPointerDown, line 710](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L710)
- [onPointerUp, line 711](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L711)
- [onPointerCancel, line 712](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L712)
- [onPointerLeave, line 713](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L713)
- [onClick, line 714](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L714)

## Motion locations

- [duration, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L89): 0
- [duration, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L89): computed; read the linked expression
- [ease, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.jsx#L89): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/PromptBar/PromptBar.css); motion-related lines: 34, 43, 58, 161, 193, 216, 284, 305, 387, 412, 439, 443, 447, 450, 471, 497, 500, 504, 509.

## Observed source structure

Literal state assignments: setDraft →  (line 409).

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
