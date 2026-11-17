# Card swap

Public reference: https://bencho.dev/blocks/card-swap

[Original API and usage guide](../upstream-free/blocks/card-swap/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [CardSwap.css](../upstream-free/blocks/card-swap/CardSwap.css): 54 lines; SHA-256 `5999d450f3b0c7f42d21ec1ba9947411103f46b7181c443ae9dcb190fdf9ae8e`.
- [CardSwap.tsx](../upstream-free/blocks/card-swap/CardSwap.tsx): 159 lines; SHA-256 `66e1842e1b9d0c98ccc4ca1de0644a89b2bc99cba7ae06086b6ffa417f82052a`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [CardSwap.css:30](../upstream-free/blocks/card-swap/CardSwap.css#L30): `transition: transform 600ms cubic-bezier(0.22, 1, 0.36, 1);`
- [CardSwap.tsx:13](../upstream-free/blocks/card-swap/CardSwap.tsx#L13): `changing its slot and letting the transition carry it — the card`
- [CardSwap.tsx:59](../upstream-free/blocks/card-swap/CardSwap.tsx#L59): `for (const el of Object.values(els.current)) if (el) { el.style.transition = ""; el.style.transform = ""; }`
- [CardSwap.tsx:81](../upstream-free/blocks/card-swap/CardSwap.tsx#L81): `el.style.transition = "none";`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
