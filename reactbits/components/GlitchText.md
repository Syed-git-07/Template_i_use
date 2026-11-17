# GlitchText

Category: TextAnimations. Public entry: [GlitchText](https://reactbits.dev/text-animations/glitch-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/GlitchText/GlitchText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/GlitchText/GlitchText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/GlitchText/GlitchText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/GlitchText/GlitchText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | string |  | — |
| mode | "slices" \| "rgb" \| "scan" \| "noise" | "slices" | slices |
| trigger | "always" \| "hover" \| "click" | "always" | always |
| speed | number | 0.5 | 0.5 |
| intensity | number | 0.5 | 0.5 |
| burstDuration | number | 0.6 | 0.6 |
| flicker | boolean | false | false |
| offset | number | 10 | 10 |
| skew | number | 0 | 0 |
| enableShadows | boolean | true | true |
| shadowColors | [string, string] | ['#ff0000', '#00ffff'] | — |
| color | string | "currentColor" | — |
| fontSize | number \| string | "clamp(2rem, 10vw, 8rem)" | — |
| fontWeight | number \| string | 900 | — |
| enableOnHover | boolean | false | false |
| className | string |  |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 308](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/GlitchText/GlitchText.jsx#L308)
- [pointerleave, line 309](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/GlitchText/GlitchText.jsx#L309)
- [click, line 311](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/GlitchText/GlitchText.jsx#L311)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/GlitchText/GlitchText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
