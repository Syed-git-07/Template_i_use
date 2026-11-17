# FallingText

Category: TextAnimations. Public entry: [FallingText](https://reactbits.dev/text-animations/falling-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/FallingText/FallingText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/FallingText/FallingText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/FallingText/FallingText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | '' |  |
| highlightWords | string[] | [] | — |
| highlightClass | string | 'highlighted' | highlighted |
| trigger | 'auto' \| 'hover' \| 'click' \| 'scroll' | 'auto' | auto |
| variant | 'text' \| 'tiles' | 'text' | text |
| split | 'words' \| 'letters' | 'words' | words |
| order | 'random' \| 'sequence' \| 'center' \| 'together' | 'random' | random |
| stagger | number | 0.03 | 0.03 |
| gravity | number | 1 | 1 |
| bounciness | number | 0.2 | 0.2 |
| scatter | number | 0.5 | 0.5 |
| draggable | boolean | true | true |
| mouseConstraintStiffness | number | 0.2 | 0.2 |
| cursorPush | number | 0.5 | 0.5 |
| restoreDelay | number | 0 | 0 |
| fontSize | string | '1rem' | 1rem |
| accentColor | string | '#5b8cff' | #5b8cff |
| theme | 'dark' \| 'light' | 'dark' | dark |
| backgroundColor | string | 'transparent' | transparent |
| wireframes | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, matter-js

## Interaction locations

- [pointerenter, line 482](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L482)
- [pointerleave, line 483](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L483)
- [click, line 484](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L484)
- [pointerdown, line 485](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L485)
- [pointermove, line 486](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L486)
- [pointerup, line 487](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L487)
- [pointercancel, line 488](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L488)

## Motion locations

- [friction, line 224](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L224): 0.8
- [friction, line 225](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L225): 0.3
- [friction, line 226](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L226): 0.3
- [friction, line 227](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L227): 0.3
- [friction, line 244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L244): 0.4
- [duration, line 323](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L323): 760
- [delay, line 324](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L324): computed; read the linked expression
- [stiffness, line 389](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L389): computed; read the linked expression
- [damping, line 390](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L390): 0.08
- [threshold, line 470](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.jsx#L470): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/FallingText/FallingText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
