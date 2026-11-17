# Search

Public reference: https://bencho.dev/blocks/seek

[Original API and usage guide](../upstream-free/blocks/seek/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Seek.css](../upstream-free/blocks/seek/Seek.css): 276 lines; SHA-256 `77afba0f441dbfb5e84a95c965338757277d72e33b071d5ceef009e25fd7c200`.
- [Seek.tsx](../upstream-free/blocks/seek/Seek.tsx): 511 lines; SHA-256 `7275290676e0304ca9b0c9ccb8a34d4518f415312a51b8b8566c1dae3091c08f`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Seek.css:50](../upstream-free/blocks/seek/Seek.css#L50): `how far through that spring it is. That is the whole reason`
- [Seek.css:135](../upstream-free/blocks/seek/Seek.css#L135): `transition:`
- [Seek.css:137](../upstream-free/blocks/seek/Seek.css#L137): `background 220ms ease;`
- [Seek.css:181](../upstream-free/blocks/seek/Seek.css#L181): `transition: transform 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Seek.css:214](../upstream-free/blocks/seek/Seek.css#L214): `transition: stroke 220ms ease, stroke-width 220ms ease;}`
- [Seek.tsx:46](../upstream-free/blocks/seek/Seek.tsx#L46): `/* ── inlined from lab/spring ──────────────────────── */`
- [Seek.tsx:47](../upstream-free/blocks/seek/Seek.tsx#L47): `/* ── one spring, for everything that settles ───────────────`
- [Seek.tsx:62](../upstream-free/blocks/seek/Seek.tsx#L62): `a second and the damping is RAISED to it rather than`
- [Seek.tsx:65](../upstream-free/blocks/seek/Seek.tsx#L65): `version that makes a spring behave differently on a busy`
- [Seek.tsx:73](../upstream-free/blocks/seek/Seek.tsx#L73): `/* 0..100 into the two numbers a spring actually has.`
- [Seek.tsx:84](../upstream-free/blocks/seek/Seek.tsx#L84): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Seek.tsx:85](../upstream-free/blocks/seek/Seek.tsx#L85): `as stiffness and decay, because the ratio is the thing a`
- [Seek.tsx:91](../upstream-free/blocks/seek/Seek.tsx#L91): `The first version of this ran 0.06..0.26 stiffness against`
- [Seek.tsx:106](../upstream-free/blocks/seek/Seek.tsx#L106): `/* stiffness: how hard it is pulled toward the target */`
- [Seek.tsx:112](../upstream-free/blocks/seek/Seek.tsx#L112): `/* Units matter. The snap threshold is absolute, so a caller`
- [Seek.tsx:113](../upstream-free/blocks/seek/Seek.tsx#L113): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Seek.tsx:225](../upstream-free/blocks/seek/Seek.tsx#L225): `spring = 20,`
- [Seek.tsx:255](../upstream-free/blocks/seek/Seek.tsx#L255): `spring?: number;`
- [Seek.tsx:311](../upstream-free/blocks/seek/Seek.tsx#L311): `What the spring is for here is the tiny overshoot at the`
- [Seek.tsx:313](../upstream-free/blocks/seek/Seek.tsx#L313): `and not enough to notice as a bounce. */`
- [Seek.tsx:315](../upstream-free/blocks/seek/Seek.tsx#L315): `const w = useSpring(target, clamp(spring, 0, 100), still);`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
