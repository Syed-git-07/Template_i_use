# LogoLoop

Category: Animations. Public entry: [LogoLoop](https://reactbits.dev/animations/logo-loop).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Animations/LogoLoop/LogoLoop.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Animations/LogoLoop/LogoLoop.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Animations/LogoLoop/LogoLoop.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| logos | LogoItem[] | required | — |
| speed | number | 120 | 120 |
| direction | 'left' \| 'right' \| 'up' \| 'down' | 'left' | left |
| width | number \| string | '100%' | 100% |
| logoHeight | number | 28 | 28 |
| gap | number | 32 | 32 |
| hoverSpeed | number | undefined | — |
| pauseOnHover | boolean | undefined | — |
| fadeOut | boolean | true | true |
| fadeOutWidth | number | 0.12 | 0.12 |
| scaleOnHover | boolean | false | false |
| layout | 'line' \| 'wave' \| 'arc' \| 'orbit' | 'line' | line |
| bend | number | 0.5 | 0.5 |
| focus | number | 0 | 0 |
| magnify | number | 0 | 0 |
| tiltX | number | 0 | 0 |
| tiltY | number | 0 | 0 |
| step | boolean | false | false |
| muted | number | 0 | 0 |
| labels | 'none' \| 'inline' \| 'below' \| 'hover' | 'none' | none |
| draggable | boolean | true | true |
| scrollBoost | number | 0 | 0 |
| intro | boolean | true | true |
| renderItem | (item: LogoItem, key: React.Key) => React.ReactNode | undefined | — |
| ariaLabel | string | 'Partner logos' | Partner logos |
| className | string | undefined | — |
| style | React.CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointerenter, line 791](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L791)
- [pointerleave, line 792](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L792)
- [pointerdown, line 793](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L793)
- [pointermove, line 794](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L794)
- [pointerup, line 795](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L795)
- [pointercancel, line 796](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L796)
- [lostpointercapture, line 797](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L797)
- [click, line 798](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L798)
- [dragstart, line 799](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L799)
- [focusin, line 800](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L800)
- [focusout, line 801](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L801)
- [scroll, line 802](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L802)
- [scroll, line 803](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L803)
- [change, line 804](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L804)
- [resize, line 833](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L833)
- [visibilitychange, line 852](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L852)

## Motion locations

- [velocity, line 78](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L78): 0
- [threshold, line 844](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.jsx#L844): 0.1

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Animations/LogoLoop/LogoLoop.css); motion-related lines: 85, 118, 153, 201, 206.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
