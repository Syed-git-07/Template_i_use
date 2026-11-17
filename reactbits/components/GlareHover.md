# GlareHover

Category: Animations. Public entry: [GlareHover](https://reactbits.dev/animations/glare-hover).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/GlareHover/GlareHover.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/GlareHover/GlareHover.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/GlareHover/GlareHover.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| mode | 'hover' \| 'follow' \| 'loop' \| 'click' | 'hover' | hover |
| variant | 'streak' \| 'twin' \| 'sheen' | 'streak' | streak |
| glareColor | string | '#ffffff' | #ffffff |
| glareOpacity | number | 0.5 | 0.5 |
| glareSize | number | 30 | 30 |
| softness | number | 0.6 | 0.6 |
| glareAngle | number | -45 | -45 |
| blendMode | string | 'screen' | screen |
| rimGlint | boolean | true | true |
| transitionDuration | number | 650 | 650 |
| interval | number | 3 | 3 |
| playOnce | boolean | false | false |
| intro | boolean | false | false |
| width | string | 'auto' | auto |
| height | string | 'auto' | auto |
| background | string | 'transparent' | transparent |
| borderRadius | string | '10px' | 10px |
| borderColor | string | 'transparent' | transparent |
| className | string | '' |  |
| style | CSSProperties | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 212](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L212)
- [pointermove, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L213)
- [pointerleave, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L214)
- [pointerdown, line 215](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L215)
- [focusin, line 216](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L216)

## Motion locations

- [velocity, line 73](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L73): 0
- [duration, line 151](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L151): computed; read the linked expression
- [threshold, line 229](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.jsx#L229): 0.4

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/GlareHover/GlareHover.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
