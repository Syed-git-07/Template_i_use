# Aspect ratio

Public reference: https://bencho.dev/blocks/aspect

[Original API and usage guide](../upstream-free/blocks/aspect/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Aspect.css](../upstream-free/blocks/aspect/Aspect.css): 105 lines; SHA-256 `e69d0f2971f66631e6ed033bf048f4fc08385f5ac2dad38aaa42590cef86f883`.
- [Aspect.tsx](../upstream-free/blocks/aspect/Aspect.tsx): 202 lines; SHA-256 `37cb6ccda091dfaa439494a6d29f7fa880c4e58a11ba52b3cfe32d5fd94e5cfc`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Aspect.css:10](../upstream-free/blocks/aspect/Aspect.css#L10): `what is here is the transition itself and the chrome. */`
- [Aspect.css:35](../upstream-free/blocks/aspect/Aspect.css#L35): `transition:`
- [Aspect.css:70](../upstream-free/blocks/aspect/Aspect.css#L70): `the thumb is not on a duration of its own — it is a`
- [Aspect.css:75](../upstream-free/blocks/aspect/Aspect.css#L75): `transition: transform calc(var(--asp-ms, 600ms) * 0.55)`
- [Aspect.css:90](../upstream-free/blocks/aspect/Aspect.css#L90): `transition: color 160ms ease, scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Aspect.css:104](../upstream-free/blocks/aspect/Aspect.css#L104): `.asp-pic, .asp-thumb, .asp-tab { transition-duration: 160ms; }`
- [Aspect.tsx:7](../upstream-free/blocks/aspect/Aspect.tsx#L7): `when it lands. Their character lives in a duration and in`
- [Aspect.tsx:25](../upstream-free/blocks/aspect/Aspect.tsx#L25): `whatever the component's own tuned duration is. 0 is a`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
