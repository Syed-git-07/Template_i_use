# Dock

Category: Components. Public entry: [Dock](https://reactbits.dev/components/dock).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Dock/Dock.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Dock/Dock.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Dock/Dock.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | DockItemData[] | [] | — |
| items[].menu | DockMenuItem[] | - | — |
| position | 'bottom' \| 'top' \| 'left' \| 'right' | 'bottom' | bottom |
| theme | 'dark' \| 'light' | 'dark' | dark |
| baseItemSize | number | 50 | 50 |
| magnification | number | 70 | 70 |
| distance | number | 200 | 200 |
| panelHeight | number | 68 | 68 |
| gap | number | 10 | 10 |
| roundness | number | 0.5 | 0.5 |
| spring | { mass?: number; stiffness?: number; damping?: number } | { mass: 0.1, stiffness: 150, damping: 12 } | — |
| bounce | boolean | true | true |
| autoHide | boolean | false | false |
| tiles | boolean | true | true |
| showLabels | boolean | true | true |
| showIndicators | boolean | true | true |
| showBadges | boolean | true | true |
| badgeColor | string | '#ff453a' | #ff453a |
| accentColor | string | '#0a84ff' | #0a84ff |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, react-dom

## Interaction locations

- [onKeyDown, line 350](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L350)
- [onPointerEnter, line 351](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L351)
- [onPointerLeave, line 352](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L352)
- [onPointerMove, line 380](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L380)
- [onPointerUp, line 381](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L381)
- [onClick, line 386](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L386)
- [onSelect, line 419](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L419)
- [onDismiss, line 420](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L420)
- [onBack, line 421](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L421)
- [onEnter, line 426](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L426)
- [pointermove, line 756](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L756)
- [pointerdown, line 757](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L757)
- [pointerleave, line 758](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L758)
- [pointercancel, line 759](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L759)
- [focusin, line 760](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L760)
- [focusout, line 761](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L761)
- [pointermove, line 762](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L762)
- [pointerdown, line 763](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L763)
- [pointerdown, line 818](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L818)
- [scroll, line 819](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L819)
- [resize, line 820](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L820)
- [blur, line 821](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L821)
- [pointerup, line 888](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L888)
- [pointermove, line 896](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L896)
- [pointerup, line 897](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L897)
- [pointercancel, line 898](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L898)
- [onPointerDown, line 956](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L956)
- [onContextMenu, line 967](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L967)
- [onClick, line 973](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L973)
- [onFocus, line 981](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L981)
- [onBlur, line 984](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L984)
- [onKeyDown, line 985](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L985)
- [onSelect, line 1013](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L1013)
- [onDismiss, line 1017](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L1017)
- [onExited, line 1018](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L1018)

## Motion locations

- [duration, line 187](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L187): 120
- [duration, line 190](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L190): computed; read the linked expression
- [duration, line 194](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L194): computed; read the linked expression
- [mass, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L446): 0.1
- [stiffness, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L446): 150
- [damping, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L446): 12
- [mass, line 495](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L495): computed; read the linked expression
- [stiffness, line 496](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L496): computed; read the linked expression
- [damping, line 497](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L497): computed; read the linked expression
- [velocity, line 553](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.jsx#L553): 0

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Dock/Dock.css); motion-related lines: 17, 25, 171, 184, 292, 419, 507, 511.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
