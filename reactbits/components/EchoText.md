# EchoText

Category: TextAnimations. Public entry: [EchoText](https://reactbits.dev/text-animations/echo-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/EchoText/EchoText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/EchoText/EchoText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/EchoText/EchoText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Motion Echo" | Motion Echo |
| echoes | number | 12 | 12 |
| lag | number | 0.24 | 0.24 |
| offset | number | 36 | 36 |
| direction | "right" \| "left" \| "up" \| "down" \| "diagonal" | "right" | right |
| fade | number | 0.72 | 0.72 |
| blur | number | 3 | 3 |
| tint | string \| false | "#7dd3fc" | #7dd3fc |
| echoColors | [string, string] | undefined | — |
| echoStyle | "solid" \| "outline" | "solid" | solid |
| echoScale | number | 1 | 1 |
| mode | "entrance" \| "pointer" \| "both" | "both" | both |
| trail | "pointer" \| "auto" \| "scroll" | "pointer" | pointer |
| clickBurst | boolean | true | true |
| cursorRadius | number | 320 | 320 |
| duration | number | 900 | 900 |
| ease | "linear" \| "ease-out" \| "ease-in-out" \| "snappy" | "ease-out" | ease-out |
| fontSize | string \| number | "clamp(3rem, 9vw, 7rem)" | clamp(3rem, 9vw, 7rem) |
| fontWeight | string \| number | 800 | 800 |
| color | string | "currentColor" | currentColor |
| className | string | "" |  |
| style | CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 83](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx#L83)
- [pointermove, line 356](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx#L356)
- [pointerout, line 357](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx#L357)
- [scroll, line 363](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx#L363)
- [click, line 366](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.jsx#L366)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/EchoText/EchoText.css); motion-related lines: 44.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
