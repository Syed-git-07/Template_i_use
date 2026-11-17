# TextType

Category: TextAnimations. Public entry: [TextType](https://reactbits.dev/text-animations/text-type).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TextType/TextType.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TextType/TextType.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TextType/TextType.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string \| string[] | - | — |
| as | ElementType | div | div |
| prefix | string | '' |  |
| prefixColor | string | 'currentColor' | currentColor |
| typingSpeed | number | 50 | 50 |
| initialDelay | number | 0 | 0 |
| pauseDuration | number | 2000 | 2000 |
| deletingSpeed | number | 30 | 30 |
| deleteMode | 'backspace' \| 'select' | 'backspace' | backspace |
| typeEffect | 'none' \| 'fade' \| 'blur' \| 'rise' | 'none' | none |
| mistakes | number | 0 | 0 |
| variableSpeed | {min: number, max: number} | undefined | — |
| loop | boolean | true | true |
| showCursor | boolean | true | true |
| cursorStyle | 'character' \| 'bar' \| 'block' \| 'underscore' | 'character' | character |
| cursorCharacter | string \| React.ReactNode | \| | \| |
| cursorColor | string | 'currentColor' | currentColor |
| cursorBlinkDuration | number | 0.5 | 0.5 |
| cursorGlide | boolean | true | true |
| hideCursorWhileTyping | boolean | false | false |
| cursorClassName | string | '' |  |
| className | string | '' |  |
| textColors | string[] | [] | — |
| onSentenceComplete | (sentence: string, index: number) => void | undefined | — |
| startOnVisible | boolean | false | false |
| reverseMode | boolean | false | false |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [change, line 149](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L149)

## Motion locations

- [duration, line 51](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L51): 360
- [duration, line 58](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L58): 520
- [duration, line 65](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L65): 480
- [threshold, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L162): 0.1
- [duration, line 179](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L179): computed; read the linked expression
- [ease, line 179](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L179): "sine.inOut"
- [duration, line 180](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L180): computed; read the linked expression
- [ease, line 180](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L180): "sine.inOut"
- [duration, line 211](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L211): computed; read the linked expression
- [ease, line 211](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L211): "power3.out"
- [duration, line 219](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L219): 0.12
- [ease, line 219](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.jsx#L219): "power1.out"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextType/TextType.css); motion-related lines: 38.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
