# DecayCard

Category: Components. Public entry: [DecayCard](https://reactbits.dev/components/decay-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DecayCard/DecayCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/DecayCard/DecayCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/DecayCard/DecayCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/DecayCard/DecayCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| image | string | - | https://images.unsplash.com/photo-1762846818262-33c197852fa8?w=900&q=80&auto=format&fit=crop |
| children | ReactNode | - | — |
| width | number | 300 | 300 |
| height | number | 400 | 400 |
| intensity | number | 0.5 | 0.5 |
| sensitivity | number | 0.5 | 0.5 |
| hoverDecay | number | 0.05 | 0.05 |
| recovery | number | 0.6 | 0.6 |
| idle | number | 0.35 | 0.35 |
| grain | number | 0.25 | 0.25 |
| detail | number | 5 | 5 |
| pattern | number | 4 | 4 |
| flow | number | 0 | 0 |
| chroma | number | 0 | 0 |
| travel | number | 50 | 50 |
| tilt | number | 10 | 10 |
| scope | 'window' \| 'card' | 'window' | window |
| radius | number | 0 | 0 |
| grayscale | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 457](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DecayCard/DecayCard.jsx#L457)
- [pointerenter, line 458](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DecayCard/DecayCard.jsx#L458)
- [pointerleave, line 459](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DecayCard/DecayCard.jsx#L459)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/DecayCard/DecayCard.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
