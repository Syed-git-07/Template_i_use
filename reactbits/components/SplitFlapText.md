# SplitFlapText

Category: TextAnimations. Public entry: [SplitFlapText](https://reactbits.dev/text-animations/split-flap-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitFlapText/SplitFlapText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/SplitFlapText/SplitFlapText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/SplitFlapText/SplitFlapText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/SplitFlapText/SplitFlapText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| words | string[] | ['LAUNCH READY', 'SYNC ONLINE', 'SIGNAL LIVE'] | — |
| text | string | undefined | — |
| flipDuration | number | 0.12 | 0.12 |
| stagger | number | 0.06 | 0.06 |
| cycleDelay | number | 2400 | 2400 |
| charset | "alpha" \| "alphanumeric" \| "numeric" \| string | "alphanumeric" | alphanumeric |
| flipsPerChar | number | 8 | 8 |
| align | "left" \| "center" \| "right" | "left" | left |
| tileColor | string | "#111827" | #111827 |
| textColor | string | "#f8fafc" | #f8fafc |
| tileRadius | number \| string | 8 | 8 |
| gap | number \| string | 6 | 6 |
| fontSize | number \| string | 52 | 52 |
| loop | boolean | true | true |
| padTo | number | 12 | 12 |
| intro | boolean | true | true |
| order | "left" \| "right" \| "center" \| "random" | "left" | left |
| tileStyle | "board" \| "minimal" | "board" | board |
| glare | number | 0 | 0 |
| depth | number | 0.5 | 0.5 |
| className | string | "" |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 84](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitFlapText/SplitFlapText.jsx#L84)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/SplitFlapText/SplitFlapText.css); motion-related lines: 148, 155, 165, 176, 191, 195, 226, 230, 233, 237, 247, 252, 261, 273, 276, 285, 302, 315, 354, 393, 398.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
