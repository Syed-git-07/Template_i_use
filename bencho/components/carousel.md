# Carousel

Public reference: https://bencho.dev/blocks/carousel

[Original API and usage guide](../upstream-free/blocks/carousel/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Carousel.css](../upstream-free/blocks/carousel/Carousel.css): 92 lines; SHA-256 `71f42321f93fe63838169d89031656544e602948648aed90d16ffd1829c7c691`.
- [Carousel.tsx](../upstream-free/blocks/carousel/Carousel.tsx): 744 lines; SHA-256 `4ea400d38ec4a131c22fbea4083c651c9a768271f02e036e5b8963845613d832`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Carousel.css:37](../upstream-free/blocks/carousel/Carousel.css#L37): `transition of its own, or the easing and the drag would`
- [Carousel.css:39](../upstream-free/blocks/carousel/Carousel.css#L39): `the transition rather than the finger */`
- [Carousel.css:64](../upstream-free/blocks/carousel/Carousel.css#L64): `animation: car-bob 5s ease-in-out infinite;}`
- [Carousel.css:72](../upstream-free/blocks/carousel/Carousel.css#L72): `/* no transition: the tilt is sprung in the component, and a`
- [Carousel.css:73](../upstream-free/blocks/carousel/Carousel.css#L73): `transition on top would be a second opinion about how this`
- [Carousel.tsx:3](../upstream-free/blocks/carousel/Carousel.tsx#L3): `/* ── inlined from lab/spring ──────────────────────── */`
- [Carousel.tsx:4](../upstream-free/blocks/carousel/Carousel.tsx#L4): `/* ── one spring, for everything that settles ───────────────`
- [Carousel.tsx:19](../upstream-free/blocks/carousel/Carousel.tsx#L19): `a second and the damping is RAISED to it rather than`
- [Carousel.tsx:22](../upstream-free/blocks/carousel/Carousel.tsx#L22): `version that makes a spring behave differently on a busy`
- [Carousel.tsx:30](../upstream-free/blocks/carousel/Carousel.tsx#L30): `/* 0..100 into the two numbers a spring actually has.`
- [Carousel.tsx:41](../upstream-free/blocks/carousel/Carousel.tsx#L41): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Carousel.tsx:42](../upstream-free/blocks/carousel/Carousel.tsx#L42): `as stiffness and decay, because the ratio is the thing a`
- [Carousel.tsx:48](../upstream-free/blocks/carousel/Carousel.tsx#L48): `The first version of this ran 0.06..0.26 stiffness against`
- [Carousel.tsx:63](../upstream-free/blocks/carousel/Carousel.tsx#L63): `/* stiffness: how hard it is pulled toward the target */`
- [Carousel.tsx:69](../upstream-free/blocks/carousel/Carousel.tsx#L69): `/* Units matter. The snap threshold is absolute, so a caller`
- [Carousel.tsx:70](../upstream-free/blocks/carousel/Carousel.tsx#L70): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Carousel.tsx:129](../upstream-free/blocks/carousel/Carousel.tsx#L129): `when it lands. Their character lives in a duration and in`
- [Carousel.tsx:147](../upstream-free/blocks/carousel/Carousel.tsx#L147): `whatever the component's own tuned duration is. 0 is a`
- [Carousel.tsx:633](../upstream-free/blocks/carousel/Carousel.tsx#L633): `the parent. It costs nothing at rest: a spring at its target`
- [Carousel.tsx:653](../upstream-free/blocks/carousel/Carousel.tsx#L653): `spring is on the POSITION rather than on the rotation, so`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
