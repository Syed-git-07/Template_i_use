# RotatingText

Category: TextAnimations. Public entry: [RotatingText](https://reactbits.dev/text-animations/rotating-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/RotatingText/RotatingText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/RotatingText/RotatingText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/RotatingText/RotatingText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| texts | string[] | [] | — |
| effect | 'slide' \| 'flip' \| 'blur' \| 'scale' \| 'drop' | "slide" | slide |
| direction | 'up' \| 'down' | "up" | up |
| highlight | boolean | false | false |
| highlightColor | string | "#a855f7" | #a855f7 |
| rotationInterval | number | 2000 | 2000 |
| blur | number | 0 | 0 |
| staggerDuration | number | 0 | 0 |
| staggerFrom | 'first' \| 'last' \| 'center' \| 'random' \| number | "first" | first |
| splitBy | 'characters' \| 'words' \| 'lines' \| string | "characters" | characters |
| loop | boolean | true | true |
| auto | boolean | true | true |
| pauseOnHover | boolean | false | false |
| initial | object | - | — |
| animate | object | - | — |
| exit | object | - | — |
| transition | object | - | — |
| animatePresenceMode | 'wait' \| 'sync' | "wait" | wait |
| animatePresenceInitial | boolean | false | false |
| onNext | (index: number) => void | undefined | — |
| mainClassName | string | '' | — |
| splitLevelClassName | string | '' | — |
| elementLevelClassName | string | '' | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onMouseEnter, line 319](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L319)
- [onMouseLeave, line 320](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L320)

## Motion locations

- [damping, line 39](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L39): 25
- [stiffness, line 39](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L39): 300
- [damping, line 40](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L40): 34
- [stiffness, line 40](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L40): 320
- [damping, line 48](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L48): 25
- [stiffness, line 48](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L48): 300
- [duration, line 54](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L54): 0.6
- [ease, line 54](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L54): computed; read the linked expression
- [duration, line 55](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L55): 0.32
- [ease, line 55](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L55): computed; read the linked expression
- [duration, line 61](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L61): 0.55
- [ease, line 61](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L61): computed; read the linked expression
- [damping, line 67](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L67): 17
- [stiffness, line 67](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L67): 240
- [damping, line 73](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L73): 18
- [stiffness, line 73](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L73): 320
- [mass, line 73](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L73): 0.9
- [duration, line 74](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L74): 0.3
- [ease, line 74](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.jsx#L74): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/RotatingText/RotatingText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
