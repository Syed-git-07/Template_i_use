# Tilt card

Public reference: https://bencho.dev/blocks/tilt

[Original API and usage guide](../upstream-free/blocks/tilt/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Tilt.css](../upstream-free/blocks/tilt/Tilt.css): 43 lines; SHA-256 `431f265672547c0e497f03ce7b7f4868cafbf7b5c526c4f34fc845976ab42167`.
- [Tilt.tsx](../upstream-free/blocks/tilt/Tilt.tsx): 333 lines; SHA-256 `da924f1cf46b655e8066ea38b6499fff19a25055843ce7bb25ca075bd8dd012b`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Tilt.tsx:3](../upstream-free/blocks/tilt/Tilt.tsx#L3): `/* ── inlined from lab/spring ──────────────────────── */`
- [Tilt.tsx:4](../upstream-free/blocks/tilt/Tilt.tsx#L4): `/* ── one spring, for everything that settles ───────────────`
- [Tilt.tsx:19](../upstream-free/blocks/tilt/Tilt.tsx#L19): `a second and the damping is RAISED to it rather than`
- [Tilt.tsx:22](../upstream-free/blocks/tilt/Tilt.tsx#L22): `version that makes a spring behave differently on a busy`
- [Tilt.tsx:30](../upstream-free/blocks/tilt/Tilt.tsx#L30): `/* 0..100 into the two numbers a spring actually has.`
- [Tilt.tsx:41](../upstream-free/blocks/tilt/Tilt.tsx#L41): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Tilt.tsx:42](../upstream-free/blocks/tilt/Tilt.tsx#L42): `as stiffness and decay, because the ratio is the thing a`
- [Tilt.tsx:48](../upstream-free/blocks/tilt/Tilt.tsx#L48): `The first version of this ran 0.06..0.26 stiffness against`
- [Tilt.tsx:63](../upstream-free/blocks/tilt/Tilt.tsx#L63): `/* stiffness: how hard it is pulled toward the target */`
- [Tilt.tsx:69](../upstream-free/blocks/tilt/Tilt.tsx#L69): `/* Units matter. The snap threshold is absolute, so a caller`
- [Tilt.tsx:70](../upstream-free/blocks/tilt/Tilt.tsx#L70): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Tilt.tsx:160](../upstream-free/blocks/tilt/Tilt.tsx#L160): `here has a transition of its own — see the note on Sound`
- [Tilt.tsx:212](../upstream-free/blocks/tilt/Tilt.tsx#L212): `spring is on the POSITION rather than on the rotation, so`
- [Tilt.tsx:221](../upstream-free/blocks/tilt/Tilt.tsx#L221): `mass, and the settle on the way out is the only reason`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
