# GlideSelect

Category: Micro. Public entry: [GlideSelect](https://reactbits.dev/micro/glide-select).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Micro/GlideSelect/GlideSelect.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Micro/GlideSelect/GlideSelect.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Micro/GlideSelect/GlideSelect.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| options | (string \| { value: string; label: ReactNode; tag?: string })[] | ["One", "Two", "Three"] | — |
| value | string | undefined | — |
| defaultValue | string | undefined | — |
| onChange | (value: string, option) => void | - | — |
| placeholder | string | "Select…" | Select… |
| showTags | boolean | true | true |
| accentColor | string | "#f5f5f5" | #f5f5f5 |
| surfaceColor | string | "#27272a" | #27272a |
| highlightColor | string | "#3f3f46" | #3f3f46 |
| textColor | string | "#f5f5f5" | #f5f5f5 |
| size | "sm" \| "md" \| "lg" | "md" | md |
| radius | number | 10 | 10 |
| menuWidth | number | 176 | 176 |
| placement | "top" \| "bottom" | "bottom" | bottom |
| align | "left" \| "right" | "left" | left |
| popDuration | number | 180 | 180 |
| glideDuration | number | 220 | 220 |
| rememberPosition | boolean | true | true |
| disabled | boolean | false | false |
| ariaLabel | string | "Select" | Select |
| className | string | "" |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerdown, line 183](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L183)
- [onAnimationEnd, line 251](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L251)
- [onPointerDown, line 266](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L266)
- [onKeyDown, line 272](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L272)
- [onPointerOver, line 289](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L289)
- [onPointerLeave, line 290](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L290)
- [onPointerDown, line 293](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L293)
- [onPointerMove, line 294](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L294)
- [onPointerUp, line 295](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L295)
- [onPointerCancel, line 296](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L296)
- [onLostPointerCapture, line 297](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.jsx#L297)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Micro/GlideSelect/GlideSelect.css); motion-related lines: 48, 76, 79, 89, 108, 119, 156, 176, 213, 216, 220, 224, 228, 232, 240.

## Observed source structure

Literal state assignments: setPhase → open (line 121); setPhase → closed (line 128); setPhase → closing (line 133); setPhase → closed (line 134).

Signals present: keyboard, pointer_cancel, cleanup.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
