# Palette

Public reference: https://bencho.dev/blocks/palette

[Original API and usage guide](../upstream-free/blocks/palette/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Palette.css](../upstream-free/blocks/palette/Palette.css): 153 lines; SHA-256 `fd33c35f85b5ad97f22d927070d867715fb47ed94f69933027330d3f680c5076`.
- [Palette.tsx](../upstream-free/blocks/palette/Palette.tsx): 613 lines; SHA-256 `ff2e0a42b5450ad7add01d97597891801d741fec0ad8cf249af2d618f1ce1152`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Palette.css:60](../upstream-free/blocks/palette/Palette.css#L60): `transition: scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Palette.css:87](../upstream-free/blocks/palette/Palette.css#L87): `/* transform and width are written per frame — no transition,`
- [Palette.css:89](../upstream-free/blocks/palette/Palette.css#L89): `other and what you see is the transition rather than the`
- [Palette.css:92](../upstream-free/blocks/palette/Palette.css#L92): `/* the height is written per frame too — 'bounce' and 'orb'`
- [Palette.css:108](../upstream-free/blocks/palette/Palette.css#L108): `transition: color 160ms ease;}`
- [Palette.css:141](../upstream-free/blocks/palette/Palette.css#L141): `transition: rotate 600ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Palette.css:144](../upstream-free/blocks/palette/Palette.css#L144): `.pal-go, .pal-go svg, .pal-tool { transition-duration: 160ms; }`
- [Palette.tsx:37](../upstream-free/blocks/palette/Palette.tsx#L37): `Shared parts for the Framer Motion layer: one spring, one`
- [Palette.tsx:89](../upstream-free/blocks/palette/Palette.tsx#L89): `when it lands. Their character lives in a duration and in`
- [Palette.tsx:107](../upstream-free/blocks/palette/Palette.tsx#L107): `whatever the component's own tuned duration is. 0 is a`
- [Palette.tsx:112](../upstream-free/blocks/palette/Palette.tsx#L112): `/* ── inlined from lab/spring ──────────────────────── */`
- [Palette.tsx:113](../upstream-free/blocks/palette/Palette.tsx#L113): `/* ── one spring, for everything that settles ───────────────`
- [Palette.tsx:128](../upstream-free/blocks/palette/Palette.tsx#L128): `a second and the damping is RAISED to it rather than`
- [Palette.tsx:131](../upstream-free/blocks/palette/Palette.tsx#L131): `version that makes a spring behave differently on a busy`
- [Palette.tsx:367](../upstream-free/blocks/palette/Palette.tsx#L367): `turned edge-on, 'split' parted in two, 'bounce' squashed`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
