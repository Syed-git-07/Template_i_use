# ReflectiveCard

Category: Components. Public entry: [ReflectiveCard](https://reactbits.dev/components/reflective-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ReflectiveCard/ReflectiveCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ReflectiveCard/ReflectiveCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ReflectiveCard/ReflectiveCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| name | string | 'Alexander Doe' | Alexander Doe |
| role | string | 'Senior Developer' | Senior Developer |
| badge | string | 'Verified' | Verified |
| status | string | 'Active' | Active |
| statusColor | string | '#22c55e' | #22c55e |
| idLabel | string | 'ID number' | ID number |
| idValue | string | '8901 2345 6789' | 8901 2345 6789 |
| children | ReactNode | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| videoSrc | string | - | — |
| webcam | boolean | false | false |
| onWebcamError | (error: Error) => void | - | — |
| tint | string | '#ffffff' | #ffffff |
| metalness | number | 1 | 1 |
| roughness | number | 0.3 | 0.3 |
| blurStrength | number | 6 | 6 |
| grayscale | number | 1 | 1 |
| warp | number | 0.6 | 0.6 |
| warpScale | number | 1 | 1 |
| shine | number | 1 | 1 |
| bevel | number | 3 | 3 |
| glare | number | 0.5 | 0.5 |
| enableTilt | boolean | true | true |
| tiltStrength | number | 12 | 12 |
| intro | boolean | true | true |
| width | number \| string | 320 | 320 |
| height | number \| string | 500 | 500 |
| radius | number | 24 | 24 |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerenter, line 864](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L864)
- [pointermove, line 865](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L865)
- [pointerleave, line 866](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L866)
- [pointerdown, line 867](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L867)
- [pointerup, line 868](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L868)
- [pointercancel, line 869](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L869)
- [webglcontextlost, line 878](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L878)
- [webglcontextrestored, line 879](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L879)
- [visibilitychange, line 904](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.jsx#L904)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ReflectiveCard/ReflectiveCard.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, microphone, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
