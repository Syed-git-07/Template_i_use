# Slosh slider

Public reference: https://bencho.dev/blocks/slosh

[Original API and usage guide](../upstream-free/blocks/slosh/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Slosh.css](../upstream-free/blocks/slosh/Slosh.css): 216 lines; SHA-256 `c4ae8776c1ddd79d9c9b9573b5835c3af20b89c57ca587d78e66cbfda6180aee`.
- [Slosh.tsx](../upstream-free/blocks/slosh/Slosh.tsx): 295 lines; SHA-256 `60133e98810fde2ae3c4f96b0ed79976840e42b6ab0c18f353ff05024b350350`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Slosh.css:104](../upstream-free/blocks/slosh/Slosh.css#L104): `is written by the loop, and a transition on top of a spring`
- [Slosh.css:206](../upstream-free/blocks/slosh/Slosh.css#L206): `the thing with the mass. */`
- [Slosh.tsx:10](../upstream-free/blocks/slosh/Slosh.tsx#L10): `clicked is friction with a smirk on it. A button that`
- [Slosh.tsx:33](../upstream-free/blocks/slosh/Slosh.tsx#L33): `A slider whose value has mass.`
- [Slosh.tsx:37](../upstream-free/blocks/slosh/Slosh.tsx#L37): `spring behind it, softer and barely damped, so a fast drag`
- [Slosh.tsx:135](../upstream-free/blocks/slosh/Slosh.tsx#L135): `/* the coast. Friction is per frame, so it is raised to`
- [Slosh.tsx:151](../upstream-free/blocks/slosh/Slosh.tsx#L151): `not a very stiff spring that still rings */`
- [Slosh.tsx:155](../upstream-free/blocks/slosh/Slosh.tsx#L155): `/* stiffness falls and damping rises together: thin`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
