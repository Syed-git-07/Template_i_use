# TextLoop

Category: TextAnimations. Public entry: [TextLoop](https://reactbits.dev/text-animations/text-loop).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TextLoop/TextLoop.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TextLoop/TextLoop.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TextLoop/TextLoop.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "React ✦ Bits" | React ✦ Bits |
| shape | "wave" \| "circle" \| "infinity" \| "arch" \| "line" | "wave" | wave |
| path | string | undefined | — |
| speed | number | 90 | 90 |
| direction | "forward" \| "reverse" | "forward" | forward |
| separator | string | "✦" | ✦ |
| curviness | number | 90 | 90 |
| tilt | number | 0 | 0 |
| cross | boolean | false | false |
| crossColor | string | - | — |
| crossAngle | number | 16 | 16 |
| draggable | boolean | false | false |
| scrollBoost | number | 0 | 0 |
| fontSize | number | 46 | 46 |
| fontWeight | number | 800 | 800 |
| letterSpacing | number | 2 | 2 |
| uppercase | boolean | true | true |
| outline | boolean | false | false |
| outlineWidth | number | 1.5 | 1.5 |
| color | string | - | — |
| ribbon | boolean | true | true |
| ribbonColor | string | "#5227FF" | #5227FF |
| ribbonWidth | number | 86 | 86 |
| edgeFade | number | 0 | 0 |
| pauseOnHover | boolean | true | true |
| className | string | "" |  |
| style | object | {} | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [pointerenter, line 387](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L387)
- [pointerleave, line 388](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L388)
- [pointerdown, line 391](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L391)
- [pointermove, line 392](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L392)
- [pointerup, line 393](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L393)
- [pointercancel, line 394](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L394)
- [scroll, line 396](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L396)

## Motion locations

- [duration, line 313](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L313): computed; read the linked expression
- [ease, line 314](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.jsx#L314): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextLoop/TextLoop.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
