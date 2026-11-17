# Slingshot

Public reference: https://bencho.dev/blocks/slingshot

[Original API and usage guide](../upstream-free/blocks/slingshot/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Slingshot.css](../upstream-free/blocks/slingshot/Slingshot.css): 32 lines; SHA-256 `d2c9deb1237333d6cd5df04afa9e3e10c9b1b23014d25013b276bf5da7a32645`.
- [Slingshot.tsx](../upstream-free/blocks/slingshot/Slingshot.tsx): 381 lines; SHA-256 `58043e410d3c346f5afdadad9ea9c095d1da34679b4d77efcc06f4d110407626`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Slingshot.css:30](../upstream-free/blocks/slingshot/Slingshot.css#L30): `transition: opacity 160ms ease;}`
- [Slingshot.tsx:15](../upstream-free/blocks/slingshot/Slingshot.tsx#L15): `go and the band snaps back on a spring, past its rest and home.`
- [Slingshot.tsx:17](../upstream-free/blocks/slingshot/Slingshot.tsx#L17): `── THE BAND IS A SPRING, THE FLIGHT IS GRAVITY ─────────`
- [Slingshot.tsx:68](../upstream-free/blocks/slingshot/Slingshot.tsx#L68): `/* how lively a bounce off the walls is, 0..100 */`
- [Slingshot.tsx:69](../upstream-free/blocks/slingshot/Slingshot.tsx#L69): `bounce = 30,`
- [Slingshot.tsx:72](../upstream-free/blocks/slingshot/Slingshot.tsx#L72): `bounce?: number;`
- [Slingshot.tsx:79](../upstream-free/blocks/slingshot/Slingshot.tsx#L79): `const knobs = useRef({ power, bounce });`
- [Slingshot.tsx:80](../upstream-free/blocks/slingshot/Slingshot.tsx#L80): `knobs.current = { power, bounce };`
- [Slingshot.tsx:242](../upstream-free/blocks/slingshot/Slingshot.tsx#L242): `const e = 0.2 + (knobs.current.bounce / 100) * 0.6;`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
