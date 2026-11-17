# StaggeredMenu

Category: Components. Public entry: [StaggeredMenu](https://reactbits.dev/components/staggered-menu).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/StaggeredMenu/StaggeredMenu.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/StaggeredMenu/StaggeredMenu.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/StaggeredMenu/StaggeredMenu.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| position | "left" \| "right" | "right" | right |
| colors | string[] | ["#B497CF", "#5227FF"] | — |
| items | StaggeredMenuItem[] | [] | — |
| socialItems | StaggeredMenuSocialItem[] | [] | — |
| displaySocials | boolean | true | true |
| displayItemNumbering | boolean | true | true |
| className | string | undefined | — |
| logoUrl | string | /src/assets/logos/reactbits-gh-white.svg | /src/assets/logos/reactbits-gh-white.svg |
| menuButtonColor | string | "#fff" | #fff |
| openMenuButtonColor | string | "#fff" | #fff |
| accentColor | string | undefined | #5227FF |
| changeMenuColorOnOpen | boolean | true | true |
| onMenuOpen | () => void | undefined | — |
| onMenuClose | () => void | undefined | — |
| closeOnClickAway | boolean | true | true |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [mousedown, line 349](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L349)
- [onClick, line 390](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L390)

## Motion locations

- [duration, line 113](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L113): 0.5
- [ease, line 113](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L113): "power4.out"
- [duration, line 121](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L121): computed; read the linked expression
- [ease, line 121](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L121): "power4.out"
- [duration, line 133](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L133): 1
- [ease, line 134](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L134): "power4.out"
- [duration, line 143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L143): 0.6
- [ease, line 144](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L144): "power2.out"
- [duration, line 160](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L160): 0.5
- [ease, line 161](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L161): "power2.out"
- [duration, line 172](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L172): 0.55
- [ease, line 173](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L173): "power3.out"
- [duration, line 216](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L216): 0.32
- [ease, line 217](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L217): "power3.in"
- [duration, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L242): 0.8
- [ease, line 242](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L242): "power4.out"
- [duration, line 244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L244): 0.35
- [ease, line 244](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L244): "power3.inOut"
- [delay, line 257](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L257): 0.18
- [duration, line 258](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L258): 0.3
- [ease, line 259](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L259): "power2.out"
- [duration, line 302](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L302): computed; read the linked expression
- [ease, line 303](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.jsx#L303): "power4.out"

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/StaggeredMenu/StaggeredMenu.css); motion-related lines: 244, 279, 289.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
