# ParticleText

Category: TextAnimations. Public entry: [ParticleText](https://reactbits.dev/text-animations/particle-text).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/ParticleText/ParticleText.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/ParticleText/ParticleText.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/ParticleText/ParticleText.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "React Bits" | React Bits |
| color | string | "currentColor" | currentColor |
| highlightColor | string | "#ff5a36" | #ff5a36 |
| intro | "gather" \| "rain" \| "spiral" \| "scan" | "gather" | gather |
| gatherDuration | number | 1600 | 1600 |
| stagger | number | 420 | 420 |
| scatter | number | 180 | 180 |
| trigger | "mount" \| "hover" \| "click" | "mount" | mount |
| clickBurst | boolean | true | true |
| burstStrength | number | 1 | 1 |
| pointerRepel | number | 40 | 40 |
| repelRadius | number | 120 | 120 |
| idleDrift | number | 0.7 | 0.7 |
| shape | "circle" \| "square" \| "line" | "circle" | circle |
| highlightMode | "motion" \| "gradient" | "motion" | motion |
| particleSize | number | 2 | 2 |
| density | number | 4 | 4 |
| glow | boolean | true | true |
| fontSize | number \| string | "clamp(3rem, 12vw, 8rem)" | clamp(3rem, 12vw, 8rem) |
| fontWeight | number \| string | 800 | 800 |
| fontFamily | string | "inherit" | inherit |
| className | string | "" |  |
| style | React.CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 745](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L745)
- [pointerenter, line 746](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L746)
- [pointermove, line 747](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L747)
- [pointerleave, line 748](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L748)
- [pointerdown, line 749](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L749)
- [click, line 750](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L750)
- [change, line 768](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L768)

## Motion locations

- [duration, line 147](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L147): 1
- [delay, line 650](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.jsx#L650): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/ParticleText/ParticleText.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
