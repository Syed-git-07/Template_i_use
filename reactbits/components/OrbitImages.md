# OrbitImages

Category: Animations. Public entry: [OrbitImages](https://reactbits.dev/animations/orbit-images).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/OrbitImages/OrbitImages.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/OrbitImages/OrbitImages.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/OrbitImages/OrbitImages.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| images | Array<string \| { src: string; alt?: string }> | [] | — |
| altPrefix | string | 'Orbiting image' | Orbiting image |
| shape | 'ellipse' \| 'circle' \| 'square' \| 'rectangle' \| 'triangle' \| 'star' \| 'heart' \| 'infinity' \| 'wave' \| 'custom' | 'ellipse' | ellipse |
| customPath | string | undefined | — |
| baseWidth | number | 1400 | 1400 |
| radiusX | number | 700 | 700 |
| radiusY | number | 170 | 170 |
| radius | number | 300 | 300 |
| starPoints | number | 5 | 5 |
| starInnerRatio | number | 0.5 | 0.5 |
| rotation | number | -8 | -8 |
| duration | number | 40 | 40 |
| itemSize | number | 64 | 64 |
| direction | 'normal' \| 'reverse' | 'normal' | normal |
| fill | boolean | true | true |
| depth | number | 0.5 | 0.5 |
| alignToPath | boolean | false | false |
| itemRadius | number \| string | 12 | 12 |
| shadow | number | 0.3 | 0.3 |
| hoverScale | number | 1.08 | 1.08 |
| hoverSpeed | number | 0.3 | 0.3 |
| draggable | boolean | true | true |
| clickToFront | boolean | true | true |
| onItemClick | (index: number, src: string) => void | undefined | — |
| showPath | boolean | false | false |
| pathColor | string | 'rgba(128,128,128,0.35)' | rgba(128,128,128,0.35) |
| pathWidth | number | 2 | 2 |
| pathDash | number | 0 | 0 |
| easing | 'linear' \| 'easeIn' \| 'easeOut' \| 'easeInOut' | 'linear' | linear |
| paused | boolean | false | false |
| intro | boolean | true | true |
| centerContent | ReactNode | undefined | — |
| width | number \| string | '100%' | 100% |
| height | number \| string | 'auto' | auto |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 542](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L542)
- [pointerleave, line 543](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L543)
- [pointerover, line 544](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L544)
- [pointerdown, line 545](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L545)
- [pointermove, line 546](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L546)
- [pointerup, line 547](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L547)
- [pointercancel, line 548](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L548)
- [lostpointercapture, line 549](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L549)
- [click, line 550](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L550)
- [keydown, line 551](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L551)
- [focusin, line 552](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L552)
- [change, line 553](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L553)
- [visibilitychange, line 580](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L580)
- [resize, line 581](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L581)

## Motion locations

- [threshold, line 572](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.jsx#L572): 0.05

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/OrbitImages/OrbitImages.css); motion-related lines: 52, 92, 94.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
