# DecryptedText

Category: TextAnimations. Public entry: [DecryptedText](https://reactbits.dev/text-animations/decrypted-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DecryptedText/DecryptedText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/DecryptedText/DecryptedText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/DecryptedText/DecryptedText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/DecryptedText/DecryptedText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | - | — |
| effect | 'scramble' \| 'flip' \| 'fade' | 'scramble' | scramble |
| scrambleColor | string | '' |  |
| speed | number | 50 | 50 |
| maxIterations | number | 10 | 10 |
| sequential | boolean | false | false |
| revealDirection | 'start' \| 'end' \| 'center' \| 'random' | 'start' | start |
| useOriginalCharsOnly | boolean | false | false |
| characters | string | 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+' | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+ |
| animateOn | 'view' \| 'hover' \| 'inViewHover' \| 'click' | 'hover' | hover |
| clickMode | 'once' \| 'toggle' | 'once' | once |
| hoverRadius | number | 0 | 0 |
| loop | boolean | false | false |
| loopDelay | number | 2000 | 2000 |
| className | string | '' |  |
| parentClassName | string | '' |  |
| encryptedClassName | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations


## Motion locations

- [threshold, line 438](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DecryptedText/DecryptedText.jsx#L438): 0.1
- [duration, line 456](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DecryptedText/DecryptedText.jsx#L456): computed; read the linked expression
- [duration, line 461](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/DecryptedText/DecryptedText.jsx#L461): computed; read the linked expression

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
