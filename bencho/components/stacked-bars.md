# Stacked bars

Public reference: https://bencho.dev/blocks/stacked-bars

[Original API and usage guide](../upstream-free/blocks/stacked-bars/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [StackedBars.css](../upstream-free/blocks/stacked-bars/StackedBars.css): 221 lines; SHA-256 `74ef85e104db8c0bbf7392979c4361f52144bdd5467735274500914c2f9e78f0`.
- [StackedBars.tsx](../upstream-free/blocks/stacked-bars/StackedBars.tsx): 311 lines; SHA-256 `6e99a5cff332c6b5195363654e9cdf7893d307520aaa99a01dcb67e40007702d`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [StackedBars.css:61](../upstream-free/blocks/stacked-bars/StackedBars.css#L61): `transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [StackedBars.css:78](../upstream-free/blocks/stacked-bars/StackedBars.css#L78): `transition: color 160ms ease, scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [StackedBars.css:107](../upstream-free/blocks/stacked-bars/StackedBars.css#L107): `animation-delay: calc(var(--i, 0) * 70ms);}`
- [StackedBars.css:131](../upstream-free/blocks/stacked-bars/StackedBars.css#L131): `transition:`
- [StackedBars.css:134](../upstream-free/blocks/stacked-bars/StackedBars.css#L134): `background-color 160ms ease;}`
- [StackedBars.css:160](../upstream-free/blocks/stacked-bars/StackedBars.css#L160): `transition: opacity 160ms ease;}`
- [StackedBars.css:164](../upstream-free/blocks/stacked-bars/StackedBars.css#L164): `/* the tooltip: beside the column, gliding on a spring */`
- [StackedBars.css:182](../upstream-free/blocks/stacked-bars/StackedBars.css#L182): `transition: opacity 160ms ease;}`
- [StackedBars.tsx:11](../upstream-free/blocks/stacked-bars/StackedBars.tsx#L11): `faded), and one tooltip glides beside it on a spring with the`
- [StackedBars.tsx:16](../upstream-free/blocks/stacked-bars/StackedBars.tsx#L16): `offset a beat after its left neighbour. The same transition`
- [StackedBars.tsx:28](../upstream-free/blocks/stacked-bars/StackedBars.tsx#L28): `const SPRING = { type: "spring" as const, stiffness: 380, damping: 34 };`
- [StackedBars.tsx:110](../upstream-free/blocks/stacked-bars/StackedBars.tsx#L110): `}, { threshold: 0.3 });`
- [StackedBars.tsx:172](../upstream-free/blocks/stacked-bars/StackedBars.tsx#L172): `else animate(mv, v, SPRING);`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
