# Toast stack

Public reference: https://bencho.dev/blocks/toast-stack

[Original API and usage guide](../upstream-free/blocks/toast-stack/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [ToastStack.css](../upstream-free/blocks/toast-stack/ToastStack.css): 91 lines; SHA-256 `56f28f2bdffc865f660da8165f1b19fa1328a7dfa16ea0cc5d67f3c7d81ab6cd`.
- [ToastStack.tsx](../upstream-free/blocks/toast-stack/ToastStack.tsx): 174 lines; SHA-256 `29deb67611187bc8c6ee7d9bf1833f93423664f101a17b9dd94bd4cf32c38115`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [ToastStack.css:28](../upstream-free/blocks/toast-stack/ToastStack.css#L28): `transition: background-color 220ms ease, box-shadow 220ms ease;}`
- [ToastStack.css:39](../upstream-free/blocks/toast-stack/ToastStack.css#L39): `.tst-toast > * { transition: opacity 220ms ease; }`
- [ToastStack.css:71](../upstream-free/blocks/toast-stack/ToastStack.css#L71): `transition: scale 160ms cubic-bezier(0.22, 1, 0.36, 1);`
- [ToastStack.css:87](../upstream-free/blocks/toast-stack/ToastStack.css#L87): `transition: background-color 160ms ease, color 160ms ease;}`
- [ToastStack.tsx:11](../upstream-free/blocks/toast-stack/ToastStack.tsx#L11): `── ONE SPRING, THREE PLACES ────────────────────────────`
- [ToastStack.tsx:15](../upstream-free/blocks/toast-stack/ToastStack.tsx#L15): `move — every toast heading for its new place on the same spring,`
- [ToastStack.tsx:56](../upstream-free/blocks/toast-stack/ToastStack.tsx#L56): `const SPRING = { type: "spring", stiffness: 380, damping: 34, mass: 1 } as const;`
- [ToastStack.tsx:147](../upstream-free/blocks/toast-stack/ToastStack.tsx#L147): `transition={out ? { duration: 0.22, ease: [0.4, 0, 1, 1] } : SPRING}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
