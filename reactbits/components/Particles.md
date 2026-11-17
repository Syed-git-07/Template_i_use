# Particles

Category: Backgrounds. Public entry: [Particles](https://reactbits.dev/backgrounds/particles).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Backgrounds/Particles/Particles.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Backgrounds/Particles/Particles.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Backgrounds/Particles/Particles.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| particleCount | number | 200 | 200 |
| particleSpread | number | 10 | 10 |
| speed | number | 0.1 | 0.1 |
| particleColors | string[] | ['#ffffff'] | — |
| particleBaseSize | number | 100 | 100 |
| sizeRandomness | number | 1 | 1 |
| shape | 'circle' \| 'square' \| 'ring' \| 'sparkle' | 'circle' | circle |
| glow | number | 0.5 | 0.5 |
| twinkle | number | 0.3 | 0.3 |
| depthOfField | number | 0 | 0 |
| connections | boolean | false | false |
| connectionDistance | number | 110 | 110 |
| drift | 'none' \| 'up' \| 'down' \| 'forward' | 'none' | none |
| driftSpeed | number | 1 | 1 |
| moveParticlesOnHover | boolean | true | true |
| hoverEffect | 'parallax' \| 'repel' \| 'attract' | 'parallax' | parallax |
| particleHoverFactor | number | 1 | 1 |
| hoverRadius | number | 140 | 140 |
| clickBurst | boolean | true | true |
| alphaParticles | boolean | false | false |
| cameraDistance | number | 20 | 20 |
| disableRotation | boolean | false | false |
| variation | number | 0 | 0 |
| intro | boolean | true | true |
| opacity | number | 1 | 1 |
| lightMode | boolean | false | false |
| paused | boolean | false | false |
| pixelRatio | number | auto | — |
| className | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [pointermove, line 828](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L828)
- [pointerdown, line 829](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L829)
- [pointerup, line 830](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L830)
- [pointercancel, line 831](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L831)
- [pointerleave, line 832](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L832)
- [visibilitychange, line 833](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.jsx#L833)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Backgrounds/Particles/Particles.css); motion-related lines: none matched.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, visibility, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
