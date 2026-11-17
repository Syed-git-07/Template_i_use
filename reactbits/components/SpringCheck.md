# SpringCheck

Category: Micro. Public entry: [SpringCheck](https://reactbits.dev/micro/spring-check).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/SpringCheck/SpringCheck.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/SpringCheck/SpringCheck.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/SpringCheck/SpringCheck.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| label | ReactNode | "Ship the build" | Ship the build |
| checked | boolean | undefined | — |
| defaultChecked | boolean | false | false |
| onChange | (checked: boolean) => void | - | — |
| disabled | boolean | false | false |
| color | string | "#ffffff" | #ffffff |
| fillColor | string | "#ffffff" | #ffffff |
| checkColor | string | "#0b0b0f" | #0b0b0f |
| boxSize | number | 28 | 28 |
| boxRadius | number | 9 | 9 |
| fontSize | number | 18 | 18 |
| bounce | number | 0.2 | 0.2 |
| strikeLag | number | 0.12 | 0.12 |
| doneOpacity | number | 0.42 | 0.42 |
| strike | "left" \| "center" \| "right" \| "none" | "left" | left |
| ariaLabel | string | - | — |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react, @hugeicons/core-free-icons

## Interaction locations

- [onPointerDown, line 142](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L142)
- [onPointerUp, line 143](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L143)
- [onPointerCancel, line 144](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L144)
- [onPointerLeave, line 145](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L145)
- [onClick, line 146](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L146)

## Motion locations

- [bounce, line 89](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.jsx#L89): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/SpringCheck/SpringCheck.css); motion-related lines: 49, 78, 128, 130.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
