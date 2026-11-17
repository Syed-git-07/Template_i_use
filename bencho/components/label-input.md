# Label input

Public reference: https://bencho.dev/blocks/label-input

[Original API and usage guide](../upstream-free/blocks/label-input/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [LabelInput.css](../upstream-free/blocks/label-input/LabelInput.css): 159 lines; SHA-256 `00eb733f1469eed1420946de4912d219c2819ec45b53712af2a90d52be2dc745`.
- [LabelInput.tsx](../upstream-free/blocks/label-input/LabelInput.tsx): 182 lines; SHA-256 `8f13bc6ae1abc90e811c205df4f53a105cffcef807ed1e2bd694b3b8f7153a58`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [LabelInput.css:33](../upstream-free/blocks/label-input/LabelInput.css#L33): `transition: stroke 220ms ease, stroke-width 220ms ease;}`
- [LabelInput.css:48](../upstream-free/blocks/label-input/LabelInput.css#L48): `transition: stroke 220ms ease, stroke-width 220ms ease,`
- [LabelInput.css:68](../upstream-free/blocks/label-input/LabelInput.css#L68): `transition: transform 420ms cubic-bezier(0.22, 1, 0.36, 1), color 220ms ease;`
- [LabelInput.css:85](../upstream-free/blocks/label-input/LabelInput.css#L85): `animation-delay: calc(var(--i) * 24ms);}`
- [LabelInput.css:105](../upstream-free/blocks/label-input/LabelInput.css#L105): `.lbi-field[data-flip="1"] { animation: lbi-flip-a 260ms ease-out; }`
- [LabelInput.css:107](../upstream-free/blocks/label-input/LabelInput.css#L107): `.lbi-field[data-flip="0"] { animation: lbi-flip-b 260ms ease-out; }`
- [LabelInput.css:124](../upstream-free/blocks/label-input/LabelInput.css#L124): `transition: color 160ms ease, scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [LabelInput.css:133](../upstream-free/blocks/label-input/LabelInput.css#L133): `transition: opacity 220ms ease, scale 220ms cubic-bezier(0.22, 1, 0.36, 1), filter 220ms ease;}`
- [LabelInput.css:144](../upstream-free/blocks/label-input/LabelInput.css#L144): `.lbi-label { transition-duration: 160ms; }`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
