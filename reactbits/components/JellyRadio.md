# JellyRadio

Category: Micro. Public entry: [JellyRadio](https://reactbits.dev/micro/jelly-radio).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/JellyRadio/JellyRadio.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/JellyRadio/JellyRadio.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/JellyRadio/JellyRadio.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | (string \| { value: string; label: ReactNode; icon?: ReactNode; disabled?: boolean })[] | ["Off", "Low", "Medium", "High", "Max"] | — |
| value | string | undefined | — |
| defaultValue | string | undefined | — |
| onChange | (value: string, index: number) => void | - | — |
| chipColor | string | "#27272a" | #27272a |
| activeColor | string | "#f5f5f5" | #f5f5f5 |
| textColor | string | "#f5f5f5" | #f5f5f5 |
| activeTextColor | string | "#18181b" | #18181b |
| size | "sm" \| "md" \| "lg" | "md" | md |
| gap | number | 8 | 8 |
| radius | number | 18 | 18 |
| swell | number | 0.2 | 0.2 |
| barge | number | 6 | 6 |
| shrink | number | 0.05 | 0.05 |
| jelly | number | 1 | 1 |
| bounce | number | 0.25 | 0.25 |
| stagger | number | 22 | 22 |
| stiffness | number | 580 | 580 |
| disabled | boolean | false | false |
| ariaLabel | string | "Options" | Options |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, motion/react

## Interaction locations

- [onClick, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L207)
- [onKeyDown, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L208)

## Motion locations

- [stiffness, line 13](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L13): computed; read the linked expression
- [damping, line 14](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L14): computed; read the linked expression
- [mass, line 15](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L15): computed; read the linked expression
- [delay, line 104](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.jsx#L104): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/JellyRadio/JellyRadio.css); motion-related lines: 69, 82, 104.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
