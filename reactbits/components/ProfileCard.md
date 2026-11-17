# ProfileCard

Category: Components. Public entry: [ProfileCard](https://reactbits.dev/components/profile-card).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/ProfileCard/ProfileCard.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/ProfileCard/ProfileCard.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/ProfileCard/ProfileCard.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| avatarUrl | string | '' |  |
| iconUrl | string | - | — |
| miniAvatarUrl | string | - | — |
| name | string | 'Javi A. Torres' | Javi A. Torres |
| title | string | 'Software Engineer' | Software Engineer |
| handle | string | 'javicodes' | javicodes |
| status | string | 'Online' | Online |
| statusColor | string | '#22c55e' | #22c55e |
| contactText | string | 'Contact' | Contact |
| showUserInfo | boolean | true | true |
| onContactClick | () => void | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| backdropColor | string | - | — |
| radius | number | 16 | 16 |
| holo | number | 0.8 | 0.8 |
| glare | number | 0.5 | 0.5 |
| enableTilt | boolean | true | true |
| tiltStrength | number | 12 | 12 |
| parallax | number | 8 | 8 |
| enableMobileTilt | boolean | false | false |
| mobileTiltSensitivity | number | 5 | 5 |
| intro | boolean | true | true |
| className | string | '' |  |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [pointerenter, line 210](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L210)
- [pointermove, line 211](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L211)
- [pointerleave, line 212](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L212)
- [pointerdown, line 213](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L213)
- [pointerup, line 214](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L214)
- [pointercancel, line 215](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L215)
- [deviceorientation, line 267](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L267)
- [click, line 282](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L282)
- [onClick, line 352](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.jsx#L352)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/ProfileCard/ProfileCard.css); motion-related lines: 317, 325.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, pointer_cancel, cleanup, frame_loop, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
