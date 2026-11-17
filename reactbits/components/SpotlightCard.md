# SpotlightCard

Category: Components. Public entry: [SpotlightCard](https://reactbits.dev/components/spotlight-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/SpotlightCard/SpotlightCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/SpotlightCard/SpotlightCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/SpotlightCard/SpotlightCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| spotlightColor | string | undefined | — |
| intensity | number | 0.15 | 0.15 |
| spotlightSize | number | 240 | 240 |
| softness | number | 0.7 | 0.7 |
| shape | 'circle' \| 'beam' | 'circle' | circle |
| borderGlow | number | 0.6 | 0.6 |
| proximity | number | 80 | 80 |
| smoothing | number | 0.3 | 0.3 |
| ambient | boolean | false | false |
| flare | boolean | true | true |
| grain | number | 0 | 0 |
| theme | 'dark' \| 'light' | 'dark' | dark |
| className | string | '' |  |
| style | CSSProperties | - | — |
| ...rest | HTMLAttributes<HTMLDivElement> | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 241](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L241)
- [pointerup, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L242)
- [pointercancel, line 243](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L243)
- [scroll, line 244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L244)
- [pointerout, line 245](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L245)
- [pointerdown, line 246](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L246)
- [focusin, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L247)
- [focusout, line 248](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.jsx#L248)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/SpotlightCard/SpotlightCard.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
