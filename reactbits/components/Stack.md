# Stack

Category: Components. Public entry: [Stack](https://reactbits.dev/components/stack).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Stack/Stack.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Stack/Stack.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Stack/Stack.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| cards | ReactNode[] | four sample photos | — |
| layout | 'fan' \| 'cascade' \| 'deck' \| 'pile' | 'fan' | fan |
| visible | number | 4 | 4 |
| spread | number | 0.5 | 0.5 |
| depth | number | 0.5 | 0.5 |
| radius | number | 16 | 16 |
| frame | number | 0 | 0 |
| frameColor | string | '#ffffff' | #ffffff |
| shadow | boolean | true | true |
| tilt | number | 30 | 30 |
| threshold | number | 90 | 90 |
| speed | number | 1 | 1 |
| sendToBackOnClick | boolean | false | false |
| autoplay | boolean | false | false |
| autoplayDelay | number | 3000 | 3000 |
| pauseOnHover | boolean | false | false |
| onChange | (index: number) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [pointermove, line 426](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L426)
- [pointerup, line 427](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L427)
- [pointercancel, line 428](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L428)
- [onKeyDown, line 494](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L494)
- [onMouseEnter, line 495](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L495)
- [onMouseLeave, line 496](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L496)
- [onPointerDown, line 523](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L523)

## Motion locations

- [threshold, line 128](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L128): computed; read the linked expression
- [duration, line 168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L168): 0.2
- [ease, line 168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L168): "easeOut"
- [delay, line 168](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L168): computed; read the linked expression
- [stiffness, line 172](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L172): computed; read the linked expression
- [damping, line 173](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L173): computed; read the linked expression
- [restDelta, line 174](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L174): 0.01
- [restSpeed, line 175](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L175): 0.5
- [duration, line 201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L201): computed; read the linked expression
- [ease, line 201](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L201): "easeOut"
- [velocity, line 203](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L203): computed; read the linked expression
- [velocity, line 204](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L204): computed; read the linked expression
- [delay, line 220](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L220): computed; read the linked expression
- [velocity, line 223](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L223): computed; read the linked expression
- [velocity, line 261](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L261): computed; read the linked expression
- [velocity, line 262](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L262): computed; read the linked expression
- [velocity, line 394](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.jsx#L394): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stack/Stack.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
