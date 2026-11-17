# PillNav

Category: Components. Public entry: [PillNav](https://reactbits.dev/components/pill-nav).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/PillNav/PillNav.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/PillNav/PillNav.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/PillNav/PillNav.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | { label: string; href?: string; icon?: ReactNode; ariaLabel?: string }[] | - | — |
| logo | string \| ReactNode | - | — |
| logoAlt | string | 'Logo' | Logo |
| logoHref | string | '#' | # |
| activeHref | string | - | — |
| defaultActiveIndex | number | 0 | 0 |
| onItemClick | (item, index, event) => void | - | — |
| linkComponent | ElementType | 'a' | a |
| theme | 'dark' \| 'light' | 'dark' | dark |
| layout | 'split' \| 'joined' | 'split' | split |
| itemStyle | 'pill' \| 'plain' | 'pill' | pill |
| hoverEffect | 'fill' \| 'glide' \| 'none' | 'fill' | fill |
| indicator | 'dot' \| 'pill' \| 'none' | 'dot' | dot |
| surface | 'glass' \| 'solid' \| 'none' | 'glass' | glass |
| size | 'sm' \| 'md' \| 'lg' | 'md' | md |
| highlightColor | string | - | — |
| highlightTextColor | string | - | — |
| barColor | string | - | — |
| textColor | string | - | — |
| bounce | number | 0.3 | 0.3 |
| stretch | number | 0.5 | 0.5 |
| collapse | 'auto' \| 'always' \| 'never' | 'auto' | auto |
| onMenuToggle | (open: boolean) => void | - | — |
| intro | boolean | true | true |
| ariaLabel | string | 'Main' | Main |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerup, line 509](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L509)
- [pointercancel, line 510](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L510)
- [pointerdown, line 672](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L672)
- [keydown, line 673](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L673)
- [onPointerEnter, line 738](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L738)
- [onPointerLeave, line 749](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L749)
- [onPointerEnter, line 759](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L759)
- [onPointerDown, line 760](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L760)
- [onFocus, line 761](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L761)
- [onBlur, line 762](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L762)
- [onClick, line 809](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L809)

## Motion locations

- [bounce, line 200](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L200): computed; read the linked expression
- [duration, line 572](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L572): 700
- [duration, line 583](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L583): 760
- [delay, line 583](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L583): 90
- [duration, line 599](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L599): 560
- [delay, line 599](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L599): computed; read the linked expression
- [duration, line 624](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L624): 560
- [duration, line 632](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L632): 420
- [delay, line 632](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L632): computed; read the linked expression
- [duration, line 642](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L642): 380
- [duration, line 649](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L649): 160
- [duration, line 685](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.jsx#L685): 900

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/PillNav/PillNav.css); motion-related lines: 160, 188, 206, 218, 224, 238, 245, 309, 355, 422, 451, 458.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
