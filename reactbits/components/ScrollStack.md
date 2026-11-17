# ScrollStack

Category: Components. Public entry: [ScrollStack](https://reactbits.dev/components/scroll-stack).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ScrollStack/ScrollStack.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ScrollStack/ScrollStack.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ScrollStack/ScrollStack.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| itemDistance | number | 100 | 100 |
| itemStackDistance | number | 24 | 24 |
| stackPosition | number \| string | '15%' | 15% |
| itemScale | number | 0.05 | 0.05 |
| baseScale | number | 0.8 | 0.8 |
| dimAmount | number | 0.2 | 0.2 |
| blurAmount | number | 0 | 0 |
| tiltAmount | number | 0 | 0 |
| rotationAmount | number | 0 | 0 |
| holdDistance | number | 200 | 200 |
| smoothScroll | boolean | true | true |
| snap | boolean | false | false |
| useWindowScroll | boolean | false | false |
| onStackComplete | () => void | - | — |
| className | string | '' |  |
| itemClassName | string | '' | — |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [scroll, line 280](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L280)
- [wheel, line 281](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L281)
- [pointerdown, line 282](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L282)
- [pointerup, line 283](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L283)
- [pointercancel, line 284](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L284)
- [resize, line 285](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.jsx#L285)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ScrollStack/ScrollStack.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
