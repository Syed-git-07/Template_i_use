# Assignees

Public reference: https://bencho.dev/blocks/picker

[Original API and usage guide](../upstream-free/blocks/picker/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Picker.css](../upstream-free/blocks/picker/Picker.css): 230 lines; SHA-256 `5adc3d4e57eef26e48a00fb184ea7d32a5aaf9d3781350122890885a165ef46f`.
- [Picker.tsx](../upstream-free/blocks/picker/Picker.tsx): 391 lines; SHA-256 `d4b081931759b3440f063e1e0e57206572266b09a122605fdc208fc6a9a3d686`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Picker.css:76](../upstream-free/blocks/picker/Picker.css#L76): `transition: width 220ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Picker.css:112](../upstream-free/blocks/picker/Picker.css#L112): `transition: rotate 220ms cubic-bezier(0.22, 1, 0.36, 1), color 160ms ease;}`
- [Picker.css:156](../upstream-free/blocks/picker/Picker.css#L156): `transition: background 160ms ease;}`
- [Picker.css:217](../upstream-free/blocks/picker/Picker.css#L217): `transition: background 160ms ease, box-shadow 160ms ease;}`
- [Picker.css:229](../upstream-free/blocks/picker/Picker.css#L229): `.pik-rail, .pik-chev { transition-duration: 160ms; }`
- [Picker.tsx:143](../upstream-free/blocks/picker/Picker.tsx#L143): `can transition it without knowing where the block is. */`
- [Picker.tsx:207](../upstream-free/blocks/picker/Picker.tsx#L207): `one CSS transition rather than by anything watching`
- [Picker.tsx:258](../upstream-free/blocks/picker/Picker.tsx#L258): `spring wobbles for a third of a second after`
- [Picker.tsx:262](../upstream-free/blocks/picker/Picker.tsx#L262): `Rotate keeps the loose spring, and it is the`
- [Picker.tsx:267](../upstream-free/blocks/picker/Picker.tsx#L267): `transition={{`
- [Picker.tsx:268](../upstream-free/blocks/picker/Picker.tsx#L268): `type: "spring", stiffness: 500, damping: 18, mass: 0.8,`
- [Picker.tsx:269](../upstream-free/blocks/picker/Picker.tsx#L269): `x: { type: "spring", stiffness: 380, damping: 34, mass: 0.7 },`
- [Picker.tsx:270](../upstream-free/blocks/picker/Picker.tsx#L270): `y: { type: "spring", stiffness: 380, damping: 34, mass: 0.7 },`
- [Picker.tsx:271](../upstream-free/blocks/picker/Picker.tsx#L271): `scale: { type: "spring", stiffness: 380, damping: 34, mass: 0.7 },`
- [Picker.tsx:272](../upstream-free/blocks/picker/Picker.tsx#L272): `opacity: { duration: 0.16 },`
- [Picker.tsx:322](../upstream-free/blocks/picker/Picker.tsx#L322): `from three quarters, with the spring doing the`
- [Picker.tsx:323](../upstream-free/blocks/picker/Picker.tsx#L323): `work, they do not. The BOUNCE is where the`
- [Picker.tsx:328](../upstream-free/blocks/picker/Picker.tsx#L328): `transition={{`
- [Picker.tsx:331](../upstream-free/blocks/picker/Picker.tsx#L331): `type: "spring", stiffness: 500, damping: 18, mass: 0.9,`
- [Picker.tsx:332](../upstream-free/blocks/picker/Picker.tsx#L332): `opacity: { duration: 0.16 },`
- [Picker.tsx:353](../upstream-free/blocks/picker/Picker.tsx#L353): `transition={{`
- [Picker.tsx:354](../upstream-free/blocks/picker/Picker.tsx#L354): `type: "spring", stiffness: 380, damping: 34, mass: 0.7,`
- [Picker.tsx:355](../upstream-free/blocks/picker/Picker.tsx#L355): `delay: 0.04 * CAST.indexOf(p) + 0.03,`
- [Picker.tsx:376](../upstream-free/blocks/picker/Picker.tsx#L376): `transition={{ type: "spring", stiffness: 500, damping: 18, mass: 0.6 }}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
