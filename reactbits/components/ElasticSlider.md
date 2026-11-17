# ElasticSlider

Category: Components. Public entry: [ElasticSlider](https://reactbits.dev/components/elastic-slider).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ElasticSlider/ElasticSlider.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ElasticSlider/ElasticSlider.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ElasticSlider/ElasticSlider.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | - | — |
| defaultValue | number | 50 | 50 |
| startingValue | number | 0 | 0 |
| maxValue | number | 100 | 100 |
| isStepped | boolean | false | false |
| stepSize | number | 1 | 1 |
| onChange | (value: number) => void | - | — |
| onChangeEnd | (value: number) => void | - | — |
| orientation | 'horizontal' \| 'vertical' | 'horizontal' | horizontal |
| leftIcon | ReactNode | volume low icon | — |
| rightIcon | ReactNode | volume high icon | — |
| iconPlacement | 'outside' \| 'inside' | 'outside' | outside |
| valuePosition | 'top' \| 'bubble' \| 'inside' \| 'none' | 'top' | top |
| formatValue | (value: number) => string | - | — |
| ticks | boolean \| number[] | false | false |
| thumb | boolean | false | false |
| fillFrom | number | startingValue | — |
| thickness | number | 6 | 6 |
| activeThickness | number | 12 | 12 |
| radius | number | - | — |
| restOpacity | number | 0.7 | 0.7 |
| growOnHover | boolean | true | true |
| maxStretch | number | 50 | 50 |
| bounce | number | 0.5 | 0.5 |
| jumpToClick | boolean | true | true |
| wheel | boolean | false | false |
| trackColor | string | 'color-mix(in srgb, currentColor 18%, transparent)' | color-mix(in srgb, currentColor 18%, transparent) |
| rangeColor | string | 'currentColor' | currentColor |
| iconColor | string | 'currentColor' | currentColor |
| contentColor | string | 'currentColor' | currentColor |
| fillContentColor | string | 'auto' | auto |
| thumbColor | string | '#ffffff' | #ffffff |
| disabled | boolean | false | false |
| ariaLabel | string | 'Slider' | Slider |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [wheel, line 404](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L404)
- [onPointerEnter, line 560](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L560)
- [onPointerLeave, line 565](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L565)
- [onPointerDown, line 593](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L593)
- [onPointerMove, line 594](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L594)
- [onPointerUp, line 595](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L595)
- [onPointerCancel, line 596](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L596)
- [onLostPointerCapture, line 597](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L597)
- [onKeyDown, line 598](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L598)
- [onFocus, line 599](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L599)
- [onBlur, line 603](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L603)

## Motion locations

- [bounce, line 156](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L156): computed; read the linked expression
- [duration, line 314](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.jsx#L314): 280

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ElasticSlider/ElasticSlider.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
