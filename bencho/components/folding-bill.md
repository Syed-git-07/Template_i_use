# Folding bill

Public reference: https://bencho.dev/blocks/folding-bill

[Original API and usage guide](../upstream-free/blocks/folding-bill/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [FoldingBill.css](../upstream-free/blocks/folding-bill/FoldingBill.css): 12 lines; SHA-256 `d9e6e9cdc77b90645c180bcafc4b42944b15d9bde340305eb12afce6c6619a49`.
- [FoldingBill.tsx](../upstream-free/blocks/folding-bill/FoldingBill.tsx): 569 lines; SHA-256 `2a9703a4f55f26d37e8d7ab88ac36c95e0063c62115cc2a855b1064ea3297ee2`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [FoldingBill.tsx:17](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L17): `bending springs are the Stiffness knob, paper at one end and`
- [FoldingBill.tsx:184](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L184): `stiffness = 40,`
- [FoldingBill.tsx:188](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L188): `stiffness?: number;`
- [FoldingBill.tsx:194](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L194): `const live = useRef({ stiffness, settle, print });`
- [FoldingBill.tsx:195](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L195): `live.current = { stiffness, settle, print };`
- [FoldingBill.tsx:465](../upstream-free/blocks/folding-bill/FoldingBill.tsx#L465): `const { stiffness: st, settle: se } = live.current;`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
