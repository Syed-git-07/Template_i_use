# BlurText

Category: TextAnimations. Public entry: [BlurText](https://reactbits.dev/text-animations/blur-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/BlurText/BlurText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/BlurText/BlurText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/BlurText/BlurText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "" |  |
| effect | "blur" \| "zoom" \| "tilt" \| "focus" \| "drift" | "blur" | blur |
| animateBy | "words" \| "letters" | "words" | words |
| direction | "top" \| "bottom" \| "left" \| "right" | "top" | top |
| staggerFrom | "start" \| "center" \| "end" \| "random" | "start" | start |
| trigger | "view" \| "load" \| "hover" \| "click" | "view" | view |
| delay | number | 200 | 200 |
| stepDuration | number | 0.35 | 0.35 |
| loop | boolean | false | false |
| loopDelay | number | 2 | 2 |
| blur | number | 10 | 10 |
| distance | number | 50 | 50 |
| color | string | "currentColor" | — |
| fromColor | string | - | — |
| focusOnHover | boolean | false | false |
| threshold | number | 0.1 | 0.1 |
| rootMargin | string | "0px" | 0px |
| animationFrom | object | undefined | — |
| animationTo | object[] | undefined | — |
| easing | Easing \| Easing[] | - | — |
| className | string | "" |  |
| onAnimationComplete | function | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: motion/react, react

## Interaction locations

- [onPointerEnter, line 378](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L378)
- [onClick, line 379](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L379)
- [onPointerEnter, line 386](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L386)
- [onPointerLeave, line 387](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L387)

## Motion locations

- [duration, line 18](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L18): 0
- [bounce, line 53](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L53): 0.25
- [bounce, line 77](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L77): 0.3
- [bounce, line 95](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L95): computed; read the linked expression
- [bounce, line 113](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L113): 0.3
- [bounce, line 128](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L128): 0.35
- [duration, line 309](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L309): computed; read the linked expression
- [delay, line 309](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L309): computed; read the linked expression
- [ease, line 309](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L309): computed; read the linked expression
- [duration, line 310](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L310): computed; read the linked expression
- [delay, line 310](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L310): computed; read the linked expression
- [ease, line 310](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L310): computed; read the linked expression
- [bounce, line 312](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L312): computed; read the linked expression
- [delay, line 312](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L312): computed; read the linked expression
- [duration, line 332](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L332): computed; read the linked expression
- [ease, line 332](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L332): computed; read the linked expression
- [delay, line 332](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/BlurText/BlurText.jsx#L332): computed; read the linked expression

## Observed source structure

Literal state assignments: setPhase → in (line 257); setPhase → rest (line 261); setPhase → out (line 286); setPhase → out (line 290); setPhase → in (line 293); setPhase → out (line 300).

Signals present: visibility.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
