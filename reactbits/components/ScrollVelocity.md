# ScrollVelocity

Category: TextAnimations. Public entry: [ScrollVelocity](https://reactbits.dev/text-animations/scroll-velocity).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ScrollVelocity/ScrollVelocity.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ScrollVelocity/ScrollVelocity.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ScrollVelocity/ScrollVelocity.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| scrollContainerRef | React.RefObject<HTMLElement> | undefined | — |
| texts | React.ReactNode[] | [] | — |
| velocity | number | 100 | 100 |
| color | string | undefined | — |
| fontSize | number \| string | undefined | — |
| fontWeight | number \| string | undefined | — |
| skewWithVelocity | number | 0 | 0 |
| scaleWithVelocity | number | 0 | 0 |
| draggable | boolean | false | false |
| outlineAlternate | boolean | false | false |
| gap | number | 0 | 0 |
| className | string | "" |  |
| damping | number | 50 | 50 |
| stiffness | number | 400 | 400 |
| numCopies | number | 6 | 6 |
| separator | React.ReactNode | '' |  |
| fadeEdges | boolean | false | false |
| pauseOnHover | boolean | false | false |
| velocityMapping | { input: number[]; output: number[] } | { input: [0, 1000], output: [0, 5] } | — |
| parallaxClassName | string | "parallax" | parallax |
| scrollerClassName | string | "scroller" | scroller |
| parallaxStyle | React.CSSProperties | undefined | — |
| scrollerStyle | React.CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [resize, line 46](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L46)
- [onPointerDown, line 239](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L239)
- [onPointerMove, line 240](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L240)
- [onPointerUp, line 241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L241)
- [onPointerCancel, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L242)
- [onClickCapture, line 243](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L243)
- [onPointerEnter, line 282](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L282)
- [onPointerLeave, line 285](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L285)

## Motion locations

- [velocity, line 111](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.jsx#L111): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ScrollVelocity/ScrollVelocity.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
