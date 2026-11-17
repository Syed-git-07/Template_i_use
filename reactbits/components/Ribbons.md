# Ribbons

Category: Animations. Public entry: [Ribbons](https://reactbits.dev/animations/ribbons).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/Ribbons/Ribbons.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/Ribbons/Ribbons.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/Ribbons/Ribbons.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| colors | string[] | ['#3847ff', '#7c84ff', '#c7cbff'] | — |
| shape | 'lens' \| 'comet' \| 'even' | 'lens' | lens |
| thickness | number | 30 | 30 |
| length | number | 1.4 | 1.4 |
| spread | number | 18 | 18 |
| stiffness | number | 0.5 | 0.5 |
| bounce | number | 0.5 | 0.5 |
| wave | number | 0 | 0 |
| softness | number | 0 | 0 |
| opacity | number | 1 | 1 |
| fade | boolean | false | false |
| backgroundColor | string | 'transparent' | transparent |
| dpr | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [webglcontextlost, line 486](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx#L486)
- [pointermove, line 487](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx#L487)
- [pointerdown, line 488](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx#L488)

## Motion locations

- [stiffness, line 163](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx#L163): computed; read the linked expression
- [bounce, line 164](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.jsx#L164): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/Ribbons/Ribbons.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
