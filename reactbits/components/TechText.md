# TechText

Category: TextAnimations. Public entry: [TechText](https://reactbits.dev/text-animations/tech-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TechText/TechText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TechText/TechText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TechText/TechText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | 'React Bits' | React Bits |
| fontFamily | string | '' |  |
| fontWeight | number | 600 | 600 |
| fontSize | number | 150 | 150 |
| letterSpacing | number | -0.05 | -0.05 |
| align | 'left' \| 'center' \| 'right' | 'center' | center |
| color | string | 'currentColor' | currentColor |
| accentColor | string | 'currentColor' | currentColor |
| reveal | 'area' \| 'letter' \| 'off' | 'letter' | letter |
| reach | number | 200 | 200 |
| softness | number | 0.7 | 0.7 |
| dashLength | number | 4 | 4 |
| dashGap | number | 2 | 2 |
| lineStyle | 'dashed' \| 'solid' | 'dashed' | dashed |
| strokeWidth | number | 1.5 | 1.5 |
| specks | number | 15 | 15 |
| selection | boolean | true | true |
| labels | boolean | true | true |
| draggable | boolean | true | true |
| bounce | number | 0.4 | 0.4 |
| clickKick | boolean | true | true |
| intro | 'none' \| 'type' \| 'assemble' \| 'metrics' | 'none' | none |
| introDuration | number | 2 | 2 |
| guides | boolean | false | false |
| sweep | boolean | true | true |
| speed | number | 1 | 1 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 951](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L951)
- [pointerenter, line 952](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L952)
- [pointerdown, line 953](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L953)
- [pointerup, line 954](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L954)
- [pointercancel, line 955](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L955)
- [pointerleave, line 956](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L956)
- [resize, line 960](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L960)
- [change, line 971](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L971)

## Motion locations

- [velocity, line 298](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L298): computed; read the linked expression
- [velocity, line 672](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.jsx#L672): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TechText/TechText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
