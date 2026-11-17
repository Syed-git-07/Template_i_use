# FuseButton

Category: Micro. Public entry: [FuseButton](https://reactbits.dev/micro/fuse-button).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/FuseButton/FuseButton.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/FuseButton/FuseButton.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/FuseButton/FuseButton.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | string | "Archive" | Archive |
| undoLabel | string | "Undo" | Undo |
| doneLabel | string | "Archived" | Archived |
| icon | ReactNode | undefined | — |
| color | string | "#f5f5f5" | #f5f5f5 |
| background | string | "#27272a" | #27272a |
| fuseColor | string | "#f5a524" | #f5a524 |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 22 | 22 |
| undoWindow | number | 4000 | 4000 |
| fuse | "outline" \| "bottom" \| "top" | "outline" | outline |
| fuseThickness | number | 1.5 | 1.5 |
| crossfadeMs | number | 200 | 200 |
| commitOn | "press" \| "fuseEnd" | "press" | press |
| pauseOnHover | boolean | true | true |
| settle | "reset" \| "stay" | "reset" | reset |
| disabled | boolean | false | false |
| onCommit | (reason: "press" \| "fuseEnd") => void | - | — |
| onUndo | () => void | - | — |
| onFuseEnd | () => void | - | — |
| onPhaseChange | (phase: "idle" \| "armed" \| "settled") => void | - | — |
| type | "button" \| "submit" \| "reset" | "button" | button |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [visibilitychange, line 128](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L128)
- [onPointerDown, line 204](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L204)
- [onPointerUp, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L205)
- [onPointerCancel, line 206](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L206)
- [onPointerEnter, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L207)
- [onPointerLeave, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L208)
- [onKeyDown, line 209](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L209)
- [onClick, line 217](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L217)
- [onClick, line 231](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L231)

## Motion locations

- [duration, line 80](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.jsx#L80): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/FuseButton/FuseButton.css); motion-related lines: 35, 82, 95, 99, 124, 157, 165, 200, 207, 214.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, pointer_cancel, visibility, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
