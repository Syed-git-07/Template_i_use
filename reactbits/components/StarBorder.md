# StarBorder

Category: Animations. Public entry: [StarBorder](https://reactbits.dev/animations/star-border).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/StarBorder/StarBorder.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/StarBorder/StarBorder.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/StarBorder/StarBorder.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| as | ElementType | 'button' | button |
| color | string | - | — |
| trailColor | string | - | — |
| duration | number | 4 | 4 |
| direction | 'clockwise' \| 'counterclockwise' | 'clockwise' | clockwise |
| stars | number | 1 | 1 |
| trailLength | number | 0.3 | 0.3 |
| thickness | number | 1 | 1 |
| radius | number | 12 | 12 |
| glow | number | 0.6 | 0.6 |
| sparkle | boolean | false | false |
| hover | 'lap' \| 'brighten' \| 'reveal' \| 'none' | 'lap' | lap |
| clickPulse | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| backgroundColor | string | - | — |
| textColor | string | - | — |
| borderColor | string | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 530](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L530)
- [pointerleave, line 531](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L531)
- [pointerdown, line 532](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L532)
- [click, line 533](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L533)
- [focus, line 534](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L534)
- [blur, line 535](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L535)

## Motion locations

- [duration, line 162](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L162): computed; read the linked expression
- [velocity, line 189](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.jsx#L189): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/StarBorder/StarBorder.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
