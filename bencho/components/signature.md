# Signature pad

Public reference: https://bencho.dev/blocks/signature

[Original API and usage guide](../upstream-free/blocks/signature/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Signature.css](../upstream-free/blocks/signature/Signature.css): 153 lines; SHA-256 `e507da6d411e78b858c9bd0c51ca1a4902542f6ba5be00c6c3424e8f51a951f5`.
- [Signature.tsx](../upstream-free/blocks/signature/Signature.tsx): 303 lines; SHA-256 `0a7f7cc619d183efbe876be48f968aa8e34c5ba91f8789bed4d4527e1817bdb2`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Signature.css:10](../upstream-free/blocks/signature/Signature.css#L10): `transition:`
- [Signature.css:30](../upstream-free/blocks/signature/Signature.css#L30): `transition: color 260ms ease;}`
- [Signature.css:60](../upstream-free/blocks/signature/Signature.css#L60): `transition: opacity 220ms ease;}`
- [Signature.css:76](../upstream-free/blocks/signature/Signature.css#L76): `transition: scale 600ms cubic-bezier(0.22, 1, 0.36, 1), opacity 420ms ease 220ms;}`
- [Signature.css:81](../upstream-free/blocks/signature/Signature.css#L81): `transition: scale 600ms cubic-bezier(0.22, 1, 0.36, 1), opacity 420ms ease 160ms;}`
- [Signature.css:83](../upstream-free/blocks/signature/Signature.css#L83): `.sig[data-settled] :is(.sig-clear, .sig-hint) { opacity: 0; transition: opacity 160ms ease; }`
- [Signature.css:85](../upstream-free/blocks/signature/Signature.css#L85): `.sig[data-settled] .sig-line { opacity: 0.08; transition: opacity 420ms ease; }`
- [Signature.css:113](../upstream-free/blocks/signature/Signature.css#L113): `animation: sig-said 320ms ease 420ms both;`
- [Signature.css:140](../upstream-free/blocks/signature/Signature.css#L140): `transition: opacity 160ms ease, scale 220ms cubic-bezier(0.24, 1.34, 0.38, 1), background 160ms ease;`
- [Signature.tsx:45](../upstream-free/blocks/signature/Signature.tsx#L45): `const ease = (k: number) => (k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2);`
- [Signature.tsx:199](../upstream-free/blocks/signature/Signature.tsx#L199): `setCut(Math.round(n * (1 - ease(k))));`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
