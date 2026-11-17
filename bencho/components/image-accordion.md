# Image accordion

Public reference: https://bencho.dev/blocks/image-accordion

[Original API and usage guide](../upstream-free/blocks/image-accordion/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Accordion.css](../upstream-free/blocks/image-accordion/Accordion.css): 65 lines; SHA-256 `2022020e74ccc9328f6a5ae477a5e4c8515365d1220cbd908fbd8ff1300366f7`.
- [Accordion.tsx](../upstream-free/blocks/image-accordion/Accordion.tsx): 406 lines; SHA-256 `5933c9617e4fe4175837a44543bcd3b758dcbc52bcd6a21ce28b9450e3f8a639`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Accordion.tsx:3](../upstream-free/blocks/image-accordion/Accordion.tsx#L3): `/* ── inlined from lab/spring ──────────────────────── */`
- [Accordion.tsx:4](../upstream-free/blocks/image-accordion/Accordion.tsx#L4): `/* ── one spring, for everything that settles ───────────────`
- [Accordion.tsx:19](../upstream-free/blocks/image-accordion/Accordion.tsx#L19): `a second and the damping is RAISED to it rather than`
- [Accordion.tsx:22](../upstream-free/blocks/image-accordion/Accordion.tsx#L22): `version that makes a spring behave differently on a busy`
- [Accordion.tsx:30](../upstream-free/blocks/image-accordion/Accordion.tsx#L30): `/* 0..100 into the two numbers a spring actually has.`
- [Accordion.tsx:41](../upstream-free/blocks/image-accordion/Accordion.tsx#L41): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Accordion.tsx:42](../upstream-free/blocks/image-accordion/Accordion.tsx#L42): `as stiffness and decay, because the ratio is the thing a`
- [Accordion.tsx:48](../upstream-free/blocks/image-accordion/Accordion.tsx#L48): `The first version of this ran 0.06..0.26 stiffness against`
- [Accordion.tsx:63](../upstream-free/blocks/image-accordion/Accordion.tsx#L63): `/* stiffness: how hard it is pulled toward the target */`
- [Accordion.tsx:69](../upstream-free/blocks/image-accordion/Accordion.tsx#L69): `/* Units matter. The snap threshold is absolute, so a caller`
- [Accordion.tsx:70](../upstream-free/blocks/image-accordion/Accordion.tsx#L70): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Accordion.tsx:176](../upstream-free/blocks/image-accordion/Accordion.tsx#L176): `against Bencho's own spring and knobs rather than copied. */`
- [Accordion.tsx:289](../upstream-free/blocks/image-accordion/Accordion.tsx#L289): `/* the spring, 0..100 — see springOf in ./spring */`
- [Accordion.tsx:290](../upstream-free/blocks/image-accordion/Accordion.tsx#L290): `bounce = 10,`
- [Accordion.tsx:296](../upstream-free/blocks/image-accordion/Accordion.tsx#L296): `bounce?: number;`
- [Accordion.tsx:304](../upstream-free/blocks/image-accordion/Accordion.tsx#L304): `/* ── one spring each, and NO stagger ───────────────────────`
- [Accordion.tsx:318](../upstream-free/blocks/image-accordion/Accordion.tsx#L318): `itself, which is the units note on useSpring — a spring`
- [Accordion.tsx:322](../upstream-free/blocks/image-accordion/Accordion.tsx#L322): `const a0 = useSpring(want(0), bounce, still);`
- [Accordion.tsx:323](../upstream-free/blocks/image-accordion/Accordion.tsx#L323): `const a1 = useSpring(want(1), bounce, still);`
- [Accordion.tsx:324](../upstream-free/blocks/image-accordion/Accordion.tsx#L324): `const a2 = useSpring(want(2), bounce, still);`
- [Accordion.tsx:325](../upstream-free/blocks/image-accordion/Accordion.tsx#L325): `const a3 = useSpring(want(3), bounce, still);`
- [Accordion.tsx:326](../upstream-free/blocks/image-accordion/Accordion.tsx#L326): `const a4 = useSpring(want(4), bounce, still);`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
