# AnimatedList

Category: Components. Public entry: [AnimatedList](https://reactbits.dev/components/animated-list).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/AnimatedList/AnimatedList.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/AnimatedList/AnimatedList.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/AnimatedList/AnimatedList.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | (string \| { id?, icon?, image?, title, description?, meta? })[] | sample files | — |
| onItemSelect | (item, index) => void | - | — |
| renderItem | (item, index, selected) => ReactNode | - | — |
| initialSelectedIndex | number | -1 | -1 |
| selectOnHover | boolean | true | true |
| enableArrowNavigation | boolean | true | true |
| loop | boolean | false | false |
| animation | 'pop' \| 'slide' \| 'fade' \| 'none' | 'pop' | pop |
| animateOnce | boolean | false | false |
| stagger | number | 0.05 | 0.05 |
| showGradients | boolean | true | true |
| fadeSize | number | 56 | 56 |
| displayScrollbar | boolean | true | true |
| frame | boolean | true | true |
| theme | 'dark' \| 'light' | 'dark' | dark |
| accentColor | string | - | — |
| radius | number | 14 | 14 |
| gap | number | 8 | 8 |
| width | number \| string | 420 | 420 |
| maxHeight | number \| string | 440 | 440 |
| className | string | '' |  |
| itemClassName | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [scroll, line 410](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L410)
- [keydown, line 411](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L411)
- [pointerenter, line 412](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L412)
- [pointerleave, line 413](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L413)
- [pointermove, line 414](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L414)
- [onPointerEnter, line 519](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L519)
- [onClick, line 520](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.jsx#L520)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AnimatedList/AnimatedList.css); motion-related lines: 186.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
