# TextPressure

Category: TextAnimations. Public entry: [TextPressure](https://reactbits.dev/text-animations/text-pressure).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/TextAnimations/TextPressure/TextPressure.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/TextAnimations/TextPressure/TextPressure.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/TextAnimations/TextPressure/TextPressure.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| text | string | "Compressa" | Compressa |
| fontFamily | string | Roboto Flex | Roboto Flex |
| fontUrl | string | URL to Roboto Flex on Google Fonts | https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wdth,wght@8..144,25..151,100..1000&display=swap |
| textColor | string | 'currentColor' | currentColor |
| pressureColor | string | '' |  |
| strokeColor | string | #FF0000 | #FF0000 |
| idle | 'none' \| 'wave' \| 'pulse' | 'none' | none |
| idleSpeed | number | 1 | 1 |
| radius | number | 0.5 | 0.5 |
| smoothing | number | 0.5 | 0.5 |
| clickRipple | boolean | true | true |
| flex | boolean | true | true |
| scale | boolean | false | false |
| alpha | boolean | false | false |
| stroke | boolean | false | false |
| width | boolean | true | true |
| weight | boolean | true | true |
| italic | boolean | true | true |
| strokeWidth | number | 3 | 3 |
| className | string | "" |  |
| minFontSize | number | 24 | 24 |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [mousemove, line 151](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L151)
- [touchstart, line 152](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L152)
- [touchmove, line 153](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L153)
- [touchend, line 154](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L154)
- [touchcancel, line 155](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L155)
- [scroll, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L156)
- [mouseleave, line 157](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L157)
- [loadingdone, line 158](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L158)
- [pointerdown, line 159](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/TextAnimations/TextPressure/TextPressure.jsx#L159)

## Motion locations


## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
