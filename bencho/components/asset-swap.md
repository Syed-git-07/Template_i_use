# Asset swap

Public reference: https://bencho.dev/blocks/asset-swap

[Original API and usage guide](../upstream-free/blocks/asset-swap/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Swap.css](../upstream-free/blocks/asset-swap/Swap.css): 184 lines; SHA-256 `8ce1f921a06eb6ec96b76944c965ee1988a73f4b4f3be68bad3102930998340c`.
- [Swap.tsx](../upstream-free/blocks/asset-swap/Swap.tsx): 372 lines; SHA-256 `d3bb3739b9c36db3caac214712afc08e89159baf0c0f588c6a7731855928c9ef`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Swap.css:82](../upstream-free/blocks/asset-swap/Swap.css#L82): `transition: background 160ms ease, scale 160ms ease;`
- [Swap.tsx:178](../upstream-free/blocks/asset-swap/Swap.tsx#L178): `bounce = 30,`
- [Swap.tsx:183](../upstream-free/blocks/asset-swap/Swap.tsx#L183): `bounce?: number;`
- [Swap.tsx:204](../upstream-free/blocks/asset-swap/Swap.tsx#L204): `const spring = { type: "spring" as const, duration: 0.6, bounce: (Math.min(100, Math.max(0, bounce)) / 100) * 0.5 };`
- [Swap.tsx:206](../upstream-free/blocks/asset-swap/Swap.tsx#L206): `const grow = { type: "spring" as const, duration: 0.6, bounce: 0.12 };`
- [Swap.tsx:278](../upstream-free/blocks/asset-swap/Swap.tsx#L278): `transition={{`
- [Swap.tsx:281](../upstream-free/blocks/asset-swap/Swap.tsx#L281): `scaleY: { type: "spring", duration: 0.6, bounce: 0 },`
- [Swap.tsx:282](../upstream-free/blocks/asset-swap/Swap.tsx#L282): `opacity: squeezed ? { delay: 0.1, duration: 0.16 } : { delay: 0.06, duration: 0.22 },`
- [Swap.tsx:300](../upstream-free/blocks/asset-swap/Swap.tsx#L300): `transition={on ? { duration: 0.16 } : { delay: 0.14, duration: 0.22 }}`
- [Swap.tsx:324](../upstream-free/blocks/asset-swap/Swap.tsx#L324): `animate={{ opacity: 1, transition: { delay: 0.1, duration: 0.22 } }}`
- [Swap.tsx:325](../upstream-free/blocks/asset-swap/Swap.tsx#L325): `exit={{ opacity: 0, transition: { duration: 0.16 } }}`
- [Swap.tsx:356](../upstream-free/blocks/asset-swap/Swap.tsx#L356): `transition={{`
- [Swap.tsx:357](../upstream-free/blocks/asset-swap/Swap.tsx#L357): `default: spring,`
- [Swap.tsx:358](../upstream-free/blocks/asset-swap/Swap.tsx#L358): `scale: lifted === null ? { type: "spring", duration: 0.42, bounce: 0.35 } : { duration: 0.16 },`
- [Swap.tsx:359](../upstream-free/blocks/asset-swap/Swap.tsx#L359): `opacity: { duration: lifted === null ? 0.18 : 0.1 },`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
