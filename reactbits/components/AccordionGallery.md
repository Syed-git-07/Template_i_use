# AccordionGallery

Category: Components. Public entry: [AccordionGallery](https://reactbits.dev/components/accordion-gallery).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/AccordionGallery/AccordionGallery.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/AccordionGallery/AccordionGallery.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/AccordionGallery/AccordionGallery.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| items | Array<{ image: string; label?: string; link?: string; alt?: string }> | 5 sample panels | — |
| defaultIndex | number | 2 | 2 |
| accentColor | string | "#ffffff" | #ffffff |
| overlayColor | string | "#060010" | #060010 |
| textColor | string | "#ffffff" | #ffffff |
| grayscale | boolean | true | true |
| showLabels | boolean | true | true |
| duration | number | 0.6 | 0.6 |
| ease | string | "power3.out" | power3.out |
| parallax | number | 0.5 | 0.5 |
| tilt | number | 8 | 8 |
| stagger | number | 0.06 | 0.06 |
| trigger | "hover" \| "click" | "hover" | hover |
| height | number | 460 | 460 |
| gap | number | 10 | 10 |
| radius | number | 16 | 16 |
| expandRatio | number | 0.52 | 0.52 |
| orientation | "horizontal" \| "vertical" | "horizontal" | horizontal |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, gsap

## Interaction locations

- [onClick, line 205](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L205)
- [onMouseEnter, line 206](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L206)
- [onFocus, line 207](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L207)
- [onKeyDown, line 208](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L208)

## Motion locations

- [duration, line 78](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L78): computed; read the linked expression
- [duration, line 93](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L93): computed; read the linked expression
- [duration, line 102](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L102): computed; read the linked expression
- [duration, line 104](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.jsx#L104): computed; read the linked expression

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/AccordionGallery/AccordionGallery.css); motion-related lines: 140.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, keyboard, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
