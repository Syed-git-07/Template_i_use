# CardNav

Category: Components. Public entry: [CardNav](https://reactbits.dev/components/card-nav).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/CardNav/CardNav.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/CardNav/CardNav.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/CardNav/CardNav.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | { label: string; description?: string; bgColor?: string; textColor?: string; links: { label: string; href?: string; ariaLabel?: string }[] }[] | - | — |
| logo | string \| ReactNode | - | — |
| logoAlt | string | 'Logo' | Logo |
| logoHref | string | '#' | # |
| cta | { label: string; href?: string; onClick?: (event) => void } | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| surface | 'glass' \| 'solid' | 'glass' | glass |
| openOn | 'click' \| 'hover' | 'click' | click |
| cardEffect | 'rise' \| 'unfold' \| 'fade' | 'rise' | rise |
| stagger | number | 0.12 | 0.12 |
| bounce | number | 0.2 | 0.2 |
| speed | number | 1 | 1 |
| cardHeight | number | 176 | 176 |
| maxWidth | number | 800 | 800 |
| accentColor | string | - | — |
| menuLabel | boolean | true | true |
| intro | boolean | true | true |
| defaultOpen | boolean | false | false |
| open | boolean | - | — |
| onOpenChange | (open: boolean) => void | - | — |
| linkComponent | ElementType | 'a' | a |
| onLinkClick | (link, item, event) => void | - | — |
| ariaLabel | string | 'Main' | Main |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerdown, line 340](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L340)
- [keydown, line 341](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L341)
- [onPointerEnter, line 428](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L428)
- [onPointerLeave, line 429](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L429)
- [onClick, line 441](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L441)

## Motion locations

- [bounce, line 177](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L177): computed; read the linked expression
- [duration, line 364](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L364): 820
- [duration, line 372](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L372): 560
- [delay, line 372](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.jsx#L372): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CardNav/CardNav.css); motion-related lines: 65, 99, 130, 181, 321, 342, 365, 369.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
