# feature-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/feature-carousel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/feature-carousel.tsx); SHA-256 `640b26986b8a4655670ccb5c3480e0367eb0339e8e9553a84388806f62a47d6a`; 735 lines.

Imports: `react`, `next/image`, `clsx`, `motion/react`, `react-wrap-balancer`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| "--x" | MotionValue<string> | False | 47 |
| "--y" | MotionValue<string> | False | 48 |
| title | string | False | 52 |
| description | string | False | 53 |
| bgClass | string | True | 54 |
| step1dark1 | StaticImageData \| string | True | 58 |
| step1dark2 | StaticImageData \| string | True | 59 |
| step1light1 | StaticImageData \| string | False | 60 |
| step1light2 | StaticImageData \| string | False | 61 |
| step2dark1 | StaticImageData \| string | True | 62 |
| step2dark2 | StaticImageData \| string | True | 63 |
| step2light1 | StaticImageData \| string | False | 64 |
| step2light2 | StaticImageData \| string | False | 65 |
| step3dark | StaticImageData \| string | True | 66 |
| step3light | StaticImageData \| string | False | 67 |
| step4light | StaticImageData \| string | False | 68 |
| alt | string | False | 69 |
| step1img1Class | string | True | 73 |
| step1img2Class | string | True | 74 |
| step2img1Class | string | True | 75 |
| step2img2Class | string | True | 76 |
| step3imgClass | string | True | 77 |
| step4imgClass | string | True | 78 |
| image | ImageSet | False | 79 |
| src | StaticImageData \| string | False | 83 |
| alt | string | False | 84 |
| className | string | True | 85 |
| style | React.CSSProperties | True | 86 |
| width | number | True | 87 |
| height | number | True | 88 |
| id | string | False | 92 |
| name | string | False | 93 |
| title | string | False | 94 |
| description | string | False | 95 |
| preset | AnimationPreset | True | 172 |
| delay | number | True | 173 |
| onAnimationComplete | () => void | True | 174 |
| children | React.ReactNode | False | 356 |
| step | number | False | 357 |
| steps | readonly Step[] | False | 449 |
| current | number | False | 450 |
| onChange | (index: number) => void | False | 451 |

### Defaults and motion

- Default `width` = `1200` (line 297).
- Default `height` = `630` (line 297).
- Default `preset` = `"fadeInScale"` (line 328).
- Default `delay` = `0` (line 329).
- `stiffness`: 300 (line 140).
- `damping`: 25 (line 141).
- `mass`: 0.5 (line 142).
- `stiffness`: 300 (line 151).
- `damping`: 25 (line 152).
- `mass`: 0.5 (line 153).
- `stiffness`: 300 (line 162).
- `damping`: 25 (line 163).
- `mass`: 0.5 (line 164).
- `duration`: 0.3 (line 402).
- `ease`: computed; inspect expression (line 403).
- `delay`: 0.1 (line 411).
- `duration`: 0.3 (line 412).
- `ease`: computed; inspect expression (line 413).
- `delay`: 0.2 (line 422).
- `duration`: 0.3 (line 423).
- `ease`: computed; inspect expression (line 424).
- `duration`: 0.3 (line 471).
- `stiffness`: 300 (line 505).
- `damping`: 20 (line 506).
- `delay`: 0.2 (line 719).

### Input, style and lifecycle

Events: onAnimationComplete (line 342); onMouseMove (line 378); onClick (line 482); onAnimationComplete (line 603); onAnimationComplete (line 633); onAnimationComplete (line 665); onAnimationComplete (line 684); onChange (line 722); onClick (line 726).

Typography/style anchors: 138, 149, 160.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
