# PatternWaves

Category: Backgrounds. Public entry: [PatternWaves](https://reactbits.dev/backgrounds/pattern-waves).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/PatternWaves/PatternWaves.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/PatternWaves/PatternWaves.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/PatternWaves/PatternWaves.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| preset | 'silk' \| 'ocean' \| 'pond' \| 'lines' \| 'terminal' \| 'mesh' | 'silk' | silk |
| pattern | 'dot' \| 'square' \| 'plus' \| 'line' \| 'glyph' | from preset | — |
| wave | 'silk' \| 'swell' \| 'ripple' | from preset | — |
| color | string | '#ffffff' | #ffffff |
| backgroundColor | string | '#000000' | #000000 |
| spacing | number | from preset | — |
| markSize | number | from preset | — |
| depth | number | from preset | — |
| light | number | from preset | — |
| shine | number | from preset | — |
| contrast | number | from preset | — |
| speed | number | from preset | — |
| scale | number | from preset | — |
| direction | number | from preset | — |
| opacity | number | 1 | 1 |
| fade | 'edges' \| 'center' \| 'bottom' \| 'top' \| 'none' | 'edges' | edges |
| fadeSize | number | 0.5 | 0.5 |
| characters | string | '.:-=+*#%@' | .:-=+*#%@ |
| interactive | boolean | true | true |
| cursorSize | number | 50 | 50 |
| cursorStrength | number | 0.6 | 0.6 |
| intro | boolean | true | true |
| paused | boolean | false | false |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, ogl

## Interaction locations

- [pointermove, line 856](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L856)
- [pointerdown, line 857](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L857)
- [pointerout, line 858](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L858)
- [pointerup, line 859](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L859)
- [blur, line 860](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L860)
- [visibilitychange, line 861](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.jsx#L861)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/PatternWaves/PatternWaves.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, visibility, cleanup, frame_loop, webgl, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
