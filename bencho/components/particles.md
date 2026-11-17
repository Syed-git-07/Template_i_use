# Particles

Public reference: https://bencho.dev/blocks/particles

[Original API and usage guide](../upstream-free/blocks/particles/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Particles.css](../upstream-free/blocks/particles/Particles.css): 14 lines; SHA-256 `40c8e5ae95b1e01e8a27fabec6f35fca112be2b78d99f903af2724484b5a4bd6`.
- [Particles.tsx](../upstream-free/blocks/particles/Particles.tsx): 289 lines; SHA-256 `c5fc53cb7549975724e340674f408b500f427cbf1f2dc86e3036e8d480a6139b`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Particles.tsx:5](../upstream-free/blocks/particles/Particles.tsx#L5): `away from the pointer and spring home behind it; press and a`
- [Particles.tsx:21](../upstream-free/blocks/particles/Particles.tsx#L21): `/* ── inlined from lab/spring ──────────────────────── */`
- [Particles.tsx:22](../upstream-free/blocks/particles/Particles.tsx#L22): `/* ── one spring, for everything that settles ───────────────`
- [Particles.tsx:37](../upstream-free/blocks/particles/Particles.tsx#L37): `a second and the damping is RAISED to it rather than`
- [Particles.tsx:40](../upstream-free/blocks/particles/Particles.tsx#L40): `version that makes a spring behave differently on a busy`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
