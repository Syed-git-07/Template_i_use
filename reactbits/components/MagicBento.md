# MagicBento

Category: Components. Public entry: [MagicBento](https://reactbits.dev/components/magic-bento).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/MagicBento/MagicBento.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/MagicBento/MagicBento.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/MagicBento/MagicBento.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | MagicBentoItem[] | Six feature cards | — |
| items[].visual | ReactNode \| string | - | — |
| items[].content | ReactNode | - | — |
| items[].image | string | - | — |
| columns | number | 4 | 4 |
| rowHeight | number | 200 | 200 |
| gap | number | 12 | 12 |
| radius | number | 20 | 20 |
| theme | 'dark' \| 'light' | 'dark' | dark |
| glowColor | string | Text color | — |
| enableBorderGlow | boolean | true | true |
| enableSpotlight | boolean | true | true |
| spotlightRadius | number | 300 | 300 |
| enableStars | boolean | false | false |
| particleCount | number | 24 | 24 |
| enableTilt | boolean | false | false |
| enableMagnetism | boolean | false | false |
| clickEffect | boolean | true | true |
| textAutoHide | boolean | true | true |
| intro | boolean | true | true |
| disableAnimations | boolean | false | false |
| onItemClick | (item, index) => void | - | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerMove, line 245](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L245)
- [onPointerDown, line 246](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L246)
- [onPointerLeave, line 247](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L247)
- [pointermove, line 956](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L956)
- [pointerdown, line 957](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L957)
- [pointerup, line 958](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L958)
- [pointercancel, line 959](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L959)
- [scroll, line 960](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L960)
- [resize, line 961](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L961)
- [pointerout, line 962](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L962)
- [click, line 963](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L963)
- [keydown, line 964](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L964)

## Motion locations

- [duration, line 536](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L536): 1.1
- [threshold, line 931](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.jsx#L931): 0.15

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/MagicBento/MagicBento.css); motion-related lines: 13, 64, 402, 445, 819, 833, 847, 851, 855, 859, 865, 869, 873, 877, 883, 887, 891, 895, 900, 904, 908, 912, 917, 936, 940, 944, 948, 952, 956, 959, 968, 977, 986, 997, 1006, 1015, 1024, 1037, 1043, 1054, 1063, 1082, 1091, 1102, 1115.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
