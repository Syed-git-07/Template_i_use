# SloshGauge

Category: Micro. Public entry: [SloshGauge](https://reactbits.dev/micro/slosh-gauge).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SloshGauge/SloshGauge.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SloshGauge/SloshGauge.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SloshGauge/SloshGauge.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | undefined | — |
| defaultValue | number | 60 | 60 |
| onChange | (value: number) => void | - | — |
| interactive | boolean | false | false |
| showValue | boolean | true | true |
| disabled | boolean | false | false |
| liquidColor | string | "#f5f5f5" | #f5f5f5 |
| glassColor | string | "#27272a" | #27272a |
| width | number | 88 | 88 |
| height | number | 180 | 180 |
| radius | number | 20 | 20 |
| ticks | number | 4 | 4 |
| viscosity | number | 0.15 | 0.15 |
| tilt | number | 0.45 | 0.45 |
| splash | number | 0.42 | 0.42 |
| unit | string | "%" | % |
| ariaLabel | string | "Level" | Level |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [change, line 143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L143)
- [onPointerDown, line 276](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L276)
- [onPointerMove, line 277](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L277)
- [onPointerUp, line 278](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L278)
- [onPointerCancel, line 279](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L279)
- [onLostPointerCapture, line 280](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L280)
- [onKeyDown, line 281](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.jsx#L281)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SloshGauge/SloshGauge.css); motion-related lines: 84.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
