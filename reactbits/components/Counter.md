# Counter

Category: Components. Public entry: [Counter](https://reactbits.dev/components/counter).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Counter/Counter.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Counter/Counter.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Counter/Counter.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Counter/Counter.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | number | 0 | 0 |
| locale | string | 'en-US' | en-US |
| format | Intl.NumberFormatOptions | - | — |
| decimals | number | - | — |
| minDigits | number | 1 | 1 |
| prefix | ReactNode | - | — |
| suffix | ReactNode | - | — |
| direction | 'auto' \| 'up' \| 'down' \| 'shortest' | 'auto' | auto |
| duration | number | 0.7 | 0.7 |
| bounce | number | 0.2 | 0.2 |
| stagger | number | 0.04 | 0.04 |
| motionBlur | boolean | true | true |
| intro | boolean | true | true |
| fade | number | 0.3 | 0.3 |
| fontSize | number \| string | 100 | 100 |
| fontWeight | number \| string | 'inherit' | inherit |
| textColor | string | 'inherit' | inherit |
| gap | number | 0 | 0 |
| padding | number | 0 | 0 |
| tabular | boolean | true | true |
| digitStyle | CSSProperties | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations


## Motion locations

- [duration, line 177](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Counter/Counter.jsx#L177): computed; read the linked expression
- [bounce, line 178](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Counter/Counter.jsx#L178): computed; read the linked expression
- [threshold, line 447](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Counter/Counter.jsx#L447): 0.5

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Counter/Counter.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
