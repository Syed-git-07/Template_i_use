# OptionWheel

Category: Components. Public entry: [OptionWheel](https://reactbits.dev/components/option-wheel).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/OptionWheel/OptionWheel.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/OptionWheel/OptionWheel.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/OptionWheel/OptionWheel.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | string[] | [...] | — |
| defaultSelected | number | 3 | 3 |
| onChange | (index, item) => void | - | — |
| textColor | string | "#a6a6a6" | #a6a6a6 |
| activeColor | string | "#ffffff" | #ffffff |
| side | "left" \| "right" | "left" | left |
| fontSize | number | 3 | 3 |
| spacing | number | 1.4 | 1.4 |
| curve | number | 1 | 1 |
| tilt | number | 6 | 6 |
| blur | number | 2 | 2 |
| fade | number | 0.25 | 0.25 |
| minOpacity | number | 0.05 | 0.05 |
| smoothing | number | 200 | 200 |
| inset | number | 80 | 80 |
| loop | boolean | false | false |
| draggable | boolean | true | true |
| soundUrl | string | "" |  |
| soundVolume | number | 0.5 | 0.5 |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [wheel, line 193](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L193)
- [onPointerDown, line 283](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L283)
- [onPointerMove, line 284](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L284)
- [onPointerUp, line 285](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L285)
- [onPointerCancel, line 286](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L286)
- [onKeyDown, line 287](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L287)
- [onClick, line 298](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.jsx#L298)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/OptionWheel/OptionWheel.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
